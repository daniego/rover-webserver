FROM resin/rpi-raspbian
MAINTAINER Daniel Floris <daniel.floris@gmail.com>

RUN apt-get update && \
    apt-get install -y \
    nginx \
    python3 \
    python3-venv

ADD webserver/requirements.txt /srv/rover-webserver/requirements.txt
RUN python3 -m venv /opt/rover-webserver && \
    cd /srv/rover-webserver && \
    /opt/rover-webserver/bin/pip install -r requirements.txt

RUN echo "source /opt/rover-webserver/bin/activate" >> /root/.bashrc


ADD etc/nginx/sites-enabled/nginx80 /etc/nginx/sites-enabled/nginx80
RUN rm /etc/nginx/sites-enabled/default
ADD etc/supervisor/conf.d/webserver.conf /etc/supervisor/conf.d/webserver.conf

ADD webserver/ /srv/rover-webserver/webserver

WORKDIR /srv/rover-webserver

EXPOSE 80 8089

ENTRYPOINT /opt/rover-webserver/bin/python /srv/rover-webserver/webserver/main.py
