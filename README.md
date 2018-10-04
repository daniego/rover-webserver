# rover-webserver

This is container to serve the admin web content

# Build local container
docker build -t rover-webserver .


# Run container

# Run container with local code
docker run -it -p 80:80 -p 443:443 -p 8089:8089 -v `pwd`:/srv/rover-webserver -v `pwd`/container_fs/etc/nginx/nginx80.template:/etc/nginx/nginx80.template -e UV4L_HOST="192.168.178.101" -e ENGINE_HOST="192.168.178.242:8089" rover-webserver

# Run and login

# Run and login with local code
docker run -it -p 80:80 -p 443:443 -p 8089:8089 -v `pwd`:/srv/rover-webserver -v `pwd`/container_fs/etc/nginx/nginx80.template:/etc/nginx/nginx80.template --entrypoint="bash" -e UV4L_HOST="192.168.178.101" rover-webserver

# Login into the container





# Get camera info
Note: the camera is not recognized in live mode
docker run -it --device=/dev/bus/usb/`lsusb | grep Ricoh|awk {'print $2'}`/`lsusb | grep Ricoh|awk {'print $4'}|sed 's/:$//'` thetacontroller ptpcam -l

# read camera info
ptpcam -l


/etc/ssl/private/nginx-selfsigned.key

# TODO
set BLE service and characteristics via environment variable
