from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from helpers.config import get_settings,Settings
from controllers import Data_Controller, ProjectController # you didn't specify what to get from controller so the compiler will look at __init__.py of the folder
import os

data_router = APIRouter(
    prefix='/api/v1/data',
    tags=["api_v1","data"]
)

@data_router.post("/upload/{project_id}")
async def upload_data( project_id: str,
                       file: UploadFile, 
                       app_settings: Settings = Depends(get_settings)):
    
    # validate file properties
    is_valid, result_signal = Data_Controller().validate_uploaded_files(file=file)

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal":result_signal
            }
        )


