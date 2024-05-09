from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Optional
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
import mysql.connector
import json

## DB connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="＊＊＊＊＊",
  database= "website"
)
cursor = mydb.cursor()

## API 設定
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"))
templates = Jinja2Templates(directory="templates")

# #設定middleware
app.add_middleware(SessionMiddleware, secret_key="random_string", max_age=None)

@app.middleware("http")
async def check_state(request: Request, call_next):
    response = await call_next(request)
    return response


# load homepage
@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})

## Sign Up
@app.post("/signup")
async def signup(request: Request, name: Optional[str] = Form(None),username: Optional[str] = Form(None), password: Optional[str] = Form(None)):
    cursor.execute("select username from member")
    result = cursor.fetchall()
    if any(username == row[0] for row in result):
      return RedirectResponse(url="/error?message=Repeated Username", status_code=303)
    else:
      sql_command = "insert into member(name,username,password) values(%s,%s,%s)"
      val = (name,username,password)
      cursor.execute(sql_command,val)
      mydb.commit()
      return RedirectResponse(url="/",status_code=303 )
    
## Error Page
@app.get("/error", response_class=HTMLResponse)
async def read_error(request: Request,message:str=None):
    return templates.TemplateResponse("error.html", {"request": request,"message":message})

  
## Sign In
@app.post("/signin")
async def signin(request: Request, username: Optional[str] = Form(None), password: Optional[str] = Form(None)):
    cursor.execute("select id, username, password from member")
    result = list(cursor.fetchall())
    matches = False
    index = 0
    for i in range(len(result)):
      if result[i][1:] == (username,password):
          matches = True
          index = i
          break
    if matches == True:
      request.session["SIGNED_IN"] = True
      request.session["USERNAME"] = username
      request.session["ID"] = result[index][0]
      return RedirectResponse(url="/member",status_code=303)
    else:
      return RedirectResponse(url="/error?message=Username or password is not correct", status_code=303)


## Member Page
@app.get("/member", response_class=HTMLResponse)
async def read_member(request: Request, message:str=None):
    #檢查登入state, 沒有登入則導回login page
    if request.session.get("SIGNED_IN") == True:
        username = request.session.get("USERNAME")
        cursor.execute("select message.member_id, message.content, member.username from message join member on message.member_id = member.id order by message.time desc")
        result = cursor.fetchall()
        formatted_data = [{'id': item[0], 'content': item[1], 'username': item[2]} for item in result]
        json_data = json.dumps(formatted_data)
        return templates.TemplateResponse("member.html", {"request": request,"username": username,"formatted_data":formatted_data})
    else:
        return RedirectResponse(url="/")

## createMessage
@app.post("/createMessage")
async def signin(request: Request, message: Optional[str] = Form(None)):
  id = request.session["ID"]
  sql_command = "insert into message(member_id,content) values(%s,%s)"
  val = (id,message)
  cursor.execute(sql_command,val)
  mydb.commit()
  return RedirectResponse(url="/member",status_code=303)
    

## Sign Out
@app.get("/signout")
async def signout(request: Request):
    request.session["SIGNED_IN"] = False
    return RedirectResponse(url="/")



