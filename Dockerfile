FROM amancevice/pandas:1.4.3-alpine

COPY . /root/ddlb

WORKDIR /root/ddlb/

RUN pip3 install pytest==7.2.1
RUN pip3 install scrapy==2.7.1

ENV PYTHONPATH "${PYTHONPATH}:/ddlb"