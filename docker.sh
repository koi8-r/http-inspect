#!/bin/bash


unset DOCKER_HOST

docker build -t vpburchenya/http-inspect .
docker push vpburchenya/http-inspect

