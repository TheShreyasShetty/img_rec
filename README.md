# Image Recognition API using FastAPI and Docker

This repository contains code for an Image Recognition API built with FastAPI and containerized using Docker. The API allows users to submit images and receive predictions based on the content of the images. Below are instructions to set up and use the API.

## Prerequisites

Before you proceed, make sure you have the following installed:

1. [Docker](https://www.docker.com/)
2. [Git](https://git-scm.com/)

## Getting Started

To get started, follow the steps below:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/image_Rec.git
```

2. Navigate to the cloned repository:

```bash
cd image_Rec
```

3. Build the Docker image:

```bash
docker build -t image_recognition_api.
```

4. Run the Docker container:

```bash
docker run -d -p 8000:8000 --name image_api image_recognition_api
```

The API should now be up and running on http://localhost:8000.

## API Documentation

To interact with the API, you can use the provided Swagger documentation. Open your web browser and go to:

```
http://localhost:8000/docs
```

This interactive page will allow you to test the API, submit image files, and see the responses. It provides a user-friendly interface to explore and interact with the API endpoints.

## Making API Requests

In addition to using the Swagger UI, you can also interact with the API programmatically using HTTP requests. Below is an example using Python's `requests` library:

```python
import requests

api_url = "http://localhost:8000/predict"

# Replace 'path/to/your/image.jpg' with the actual path to your image file
image_file_path = "path/to/your/image.jpg"

files = {"file": open(image_file_path, "rb")}
response = requests.post(api_url, files=files)

if response.status_code == 200:
    predictions = response.json()
    print(predictions)
else:
    print("Failed to get predictions. Status code:", response.status_code)
```

## Customization

If you want to use a different machine-learning model for image recognition, you can modify the relevant code in the FastAPI app (`app/main.py`). You can also customize the Dockerfile if you need to include additional dependencies or configurations.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This project was built with the help of FastAPI and Docker. Thanks to their respective communities for providing excellent tools and documentation.
