from locust import HttpUser, task, between
import time


class PromoMgmtSvcLoadTest(HttpUser):
    wait_time = between(1, 3)
    promo_id = "af1ffd87-6a4c-408f-b7fb-54f5a37dd093"
    auth = "Bearer __THIS_IS_STATIC_TOKEN"
    app_id = "efisheryku"

    @task(1)
    def validate(self):
        print("---validating promo---")
        resp = self.client.post("/v1/api/promo/validate", headers=self._get_headers(), json=self._get_body())
        if resp.status_code >= 400:
            print(resp.json())

    @task(1)
    def filter_by_order(self):
        print("---filtering promo by order---")
        resp = self.client.post("/v1/api/promo/filter-by-order", headers=self._get_headers(), json=self._get_body())
        if resp.status_code >= 400:
            print(resp.json())

    @task
    def apply(self):
        print("---applying promo---")
        resp = self.client.post("/v1/api/promo/apply", headers=self._get_headers(), json=self._get_body())
        if resp.status_code >= 400:
            print(resp.json())

    def _get_body(self):
        return {
            "channel": "efisheryku",
            "product_type": "feed",
            "promo_id": self.promo_id,
            "payment_method": "kabayan",
            "order": {
                "id": "d621c23d-a6d6-4433-8ed8-01a5869fb3f1",
                "date": "2022-10-17T12:14:05.000+07:00",
                "details": [
                    {
                        "brand_id": "cihuy",
                        "sku_id": "lele",
                        "total_amount": 6000,
                        "total_qty": 10,
                        "unit": "pc"
                    },
                    {
                        "brand_id": "cihuy",
                        "sku_id": "random_sku",
                        "total_amount": 6000,
                        "total_qty": 10,
                        "unit": "pc"
                    },
                    {
                        "brand_id": "abogoboga",
                        "supplier_id": "some supplier",
                        "sku_id": "patin",
                        "total_amount": 7000,
                        "total_qty": 25,
                        "unit": "sack"
                    },
                    {
                        "brand_id": "abogoboga",
                        "sku_id": "hiu",
                        "supplier_id": "wehehe",
                        "total_amount": 5000,
                        "total_qty": 1,
                        "unit": "kg"
                    },
                    {
                        "brand_id": "abogoboga",
                        "sku_id": "lumba-lumba",
                        "supplier_id": "wehehe",
                        "total_amount": 5000,
                        "total_qty": 1000,
                        "unit": "pc"
                    }
                ],
                "total_amount": 29000,
                "total_qty": 1046
            }
        }

    def _get_headers(self):
        return {"Authorization": self.auth, "X-Load-Test": "locust-load-test", "X-App-Id": self.app_id}
