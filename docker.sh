#!/bin/bash


unset DOCKER_HOST

docker build -t vpburchenya/http-inspect:v1.5 .
docker push vpburchenya/http-inspect:v1.5

