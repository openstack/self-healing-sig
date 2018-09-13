#!/bin/bash
set -ux

# Allow local registry, and restart docker
sed  -i -e "/^OPTIONS=/ s/'$/ --insecure-registry 192.168.1.101:5000'/" /etc/sysconfig/docker
systemctl restart docker

# Use `docker.io/rico/heat-container-agent-with-docker` if you not using `192.168.1.101:5000/heat-container-agent-with-docker`
# heat-docker-agent service
cat <<EOF > /etc/systemd/system/heat-container-agent.service

[Unit]
Description=Heat Container Agent
After=docker.service
Requires=docker.service

[Service]
TimeoutSec=5min
RestartSec=5min
User=root
Restart=on-failure
ExecStartPre=-/usr/bin/docker rm -f heat-container-agent-with-docker
ExecStartPre=-/usr/bin/docker pull 192.168.1.101:5000/heat-container-agent-with-docker
ExecStart=/usr/bin/docker run --name heat-container-agent-with-docker \\
--privileged \\
--net=host \\
-v /run/systemd:/run/systemd \\
-v /etc/sysconfig:/etc/sysconfig \\
-v /etc/systemd/system:/etc/systemd/system \\
-v /var/lib/heat-cfntools:/var/lib/heat-cfntools \\
-v /var/lib/cloud:/var/lib/cloud \\
-v /var/run/docker.sock:/var/run/docker.sock \\
-v /tmp:/tmp \\
-v /etc/hosts:/etc/hosts \\
192.168.1.101:5000/heat-container-agent-with-docker
ExecStop=/usr/bin/docker stop heat-container-agent-with-docker

[Install]
WantedBy=multi-user.target

EOF

# enable and start heat-container-agent
chmod 0640 /etc/systemd/system/heat-container-agent.service
/usr/bin/systemctl enable heat-container-agent.service
/usr/bin/systemctl start --no-block heat-container-agent.service
