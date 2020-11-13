#!/bin/bash


unset DOCKER_HOST

docker build -t vpburchenya/http-inspect:v1.4 .
docker push vpburchenya/http-inspect:v1.4

