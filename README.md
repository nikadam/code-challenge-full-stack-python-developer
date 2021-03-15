# Picture Search By Geolocation

## Challenge Description 
Write a responsive application that search for pictures using Flickr API, based on user input and present the results.

This challenge is designed to test your ability to write code that inter-operates with a third-party API as well as develop a simple user interface.

## Challenge Specification
The user should be able to:
- Search for a location, and see the thumbnails of the first 10 photos available for that location. Navigation should be available to get the next 10 photos
- Perform the search either by entering latitude and longitude, or selecting a location from a preset list. Locations in the preset list should be represented by a human-readable name.
- Add entries to the preset list by supplying a longitude, latitude and name. **This list should be stored in the backend.
- Add photos in a search result to a favourites list. **This list should be stored in the backend.
- View thumbnails of the photos in the favourite list
- Your frontend should not connect to Flickr API directly.

## What we are looking for
How you design and structure an application given a set of requirements.

How you build maintainable code.

How does the final result look like and the user experience is considered.

## Frameworks
Any Python framework is acceptable - but the use of a framework is not required.

You can use any third party CSS frameworks to make your life easier.

Avoid using unnecessary libraries

## Build/Run
Use any build tools you prefer;

We want to easily run your application, so provide a brief description on how to build, run and test your project.

*Bonus points are given for how well you present this project's documentation.*

## Deliverables
Git repository (e.g.: Github, Bitbucket, etc)

Bonus for a live running version

## Hints
We don't have any time limit for this test, but we believe you can finish it within 30 hrs.

We would like to see a production quality project, ready to ship. 

Keep in mind edge cases and error handling. Let us see your understanding of it from code, build process and view design/layout point of views.

## References/Links
Flickr API: http://www.flickr.com/services/api/

OpenStreetMap: https://nominatim.openstreetmap.org/ (for getting sample lat-long values)

## Install
The instructions assume that you have already installed [Docker](https://docs.docker.com/installation/) and [Docker Compose](https://docs.docker.com/compose/install/). 

In order to get started be sure to clone this project onto your Machine. 

    
    git clone https://github.com/nikadam/code-challenge-full-stack-python-developer.git .

# Set the following values in a .env file

SECRET_KEY=+4!ew=onpd0c$di@laxt6wyb)l3@s3q!@0dt++@8l6n&i+0+vn </br>
ALLOWED_HOSTS=localhost 127.0.0.1 0.0.0.0 [::1]
ENGINE=django.db.backends.postgresql</br>
DB_NAME=flickr</br>
POSTGRES_USER=flickr</br>
POSTGRES_PASSWORD=flickr123</br>
DB_HOST=db</br>
DB_PORT=5432</br>
APP_PORT=8000</br>
DJANGO_SU_NAME=admin</br>
DJANGO_SU_EMAIL=admin@admin.com</br>
DJANGO_SU_PASSWORD=admin</br>

FLICKR_API_KEY=</br>

# How to get up and running
Once you've cloned the project to your host we can now start our code-challenge project. Easy! Navigate to the directory in which you cloned the project. Run the following commands from this directory 
    

    docker-compose up --build

Once Setup completed you can visit the website [Localhost](http://0.0.0.0:1300/)
</br>

The  docker-compose command will pull the images from Docker Hub and then link them together based on the information inside the docker-compose.yml file. This will create ports, links between containers, and configure applications as requrired. After the command completes we can now view the status of our stack

    docker-compose ps
