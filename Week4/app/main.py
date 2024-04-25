from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Optional
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware


app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"))
templates = Jinja2Templates(directory="app/templates")

#設定middleware
app.add_middleware(SessionMiddleware, secret_key="random_string", max_age=None)

@app.middleware("http")
async def check_state(request: Request, call_next):
    response = await call_next(request)
    # session = request.session
    # logged_in = session.get("SIGNED-IN",True)
    # #沒登入，導回login page
    # if not logged_in:
    #     return RedirectResponse(url="/")
    
    return response


user_db = [{
    "username":"test",
    "password":"test"
}]

@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/member", response_class=HTMLResponse)
async def read_member(request: Request, message:str=None):
    #檢查登入state, 沒有登入則導回login page
    if request.session.get("SIGNED_IN") == True:
        return templates.TemplateResponse("member.html", {"request": request, "message":message})
    else:
        return RedirectResponse(url="/")
    

@app.get("/error", response_class=HTMLResponse)
async def read_error(request: Request,message:str=None):
    return templates.TemplateResponse("error.html", {"request": request,"message":message})


@app.post("/signin")
async def signin(request: Request, username: Optional[str] = Form(None), password: Optional[str] = Form(None)):
    if not username or not password:
        return RedirectResponse(url="/error?message=Please enter username and password", status_code=303)
    else:
        for item in user_db:
            if item["username"] == username and item["password"] == password:
                request.session["SIGNED_IN"] = True
                return RedirectResponse(url="/member", status_code=303)
            else:
                
                return RedirectResponse(url="/error?message=Username or password is not correct", status_code=303)
        

@app.get("/signout")
async def signout(request: Request):
    request.session["SIGNED_IN"] = False
    return RedirectResponse(url="/")