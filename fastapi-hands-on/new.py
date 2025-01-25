"""
Author: Updated Script
Version: 2.0

This module demonstrates the usage of the `requests-html` library in Python for web scraping.
It extracts information such as title, datetime, and paragraphs for multiple links.

"""

from requests_html import HTMLSession

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
    data = {"ID": article_id, "Title": None, "Datetime": None, "Paragraphs": None}
    try:
        response = session.get(url)
        
        # Extract title
        title_tag = response.html.find('h1', first=True)
        data["Title"] = title_tag.text if title_tag else "No title found"
        
        # Extract datetime
        datetime_element = response.html.find('time', first=True)
        data["Datetime"] = datetime_element.attrs.get('datetime', 'No datetime attribute') if datetime_element else "No datetime element found"
        
        # Extract paragraphs
        paragraphs = response.html.find('p')
        if paragraphs:
            data["Paragraphs"] = "\n".join(p.text for p in paragraphs if p.text.strip())
        else:
            data["Paragraphs"] = "No paragraphs found"

    except Exception as e:
        print(f"An error occurred while processing ID {article_id}: {e}")
    finally:
        session.close()
    
    return data

def main():
    """
    Main function to extract information from multiple web pages.
    """
    links = {
        1: "https://www.prothomalo.com/sports/cricket/dwcawlhkqs",
        2: "https://www.prothomalo.com/sports/football/30m8dv7avi",
        3: "https://www.prothomalo.com/sports/y1xwv76h11",
        4: "https://www.prothomalo.com/sports/cricket/7zhf15l6u5",
        5: "https://www.prothomalo.com/sports/0glslftkg4",
    }

    print("Extracting information from web pages...\n")
    for article_id, url in links.items():
        article_data = extract_information(url, article_id)
        print(f"ID: {article_data['ID']}")
        print(f"Title: {article_data['Title']}")
        print(f"Datetime: {article_data['Datetime']}")
        print("Paragraphs:\n", article_data["Paragraphs"])
        print("-" * 80)

if __name__ == "__main__":
    main()
