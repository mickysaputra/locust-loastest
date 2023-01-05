import random
import string
from locust import HttpUser, task

class FmsV2FileUpload(HttpUser):
    @task
    def upload(self):
        letters = string.ascii_lowercase

        headers = {
            'Authorization': 'Bearer 419vmKxA6KRbSeqcU4oGzwCPFTwxPIQp'
        }

        payload = {
            'files': (''.join(random.choice(letters) for i in range(10)), open('./locustfiles/fms-v2/file_average.file', 'rb')),
            'album': (None, 'load-test'),
            'bucket': (None, 'public-tools'),
            'private': (None, 'true')
        }

        self.client.post("/upload", files=payload, headers=headers)
