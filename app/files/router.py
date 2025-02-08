from fastapi import APIRouter, UploadFile, status
from app.files.services import image_upload

files_router = APIRouter()


@files_router.post(path="/image", status_code=status.HTTP_201_CREATED)
async def upload_image(image: UploadFile):
    await image_upload(image)
    return {"file": image.filename}
