From locustio/locust:latest

COPY locustfiles /mnt/locust/locustfiles

CMD ["-f", "/mnt/locust/locustfiles", "--worker", "--master-host","locust-loadtest--master.service.consul"]
