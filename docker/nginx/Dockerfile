FROM ubuntu:14.04
MAINTAINER chris elliott <ctelliott@gmail.com>

RUN apt-get update && \
	apt-get install --no-install-recommends -q -y --force-yes \
		supervisor \
		nginx \
		apache2-utils && \
	apt-get clean && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Add image configuration and scripts.
ADD supervisor/nginx.conf /etc/supervisor/conf.d/nginx.conf

# Add nginx config.
ADD config /var/config/nginx

# Create log files
RUN mkdir -p /var/log/nginx
RUN touch /var/log/nginx/access.log \
	/var/log/nginx/error.log \
	/var/log/nginx/stdout.log \
	/var/log/nginx/stderr.log

# Add docker-entrypoint.sh
COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
