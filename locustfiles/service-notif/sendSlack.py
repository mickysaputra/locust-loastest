from locust import HttpUser, task
import json

headers = {"Authorization": "Bearer " + "DSQYPS3c6emppJJ6x80JKYrZ9J3LNHtO", "x-client-id": "LOAD-TEST"}

class SlackNotif(HttpUser):
    @task
    def send_slack(self):
        with self.client.post("/slack/send", catch_response=True, json={"channel": "public-testing-bot", "content": "smoke test ian kirim slack new queue system", "mentions": ["U02DZ78MS4E"]},headers=headers) as response :
            if response.status_code != 200:
                response.failure('status code not 200')
            else :
                response.success()