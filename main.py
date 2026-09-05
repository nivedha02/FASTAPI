from fastapi import FastAPI
app=FastAPI()

#@app->decorator (path to go) def function followed by message
@app.get("/")
def root():
    return{"message":"Welcome World!!"} 

@app.get("/post")
def get_post():
    return{"data":"This is my post"}
