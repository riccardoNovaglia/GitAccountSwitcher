#!/usr/bin/env bash
eval $(docker-machine env --shell bash)

docker build -t functionaltest .

if [ $# -eq 1 ];
then
    echo "docker run -it functionaltest docker_tests:only='$1'"
    docker run -it functionaltest docker_tests:only=\'$1\'
else
    echo else
    docker run -it functionaltest
fi
