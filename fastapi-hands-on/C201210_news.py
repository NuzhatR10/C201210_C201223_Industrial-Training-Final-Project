from requests_html import HTMLSession
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

# FastAPI app instance
app = FastAPI(
title="Nuzhat Rahman's FastAPI News Scraper & Engine",
description="A news scraper and API application built by Nuzhat Rahman.",
version="1.0.0"

)

# Data store for news articles
news = {}

def extract_information(url, article_id):
    """
    Extracts specific information from a webpage using CSS selectors.

    Parameters:
    url : str
        The URL of the website to scrape.
    article_id : int
        The ID of the article.

    Returns:
    dict
        A dictionary containing the extracted information.
    """
    session = HTMLSession()
    data = {
        "ID": article_id,
        "Title": None,
        "Datetime": None,
        "Content": None,
        "Images": None,
        "Summary": None,
        "Category": None,
        "ReporterID": None,
        "PublisherID": None
    }
    try:
        response = session.get(url)

        # Extract title
        title_tag = response.html.find('h1', first=True)
        data["Title"] = title_tag.text if title_tag else "No title found"

        # Extract datetime
        datetime_element = response.html.find('time', first=True)
        data["Datetime"] = datetime_element.attrs.get('datetime', 'No datetime attribute') if datetime_element else "No datetime element found"

        # Extract paragraphs for content
        paragraphs = response.html.find('p')
        if paragraphs:
            data["Content"] = "\n".join(p.text for p in paragraphs if p.text.strip())
        else:
            data["Content"] = "No content found"

        




        # Extract category
        category_element = response.html.find('.print-entity-section-wrapper', first=True)
        data["Category"] = category_element.text if category_element else "Uncategorized"

        # Extract reporter
        reporter_element = response.html.find('.contributor-name', first=True)
        data["ReporterID"] = reporter_element.text if reporter_element else "No Reporter ID"

        # Extract publisher
        publisher_website = url.split('/')[2]  # Extract domain from URL
        data["PublisherID"] = publisher_website.split('.')[-2]  # Extract main domain

        # Generate summary (first 2 sentences)
        meta_description = response.html.find('meta[name="description"]', first=True)
        data["Summary"] = meta_description.attrs.get('content', 'No summary found') if meta_description else "No summary available"

    except Exception as e:
        print(f"An error occurred while processing ID {article_id}: {e}")
    finally:
        session.close()

    return data

def scrape_news():
    """
    Scrapes predefined news articles and stores them in the `news` dictionary.
    """
    links = {
        1: "https://www.prothomalo.com/sports/cricket/dwcawlhkqs",
        2: "https://www.prothomalo.com/sports/football/30m8dv7avi",
        3: "https://www.prothomalo.com/sports/cricket/db492z2k9h",
        4: "https://www.prothomalo.com/sports/cricket/7zhf15l6u5",
        5: "https://www.prothomalo.com/sports/0glslftkg4",
        6: "https://www.prothomalo.com/sports/cricket/cx6ir3ztlq"
    }

    print("Scraping news articles...")
    for article_id, url in links.items():
        article_data = extract_information(url, article_id)
        news[article_id] = {
            "id": article_data["ID"],
            "title": article_data["Title"],
            "content": article_data["Content"],
            "datetime": article_data["Datetime"],
            "images": article_data["Images"],
            "summary": article_data["Summary"],
            "category": article_data["Category"],
            "reporter_id": article_data["ReporterID"],
            "publisher_id": article_data["PublisherID"]
        }
    print("Scraping completed.")

class News(BaseModel):
    title: str
    content: str | None = None
    images: list[str] | None = None
    summary: str | None = None
    category: str | None = None
    reporter_id: str | None = None
    publisher_id: str | None = None

@app.on_event("startup")
def startup_event():
    """
    Runs at application startup to scrape and populate news articles.
    """
    scrape_news()

@app.get("/")
def heartbeat():
    return {"message": "Hello, I am Nuzhat!"}

# Get all news
@app.get("/all_news")
def all_news():
    return news

# Filter news by title using query parameters
@app.get("/news/title")
def news_by_title(title_contains: str):
    filtered_news = [single_news for single_news in news.values() if title_contains.lower() in single_news["title"].lower()]
    if not filtered_news:
        return {"data": f"No news found with title containing '{title_contains}'"}
    return filtered_news

# Filter news by category
@app.get("/news/category")
def news_by_category(category: str):
    filtered_news = [news_item for news_item in news.values() if news_item.get("category", "").lower() == category.lower()]
    if not filtered_news:
        return {"data": f"No news found in category '{category}'"}
    return filtered_news

# Filter news by publisher
@app.get("/news/publisher")
def news_by_publisher(publisher: str):
    filtered_news = [news_item for news_item in news.values() if publisher.lower() in news_item.get("publisher_id", "").lower()]
    if not filtered_news:
        return {"data": f"No news found from publisher '{publisher}'"}
    return filtered_news

# Filter news by summary
@app.get("/news/summary")
def news_by_summary(summary_contains: str):
    filtered_news = [news_item for news_item in news.values() if summary_contains.lower() in news_item.get("summary", "").lower()]
    if not filtered_news:
        return {"data": f"No news found with summary containing '{summary_contains}'"}
    return filtered_news

@app.get("/news/{id}/summary")
def news_summary_by_id(id: int):
    """
    Fetch the summary of a news article by its ID.

    Parameters:
    id : int
        The ID of the news article.

    Returns:
    dict
        A dictionary containing the summary or an error message if the ID is not found.
    """
    if id not in news:
        return {"error": f"News with id {id} not found"}
    return {"id": id, "summary": news[id].get("summary", "No summary available")}

# Get news by ID
@app.get("/news/{id}")
def news_by_id(id: int):
    if id not in news:
        return {"error": f"News with id {id} not found"}
    return news[id]

# Create new news
@app.post("/create-news")
def create_news(response_news: News):
    id = max(news.keys()) + 1
    news[id] = {
        "id": id,
        "title": response_news.title,
        "content": response_news.content,
        "images": response_news.images,
        "summary": response_news.summary,
        "category": response_news.category,
        "reporter_id": response_news.reporter_id,
        "publisher_id": response_news.publisher_id
    }
    return news[id]

if __name__ == '__main__':
    uvicorn.run("C201210_news:app", host='localhost', port=8000, reload=True)
