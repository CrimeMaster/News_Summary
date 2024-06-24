from typing import Annotated, Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel
from NewSummary import allNews
from Text_Summarization import summarizer
from datetime import datetime

app = FastAPI()
today = datetime.now()

#GET - Get an Information
#POST - Create Something new
#PUT - UPDATE
#DELETE - DELETE SOMETHING

news = {
    1: {
        "Title" : "NEET-UG Row: CBI takes over probe into irregularities in medical exam; registers FIR",
        "wordcount" : 800,
        "date" : "June 23, 2024"
    }
}

class News(BaseModel):
    Title: str
    wordcount: int
    date: str

class UpdateNews(BaseModel):
    Title: Optional[str] = None
    wordcount: Optional[int] = None
    date: Optional[str] = None



@app.get("/")
def index():
    return news


@app.get("/get-news/{news_id}")
def get_newsId(news_id: Annotated[int | None, Path(description="The ID of news you want to view", gt=0, lt=10) ]):
    if news_id not in news:
        return {"Error": "news does not exist"}
    return news[news_id]

@app.get("/get-by-title")
def get_byTitle(title : Optional[str] = None):
    for news_id in news:
        if news[news_id]["Title"] == title:
            return news[news_id]
        return {"data" : "Not Found"}



@app.post("/post-news/{news_id}")
def create_news(news_id : int, n : News):
    if news_id in news:
        return {"Error" : "News exists"}
    news[news_id] = n
    return news[news_id]

@app.post("/post-news")
def create_newsUrl(url : Optional[str] = None):
    title, data = allNews(url)
    
    # Check if news with the same title already exists
    exists = any(news[news_id]["Title"] == title for news_id in news)
    if exists:
        return {"Error": "News exists"}
    
    # Add the new news item
    next_key = len(news) + 1
    new_item = {
        "Title": title,
        "wordcount": len(data.split(' ')),
        "date": today.strftime("%B %d, %Y")
    }
    news[next_key] = new_item
    
    return news[next_key]

@app.delete("/delete-News/{news_id}")
def delete_news(news_id: int):
    if news_id not in news:
        return {"Error": "news does not exist"}
    
    del news[news_id]
    return {"Message": "News Deleted Succesfully"}

@app.delete("/delete-News")
def delete_newsTitle(title : Optional[str] = None):
    # Check if news with the same title already exists
    exists = any(news[news_id]["Title"] == title for news_id in news)
    if not exists:
        return {"Error": "News does not exists"}
    
    for news_id in news:
        if news[news_id]["Title"] == title:
            del news[news_id]
            return {"Message": "News Deleted Succesfully"}
                
@app.put("/update-student/{news_id}")
def update_news(news_id: int, student: UpdateNews):
    if news_id not in news:
        return {"Error": "news does nto exist"}
    
    if news.name != None:
        news[news_id].title = news.title
    
    if news.wordcount != None:
        news[news_id].wordcount = news.wordcount

    if news.date != None:
        news[news_id].date = news.date

    return news[news_id]