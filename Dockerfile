FROM python:3.7-alpine
MAINTAINER Recipe App Advanced

# tell python not buffer, for python will not allow python to buffer the outputs (print directly)
ENV PYTHONUNBUFFERED 1
#  include all the dependencies
# copy from directory adjacent to the Dockerfile, and copy from image to /requirements.txt
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# create and make "/app" to DEFAULT directory
RUN  mkdir /app
WORKDIR /app
#  copy /app from LOCAL to docker-IMAGE
COPY ./app /app

# for SECURITY, use just used for RUNNING app ONLY.
# NOT have home directory , don't allow IMAGE run app using ROOT ACCOUNT
RUN adduser -D user
USER user
