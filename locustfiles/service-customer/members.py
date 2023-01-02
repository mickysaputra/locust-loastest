from locust import HttpUser, task, between
import time

headers_x = {'X-Xlient-Id': 'TEST-LOAD', 'X-App-Id': 'TEST-LOAD', 'Content-Type': 'application/json', 'X-App-Token': 'DSQYPS3c6emppJJ6x80JKYrZ9J3LNHtO'}

class SCGetMembers(HttpUser):
    wait_time = between(1, 3)

    @task
    def get_members(self):
        self.client.get('/members?limit=10&is_user=true&page=1', headers=headers_x)