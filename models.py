from pydantic import BaseModel
from typing import Optional

class Message(BaseModel):
     app_name:str
     user_name:str
     email:str
     message:str

class Project(BaseModel):
      name:str
      desc:str
      project_url:str
      image_url:str
class UpdateProject(BaseModel):
      name:Optional[str]=None
      desc:Optional[str]=None
      project_url:Optional[str]=None
      image_url:Optional[str]=None

class FileInfo(BaseModel):
    filename: str
    file_url: str