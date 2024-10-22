import json
from fastapi import FastAPI, Depends, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database.configurations import init_db, db_session
from database.models import Item
from database.schema import ItemSchema

#configure app
app = FastAPI()

#configuring static route
app.mount("/static", StaticFiles(directory="static"), name="static")

#configuring templates
templates = Jinja2Templates(directory="templates")

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/todo")
def getItems(session: Session =Depends(db_session)):
    item = session.query(Item).all()
    return Item

@app.post("/todo/api")
def addItem(item: ItemSchema, session: Session = Depends(db_session)):
    todoitem = Item(task=item.task)
    session.add(todoitem)
    session.commit()
    session.refresh(todoitem)
    return todoitem