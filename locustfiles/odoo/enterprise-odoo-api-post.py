from locust import HttpUser, task, constant
import random
import string


def randStr(chars=string.ascii_uppercase + string.digits, N=10):
    return ''.join(random.choice(chars) for _ in range(N))


class CreatePurchaseV1(HttpUser):
    wait_time = constant(1)

    @task
    def create_purchase(self):
        with self.client.post("/efishery/api/v1/purchase",
                             json={
                                     "external_id": (randStr(N=7)),
                                     "vendor_external_id": "512xcjutszqu",
                                     "user": "engineer@efishery.com",
                                     "company": "MALL",
                                     "vendor_reference": "",
                                     "origin": "",
                                     "order_lines_vendor_pay_kabayan": True,
                                     "picking_type_id": 13,
                                     "payment_term_id": 1,
                                     "note": "terms & conditions",
                                     "auto_prf": False,
                                     "department_id": 338,
                                     "acc_name": "",
                                     "acc_number": "",
                                     "products": [
                                         {
                                             "product_external_id": "mall-product-1150",
                                             "quantity": 5,
                                             "price_unit": 300000,
                                             "description": "Testing",
                                             "uom_id": 24

                                         }
                                     ]

                             },
                             headers={
                                    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2MTQ4MjQ1OTksImV4cCI6MTY0NjM2MDU5OSwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSJ9.u0NyTeIoBhlorZq0d9sFv2k4n2UnjXBjdHtO-fctBoc',
                                    'API-KEY': 'efishery_123'},
                             catch_response=True
                             ) as response:
            if response.status_code == 400 or response.status_code == 404:
                response.failure("Request Failed!")
            elif response.elapsed.total_seconds() > 0.5:
                print("Elapsed time between request and response more than 500ms")