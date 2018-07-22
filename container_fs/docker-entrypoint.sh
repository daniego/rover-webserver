#!/bin/bash

envsubst '$UV4L_HOST' < /etc/nginx/nginx80.template > /etc/nginx/sites-enabled/nginx80

supervisord -n
