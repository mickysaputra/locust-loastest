From locustio/locust:latest


COPY locustfiles /mnt/locust/locustfiles

COPY health-checker health-checker
COPY health-check.sh /mnt/health-check.sh
COPY worker.sh worker.sh

ENTRYPOINT []

CMD ["./worker.sh"]