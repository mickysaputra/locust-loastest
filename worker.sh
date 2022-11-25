#!/bin/bash

#start second servvice here, and push it to background:
./health-checker --listener 0.0.0.0:8089 --script /mnt/health-check.sh &

#then run the last commands:
locust -f /mnt/locust/locustfiles --worker --master-host locust-loadtest--master.service.consul &

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?