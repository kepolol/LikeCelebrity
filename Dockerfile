FROM python:3.7
MAINTAINER Anton Bykov 'anton35925@gmail.com'
RUN apt-get install -y libsm6 libxext6 libxrender-dev
COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt
ENTRYPOINT ["bash", "run.sh"]
