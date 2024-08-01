import os

from fastapi import UploadFile
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from dotenv import load_dotenv
from os import getenv
from os.path import join, dirname, normpath

dotenv_path = normpath(join(dirname(__file__), '..', '.env'))
load_dotenv(dotenv_path)

SECRET_KEY = getenv("SECRET_KEY")
HASH_ALGORITHM = getenv("HASH_ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/token')

STATIC_PATH = os.path.join(os.getcwd(), 'Backend', 'Static')
os.makedirs(STATIC_PATH, exist_ok=True)


async def save_file(path: os.path, file: UploadFile):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(await file.read())


IMAGE_EXTENSIONS = [".jpeg", ".jpg", ".jpe", ".png", ".gif", ".bmp", ".tif", ".tiff", ".webp", ".svg", ".heif", ".heic",
                    ".raw", ".arw", ".cr2", ".nrw", ".k25", ".ico", ".jfif", ".ppm", ".pgm", ".pbm", ".pnm", ".eps",
                    ".dng"]

AUDIO_EXTENSIONS = [".mp3", ".wav", ".wma", ".flac", ".aac", ".m4a", ".ogg", ".oga", ".opus", ".weba", ".3gp", ".amr",
                    ".awb", ".flac", ".m4a", ".mpc", ".ogg", ".opus", ".ra", ".rm", ".wav", ".wma"]

ACCEPTED_FILE_EXTENSIONS = IMAGE_EXTENSIONS + AUDIO_EXTENSIONS