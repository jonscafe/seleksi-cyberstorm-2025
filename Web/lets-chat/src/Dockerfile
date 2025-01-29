FROM php:8.0-apache
COPY app/ /var/www/html/
COPY flag/flag.txt /var/flag.txt

RUN chmod 600 /var/flag.txt
RUN docker-php-ext-install pdo pdo_mysql
EXPOSE 80
