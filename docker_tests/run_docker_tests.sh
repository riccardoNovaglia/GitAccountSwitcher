#!/usr/bin/env bash

docker build -t functionaltest .

if [ $# -eq 1 ];
then
    docker run --rm functionaltest docker_tests:only=\'$1\'
else
    docker run --rm functionaltest
fi
