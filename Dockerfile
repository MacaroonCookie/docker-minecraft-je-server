FROM openjdk:8
LABEL maintainer="Seth Cook <cooker52@gmail.com>"

ENV MCVERSION=latest

EXPOSE 25565/tcp

RUN mkdir /minecraft /tmp/minecraft-meta

RUN apt-get update && apt-get install \
  python3

COPY minecraft-meta /tmp/minecraft-meta
RUN pip3 install /tmp/minecraft-meta

COPY run.sh /usr/sbin/minecraft-run.sh

ENTRYPOINT /usr/sbin/minecraft-run.sh
