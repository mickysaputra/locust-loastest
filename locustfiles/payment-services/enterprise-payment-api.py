from locust import HttpUser, task, between, tag

class GetPaymentSummary(HttpUser):
    wait_time = between(1, 2)

    @tag('payment_summary')
    @task
    def get_payment_summary(self):
        self.client.request_name = "Payment Summary"
        headers = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjI2NjI3MDU1NjMsImp0aSI6ImhyVmZjR0V2TE9reWdwd0wiLCJpc3MiOiJlZmlzaGVyeS1zZXJ2aWNlLWF1dGgiLCJpZCI6MCwidXVpZCI6IjcwZmMxODNhLTEyZTMtNGMyNy1iMTQ3LTYxNmM4Mzg1MzA0NSIsInN1YiI6MCwiZW1haWwiOiJsaW5nZ2EuaGVyeWFkaUBlZmlzaGVyeS5jb20iLCJuYW1lIjoiTGluZ2dhIFNhdHlhIEhlcnlhZGkiLCJwaG9uZSI6IiIsImlzQWRtaW4iOjAsInN0YXR1cyI6IiIsImlzX25iaW90IjpmYWxzZSwic3ViZGlzdHJpY3RfaWQiOiIiLCJwcm92X2NvZGUiOjAsImN1c3RvbWVyX251bWJlciI6IiIsImFwcF91c2VyX2lkIjowLCJ1c2VybmFtZSI6IiIsImFkZHJlc3MiOiIiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EtL0FGZFp1Y3JzOWdqRXF0djJQcHBqTUlrNy1xOUpMcFJZZDdteFZBb2ZKWlRPPXM5Ni1jIiwiY29tcGFueV9uYW1lIjoiIiwiY3JlYXRlZF9hdCI6IjAwMDEtMDEtMDFUMDA6MDA6MDBaIiwidXBkYXRlZF9hdCI6IjAwMDEtMDEtMDFUMDA6MDA6MDBaIiwibG9jYXRpb24iOiIiLCJpbnRlcmVzdCI6IiIsInZlcnNpb24iOjIsImxlYWRfaWQiOiIiLCJsZWFkX25hbWUiOiJMaW5nZ2EgU2F0eWEgSGVyeWFkaSIsInNsYWNrX2lkIjoiIiwiZG9tYWlucyI6W10sInJvbGVzIjpbXSwicGVybWlzc2lvbnMiOltdfQ.CUiUINfYOb6lDVaU5LnUszvjaAF6Ry_vHvWtXwjbmcg"
        }
        url = "/public/v2/payment-summary/cdc5fe5b-6447-447c-9636-2cdffbd09f47"
        self.client.get(url, headers=headers)

class GetPayment(HttpUser):
    wait_time = between(1, 2)

    @tag('payment')
    @task
    def get_payment(self):
        self.client.request_name = "Payment"
        headers = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjI2NjI3MDU1NjMsImp0aSI6ImhyVmZjR0V2TE9reWdwd0wiLCJpc3MiOiJlZmlzaGVyeS1zZXJ2aWNlLWF1dGgiLCJpZCI6MCwidXVpZCI6IjcwZmMxODNhLTEyZTMtNGMyNy1iMTQ3LTYxNmM4Mzg1MzA0NSIsInN1YiI6MCwiZW1haWwiOiJsaW5nZ2EuaGVyeWFkaUBlZmlzaGVyeS5jb20iLCJuYW1lIjoiTGluZ2dhIFNhdHlhIEhlcnlhZGkiLCJwaG9uZSI6IiIsImlzQWRtaW4iOjAsInN0YXR1cyI6IiIsImlzX25iaW90IjpmYWxzZSwic3ViZGlzdHJpY3RfaWQiOiIiLCJwcm92X2NvZGUiOjAsImN1c3RvbWVyX251bWJlciI6IiIsImFwcF91c2VyX2lkIjowLCJ1c2VybmFtZSI6IiIsImFkZHJlc3MiOiIiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EtL0FGZFp1Y3JzOWdqRXF0djJQcHBqTUlrNy1xOUpMcFJZZDdteFZBb2ZKWlRPPXM5Ni1jIiwiY29tcGFueV9uYW1lIjoiIiwiY3JlYXRlZF9hdCI6IjAwMDEtMDEtMDFUMDA6MDA6MDBaIiwidXBkYXRlZF9hdCI6IjAwMDEtMDEtMDFUMDA6MDA6MDBaIiwibG9jYXRpb24iOiIiLCJpbnRlcmVzdCI6IiIsInZlcnNpb24iOjIsImxlYWRfaWQiOiIiLCJsZWFkX25hbWUiOiJMaW5nZ2EgU2F0eWEgSGVyeWFkaSIsInNsYWNrX2lkIjoiIiwiZG9tYWlucyI6W10sInJvbGVzIjpbXSwicGVybWlzc2lvbnMiOltdfQ.CUiUINfYOb6lDVaU5LnUszvjaAF6Ry_vHvWtXwjbmcg"
        }
        url = "/v2/payments/629ada69-970f-48b3-9933-262dfd0d2e67"
        self.client.get(url, headers=headers)