#!/bin/sh

docker-compose down

docker image rm dog-shark-bot_bot

docker-compose up -d