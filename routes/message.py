from fastapi import APIRouter
from models import Message
from db import db
from helpers.obj_helper import objectid_to_str
router = APIRouter()

@router.post("/")
def send_message(msg: Message):
  try:
    data=msg.model_dump()
    res=db["message"].insert_one(data)
    if res and res.inserted_id:
      return {
          "details":"Message Send Successfully",
          "data":str(res.inserted_id)}
  except Exception as e:
       return {"details":str(e)}

@router.get("/")
def get_messages():
    try:
       res=db["message"].find().to_list()
       if res:
          data=objectid_to_str(res)
          return {"data":data}
    except Exception as e:
       return {"details":str(e)}
