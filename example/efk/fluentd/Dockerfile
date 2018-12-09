FROM fluent/fluentd:v1.3-debian

RUN apt-get update
RUN apt-get install -y --no-install-recommends sudo make gcc g++ libc-dev ruby-dev
RUN sudo gem install fluent-plugin-elasticsearch
