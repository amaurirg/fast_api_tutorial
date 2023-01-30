from fastapi import FastAPI, Form, File, UploadFile

app = FastAPI()

@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}


@app.post("/files/")
async def create_file(file: bytes = File()):
    print(file)
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    print(file)
    # import pdb; pdb.set_trace()
    return {"filename": file.filename}

