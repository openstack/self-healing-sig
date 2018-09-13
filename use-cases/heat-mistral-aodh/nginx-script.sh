#!/bin/sh -x

# use docker pull nginx if you not using local registry hub
docker pull 192.168.1.101:5000/nginx
docker run -d --name nginx-container -p 80:80 192.168.1.101:5000/nginx

echo "Rico Lin said hello from Vietnam InfraDay to $host::$version" > rico.html
docker cp $PWD/rico.html nginx-container:/usr/share/nginx/html/
cat rico.html > $heat_outputs_path.result

echo "Output to stderr" 1>&2
