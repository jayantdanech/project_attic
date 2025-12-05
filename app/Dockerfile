FROM python:3.11-slim

# Variables
ENV APP_USER=appuser
ENV APP_HOME=/app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8080

# Install Dependencies
RUN set -eux \
&& apt-get update \
&& apt-get install -y --no-install-recommends build-essential ca-certificates
RUN rm -rf /var/lib/apt/lists/*
RUN addgroup --system $APP_USER \
&& adduser --system --ingroup $APP_USER --home $APP_HOME --shell /usr/sbin/nologin $APP_USER
RUN mkdir -p $APP_HOME

WORKDIR $APP_HOME

# Copy & Install requirements for dependency built
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt 

# Copy app codes
COPY app.py ./

# non-root user permissions & work
RUN chown -R $APP_USER:$APP_USER $APP_HOME
USER $APP_USER

EXPOSE $PORT
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8080", "--workers", "1", "--threads", "4"]
