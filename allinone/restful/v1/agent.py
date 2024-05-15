from allinone import db
# from allinone.model.label import Label
# from allinone.model.node import Node
from flask import request
from flask import session
from flask_restful import abort
# from flask_restful import Resource
from flask_restx import Resource
import json   

class AgentHistoryShow(Resource): 
    def get(self):  
        return {
            "success": True,
            'node_list': [1,2,3]
        }