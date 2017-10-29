FROM resin/rpi-raspbian
MAINTAINER Daniel Floris <daniel.floris@gmail.com>

# RUN echo "deb http://nginx.org/packages/mainline/debian/ codename nginx" >> /etc/apt/sources.list.d/nginx.list
# RUN echo "deb-src http://nginx.org/packages/mainline/debian/ codename nginx" >> /etc/apt/sources.list.d/nginx.list


RUN apt-get update && \
    apt-get install -y \
    nginx \
    python3 \
    python3-venv \
    # dev tools
    vim

ADD webserver/requirements.txt /srv/rover-webserver/requirements.txt
RUN python3 -m venv /opt/rover-webserver && \
    cd /srv/rover-webserver && \
    /opt/rover-webserver/bin/pip install -r requirements.txt

RUN echo "source /opt/rover-webserver/bin/activate" >> /root/.bashrc

RUN rm /etc/nginx/sites-enabled/default

ADD container_fs /
ADD webserver/ /srv/rover-webserver/webserver

WORKDIR /srv/rover-webserver

EXPOSE 80 443 8089

ENTRYPOINT /docker-entrypoint.sh
