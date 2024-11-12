from bson import ObjectId
def objectid_to_str(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    if isinstance(obj, dict):
        return {key: objectid_to_str(value) for key, value in obj.items()}
    if isinstance(obj, list):
        return [objectid_to_str(item) for item in obj]
    return obj
