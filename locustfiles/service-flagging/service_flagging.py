from locust import HttpUser, task
import random

class ServiceFlagging(HttpUser):
    @task
    def evaluate_flag(self):
        user_id = random.randint(1, 10000)

        self.client.post("/api/v1/evaluation", json={
            "entityID": str(user_id),
            "entityType": "user",
            "entityContext": {
                "user_id": user_id
            },
            "enableDebug": False,
            "flagID": 3,
            "flagKey": ""
        })
