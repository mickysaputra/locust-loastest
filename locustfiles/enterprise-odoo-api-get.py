from locust import HttpUser, task, between, tag


class GetPartner(HttpUser):
    wait_time = between(1, 5)

    @tag('partner')
    @task
    def get_partner(self):
        with self.client.get('/efishery/api/v1/partner/51234qs6q6u8',
                             headers={'Accept': 'application/json', 'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2MTQ4MjQ1OTksImV4cCI6MTY0NjM2MDU5OSwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSJ9.u0NyTeIoBhlorZq0d9sFv2k4n2UnjXBjdHtO-fctBoc'}, catch_response=True
                             ) as response:
            if response.status_code == 400 or response.status_code == 404:
                response.failure("Request Failed!")
            elif response.elapsed.total_seconds() > 0.5:
                print("Elapsed time between request and response more than 500ms")


class GetProduct(HttpUser):
    wait_time = between(1, 5)

    @tag('product')
    @task
    def get_product(self):
        with self.client.get('/efishery/api/v2/product/mall-product-1794',
                             headers={'Accept': 'application/json', 'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2MTQ4MjQ1OTksImV4cCI6MTY0NjM2MDU5OSwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSJ9.u0NyTeIoBhlorZq0d9sFv2k4n2UnjXBjdHtO-fctBoc'}, catch_response=True
                             ) as response:
            if response.status_code == 400 or response.status_code == 404:
                response.failure("Request Failed!")
            elif response.elapsed.total_seconds() > 0.5:
                print("Elapsed time between request and response more than 500ms")


class GetPurchase(HttpUser):
    wait_time = between(1, 5)

    @tag('purchase')
    @task
    def get_purchase(self):
        with self.client.get('/efishery/api/v1/purchase/UE8vRlJNLzIwMjMvMDMvMDE3NTQ=',
                             headers={'Accept': 'application/json', 'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2MTQ4MjQ1OTksImV4cCI6MTY0NjM2MDU5OSwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSJ9.u0NyTeIoBhlorZq0d9sFv2k4n2UnjXBjdHtO-fctBoc'}, catch_response=True
                             ) as response:
            if response.status_code == 400 or response.status_code == 404:
                response.failure("Request Failed!")
            elif response.elapsed.total_seconds() > 0.5:
                print("Elapsed time between request and response more than 500ms")


class GetSale(HttpUser):
    wait_time = between(1, 5)

    @tag('sale')
    @task
    def get_sale(self):
        with self.client.get('/efishery/api/v1/sale/order/TVBMLzIwMjIxMTIyL1NIUi8zNzI4Mzc=',
                             headers={'Accept': 'application/json', 'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2MTQ4MjQ1OTksImV4cCI6MTY0NjM2MDU5OSwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSJ9.u0NyTeIoBhlorZq0d9sFv2k4n2UnjXBjdHtO-fctBoc'}, catch_response=True
                             ) as response:
            if response.status_code == 400 or response.status_code == 404:
                response.failure("Request Failed!")
            elif response.elapsed.total_seconds() > 0.5:
                print("Elapsed time between request and response more than 500ms")
