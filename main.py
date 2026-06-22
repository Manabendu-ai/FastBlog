from fastapi import FastAPI

app = FastAPI()

@app.get("/blog/{id}")
def get_blog_by_id(id):
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