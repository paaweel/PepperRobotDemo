FROM ubuntu:20.04

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install apt-utils python2 iproute2 telnet iputils-ping curl
RUN curl https://bootstrap.pypa.io/get-pip.py --output get-pip.py
RUN python2 get-pip.py
RUN apt-get install -y libpython2.7
RUN apt-get install -y libatlas3-base

RUN pip2 install virtualenv
ENV VIRTUAL_ENV=/opt/venv
RUN python2 -m virtualenv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PYTHONPATH="$PYTHONPATH:/home/naoqi_lib/pynaoqi-python2.7-2.5.5.5-linux64/lib/python2.7/site-packages"
# ENV LD_LIBRARY_PATH="/home/naoqi_lib/pynaoqi-python2.7-2.5.5.5-linux64:$LD_LIBRARY_PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .

CMD ["python2", "main.py"]
