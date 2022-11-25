import time
from locust import HttpUser, task, between
import random

class TestGetDocusign(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_digital_sign(self):

       
        self.client.get('/api/docsigns/5d3dc96e-d8ae-43d9-8608-6b3f7b744fd8?participant_id=2',json=
                            {},
                         headers={'x-client-version': '0.1.0', 'x-client-id': 'OCTO','Content-Type': 'application/json','Authorization': 'Bearer DSQYPS3c6emppJJ6x80JKYrZ9J3LNHtO'})


    