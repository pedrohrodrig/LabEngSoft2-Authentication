#!/bin/bash

DRY_RUN=$1

echo "cd backend..."
# Skip actual git pull in dry run
[ "$DRY_RUN" != "true" ] && cd backend

echo "Installing pipenv..."
# Skip actual installation in dry run
[ "$DRY_RUN" != "true" ] && python3 -m pip install pipenv 

echo "Installing dependencies..."
# Skip actual installation in dry run
[ "$DRY_RUN" != "true" ] && pipenv install  

echo "Running migrations..."
# Skip actual migrations in dry run
[ "$DRY_RUN" != "true" ] && pipenv run python manage.py migrate

echo "Runserver..."
# Skip actual restart in dry run
[ "$DRY_RUN" != "true" ] && screen -d -m pipenv run python manage.py runserver 0.0.0.0:8000

echo "Redirect port..."
# Skip actual restart in dry run
[ "$DRY_RUN" != "true" ] && sudo iptables -t nat -I PREROUTING -p tcp --dport 80 -j REDIRECT --to-ports 8000

echo "Deployment complete."