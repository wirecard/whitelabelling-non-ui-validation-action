FROM python:3.7

RUN pip install pycurl gitpython

COPY . /script
#COPY . /usr/bin/
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]