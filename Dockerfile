FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN apt -y update && apt -y upgrade
RUN apt -y install libopencv-dev
RUN conda install opencv -c conda-forge
RUN pip3 install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.4.0rc0-cp36-cp36m-linux_x86_64.whl

CMD python3 /main.py
