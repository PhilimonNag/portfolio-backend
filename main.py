from fastapi import FastAPI,status
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from routes import message,projects,storage,about
from config import config
import uvicorn

app=FastAPI(
  title=config.title,
  description=config.desc
)
app.add_middleware(
  CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/",include_in_schema=False)
def index():
   return RedirectResponse("/docs",status_code=status.HTTP_308_PERMANENT_REDIRECT)

app.include_router(prefix="/about",router=about.router)
app.include_router(prefix="/storage",router=storage.router)
app.include_router(prefix="/message",router=message.router)
app.include_router(prefix="/project",router=projects.router)

if __name__=="__main__":
   uvicorn.run("main:app", host="0.0.0.0", port=config.port)