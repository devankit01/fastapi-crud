from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Author
from apis.blog_api import blog_apis_routes

app = FastAPI()


# Adding CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[], # [http://localhost:3000]
    allow_methods=['*'],
    allow_headers=['*']
)

@app.post("/authors")
async def create_author(body: Author):
    author = Author(
        first_name=body.first_name,
        last_name=body.last_name,
        email=body.email,
        date_joined=body.date_joined,
    )

    author.save()
    return author


# Adding Blog APIs to main application
app.include_router(blog_apis_routes)

