from fastapi import APIRouter
from models import Project,UpdateProject
from helpers.obj_helper import objectid_to_str
from bson import ObjectId
from db import db
router = APIRouter()

@router.post("/")
def add_project(project:Project):
    try:
      data=project.model_dump()
      res=db["project"].insert_one(data)
      if res and res.inserted_id:
        return {
            "details":"Project Added Successfully",
            "data":str(res.inserted_id)}
    except Exception as e:
        return {"details":str(e)}

@router.put("/:id")
def update_project(id:str,updateProject:UpdateProject):
    data=updateProject.model_dump(exclude_none=True)
    try:
       res=db["project"].update_one({"_id":ObjectId(id)},{"$set":data})
       if res:
          return {"details":f"updated count: {res.modified_count} {res.acknowledged}"}
    except Exception as e:
      return {"details":str(e)}

@router.get("/")
def get_projects():
    try:
       res=db["project"].find().to_list()
       if res:
          data=objectid_to_str(res)
          return {"data":data}
    except Exception as e:
       return {"details":str(e)}