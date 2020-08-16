FROM python:3.6

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN mkdir -p /home/service/src
WORKDIR /home/service/src
ADD . /home/service/src

RUN pip install -r requirements.txt

EXPOSE 9090

CMD ["python", "/home/service/src/main.py"]
