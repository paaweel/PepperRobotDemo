FROM python:3.6

RUN mkdir -p /home/service/src
WORKDIR /home/service/src
ADD . /home/service/src
RUN pip install -r requirements.txt

EXPOSE 9090
CMD ["python", "/home/service/src/main.py"]
