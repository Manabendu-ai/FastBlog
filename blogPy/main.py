from fastapi import FastAPI
from .database import Base, engine
from .routers import blog, user


Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(blog.router)
app.include_router(user.router)


# changing the default port
#
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)