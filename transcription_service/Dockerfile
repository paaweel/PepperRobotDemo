FROM python:3.7
ENV GOOGLE_APPLICATION_CREDENTIALS="/tmp/keys/YT-Voice-Control.json"


ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
RUN pip3 install -r requirements.txt

EXPOSE 9090

COPY . .

CMD ["python", "main.py"]
