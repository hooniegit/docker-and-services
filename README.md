# docker-and-services
Trial &amp; Error To Build Services Using Docker <br><br>

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
