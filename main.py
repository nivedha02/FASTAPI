from fastapi import FastAPI,Body

app=FastAPI()

#@app->decorator (path to go) def function followed by message
@app.get("/")
def root():
    return{"message":"Welcome World!!"} 

@app.get("/post")
def get_post():
    return{"data":"This is my post"}

@app.post("/postpicture")
def post_picture(payload: dict = Body(...)):
    print(payload)
    return {
        "new_post": f"title {payload['title']} and description {payload['description']}"
    }
1.10 hrs
