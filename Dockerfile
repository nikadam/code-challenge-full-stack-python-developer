FROM python:3.8.3-alpine

ENV HOME_DIR=/home/app/code-challenge-full-stack-python-developer
ENV APP_USER=flickr
RUN addgroup -S $APP_USER && adduser -S $APP_USER -G $APP_USER
# set work directory


RUN mkdir -p $HOME_DIR
RUN mkdir -p $HOME_DIR/static

# where the code lives
WORKDIR $HOME_DIR

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk del build-deps \
    && apk --no-cache add musl-dev linux-headers g++
# install dependencies
RUN pip install --upgrade pip
# copy project
COPY . $HOME_DIR
RUN pip install -r requirements.txt
COPY ./entrypoint.sh $HOME_DIR

CMD ["/bin/bash", "/home/app/code-challenge-full-stack-python-developer/entrypoint.sh"]
