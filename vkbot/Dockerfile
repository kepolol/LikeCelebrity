FROM python:3.7
MAINTAINER Anton Bykov 'anton35925@gmail.com'
RUN apt-get install -y libsm6 libxext6 libxrender-dev
COPY . /vkbot
WORKDIR /vkbot
RUN pip install -r requirements.txt
ENTRYPOINT ["bash"]
CMD ["run.sh"]
