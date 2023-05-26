from locust import HttpUser, task, between, tag

class RetryReciept(HttpUser):
    wait_time = between(1, 5)

    @tag('retry_payout_receipt_durianpay)')
    @task
    def patch_retry_payout_receipt_durianpay(self):
        self.client.request_name = "Retry Payout Receipt Durianpay"
        headers = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjI2NjI3MDU1NjMsImp0aSI6ImhyVmZjR0V2TE9reWdwd0wiLCJpc3MiOiJlZmlzaGVyeS1zZXJ2aWNlLWF1dGgiLCJpZCI6MCwidXVpZCI6IjcwZmMxODNhLTEyZTMtNGMyNy1iMTQ3LTYxNmM4Mzg1MzA0NSIsInN1YiI6MCwiZW1haWwiOiJhbndhcnVkZGluLmthbWFsQGVmaXNoZXJ5LmNvbSIsIm5hbWUiOiJBbndhciBLYW1hbCBJYnJhaGltIiwicGhvbmUiOiIiLCJpc0FkbWluIjowLCJzdGF0dXMiOiIiLCJpc19uYmlvdCI6ZmFsc2UsInN1YmRpc3RyaWN0X2lkIjoiIiwicHJvdl9jb2RlIjowLCJjdXN0b21lcl9udW1iZXIiOiIiLCJhcHBfdXNlcl9pZCI6MCwidXNlcm5hbWUiOiIiLCJhZGRyZXNzIjoiIiwicGljdHVyZSI6IiIsImNvbXBhbnlfbmFtZSI6IiIsImNyZWF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsInVwZGF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsImxvY2F0aW9uIjoiIiwiaW50ZXJlc3QiOiIiLCJ2ZXJzaW9uIjoyLCJsZWFkX2lkIjoiIiwibGVhZF9uYW1lIjoiQW53YXIgS2FtYWwgSWJyYWhpbSIsInNsYWNrX2lkIjoiIiwiZG9tYWlucyI6W10sInJvbGVzIjpbXSwicGVybWlzc2lvbnMiOltdfQ.DZqjZOjdTI7FfHDmaL8GwnJz1McyMRzVHDQ0MfXR7yg"
        }
        url = "/public/v1/payout/generate-receipt/durianpay?reference_no=dis_pC4PIFx1vJ8015&company=SHRIMP&batch_item_id=dis_split_RUHt5wDjg35580"
        self.client.patch(url, headers=headers)

    @tag('retry_payout_receipt_iris)')
    @task
    def patch_retry_payout_receipt_iris(self):
        self.client.request_name = "Retry Payout Receipt IRIS"
        headers = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjI2NjI3MDU1NjMsImp0aSI6ImhyVmZjR0V2TE9reWdwd0wiLCJpc3MiOiJlZmlzaGVyeS1zZXJ2aWNlLWF1dGgiLCJpZCI6MCwidXVpZCI6IjcwZmMxODNhLTEyZTMtNGMyNy1iMTQ3LTYxNmM4Mzg1MzA0NSIsInN1YiI6MCwiZW1haWwiOiJhbndhcnVkZGluLmthbWFsQGVmaXNoZXJ5LmNvbSIsIm5hbWUiOiJBbndhciBLYW1hbCBJYnJhaGltIiwicGhvbmUiOiIiLCJpc0FkbWluIjowLCJzdGF0dXMiOiIiLCJpc19uYmlvdCI6ZmFsc2UsInN1YmRpc3RyaWN0X2lkIjoiIiwicHJvdl9jb2RlIjowLCJjdXN0b21lcl9udW1iZXIiOiIiLCJhcHBfdXNlcl9pZCI6MCwidXNlcm5hbWUiOiIiLCJhZGRyZXNzIjoiIiwicGljdHVyZSI6IiIsImNvbXBhbnlfbmFtZSI6IiIsImNyZWF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsInVwZGF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsImxvY2F0aW9uIjoiIiwiaW50ZXJlc3QiOiIiLCJ2ZXJzaW9uIjoyLCJsZWFkX2lkIjoiIiwibGVhZF9uYW1lIjoiQW53YXIgS2FtYWwgSWJyYWhpbSIsInNsYWNrX2lkIjoiIiwiZG9tYWlucyI6W10sInJvbGVzIjpbXSwicGVybWlzc2lvbnMiOltdfQ.DZqjZOjdTI7FfHDmaL8GwnJz1McyMRzVHDQ0MfXR7yg"
        }
        url = "/public/v1/payout/generate-receipt/iris?reference_no=HFlTMWWV2lIA1df8TF&company=FISH"
        self.client.patch(url, headers=headers)