from fastapi import FastAPI
import uvicorn

from app.routers import news, summary

# app = FastAPI()

app = FastAPI(
    title="AI based News Summary API for Industrial Training CSE-50",
    version="0.2",
    description="This is the API documentation for News Summary generating by AI which is a part of final project for IIUC Industrial Training of CSE-50.",
    # terms_of_service="http://example.com/terms/",
    contact={
        "name": "Nuzhat Rahman",
        "email": "nuzhatrahman2514@gmail.com",
    },
    # license_info = {
    #     "name": "MIT License",
    #     "url": "https://opensource.org/licenses/MIT",
    # },
    redoc_url="/documentation",
    docs_url="/try-out",
)

app.include_router(news.router)
app.include_router(summary.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the News Summary API"}

if __name__ == "__main__":
    # uvicorn.run("main:app", host="localhost", port=8001, reload=True)
    uvicorn.run("main:app", host="localhost", port=8011, reload=True)