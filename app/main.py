from random import randrange
from typing import Optional

from fastapi import FastAPI,Body, Response,status , HTTPException
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
        
def find_index_post(id):
    for index,value in enumerate(my_posts):
        if value["id"]==id:
            return index
        
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

#for creation status code is 201
@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict= post.dict()
    post_dict['id']=randrange(0,1000000)
    my_posts.append(post_dict)
    return{"data": post_dict}
    print(post.rating)
    return {"data": f"title {post.title} and description {post.description} and published {post.published} and rating {post.rating}"}
#To get latest post
@app.get("/posts/latest")
def get_latest_post():
    post=my_posts[len(my_posts)-1]
    return{"latest_post": post}

#id is a path parameter which is used to get the post with the given id. The id is passed as a string in the URL and is converted to an integer using int() function. The find_post() function is called to find the post with the given id and return it. If the post is not found, it will return None.
#id is expected to be an integer, so we specify the type of id as int in the function definition. FastAPI will automatically convert the path parameter to the specified type and validate it. If the conversion fails, it will return a 422 Unprocessable Entity error.
#Whenever a post is not found, we return a 404 status code to indicate that the resource was not found. We can set the status code using the Response object from FastAPI. We can also return a custom message in the response body to provide more information about the error.
@app.get("/posts/{id}")
def get_post(id: int , Response: Response):
    print(type(id))
    post=find_post(id)
    if not post:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found")
       '''Response.status_code=status.HTTP_404_NOT_FOUND
       return{"message":f"{Response.status_code} Error!!! post with id {id} not found"}'''
    return{"post_detail": post}

#For deletion status code is 204
@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    index=find_index_post(id)
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found")
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
#To update data
@app.put("/posts/{id}")
def update_post(id:int, post:Post):
        index=find_index_post(id)
        if index==None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found")
        post_dict=post.dict()
        post_dict['id']=id
        my_posts[index]=post_dict
        return{"data":post_dict}
                  


