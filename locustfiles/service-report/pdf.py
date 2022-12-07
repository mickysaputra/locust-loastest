from locust import HttpUser, task
import uuid
import random

class Pdf(HttpUser):
    @task
    def create_pdf(self):
        headers = {
            "Content-Type": "application/json",
            "X-App-Token": "934ZpQIgvJdHTtvpEClhK6jaF0Gu5M1G"
        }

        self.client.post("/pdf", json={
            "options": {
                "format":    "A5",
                "landscape": True,
                "margin": {
                    "left":   "20px",
                    "right":  "20px",
                    "top":    "20px",
                    "bottom": "20px"
                }
            },
            "template": "feed-nota-transaksi.html",
            "bucket": "",
            "filename": "efishery-service-report-test/" + str(uuid.uuid4()),
            "data": {
                "order": {
                    "customer_name": "Dege",
                    "customer_id": "123",
                    "order_id": "ORDER/123",
                    "order_date": "2022-01-01",
                    "total_amount_petani": 1000000,
                    "tenor": 3,
                    "tenor_unit": "bulan",
                    "due_date": "2022-03-01"
                },
                "order_details": [
                    {
                        "kode_barang": "ABC001",
                        "qty": 2,
                        "unit_price_petani": 15000,
                        "subtotal_petani": 30000
                    }
                ],
                "bank_name": "BCA",
                "bank_account": "8610101234"
            }
        }, headers=headers)
