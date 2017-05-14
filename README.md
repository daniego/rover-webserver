# rover-webserver

This is container to serve the amin web content

# Build local container
docker build -t roverwebserver .

# Login into the container
docker run -it --entrypoint="bash" roverwebserver
docker run -it -p 80:80 -p 8089:8089 -v /my_projects_repo/rover-webserver:/srv/rover-webserver roverwebserver
# Get camera info
Note: the camera is not recognized in live mode
docker run -it --device=/dev/bus/usb/`lsusb | grep Ricoh|awk {'print $2'}`/`lsusb | grep Ricoh|awk {'print $4'}|sed 's/:$//'` thetacontroller ptpcam -l

# read camera info
ptpcam -l
