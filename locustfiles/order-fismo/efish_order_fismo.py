from locust import HttpUser, task, between


class CreateOrderFismo(HttpUser):
    wait_time = between(1, 3)
    headers = {
        #UAT
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTE0NzA2NjQsImp0aSI6IjhhMDQzMmE4LTdhNjktNDQxNC04OThhLTE3MGU5OWY1MTg4NyIsImlzcyI6ImVmaXNoZXJ5LXNlcnZpY2UtYXV0aC12MiIsInRva2VuX3R5cGUiOiJhY2Nlc3MtdG9rZW4iLCJyZWlzc3VlIjpmYWxzZSwiaXNfZGF0YV9zb3VyY2UiOmZhbHNlLCJkYXRhX3NvdXJjZV91c2VyX2RhdGEiOiIiLCJpZCI6MCwidXVpZCI6IjUzZmI3NDVhLWQ5ZWQtNDllZC1hMDMzLTU4ZWQ1ZjJmZjVhZCIsInN1YiI6MCwiZW1haWwiOiJoYXJ5YW5hQGVmaXNoZXJ5LmNvbSIsIm5hbWUiOiJIYXJ5YW5hIiwicGhvbmUiOiIiLCJpc19hZG1pbiI6ZmFsc2UsInN0YXR1cyI6IiIsImlzX25iaW90IjpmYWxzZSwic3ViZGlzdHJpY3RfaWQiOiIiLCJwcm92X2NvZGUiOjAsImN1c3RvbWVyX251bWJlciI6IiIsImFwcF91c2VyX2lkIjowLCJ1c2VybmFtZSI6IiIsImFkZHJlc3MiOiIiLCJwaWN0dXJlIjoiIiwiY29tcGFueV9uYW1lIjoiIiwiY3JlYXRlZF9hdCI6IjAwMDEtMDEtMDFUMDA6MDA6MDBaIiwidXBkYXRlZF9hdCI6IjAwMDEtMDEtMDFUMDA6MDA6MDBaIiwibG9jYXRpb24iOiIiLCJpbnRlcmVzdCI6IiIsInZlcnNpb24iOjIsImxlYWRfaWQiOiIiLCJsZWFkX25hbWUiOiIiLCJzbGFja19pZCI6IlUwMjcxUFdCNDJFIiwiYXBwX3Rva2VuIjoiIiwiaXNfaW50ZXJuYWxfdXNlciI6dHJ1ZSwiYXBwX3VzZXJfcm9sZXMiOm51bGwsInVhY19yb2xlcyI6W10sInVhY19wZXJtaXNzaW9ucyI6WyJhODFhOWFiMC0yNGUxLTQ2NTUtYWJmOC0xMmMyNDAwMjZhYTgiXSwiZG9tYWlucyI6bnVsbCwicm9sZXMiOm51bGwsInBlcm1pc3Npb25zIjpudWxsLCJjbGllbnRfaWQiOiI3ZTYyNjE5NS05ZWY1LTRmMzAtOWIxNC1lMDg1MGM4MTUwYTQifQ.N0_tAde7wMMNtwB_u5bPS_bSJqFASzA0Ct7c8cwPtjA",
        #"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTE0NjYyNjYsImp0aSI6IjkxZTdmN2NiLWY1YWMtNDdkNi05NGEzLTQ2Yzc1Y2M0ODcyYSIsImlzcyI6ImVmaXNoZXJ5LXNlcnZpY2UtYXV0aC12MiIsInRva2VuX3R5cGUiOiJhY2Nlc3MtdG9rZW4iLCJyZWlzc3VlIjpmYWxzZSwiaXNfZGF0YV9zb3VyY2UiOmZhbHNlLCJkYXRhX3NvdXJjZV91c2VyX2RhdGEiOiIiLCJpZCI6MCwidXVpZCI6IjQyZjc1MzEyLTU3NDQtNDk4MS05OTIzLTFiOTYwMTQ0MjAzNyIsInN1YiI6MCwiZW1haWwiOiJoYXJ5YW5hQGVmaXNoZXJ5LmNvbSIsIm5hbWUiOiJIYXJ5YW5hIiwicGhvbmUiOiIiLCJpc19hZG1pbiI6ZmFsc2UsInN0YXR1cyI6IiIsImlzX25iaW90IjpmYWxzZSwic3ViZGlzdHJpY3RfaWQiOiIiLCJwcm92X2NvZGUiOjAsImN1c3RvbWVyX251bWJlciI6IiIsImFwcF91c2VyX2lkIjowLCJ1c2VybmFtZSI6IiIsImFkZHJlc3MiOiIiLCJwaWN0dXJlIjoiIiwiY29tcGFueV9uYW1lIjoiIiwiY3JlYXRlZF9hdCI6IjAwMDEtMDEtMDFUMDA6MDA6MDBaIiwidXBkYXRlZF9hdCI6IjAwMDEtMDEtMDFUMDA6MDA6MDBaIiwibG9jYXRpb24iOiIiLCJpbnRlcmVzdCI6IiIsInZlcnNpb24iOjIsImxlYWRfaWQiOiIiLCJsZWFkX25hbWUiOiIiLCJzbGFja19pZCI6IlUwMjcxUFdCNDJFIiwiYXBwX3Rva2VuIjoiIiwiaXNfaW50ZXJuYWxfdXNlciI6dHJ1ZSwiYXBwX3VzZXJfcm9sZXMiOm51bGwsInVhY19yb2xlcyI6W10sInVhY19wZXJtaXNzaW9ucyI6WyJhYzMxNTU1ZC1jZGU2LTQ4MjEtOGY5Ny0wYjFlZmQ5N2MyNDIiXSwiZG9tYWlucyI6bnVsbCwicm9sZXMiOm51bGwsInBlcm1pc3Npb25zIjpudWxsLCJjbGllbnRfaWQiOiIzODRiYjk1My0wMjgxLTQwY2QtYWVmNi01NjEyYjRhYjk2ODMifQ.OCPHjfy2U6JQSdPb4aH9O5KOtjHzQ2RH_e4_YwB-OV0",
        "X-Client-Id": "Load-Test",
        "Content-Type": "application/json"
    }
    @task
    def create_order_fismo(self):
        host = "https://uat-fish-internal.efishery.com"
        payload_uat= {
            "type": "new",
            "order_type": "downstream",
            "buyer_lead": "7A9uqdcB6HqqLUUDjUov2P",
            "buyer_lead_outlet": "dVhuvGBsXmBrjFnxj58moL",
            "pay_with": "cash_on_delivery",
            "ship_address": "jalan",
            "ship_city": "3275",
            "pic_sales": 179,
            "supply_category": "FISMO",
            "promo": None,
            "order_from":"SD-FISMO",
            "order_requisition_attachment": [],
            "is_platform": False,
            "status": None,
            "approve_from": "",
            "order_requisition_line": [
                {
                    "supplier": [],
                    "total_price_logistic": 61500,
                    "logistic_fee_per_kg": 12300,
                    "receive_qty": 5,
                    "susut_notes": "",
                    "unit_load_device_id": "",
                    "ship_date": "2023-07-14",
                    "eta_date": "2023-07-14",
                    "eta_time": "08:00:00",
                    "commodity_id": "GURAME",
                    "product_id": "Fd3XxqhfDKMzhGdNBFWaQD",
                    "receive_total_price": 50000,
                    "prices_offering": None,
                    "receive_eta_date": None,
                    "total_price": 50000,
                    "landed_cost_per_kg": 10000,
                    "order_quantity_kg": 5,
                    "eta_time_start": "04:00:00"
                }
            ]
        }
        #create order fismo
        response = self.client.post("/api/sales/orders", json=payload_uat, headers=self.headers)
        if response.status_code == 200:
            print("create order fismo success!")
        else:
            print("Failed to create order fismo:", response.text)

