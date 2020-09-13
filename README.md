# leaveproject
A Test of my ability to create a simple rest framework for employees and capturing leave

This API is created using Python with Django using Django Rest Framework

It is dockerised and should be run using docker and docker compose

Please make sure you have docker installed:
    https://docs.docker.com
    
Also, Please ensure you run the project in a virtual environment

### Setup

    git clone https://github.com/SoldierGamma/leaveproject.git
    
    docker-compose up -d
    
then in order to create the super user please identify the appropriate container using:

    docker ps

it should be the string of characters and numbers next to: *leaveproject_web*

then please run, replacing <container_string> with the string from the above step: 

    docker exec -t -i <container_string> bash

This will start up a shell inside the container

When inside the shell please run the code below and follow the prompts when creating a superuser

    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser

###Setup Done

You can now visit the API by going to the following link:

http://localhost:8000/api/


### Testing

to run tests, please make sure the containers are built and running, then run:

    pytest
    
