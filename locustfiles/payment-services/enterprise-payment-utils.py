from locust import HttpUser, task, between, tag

class PaymentServiceUtils(HttpUser):
    wait_time = between(1, 5)

    @tag('get_iris_bank_list_information')
    @task
    def get_iris_bank_list_information(self):
        self.client.request_name = "IRIS Bank List Information"
        headers = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjI2NjI3MDU1NjMsImp0aSI6ImhyVmZjR0V2TE9reWdwd0wiLCJpc3MiOiJlZmlzaGVyeS1zZXJ2aWNlLWF1dGgiLCJpZCI6MCwidXVpZCI6IjcwZmMxODNhLTEyZTMtNGMyNy1iMTQ3LTYxNmM4Mzg1MzA0NSIsInN1YiI6MCwiZW1haWwiOiJhbndhcnVkZGluLmthbWFsQGVmaXNoZXJ5LmNvbSIsIm5hbWUiOiJBbndhciBLYW1hbCBJYnJhaGltIiwicGhvbmUiOiIiLCJpc0FkbWluIjowLCJzdGF0dXMiOiIiLCJpc19uYmlvdCI6ZmFsc2UsInN1YmRpc3RyaWN0X2lkIjoiIiwicHJvdl9jb2RlIjowLCJjdXN0b21lcl9udW1iZXIiOiIiLCJhcHBfdXNlcl9pZCI6MCwidXNlcm5hbWUiOiIiLCJhZGRyZXNzIjoiIiwicGljdHVyZSI6IiIsImNvbXBhbnlfbmFtZSI6IiIsImNyZWF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsInVwZGF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsImxvY2F0aW9uIjoiIiwiaW50ZXJlc3QiOiIiLCJ2ZXJzaW9uIjoyLCJsZWFkX2lkIjoiIiwibGVhZF9uYW1lIjoiQW53YXIgS2FtYWwgSWJyYWhpbSIsInNsYWNrX2lkIjoiIiwiZG9tYWlucyI6W10sInJvbGVzIjpbXSwicGVybWlzc2lvbnMiOltdfQ.DZqjZOjdTI7FfHDmaL8GwnJz1McyMRzVHDQ0MfXR7yg"
        }
        url = "/public/v2/midtrans/bank-list"
        self.client.get(url, headers=headers)

    @tag('post_bank_account_validation')
    @task
    def post_bank_account_validation(self):
        self.client.request_name = "Bank Account Validation"
        headers = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjI2NjI3MDU1NjMsImp0aSI6ImhyVmZjR0V2TE9reWdwd0wiLCJpc3MiOiJlZmlzaGVyeS1zZXJ2aWNlLWF1dGgiLCJpZCI6MCwidXVpZCI6IjcwZmMxODNhLTEyZTMtNGMyNy1iMTQ3LTYxNmM4Mzg1MzA0NSIsInN1YiI6MCwiZW1haWwiOiJhbndhcnVkZGluLmthbWFsQGVmaXNoZXJ5LmNvbSIsIm5hbWUiOiJBbndhciBLYW1hbCBJYnJhaGltIiwicGhvbmUiOiIiLCJpc0FkbWluIjowLCJzdGF0dXMiOiIiLCJpc19uYmlvdCI6ZmFsc2UsInN1YmRpc3RyaWN0X2lkIjoiIiwicHJvdl9jb2RlIjowLCJjdXN0b21lcl9udW1iZXIiOiIiLCJhcHBfdXNlcl9pZCI6MCwidXNlcm5hbWUiOiIiLCJhZGRyZXNzIjoiIiwicGljdHVyZSI6IiIsImNvbXBhbnlfbmFtZSI6IiIsImNyZWF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsInVwZGF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsImxvY2F0aW9uIjoiIiwiaW50ZXJlc3QiOiIiLCJ2ZXJzaW9uIjoyLCJsZWFkX2lkIjoiIiwibGVhZF9uYW1lIjoiQW53YXIgS2FtYWwgSWJyYWhpbSIsInNsYWNrX2lkIjoiIiwiZG9tYWlucyI6W10sInJvbGVzIjpbXSwicGVybWlzc2lvbnMiOltdfQ.DZqjZOjdTI7FfHDmaL8GwnJz1McyMRzVHDQ0MfXR7yg"
        }
        url = "/v1/account-validation"
        self.client.post(url, headers=headers, json =
        {
            "bank": "cimb",
            "number": "222233334444"
        })