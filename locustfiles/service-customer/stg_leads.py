from locust import HttpUser, task, between

headers_x = {'x-client-id': 'TEST-LOAD', 'X-App-Id': 'TEST-LOAD', 'Content-Type': 'application/json', 'X-App-Token': '419vmKxA6KRbSeqcU4oGzwCPFTwxPIQp'}

class SCGetLeadsSTG(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_leads(self):
        with self.client.get('/leads?limit=10&is_user=true&page=1', catch_response=True, headers=headers_x) as response:
            if response.status_code == 429:
                response.success() # if reach rate limiter, dont count as failed
            if response.status_code != 200:
                response.failure(response.content)