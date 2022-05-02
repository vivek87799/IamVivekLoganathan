FROM python:3.8-slim

COPY scripts /home/workdir
COPY requirements.txt /home/workdir

RUN apt-get update && apt-get install -y git
# RUN apt-get install ffmpeg libsm6 libxext6  -y


RUN pip install -r /home/workdir/requirements.txt

ENTRYPOINT [ "/bin/bash" ]