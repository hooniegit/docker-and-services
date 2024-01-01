# FastAPI

# Base
- Dockerfile
    - image: python:3.12-slim

# build
``` bash
# build
docker build -t fastapi-image .

# run
docker run -d -p 4000:8000 --name fastapi-container fastapi-image

# stop
docker stop fastapi-container
```

# result
<img width="441" alt="스크린샷 2024-01-01 오후 5 53 50" src="https://github.com/hooniegit/docker-and-services/assets/130134750/e069c42f-d57e-4646-ac68-d8a137b2edc5">
