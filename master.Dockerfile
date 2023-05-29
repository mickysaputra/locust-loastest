From locustio/locust:latest

RUN pip install redis

COPY locustfiles /mnt/locust/locustfiles

CMD ["-f", "/mnt/locust/locustfiles", "--class-picker", "--master"]
