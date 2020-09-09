FROM python:3.6

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
RUN apt-get update && apt-get install -y --no-install-recommends apt-utils
RUN apt-get install -y llvm
RUN apt-get install -y libsndfile1
RUN pip3 install -r requirements.txt

EXPOSE 5000

COPY . .

CMD ["python", "main.py"]
