FROM amancevice/pandas:1.4.3-alpine

COPY . /root/ddlb

WORKDIR /root/ddlb/

RUN pip install pytest==7.2.1
RUN pip install scrapy==2.7.1

ENV PYTHONPATH "${PYTHONPATH}:/ddlb"