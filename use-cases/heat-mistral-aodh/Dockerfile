FROM registry.fedoraproject.org/fedora:26
MAINTAINER “Rico Lin” <rico.lin.guanyu@gmail.com>
ENV container docker

RUN dnf -y --setopt=tsflags=nodocs install \
    redhat-rpm-config gcc python2-devel python3-devel docker findutils os-collect-config os-apply-config \
    os-refresh-config dib-utils python-pip python-docker-py \
    python-yaml python-zaqarclient && \
    dnf clean all

# pip installing dpath as python-dpath is an older version of dpath
# install docker-compose
RUN pip install --no-cache dpath docker-compose python-zaqarclient oslo.log psutil

ADD ./scripts/55-heat-config \
  /opt/stack/os-config-refresh/configure.d/

ADD ./scripts/50-heat-config-docker-compose \
  /opt/stack/os-config-refresh/configure.d/

ADD ./scripts/hooks/* \
  /var/lib/heat-config/hooks/

ADD ./scripts/heat-config-notify \
  /usr/bin/heat-config-notify

ADD ./scripts/configure_container_agent.sh /tmp/
RUN chmod 700 /tmp/configure_container_agent.sh
RUN /tmp/configure_container_agent.sh

#create volumes to share the host directories
VOLUME [ "/var/lib/cloud"]
VOLUME [ "/var/lib/heat-cfntools" ]

#set DOCKER_HOST environment variable that docker-compose would use
ENV DOCKER_HOST unix:///var/run/docker.sock

CMD /usr/bin/os-collect-config
