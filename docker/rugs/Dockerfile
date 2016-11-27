FROM ubuntu:14.04
MAINTAINER chris elliott <ctelliott@gmail.com>

# Install some project specific stuff.
# Clean up APT when done
RUN apt-get update && \
    apt-get -y -q upgrade && \
    apt-get install --no-install-recommends -q -y \
  build-essential \
    python-dev \
    python-pip \
    libzmq-dev \
    supervisor \
    ntp \
    curl && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD ./requirements /requirements
RUN pip install -r /requirements/prod.txt

WORKDIR /app

CMD ["/bin/bash", "-l"]
