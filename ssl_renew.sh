#!/bin/bash

/usr/local/bin/docker-compose -f /home/soumithri/home/website/docker-compose.yml run certbot renew \
&& /usr/local/bin/docker-compose -f /home/soumithri/home/website/docker-compose.yml kill -s SIGHUP nginx
