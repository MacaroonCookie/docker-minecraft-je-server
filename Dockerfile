FROM openjdk:8

LABEL maintainer="Seth Cook <cooker52@gmail.com>"

RUN mkdir /minecraft /tmp/minecraft-meta

RUN apt-get update && apt-get install \
  python3

COPY minecraft-meta /tmp/minecraft-meta
RUN cd /tmp/minecraft-meta && python3 setup.py install

ENTRYPOINT /usr/sbin/minecraft-start.sh
