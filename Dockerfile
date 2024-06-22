FROM python:3.9.6-slim

WORKDIR /app


# RUN apt -y update && apt -y upgrade
# RUN apt -y install libopencv-dev
RUN apt-get update && apt-get install -y \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libglib2.0-0 \
    libopencv-dev

RUN pip3 install opencv-python
RUN pip3 install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.4.0rc0-cp36-cp36m-linux_x86_64.whl

COPY requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "/main.py"]
