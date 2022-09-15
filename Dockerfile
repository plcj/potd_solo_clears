FROM amancevice/pandas:1.4.3-alpine

COPY . /root/psc

WORKDIR /root/psc/

RUN pip install pytest==7.1.2
RUN pip install scrapy==2.6.2

ENV PYTHONPATH "${PYTHONPATH}:/psc"