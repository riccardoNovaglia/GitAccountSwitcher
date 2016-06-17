FROM ubuntu:15.04

RUN apt-get update -y && apt-get install -y \
    git \
    openssh-client \
    python \
    python-pip \
    python-dev \
    build-essential

RUN pip install --upgrade pip \
    && pip install --upgrade virtualenv \
    && pip install --upgrade fabric

ENV GIT_SWITCH_PATH /gitAccountSwitcher
WORKDIR $GIT_SWITCH_PATH

COPY fabfile.py requirements.txt $GIT_SWITCH_PATH/
RUN fab setup_env

COPY . $GIT_SWITCH_PATH

ENTRYPOINT ["fab"]
CMD ["docker_ft"]
