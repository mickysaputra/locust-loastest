from pickle import FALSE
import time
import json

from zmq import NULL
from locust import HttpUser, task, between
import random

class TestSupply(HttpUser):
    wait_time = between(1, 5)


    @task
    def post_create_supply_non_digital_sign(self):
        
        self.client.post('/v1/supply/validation/8d153006-2b9c-48c0-9542-8393f34f0d6a',json=
        {
            "approval_submission": True,
            "contract_attachment": "https://public-tools.s3.ap-southeast-1.amazonaws.com/sales-diary/contract_attachment_1666700724989-bXav_.pdf",
            "contract_date": "2022-10-25",
            "fish_size": True,
            "harvest_date": True,
            "harvest_date_end": "2022-10-25T00:00:00Z",
            "harvest_date_start": "2022-10-25T00:00:00Z",
            "harvest_total": True,
            "harvest_type": True,
            "is_contract": True,
            "pond_count": True,
            "pond_photo": "https://public-tools.s3.ap-southeast-1.amazonaws.com/sales-diary/pond_photo_1666700724982-lYhwC.jpg",
            "price_on_contract": 1200000,
            "rejected_reason": "",
            "return_url_ct": "https://uat-fish-internal.efishery.com/docsigns/show",
            "selfie_photo": "https://public-tools.s3.ap-southeast-1.amazonaws.com/sales-diary/selfie_photo_1666700724988-MmXTQ.jpg",
            "selling_price_after_harvest": True,
            "selling_price_before_harvest": True,
            "validation_note": "okok"
            },
                         headers={'x-client-version': 'stri', 'x-client-id': 'SALES-DIARY', 'Content-Type': 'application/json', 'x-app-code': 'DSQYPS3c6emppJJ6x80JKYrZ9J3LNHtO'})



    
    @task
    def post_supply_validation_non_digital_sign(self):

       self.client.post('/v2/supply',json=
       {
        "supply_type": "FISH",
        "supplier_id": "512kcapkshn3",
        "pond_count": 10,
        "product_id": "6waoHudXTL47jnGHHwfEtg",
        "harvest_date_start": "2022-09-15",
        "harvest_date_end": "2022-09-15",
        "harvest_tonnage_estimation_kg": 120,
        "commodity_size": 800,
        "commodity_size_max": 1000,
        "unit_commodity_size": "EKOR/KG",
        "price_on_farm": 12000,
        "price_on_farm_max": NULL,
        "price_on_car": 12300,
        "feed_consumption_kg": 20,
        "is_interest": True,
        "reason_not_interested": "",
        "status": "DRAFT",
        "is_contract": True,
        "pond_address": "Tasik",
        "pond_subdistrict_name": "WARGAKERTA",
        "pond_subdistrict_id": 3206191002,
        "pond_district_name": "SUKARAME",
        "pond_district_id": 3206191,
        "pond_city_name": "KABUPATEN TASIKMALAYA",
        "pond_city_id": 3206,
        "pond_province_name": "JAWA BARAT",
        "pond_province_id": 32,
        "contract_attachment": "",
        "is_pay_kabayan": False,
        "ar_amount_pay": 0,
        "promo_code": "",
        "price_on_contract": 14000,
        "return_url_farmer": "https://uat-tambakan.efishery.com/sku/512kcapkshn3/callback/docsign",
        "return_url_rm": "https://uat-fish-internal.efishery.com/docsign/show",
        "return_url_ct": "https://uat-fish-internal.efishery.com/docsign/show",
        "number_of_seeds": 1200,
        "cultivation_duration": 2.7,
        "canvassing_doc": [],
        "is_private_pricing": False,
        "private_price_on_car": NULL,
        "private_price_on_farm": NULL,
        "supply_for": "FLB"
        },
                         headers={'x-app-id': 'Tambakan', 'x-client-version': '1.4.27-beta.1', 'x-client-id': 'Tambakan', 'Content-Type': 'application/json', 'x-app-code': 'DSQYPS3c6emppJJ6x80JKYrZ9J3LNHtO'})

    