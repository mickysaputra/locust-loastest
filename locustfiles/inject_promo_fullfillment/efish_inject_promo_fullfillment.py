from locust import HttpUser, task, between

class InjectingPromo(HttpUser):
    wait_time = between(1, 3)
    headers = {
        "X-App-Token": "419vmKxA6KRbSeqcU4oGzwCPFTwxPIQp",
        "Content-Type": "application/json"
    }

    @task
    def cash_apply_promo(self):
        host = "https://uat-efishery-service-commerce.efishery.com"
        payload_1 = {
            "no_pks": "065/MTN-LEG/EXT/III/2020",
            "lead_id": "512a4h6extps",
            "order_date": "2023-06-26T11:56:05+07:00",
            "tenor": 0,
            "created_by": {
                "name": "Nia Nuryanti",
                "email": "nia.nuryanti@efishery.com"
            },
            "order_details": [
                {
                    "pricelist_id": 9560,
                    "quantity": 10,
                    "promo_ids": [
                        239
                    ]
                }
            ],
            "voucher_ids": [],
            "shipment": {
                "receiver_name": "DONI ADRIADI",
                "receiver_address": "",
                "receiver_phone": "",
                "method": "ambil_ke_agen"
            },
            "client_code": "feedhub"
        }

        response = self.client.post("/v1/orders/promo/apply", json=payload_1, headers=self.headers)
        if response.status_code == 200:
            print("apply promo cash success!")
        else:
            print("Failed to apply promo cash:", response.text)

    @task
    def create_order_cash_promo(self):
        host = "https://uat-efishery-service-commerce.efishery.com"
        payload_2 = {
            "no_pks": "065/MTN-LEG/EXT/III/2020",
            "lead_id": "512a4h6extps",
            "order_date": "2023-06-26T11:56:05+07:00",
            "tenor": 0,
            "created_by": {
                "name": "Nia Nuryanti",
                "email": "nia.nuryanti@efishery.com"
            },
            "order_details": [
                {
                    "pricelist_id": 9560,
                    "quantity": 10,
                    "promo_ids": [
                        239
                    ]
                }
            ],
            "voucher_ids": [],
            "shipment": {
                "receiver_name": "DONI ADRIADI",
                "receiver_address": "",
                "receiver_phone": "",
                "method": "ambil_ke_agen"
            },
            "client_code": "feedhub"
        }

        response = self.client.post("/v1/orders/create", json=payload_2, headers=self.headers)
        if response.status_code == 200:
            print("create order cash with promo success")
        else:
            print("Failed to create order cash with promo:", response.text)

    @task
    def create_order_tenor_promo(self):
        host = "https://uat-efishery-service-commerce.efishery.com"
        payload_3 = {
            "no_pks": "065/MTN-LEG/EXT/III/2020",
            "lead_id": "512a4h6extps",
            "order_date": "2023-06-26T11:56:05+07:00",
            "tenor": 6,
            "created_by": {
                "name": "Nia Nuryanti",
                "email": "nia.nuryanti@efishery.com"
            },
            "order_details": [
                {
                    "pricelist_id": 9560,
                    "quantity": 10,
                    "promo_ids": [
                        239
                    ]
                }
            ],
            "voucher_ids": [],
            "shipment": {
                "receiver_name": "DONI ADRIADI",
                "receiver_address": "",
                "receiver_phone": "",
                "method": "ambil_ke_agen"
            },
            "client_code": "feedhub"
        }

        response = self.client.post("/v1/orders/create", json=payload_3, headers=self.headers)
        if response.status_code == 200:
            print("create order tenor with promo placed success")
        else:
            print("Failed to create order tenor with promo:", response.text)

    @task
    def promo_suggestion(self):
        host = "https://uat-efishery-service-commerce.efishery.com"
        payload_4 = {
            "channels": ["feedhub"],
            "details": [
                {
                    "price_list_id": "19365",
                    "total_qty": 1
                }
            ],
            "lead_id": "512345nnsrap",
            "payment_method": "cash",
            "point_id": "4",
            "product_type": "feed"
        }

        response = self.client.post("/v2/orders/promo-with-suggestion", json=payload_4, headers=self.headers)
        if response.status_code == 200:
            print("get promo suggestion success")
        else:
            print("Failed to get promo suggestion:", response.text)
