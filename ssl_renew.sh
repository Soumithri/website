#!/bin/bash

/usr/local/bin/docker-compose -f ~/home/website/docker-compose.yml run certbot renew --dry-run \
&& /usr/local/bin/docker-compose -f ~/home/website/docker-compose.yml kill -s SIGHUP nginx
