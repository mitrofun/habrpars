FROM alpine:3.8

COPY . /lib/habrpars

RUN apk update && apk add --update --no-cache --progress \
    make \
    python3 \
    ca-certificates \
    bash bash-completion \
    && update-ca-certificates 2>/dev/null || true \
    && apk add --no-cache --virtual=.build-dependencies \
    python3-dev \
    && pip3 install --upgrade pip setuptools \
    && pip3 install --no-cache-dir -r /lib/habrpars/requirements/qa.txt

WORKDIR /lib/habrpars
