from pickle import FALSE
import time
import json

from zmq import NULL
from locust import HttpUser, task, between
import random

class TestGetData3(HttpUser):
    wait_time = between(1, 5)


    @task
    def get_data_demo3(self):

        self.client.request_name = "Sample_Get_Data_User"
        self.client.get('json/1',json=
        {

        },

                         headers={'Content-Type': 'application/json'})
