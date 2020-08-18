FROM python:2.7

RUN pip install virtualenv
ENV VIRTUAL_ENV=/opt/venv
RUN python -m virtualenv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PYTHONPATH="$PYTHONPATH:/home/naoqi_lib/pynaoqi-python2.7-2.5.5.5-linux64/lib/python2.7/site-packages"

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 9090

COPY . .

CMD ["python", "main.py"]
