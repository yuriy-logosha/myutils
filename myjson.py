from datetime import datetime
from bson import ObjectId
import json


class MYJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime):
            return o.strftime("%d.%m.%Y")
        return json.JSONEncoder.default(self, o)
