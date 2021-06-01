FROM python:3.7-stretch

# .@@set=block.init block.manager.kind=deps.docker.conf-v4.yml
# .@@set=block.content={{ shell "task deps:gen-blocks" }}
RUN apt-get update &&  apt-get install -y bash \
curl \
wget \
unzip \
git
# .@@set=block.over
RUN curl --help

RUN  cd /tmp/ \
     && curl --location https://taskfile.dev/install.sh \
     | sh && chmod +x ./bin/task \
     && mv ./bin/task /usr/local/bin/task
RUN  ls /usr/local/bin/task

COPY decks/local-test-ring/install.yq.exe.yml /decks/_install_scripts/install.yq.exe.yml

RUN task -t /decks/_install_scripts/install.yq.exe.yml -o prefixed
RUN yq4 -V

RUN curl https://rclone.org/install.sh | bash
RUN rclone version

RUN  echo 
