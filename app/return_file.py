import os.path

from fastapi import FastAPI
from fastapi.responses import FileResponse

some_file_path = "/home/amauri/fast_api_tutorial/app/tests/response_wooba/"
filename = "trecho_wooba.py"
app = FastAPI()


@app.get("/arquivo")
async def arquivo():
    full_path = os.path.join(some_file_path, filename)
    return FileResponse(path=full_path, media_type="application/octet-stream", filename=filename)
