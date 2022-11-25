From locustio/locust:latest


COPY locustfiles /mnt/locust/locustfiles

COPY --chown=locust:locust health-checker health-checker
COPY --chown=locust:locust health-check.sh /mnt/health-check.sh
COPY --chown=locust:locust worker.sh worker.sh

ENTRYPOINT []

CMD ["sh","./worker.sh"]