from fastapi import FastAPI
from typing import Optional
app = FastAPI()


@app.get("/blog")
def blogs(limit: int, published : bool, sort : Optional[int] = 1): # query parameters
    # Get 10 published Blogs

    return {
        'data': {
            'limit' : limit,
            'published' : published
        }
    }

@app.get("/blog/{id}")
def get_blog_by_id(id: int):
    # calling the db for the specified blog id
    return {
        "data" : {
            "blog" : {
                "id" : id,
                "msg" : "Heyy hello"
            }
        }
    }

@app.get("/author")
def author():
    return {
        "data" : {
            "first_name" : "Manabendu",
            "last_name" : 'Karfa'
        }
    }