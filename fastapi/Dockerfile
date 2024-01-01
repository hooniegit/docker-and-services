FROM python:3.12-slim

# COPY REQUIREMENTS TO CONTAINER
COPY apt-requirements.txt /apt-requirements.txt
COPY pip-requirements.txt /pip-requirements.txt
COPY fastapi /fastapi

# APT UPDATE
RUN ["apt", "update"]

# INSTALL REQUIREMENTS
RUN ["xargs", "-a", "/apt-requirements.txt", "apt", "install", "-y"]
RUN ["pip", "install", "-r", "/pip-requirements.txt"]

# SET WORKDIR
WORKDIR /fastapi

# RUN CMD
CMD ["python", "main.py"]
