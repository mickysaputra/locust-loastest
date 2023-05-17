from locust import HttpUser, task

class AuthV2RBACRemoteEnforcer(HttpUser):
    @task
    def remote_enforce_true(self):
        with self.client.post("/rbac/enforce", json={
            "action": "list",
            "domain": "test-dege",
            "resource": "uac",
            "user": "gede.sukma@efishery.com"
        }, headers={
            "X-App-Token": "DSQYPS3c6emppJJ6x80JKYrZ9J3LNHtO"
        }) as resp:
            print(resp.status_code)

    @task
    def remote_enforce_false(self):
        with self.client.post("/rbac/enforce", json={
            "action": "delete",
            "domain": "test-dege",
            "resource": "uac",
            "user": "gede.sukma@efishery.com"
        }, headers={
            "X-App-Token": "DSQYPS3c6emppJJ6x80JKYrZ9J3LNHtO"
        }) as resp:
            print(resp.status_code)
