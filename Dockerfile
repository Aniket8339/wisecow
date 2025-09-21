# Basic dockerfile for wisecow app
FROM ubuntu:20.04

# avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# install stuff we need
RUN apt-get update && apt-get install -y \
    cowsay \
    fortune-mod \
    netcat-openbsd \
    && apt-get clean

# add cowsay to path
ENV PATH="/usr/games:$PATH"

WORKDIR /app
COPY wisecow.sh .
RUN chmod +x wisecow.sh

EXPOSE 4499

CMD ["./wisecow.sh"]
