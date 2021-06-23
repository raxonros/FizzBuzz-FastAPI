# FizzBuzz-FastAPI

Project for the deployment of an API server in python3 (Fast-API) to query the FizzBuzz entity.

```
{
  "number": 1,
  "fizzbuzz": null,
  "placeholder_post": {
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  }
}
```
The value of placeholder_post gets the data from the Endpoint api `https://jsonplaceholder.typicode.com/posts/{n}`

This server consists of two EPs `/fizzbuzz/{n}` and `/fizzbuzzList`.
The first returns the entity fizzbuzzz of number n and the second returns the first 10 entities fizzbuzz.

## Project struct
📦FizzBuzz-FastAPI
 ┣ 📂app
 ┃ ┣ 📜fizzbuzz.py
 ┃ ┣ 📜main.py
 ┃ ┣ 📜plazeholder.py
 ┃ ┗ 📜test_main.py
 ┣ 📜Dockerfile
 ┣ 📜README.md
 ┗ 📜requirements.txt

## Deploy and Testing
- First you need to install the dependencies with the command `pip3 install -r requirementes.txt`
- You can run the program in two ways, by running the command python3 `./app/main.py` or by running the command  `uvicorn main:app` inside the `./app` directory. In both ways to raise an instance on the server that by default listens on port 8000
- If you want to run the tests go to the app directory and run the command `pytest -v`

## Deploy with Docker
- If you want to deploy the service as a docker application, you can do so by generating the image with command `docker build -t <image_name> .` and creating container `docker run -d --name <container_name> -p 80:80 <image_name`.
- In this way you will have a docker listening on port 80 for requests to the service