FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    cowsay \
    fortune-mod \
    netcat-openbsd \
    && apt-get clean

ENV PATH="/usr/games:$PATH"

WORKDIR /app
COPY wisecow.sh .
RUN chmod +x wisecow.sh

EXPOSE 4499
CMD ["./wisecow.sh"]