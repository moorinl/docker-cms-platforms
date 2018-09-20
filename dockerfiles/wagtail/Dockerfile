FROM python:3.6.1
MAINTAINER R. Moorman <rob@moori.nl>

ENV DJANGO_SETTINGS_MODULE application.settings.docker

# Add user so that we run as non-root
RUN useradd --system --user-group app

# Add public directory for static and media files
RUN mkdir -p /public/media /public/static && chown -R app:app /public

# Install system packages
RUN pip install uwsgi==2.0.15

# Change working directory
WORKDIR /code/

# Copy wagtail project
COPY ./code/ /code/

# Install project requirements
RUN pip install .

# Collect static files
RUN manage.py collectstatic --noinput

# Add uwsgi configuration
COPY etc/uwsgi.ini /etc/uwsgi.ini

# Switch to app user
USER app

EXPOSE 8000

CMD /usr/local/bin/uwsgi --ini /etc/uwsgi.ini
