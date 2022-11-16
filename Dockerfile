FROM python:3.10-slim

COPY ./build /views
COPY ./requirements.txt /requirements.txt

RUN apt-get update && \
    apt-get install -y \
        build-essential \
        python3-setuptools \
        tesseract-ocr \
        make \
        gcc \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2 \
    &&  python3 -m pip install -r requirements.txt \
    && apt-get remove -y --purge make gcc build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 8000


CMD ["python", "manage.py", "runserver"]