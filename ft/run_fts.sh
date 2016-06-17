#!/usr/bin/env bash
eval $(docker-machine env --shell bash)

docker build -t functionaltest .

docker run -it functionaltest
