from fastapi import FastAPI, Response

#configure app
app = FastAPI()

#API
@app.get("/")
def awesome_api():
    return Response("Welcome to my api")