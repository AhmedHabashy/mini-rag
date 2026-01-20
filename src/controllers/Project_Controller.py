from .Base_Controller import Base_Controller
from fastapi import UploadFile
from model import ResponseSignal

class ProjectController(Base_Controller):
    
    def __init__(self):
        super.__init__()
    

    def get_project_path(self, project_id: str):
        pass
