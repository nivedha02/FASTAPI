from random import randrange
from typing import Optional

from fastapi import FastAPI,Body
from pydantic import BaseModel

app=FastAPI()

#From pydantic import BaseModel to create a model for the post - which is used to compare the data sent by the user to the model and validate it. If the data is not valid, it will return an error message.
#Optional is from typing module which is used to make the rating field optional. If the user does not provide a rating, it will be set to None.
class Post(BaseModel):
    title:str
    description:str
    published:bool=True
    rating:Optional[int]=None


#in-memory database
my_posts=[{"title":"title of post 1","content":"content of post 1","id":1},{"title":"title of post 2","content":"content of post 2","id":2}]


def find_post(id):
    for p in my_posts:
        if p["id"]==id:
            return p

#@app->decorator (path to go) def function followed by message
@app.get("/")
def root():
    return{"message":"Welcome World!!"} 

@app.get("/posts")
def get_post():
    return{"data": my_posts}

@app.post("/postpicture")
def post_picture(payload: dict = Body(...)):
    print(payload)
    return {
        "new_post": f"title {payload['title']} and description {payload['description']}"
    }

@app.post("/posts")
def create_post(post: Post):
    post_dict= post.dict()
    post_dict['id']=randrange(0,1000000)
    my_posts.append(post_dict)
    return{"data": post_dict}
    print(post.rating)
    return {"data": f"title {post.title} and description {post.description} and published {post.published} and rating {post.rating}"}

@app.get("/posts/latest")
def get_latest_post():
    post=my_posts[len(my_posts)-1]
    return{"latest_post": post}

#id is a path parameter which is used to get the post with the given id. The id is passed as a string in the URL and is converted to an integer using int() function. The find_post() function is called to find the post with the given id and return it. If the post is not found, it will return None.
#id is expected to be an integer, so we specify the type of id as int in the function definition. FastAPI will automatically convert the path parameter to the specified type and validate it. If the conversion fails, it will return a 422 Unprocessable Entity error.
@app.get("/posts/{id}")
def get_post(id: int):
    print(type(id))
    post=find_post(id)
    if not post:
        return{"message":f"post with id {id} not found"}
    return{"post_detail": post}


@app.delete("posts/{id}")
def delete_post(id:int):
    my_posts.remove(find_post(id))
    return{"message":f"post with id {id} has been deleted successfully"}
