FROM ubuntu:22.04


RUN apt-get update -y && apt-get dist-upgrade -y && apt-get install nginx -y

RUN cd /var/www/html && rm *.html

COPY . /var/www/html

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]


