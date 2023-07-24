### Credit https://github.com/networkop/docker-topo/blob/master/topo-extra-files/host/Dockerfile

FROM alpine:latest

RUN apk update && \
    apk add libteam && \
    apk add open-lldp && \
    apk add sudo && \
    apk add tcpdump && \
    apk add scapy && \
    apk add iperf3 && \
    apk add --update --no-cache openssh 

RUN adduser -u 1000 -G wheel -D alpine && \
    echo "%wheel ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \
    echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config && \
    adduser -u 1010 -G wheel -h /home/clab -s /bin/sh -D clab && \
    echo -n 'clab:clab' | chpasswd

COPY entrypoint.sh /home/alpine/
RUN chmod +x /home/alpine/entrypoint.sh

USER alpine 

ENTRYPOINT ["/home/alpine/entrypoint.sh"]
EXPOSE 22

CMD []