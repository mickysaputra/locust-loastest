import time

from locust import HttpUser,TaskSet, SequentialTaskSet, task, between, tag, constant
from locust.exception import StopUser


class UpdateProductV2(HttpUser):
    wait_time = constant(1)

    @task
    def update_product(self):
        with self.client.put("/efishery/api/v2/product/product-v2-load-test-by-qa",
                             json={
                                 "external_id": "product-v2-load-test-by-qa",
                                 "barcode": "",
                                 "category_id": 79,
                                 "name": "product v2 load erp",
                                 "uom_id": "97",
                                 "uom_po_id": "97",
                                 "can_be_sold": True,
                                 "can_be_purchase": True,
                                 "can_be_expensed": False,
                                 "can_be_rented": True,
                                 "landed_product": False,
                                 "type": "product",
                                 "sale_price": 35000,
                                 "company": "MALL",
                                 "invoice_policy": "order",
                                 "bill_policy": "purchase",
                                 "route_buy": True,
                                 "route_manufacture": False,
                                 "route_dropship": False
                             },
                             headers={'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2MTQ4MjQ1OTksImV4cCI6MTY0NjM2MDU5OSwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSJ9.u0NyTeIoBhlorZq0d9sFv2k4n2UnjXBjdHtO-fctBoc',
                                      'API-KEY': 'efishery_123'},
                             catch_response=True
                             ) as response:
            if response.status_code == 400 or response.status_code == 404:
                response.failure("Request Failed!")
            elif response.elapsed.total_seconds() > 0.5:
                print("Elapsed time between request and response more than 500ms")
