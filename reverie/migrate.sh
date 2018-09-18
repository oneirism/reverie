#!/bin/bash

sleep 10
pwd

ENV=${ENV:-"dev"}
pipenv run python manage.py makemigrations account campaign splash --settings reverie.settings.$ENV
pipenv run python manage.py migrate --noinput --settings reverie.settings.$ENV
