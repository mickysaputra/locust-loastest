from locust import HttpUser, task, between, tag

class IrisWebhookHandler(HttpUser):
    wait_time = between(1, 5)

    @tag('iris_webhook_handler')
    @task
    def post_bank_account_validation(self):
        self.client.request_name = "IRIS Webhook Handler"
        headers = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjI2NjI3MDU1NjMsImp0aSI6ImhyVmZjR0V2TE9reWdwd0wiLCJpc3MiOiJlZmlzaGVyeS1zZXJ2aWNlLWF1dGgiLCJpZCI6MCwidXVpZCI6IjcwZmMxODNhLTEyZTMtNGMyNy1iMTQ3LTYxNmM4Mzg1MzA0NSIsInN1YiI6MCwiZW1haWwiOiJhbndhcnVkZGluLmthbWFsQGVmaXNoZXJ5LmNvbSIsIm5hbWUiOiJBbndhciBLYW1hbCBJYnJhaGltIiwicGhvbmUiOiIiLCJpc0FkbWluIjowLCJzdGF0dXMiOiIiLCJpc19uYmlvdCI6ZmFsc2UsInN1YmRpc3RyaWN0X2lkIjoiIiwicHJvdl9jb2RlIjowLCJjdXN0b21lcl9udW1iZXIiOiIiLCJhcHBfdXNlcl9pZCI6MCwidXNlcm5hbWUiOiIiLCJhZGRyZXNzIjoiIiwicGljdHVyZSI6IiIsImNvbXBhbnlfbmFtZSI6IiIsImNyZWF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsInVwZGF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsImxvY2F0aW9uIjoiIiwiaW50ZXJlc3QiOiIiLCJ2ZXJzaW9uIjoyLCJsZWFkX2lkIjoiIiwibGVhZF9uYW1lIjoiQW53YXIgS2FtYWwgSWJyYWhpbSIsInNsYWNrX2lkIjoiIiwiZG9tYWlucyI6W10sInJvbGVzIjpbXSwicGVybWlzc2lvbnMiOltdfQ.DZqjZOjdTI7FfHDmaL8GwnJz1McyMRzVHDQ0MfXR7yg",
            "Iris-Signature": "67af78ad6c84c6b865041125d244f84107ed8d9f74a93af46de15103cd2201b09abcda031259caf7fc838d03346dc9854d97bddbdea992765b5847acbd220b65"
        }

        url = "/public/v1/payout/status?company=MALL"
        self.client.post(url, headers=headers, json =
        {
            "reference_no": "J8P04DPoJz8e4pWUGf",
            "amount": "1980000.00",
            "status": "completed",
            "updated_at": "2023-05-25T08:20:33Z",
            "error_code": "",
            "error_message": ""
        })