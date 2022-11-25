#!/bin/sh

# Start the first process
./health-checker --listener 0.0.0.0:8089 --script /mnt/health-check.sh

# Start the second process
locust -f /mnt/locust/locustfiles --worker --master-host locust-loadtest--master.service.consul