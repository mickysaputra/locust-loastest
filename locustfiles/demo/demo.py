from pickle import FALSE
import time
import json

from zmq import NULL
from locust import HttpUser, task, between
import random

class TestSampleShrimp(HttpUser):
    wait_time = between(1, 5)


    @task
    def get_sample_shrimp(self):

        self.client.request_name = "Sample_Get_Data_User"
        self.client.post('/api/users',json=
        {

            "name": "morpheus",
            "job": "leader"

        },

                         headers={'Content-Type': 'application/json'})
