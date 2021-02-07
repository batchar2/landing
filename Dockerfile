FROM python:3.9

RUN pip install --upgrade pip

WORKDIR /service
RUN mkdir -p /service
COPY requirements.txt /service

RUN pip3 install -r ./requirements.txt


COPY . /service

CMD /service/lp.sh
