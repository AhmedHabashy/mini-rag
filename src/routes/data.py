from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from helpers.config import get_settings,Settings
from controllers import Data_Controller, ProjectController # you didn't specify what to get from controller so the compiler will look at __init__.py of the folder
import os
from models import ResponseSignal
import aiofiles
import logging

logger = logging.getLogger('uvicorn.error')

data_router = APIRouter(
    prefix='/api/v1/data',
    tags=["api_v1","data"]
)

@data_router.post("/upload/{project_id}")
async def upload_data( project_id: str,
                       file: UploadFile, 
                       app_settings: Settings = Depends(get_settings)):
    
    # validate file properties
    data_controller = Data_Controller()
    is_valid, result_signal = data_controller.validate_uploaded_files(file=file)

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal":result_signal
            }
        )

    project_dir_path = ProjectController.get_project_path(project_id=project_id)
    file_path, file_id = data_controller.generate_unique_filename(
                orig_file_name=file.filename,
                project_id=project_id
                )

    try:
        async with open(file_path,"wb") as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:
        logger.error(f"Error while uploading file {e}")
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                'signal':ResponseSignal.FILE_UPLOAD_FAIL.value
            }
        )

    return JSONResponse(
        content={
            "signal": ResponseSignal.FILE_UPLOAD_SUCCESS.value,
            "file_id": file_id
        }
    )

