import os
from uuid import uuid4

import aiofiles
from fastapi import UploadFile

from app.auth.exceptions import AuthRequired
from app.auth.schemas import JWTData


async def image_upload(file: UploadFile, token: JWTData):
    if not token:
        raise AuthRequired()
    unique_filename = f"{uuid4()}_{file.filename}"
    file_path = os.path.join("static/images", unique_filename)
    async with aiofiles.open(file_path, mode="w+b") as buffer:
        await buffer.write(await file.read())
