from typing import Annotated

from fastapi import APIRouter, UploadFile, status
from fastapi.params import Depends

from app.auth.jwt import check_user_jwt
from app.auth.schemas import JWTData
from app.files.services import image_upload

files_router = APIRouter()


@files_router.post(path="/image", status_code=status.HTTP_201_CREATED)
async def upload_image(image: UploadFile, token: Annotated[JWTData, Depends(check_user_jwt)]):
    await image_upload(image, token)
    return {"file": image.filename}
