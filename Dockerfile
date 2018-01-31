FROM alpine:edge

# Package Management
RUN apk update

# Build Dependencies
RUN apk add --update \
  build-base \
  jpeg-dev \
  python3 \
  python3-dev \
  yarn \
  zlib-dev

# Setup User
RUN adduser -D -s /bin/bash reverie
USER reverie
ENV PATH="/home/reverie/.local/bin:${PATH}"

# Copy Source
COPY --chown=reverie . /home/reverie
WORKDIR /home/reverie

# Install Dependencies
RUN yarn install
RUN pip3 install --user reverie -r requirements.txt

# Build
RUN ls -al ~/
RUN yarn run build

# Migrations
RUN python3 manage.py makemigrations campaign
RUN python3 manage.py migrate

# Run
EXPOSE 8000
ENTRYPOINT gunicorn reverie.wsgi:application --bind 0.0.0.0:8000
