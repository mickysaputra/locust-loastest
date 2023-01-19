from locust import HttpUser, task
import json

headers = {"Authorization": "Bearer " + "DSQYPS3c6emppJJ6x80JKYrZ9J3LNHtO", "x-client-id": "LOAD-TEST"}

class OTPNotif(HttpUser):
    @task
    def send_OTP(self):
        otpBody = {
                    "sender": "EFISHERY",
                    "receivers": ["+6281320124992"],
                    "message": "test sms otp notif dev metrics counter and duration",
                    "message_type": "testing"
                }
        with self.client.post("/otp/send",
            catch_response=True, 
            data=json.dumps(otpBody),
            headers=headers) as response:
            if response.status_code != 200:
                response.failure('status code not 200')
            else :
                response.success()