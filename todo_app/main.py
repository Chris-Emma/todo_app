from fastapi import FASTAPI, Response

# configure fastapi
app = FASTAPI()

#api
@app.get("/")
def awesome_api():
    return Response("This is a new awesome api")

