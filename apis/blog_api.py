
from fastapi_utils.inferring_router import InferringRouter
from models import Author, Blog
from redis_om.model import NotFoundError


router = InferringRouter() #  Router

# Blog API
class BlogAPIView:

    # Create Blog API
    @router.post("/blogs")
    async def create_blog(body: dict):
        author = Author.get(body["author_id"])
        blog = Blog(title=body["title"], content=body["content"], author=author)

        blog.save()
        return blog

    # Get Blog API
    @router.get("/blogs/{pk}")
    async def get_blog(pk: str):
        try:
            blog = Blog.get(pk)
        except NotFoundError:
            return {"error": "not found", "status" : 404},
        return blog


    # Update Blog API
    @router.put("/blogs/{pk}")
    async def update_blog(pk: str, body: dict):
        blog = Blog.get(pk)

        blog.title = body["title"]
        blog.content = body["content"]

        blog.save()
        return blog

    # delete a blog
    @router.delete("/blogs/{pk}")
    async def delete_blog(pk: str):
        Blog.delete(pk)
        return {"success": "blog deleted successfully"}


    # Search Blog API
    def format_results(data):
        response = []
        for dat in data:
            response.append(dat.dict())

        return {"results": response}


    @router.post("/blogs/find")
    async def blog_by_name(self, title: str):
        print("Search")
        blogs = Blog.find(Blog.title % title).all()

        return self.format_results(blogs)


    @router.post("/blogs/find/author")
    async def blog_by_author(self, first_name: str):
        blogs = Blog.find(Blog.author.first_name == first_name).all()

        return self.format_results(blogs)

blog_apis_routes = router