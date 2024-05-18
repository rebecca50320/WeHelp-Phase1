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
from pydantic import BaseModel


## DB connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Flyhigh335!",
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

## request body
class NameUpdateRequest(BaseModel):
    name: str


# load homepage
@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})

## Sign Up
@app.post("/signup")
async def signup(request: Request, name: Optional[str] = Form(None),username: Optional[str] = Form(None), password: Optional[str] = Form(None)):
    sql_command = "select count(*) from member where username = %s"
    cursor.execute(sql_command,(username,))
    result = cursor.fetchone()
    if result[0] >0:
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
    sql_command = "select id from member where username = %s and password = %s"
    cursor.execute(sql_command,(username,password))
    result = cursor.fetchall()
    if len(result)>0:
      request.session["SIGNED_IN"] = True
      request.session["USERNAME"] = username
      request.session["ID"] = result[0][0]
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

## query member data by username    
@app.get("/api/member")
async def query_member(username:str):
   sql_command = 'select id,name,username from member where username = %s'
   cursor.execute(sql_command,(username,))
   result = cursor.fetchone()
   
   if result is None:
      return {"data":None}
   else:
      result_dict = {
        "id": result[0],
        "name": result[1],
        "username": result[2]
      }
      return {"data":result_dict}
   
## update member name
@app.patch("/api/member")
async def name_update(request:Request, name:NameUpdateRequest):
  sql_command = 'update member set name = %s where id= %s;'
  id = request.session.get("ID")
  cursor.execute(sql_command,(name.name,id))
  mydb.commit() 
  sql_command = 'select name from member where id= %s'
  cursor.execute(sql_command,(id,))
  result = cursor.fetchone()
   
  if result == None:
    return {"error":True}
  elif result[0] == name.name:
    return {"ok":True}


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


  

# id = 100
# name = "test1"


# sql_command = 'update member set name = %s where id= %s;'
# cursor.execute(sql_command,(name,id))
# mydb.commit()
# sql_command = 'select name from member where id= %s'
# cursor.execute(sql_command,(id,))
# result = cursor.fetchone()

# print(result)


# if result == None:
#    print("fail")
# elif result[0] == name:
#    print("ok")