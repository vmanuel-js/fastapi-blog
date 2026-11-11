from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2026",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes even better.",
        "date_posted": "April 21, 2026",
    },
]

fruits: list[dict] = [
    {
        "id": 1,
        "name": "Apple",
        "color": "Red",
        "taste": "Sweet",
        "description": "A sweet red fruit."
    },
    {
        "id": 2,
        "name": "Banana",
        "color": "Yellow",
        "taste": "Sweet",
        "description": "A sweet yellow fruit."
    },
    {
        "id": 3,
        "name": "Orange",
        "color": "Orange",
        "taste": "Citrus",
        "description": "A citrus orange fruit."
    }
]

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<ul><li>{posts[0]["title"]}</li><li>{posts[1]["title"]}</li></ul>"

@app.get("/fruits", response_class=HTMLResponse, include_in_schema=False)
def fruits_page():
    return f"<ul><li>{fruits[0]["name"]}</li><li>{fruits[1]["name"]}</li><li>{fruits[2]["name"]}</li></ul>"

@app.get("/api/posts")
def get_posts():
    return posts

@app.get("/api/fruits")
def get_fruits():
    return fruits