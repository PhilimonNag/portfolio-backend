from fastapi import APIRouter
from helpers.obj_helper import objectid_to_str
from db import db
router=APIRouter()


@router.get("/")
def get_about():
    res=db["about"].find_one({})
    return {"data":objectid_to_str(res)}

