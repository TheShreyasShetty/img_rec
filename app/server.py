from fastapi import FastAPI
from fastapi import UploadFile, File
import uvicorn
from app.prediction import predict, preprocess, read_imagefile

app = FastAPI()

@app.get('/index')
def hello_world(name: str):
    return f"Hello {name}!"

@app.post("/predict/image")
async def predict_api(file: UploadFile = File(...)):
    allowed_extensions = ("jpg", "jpeg", "png")
    extension = file.filename.split(".")[-1]
    if extension not in allowed_extensions:
        return "Image must be jpg or png format!"
    image = read_imagefile(await file.read())
    image = preprocess(image)
    prediction = predict(image)
    return prediction

# @app.post('/api/predict')
# async def predict_image(file: UploadFile = File(...)):
    # image = read_image(await file) 
    # image = preprocess(image)
    # prediction = predict(image)
    # print(prediction)
    # return prediction

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host = '0.0.0.0')
