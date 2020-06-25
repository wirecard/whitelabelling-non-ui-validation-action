FROM python:3.7

RUN pip install pycurl gitpython

COPY . /script
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]