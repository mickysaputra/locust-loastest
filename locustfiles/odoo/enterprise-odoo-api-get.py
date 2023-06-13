from locust import HttpUser, task, between, tag, constant


class GetPartner(HttpUser):
    wait_time = constant(1)

    @tag('partner')
    @task
    def get_partner(self):
        with self.client.get('/efishery/api/v1/partner/51234qs6q6u8',
                             headers={'Accept': 'application/json',
                                      'API-KEY': 'efishery_123',
                                      'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2MTQ4MjQ1OTksImV4cCI6MTY0NjM2MDU5OSwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSJ9.u0NyTeIoBhlorZq0d9sFv2k4n2UnjXBjdHtO-fctBoc'},
                             catch_response=True
                             ) as response:
            if response.status_code == 400 or response.status_code == 404:
                response.failure("Request Failed!")
            elif response.elapsed.total_seconds() > 0.5:
                print("Elapsed time between request and response more than 500ms")


class GetPartnerChild(HttpUser):
    wait_time = constant(1)

    @tag('partner_child')
    @task
    def get_partner_child(self):
        with self.client.get('/efishery/api/v1/partner/513uyvid8npp/child',
                             headers={'Accept': 'application/json',
                                      'API-KEY': 'efishery_123',
                                      'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2MTQ4MjQ1OTksImV4cCI6MTY0NjM2MDU5OSwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSJ9.u0NyTeIoBhlorZq0d9sFv2k4n2UnjXBjdHtO-fctBoc'},
                             catch_response=True
                             ) as response:
            if response.status_code == 400 or response.status_code == 404:
                response.failure("Request Failed!")
            elif response.elapsed.total_seconds() > 0.5:
                print("Elapsed time between request and response more than 500ms")


class GetProductV2(HttpUser):
    wait_time = constant(1)

    @tag('productV2')
    @task
    def get_product_v2(self):
        with self.client.get('/efishery/api/v2/product/mall-product-1794',
                             headers={'Accept': 'application/json',
                                      'API-KEY': 'efishery_123',
                                      'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2MTQ4MjQ1OTksImV4cCI6MTY0NjM2MDU5OSwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSJ9.u0NyTeIoBhlorZq0d9sFv2k4n2UnjXBjdHtO-fctBoc'},
                             catch_response=True
                             ) as response:
            if response.status_code == 400 or response.status_code == 404:
                response.failure("Request Failed!")
            elif response.elapsed.total_seconds() > 0.5:
                print("Elapsed time between request and response more than 500ms")


class GetPurchase(HttpUser):
    wait_time = constant(1)

    @tag('purchase')
    @task
    def get_purchase(self):
        with self.client.get('/efishery/api/v1/purchase/UE8vRlJNLzIwMjMvMDMvMDE3NTQ=',
                             headers={'Accept': 'application/json',
                                      'API-KEY': 'efishery_123',
                                      'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2MTQ4MjQ1OTksImV4cCI6MTY0NjM2MDU5OSwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSJ9.u0NyTeIoBhlorZq0d9sFv2k4n2UnjXBjdHtO-fctBoc'},
                             catch_response=True
                             ) as response:
            if response.status_code == 400 or response.status_code == 404:
                response.failure("Request Failed!")
            elif response.elapsed.total_seconds() > 0.5:
                print("Elapsed time between request and response more than 500ms")


class GetSale(HttpUser):
    wait_time = constant(1)

    @tag('sale')
    @task
    def get_sale(self):
        with self.client.get('/efishery/api/v1/sale/order/TVBMLzIwMjIxMTIyL1NIUi8zNzI4Mzc=',
                             headers={'Accept': 'application/json',
                                      'API-KEY': 'efishery_123',
                                      'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2MTQ4MjQ1OTksImV4cCI6MTY0NjM2MDU5OSwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSJ9.u0NyTeIoBhlorZq0d9sFv2k4n2UnjXBjdHtO-fctBoc'},
                             catch_response=True
                             ) as response:
            if response.status_code == 400 or response.status_code == 404:
                response.failure("Request Failed!")
            elif response.elapsed.total_seconds() > 0.5:
                print("Elapsed time between request and response more than 500ms")


class GetUom(HttpUser):
    wait_time = constant(1)

    @tag('uom')
    @task
    def get_uom(self):
        with self.client.get('/efishery/api/v1/uom/UOM-MPL-1662101317623',
                             headers={'Accept': 'application/json',
                                      'API-KEY': 'efishery_123',
                                      'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2MTQ4MjQ1OTksImV4cCI6MTY0NjM2MDU5OSwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSJ9.u0NyTeIoBhlorZq0d9sFv2k4n2UnjXBjdHtO-fctBoc'},
                             catch_response=True
                             ) as response:
            if response.status_code == 400 or response.status_code == 404:
                response.failure("Request Failed!")
            elif response.elapsed.total_seconds() > 0.5:
                print("Elapsed time between request and response more than 500ms")


class GetPaymentRequest(HttpUser):
    wait_time = constant(1)

    @tag('prf')
    @task
    def get_prf(self):
        with self.client.get('/efishery/api/v1/prf/39',
                             headers={'Accept': 'application/json',
                                      'API-KEY': 'efishery_123',
                                      'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2MTQ4MjQ1OTksImV4cCI6MTY0NjM2MDU5OSwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSJ9.u0NyTeIoBhlorZq0d9sFv2k4n2UnjXBjdHtO-fctBoc'},
                             catch_response=True
                             ) as response:
            if response.status_code == 400 or response.status_code == 404:
                response.failure("Request Failed!")
            elif response.elapsed.total_seconds() > 0.5:
                print("Elapsed time between request and response more than 500ms")


class GetPicking(HttpUser):
    wait_time = constant(1)

    @tag('picking')
    @task
    def get_picking(self):
        with self.client.get(
                '/efishery/api/v1/picking?so_external_id=ORDER/TEST/NAUFAL/13/03/2023/1&po_external_id=PO/MAL/2023/03/69178',
                headers={'Accept': 'application/json',
                         'API-KEY': 'efishery_123',
                         'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2MTQ4MjQ1OTksImV4cCI6MTY0NjM2MDU5OSwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSJ9.u0NyTeIoBhlorZq0d9sFv2k4n2UnjXBjdHtO-fctBoc'},
                catch_response=True
                ) as response:
            if response.status_code == 400 or response.status_code == 404:
                response.failure("Request Failed!")
            elif response.elapsed.total_seconds() > 0.5:
                print("Elapsed time between request and response more than 500ms")


class ParallelAPIRun(HttpUser):
    wait_time = constant(1)

    @task
    def get_partner(self):
        with self.client.get('/efishery/api/v1/partner/51234qs6q6u8',
                             headers={'Accept': 'application/json',
                                      'API-KEY': 'efishery_123',
                                      'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2MTQ4MjQ1OTksImV4cCI6MTY0NjM2MDU5OSwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSJ9.u0NyTeIoBhlorZq0d9sFv2k4n2UnjXBjdHtO-fctBoc'},
                             catch_response=True
                             ) as response:
            if response.status_code == 400 or response.status_code == 404:
                response.failure("Request Failed!")
            elif response.elapsed.total_seconds() > 0.5:
                print("Elapsed time between request and response more than 500ms")

    @task
    def get_partner_child(self):
        with self.client.get('/efishery/api/v1/partner/513uyvid8npp/child',
                             headers={'Accept': 'application/json',
                                      'API-KEY': 'efishery_123',
                                      'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2MTQ4MjQ1OTksImV4cCI6MTY0NjM2MDU5OSwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSJ9.u0NyTeIoBhlorZq0d9sFv2k4n2UnjXBjdHtO-fctBoc'},
                             catch_response=True
                             ) as response:
            if response.status_code == 400 or response.status_code == 404:
                response.failure("Request Failed!")
            elif response.elapsed.total_seconds() > 0.5:
                print("Elapsed time between request and response more than 500ms")

    @task
    def get_product(self):
        with self.client.get('/efishery/api/v2/product/mall-product-1794',
                             headers={'Accept': 'application/json',
                                      'API-KEY': 'efishery_123',
                                      'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2MTQ4MjQ1OTksImV4cCI6MTY0NjM2MDU5OSwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSJ9.u0NyTeIoBhlorZq0d9sFv2k4n2UnjXBjdHtO-fctBoc'},
                             catch_response=True
                             ) as response:
            if response.status_code == 400 or response.status_code == 404:
                response.failure("Request Failed!")
            elif response.elapsed.total_seconds() > 0.5:
                print("Elapsed time between request and response more than 500ms")

    @task
    def get_purchase(self):
        with self.client.get('/efishery/api/v1/purchase/UE8vRlJNLzIwMjMvMDMvMDE3NTQ=',
                             headers={'Accept': 'application/json',
                                      'API-KEY': 'efishery_123',
                                      'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2MTQ4MjQ1OTksImV4cCI6MTY0NjM2MDU5OSwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSJ9.u0NyTeIoBhlorZq0d9sFv2k4n2UnjXBjdHtO-fctBoc'},
                             catch_response=True
                             ) as response:
            if response.status_code == 400 or response.status_code == 404:
                response.failure("Request Failed!")
            elif response.elapsed.total_seconds() > 0.5:
                print("Elapsed time between request and response more than 500ms")

    @task
    def get_sale(self):
        with self.client.get('/efishery/api/v1/sale/order/TVBMLzIwMjIxMTIyL1NIUi8zNzI4Mzc=',
                             headers={'Accept': 'application/json',
                                      'API-KEY': 'efishery_123',
                                      'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2MTQ4MjQ1OTksImV4cCI6MTY0NjM2MDU5OSwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSJ9.u0NyTeIoBhlorZq0d9sFv2k4n2UnjXBjdHtO-fctBoc'},
                             catch_response=True
                             ) as response:
            if response.status_code == 400 or response.status_code == 404:
                response.failure("Request Failed!")
            elif response.elapsed.total_seconds() > 0.5:
                print("Elapsed time between request and response more than 500ms")

    @task
    def get_uom(self):
        with self.client.get('/efishery/api/v1/uom/UOM-MPL-1662101317623',
                             headers={'Accept': 'application/json',
                                      'API-KEY': 'efishery_123',
                                      'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2MTQ4MjQ1OTksImV4cCI6MTY0NjM2MDU5OSwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSJ9.u0NyTeIoBhlorZq0d9sFv2k4n2UnjXBjdHtO-fctBoc'},
                             catch_response=True
                             ) as response:
            if response.status_code == 400 or response.status_code == 404:
                response.failure("Request Failed!")
            elif response.elapsed.total_seconds() > 0.5:
                print("Elapsed time between request and response more than 500ms")

    @task
    def get_prf(self):
        with self.client.get('/efishery/api/v1/prf/39',
                             headers={'Accept': 'application/json',
                                      'API-KEY': 'efishery_123',
                                      'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2MTQ4MjQ1OTksImV4cCI6MTY0NjM2MDU5OSwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSJ9.u0NyTeIoBhlorZq0d9sFv2k4n2UnjXBjdHtO-fctBoc'},
                             catch_response=True
                             ) as response:
            if response.status_code == 400 or response.status_code == 404:
                response.failure("Request Failed!")
            elif response.elapsed.total_seconds() > 0.5:
                print("Elapsed time between request and response more than 500ms")

    @task
    def get_picking(self):
        with self.client.get(
                '/efishery/api/v1/picking?so_external_id=ORDER/TEST/NAUFAL/13/03/2023/1&po_external_id=PO/MAL/2023/03/69178',
                headers={'Accept': 'application/json',
                         'API-KEY': 'efishery_123',
                         'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2MTQ4MjQ1OTksImV4cCI6MTY0NjM2MDU5OSwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSJ9.u0NyTeIoBhlorZq0d9sFv2k4n2UnjXBjdHtO-fctBoc'},
                catch_response=True
                ) as response:
            if response.status_code == 400 or response.status_code == 404:
                response.failure("Request Failed!")
            elif response.elapsed.total_seconds() > 0.5:
                print("Elapsed time between request and response more than 500ms")


class GetHealth(HttpUser):
    wait_time = constant(1)

    @tag('health')
    @task
    def get_health(self):
        with self.client.get('/health', catch_response=True) as response:
            if response.status_code == 400 or response.status_code == 404:
                response.failure("Request Failed!")
            elif response.elapsed.total_seconds() > 0.5:
                print("Elapsed time between request and response more than 500ms")


class GetProductV3(HttpUser):
    wait_time = constant(1)

    @tag('productV3')
    @task
    def get_product_v3(self):
        with self.client.get('/efishery/api/v3/product',
                             headers={'Accept': 'application/json',
                                      'API-KEY': 'efishery_123',
                                      'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2MTQ4MjQ1OTksImV4cCI6MTY0NjM2MDU5OSwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSJ9.u0NyTeIoBhlorZq0d9sFv2k4n2UnjXBjdHtO-fctBoc'},
                             catch_response=True
                             ) as response:
            if response.status_code == 400 or response.status_code == 404:
                response.failure("Request Failed!")
            elif response.elapsed.total_seconds() > 0.5:
                print("Elapsed time between request and response more than 500ms")


class GetProductByExternalIdV3(HttpUser):
    wait_time = constant(1)

    @tag('productbyexternalidv3')
    @task
    def get_product_external_id_v3(self):
        with self.client.get('/efishery/api/v3/product/mall-product-1510',
                             headers={'Accept': 'application/json',
                                      'API-KEY': 'efishery_123',
                                      'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2MTQ4MjQ1OTksImV4cCI6MTY0NjM2MDU5OSwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSJ9.u0NyTeIoBhlorZq0d9sFv2k4n2UnjXBjdHtO-fctBoc'},
                             catch_response=True
                             ) as response:
            if response.status_code == 400 or response.status_code == 404:
                response.failure("Request Failed!")
            elif response.elapsed.total_seconds() > 0.5:
                print("Elapsed time between request and response more than 500ms")


class GetProductV3WithParam(HttpUser):
    wait_time = constant(1)

    @tag('productV3')
    @task
    def get_product_v3(self):
        with self.client.get('/efishery/api/v3/product?limit=10&offset=2&keyword=gurame&type=product&company=FRESH&category=fresh&route=buy',
                             headers={'Accept': 'application/json',
                                      'API-KEY': 'efishery_123',
                                      'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2MTQ4MjQ1OTksImV4cCI6MTY0NjM2MDU5OSwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSJ9.u0NyTeIoBhlorZq0d9sFv2k4n2UnjXBjdHtO-fctBoc'},
                             catch_response=True
                             ) as response:
            if response.status_code == 400 or response.status_code == 404:
                response.failure("Request Failed!")
            elif response.elapsed.total_seconds() > 0.5:
                print("Elapsed time between request and response more than 500ms")