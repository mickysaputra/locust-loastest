from locust import HttpUser, task
import json

headers = {"Authorization": "Bearer " + "DSQYPS3c6emppJJ6x80JKYrZ9J3LNHtO", "x-client-id": "LOAD-TEST"}

class WANotif(HttpUser):
    @task
    def send_WA(self):
        waBody = {
                    "receiver": "6281320124992",
                    "receiver_name": "yan",
                    "template_name": "test_button_image",
                    "template_id": "7dc26adc-b2c7-43e8-b280-c79f7faca30d",
                    "data": {
                        "1": "ian queue baru local"
                    },
                    "buttons": [{
                        "index": "0",
                        "type": "url",
                        "value": "career"
                    }],
                    "header": {
                        "format": "IMAGE",
                        "params": [
                        {
                            "key": "url",
                            "value": "https://efishery.com/wp-content/uploads/2022/01/Blog-Cover.png"
                        },
                        {
                            "key": "filename",
                            "value": "cover.png"
                        }]
                    },
                    "message_type": "WA-test"
                }
    
        with self.client.post("/whatsapp/v3/send", 
            catch_response=True,
            data=json.dumps(waBody),
            headers={"Authorization": "Bearer " + "419vmKxA6KRbSeqcU4oGzwCPFTwxPIQp" }) as response :
            if response.status_code != 200:
                response.failure('status code not 200')
            else :
                response.success()