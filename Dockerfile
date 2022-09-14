FROM python:3.10.7-alpine3.16

COPY . /root/psc

WORKDIR /root/psc/

RUN pip install scrapy==2.6.2
RUN pip install pytest==7.1.2

ENV PYTHONPATH "${PYTHONPATH}:/psc"