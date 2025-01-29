FROM php:8.1-apache

# Enable necessary PHP extensions
RUN apt-get update && apt-get install -y \
    libxml2-dev \
    && docker-php-ext-install dom

# Copy application files
COPY src/ /var/www/html/
COPY flag/ /var/flag/

# Set permissions
RUN chmod -R 755 /var/www/html && \
    chmod -R 600 /var/flag && \
    chown -R www-data:www-data /var/www/html /var/flag

RUN chmod -R 755 /var/flag && chown -R www-data:www-data /var/flag