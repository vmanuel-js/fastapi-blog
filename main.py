from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

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
        "description": "A sweet red fruit.",
    },
    {
        "id": 2,
        "name": "Banana",
        "color": "Yellow",
        "taste": "Sweet",
        "description": "A sweet yellow fruit.",
    },
    {
        "id": 3,
        "name": "Orange",
        "color": "Orange",
        "taste": "Citrus",
        "description": "A citrus orange fruit.",
    },
]


@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(
        request,
        "home.html",
        {"posts": posts, "title": "Home"},
    )


@app.get("/fruits", include_in_schema=False)
def fruits_page():
    return f"<ul><li>{fruits[0]['name']}</li><li>{fruits[1]['name']}</li><li>{fruits[2]['name']}</li></ul>"


@app.get("/api/posts")
def get_posts():
    return posts


@app.get("/api/fruits")
def get_fruits():
    return fruits
