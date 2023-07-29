FROM python:3.9
RUN pip3 install fastapi uvicorn pillow numpy tensorflow python-multipart
COPY ./app /app
CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "15400"]
