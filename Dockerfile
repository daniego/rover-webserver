FROM resin/rpi-raspbian
MAINTAINER Daniel Floris <daniel.floris@gmail.com>

RUN apt-get update && \
    apt-get install -y \
    nginx \
    python3 \
    python3-venv \
    # dev tools
    vim

ADD container_fs /
ADD webserver/ /srv/rover-webserver/webserver

RUN python3 -m venv /opt/rover-webserver
# && \
RUN apt install -y gcc libffi-dev
RUN /opt/rover-webserver/bin/pip install --upgrade pip setuptools
RUN apt install -y python3-dev
RUN apt install -y libssl-dev
RUN    /opt/rover-webserver/bin/pip install -r /srv/rover-webserver/webserver/requirements.txt && \
    echo "source /opt/rover-webserver/bin/activate" >> /root/.bashrc && \
    rm /etc/nginx/sites-enabled/default

WORKDIR /srv/rover-webserver

EXPOSE 80 443 8089

ENTRYPOINT /docker-entrypoint.sh
