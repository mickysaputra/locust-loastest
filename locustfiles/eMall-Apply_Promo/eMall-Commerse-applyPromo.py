from pickle import FALSE
import time
import json

from zmq import NULL
from locust import HttpUser, task, between
import random

class apply_order_cash_without_promo(HttpUser):
    wait_time = between(0.1, 2000)

    @task
    def apply_order_cash_without_promo(self):
        print("apply_order_cash_with_promo is starting")


        self.client.request_name = "Apply order cash without promo"
        self.client.post('/apply-promo',json=
                            
    {
        "order": {
                "order_type": "member",
                "no_pks": "2821/MTN-LEG/EXT/VII/2021",
                "lead_id": "513qwy9ap6hu",
                "point_id": 6,
                "order_date": "2022-12-15T16:54:52+07:00",
                "client_code": "feedhub",
                "order_details": [{
                        "product_id": 1425,
                        "qty": 5,
                        "unit": "sak",
                        "detil_pakan_jumlah_kg": 150,
                        "unit_price_petani": 398700,
                        "subtotal_petani": 1993500,
                        "jenis_barang": "pakan",
                        "product_type": "pakan",
                        "tenor": 0
                }]
        }
},
        
                         headers={'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE5NTkxODEyMDAsImp0aSI6IkhJZERxWEtXbVRGTVFsY1ciLCJpc3MiOiJlZmlzaGVyeS1zZXJ2aWNlLWF1dGgiLCJpZCI6MCwidXVpZCI6IjdlOTY0N2VlLThiYjEtNDJhNC1hZDQ0LTUzMjYwODVmZjMzZiIsInN1YiI6MCwiZW1haWwiOiJtb2hhbWFkLmhhbmlmYW5AZWZpc2hlcnkuY29tIiwibmFtZSI6ImhhbmlmYW5tIiwicGhvbmUiOiIiLCJpc0FkbWluIjowLCJzdGF0dXMiOiIiLCJpc19uYmlvdCI6ZmFsc2UsInN1YmRpc3RyaWN0X2lkIjoiIiwicHJvdl9jb2RlIjowLCJjdXN0b21lcl9udW1iZXIiOiIiLCJhcHBfdXNlcl9pZCI6MCwidXNlcm5hbWUiOiIiLCJhZGRyZXNzIjoiIiwicGljdHVyZSI6IiIsImNvbXBhbnlfbmFtZSI6IiIsImNyZWF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsInVwZGF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsImxvY2F0aW9uIjoiIiwiaW50ZXJlc3QiOiIiLCJ2ZXJzaW9uIjoyLCJsZWFkX2lkIjoiIiwibGVhZF9uYW1lIjoiaGFuaWZhbm0iLCJpYXQiOjE2NTMyOTUyNzJ9.k0nXJCXWSAIflN4tIiSZlwV-IHKGSYkd8xFsN5dCL1g'})

    
class apply_order_kabayan_without_promo(HttpUser):
    
    wait_time = between(0.1, 2000)


    @task
    def apply_order_kabayan_without_promo(self):
        print("apply_order_kabayan_without_promo is starting")


        self.client.request_name = "Apply order kabayan without promo"
        self.client.post('/apply-promo',json=
                            
    {
        "order": {
                "order_type": "kabayan",
                "no_pks": "2821/MTN-LEG/EXT/VII/2021",
                "lead_id": "513qwy9ap6hu",
                "point_id": 6,
                "order_date": "2022-12-15T16:54:52+07:00",
                "client_code": "feedhub",
                "order_details": [{
                        "product_id": 1425,
                        "qty": 5,
                        "unit": "sak",
                        "detil_pakan_jumlah_kg": 150,
                        "unit_price_petani": 412655,
                        "subtotal_petani": 2063275,
                        "jenis_barang": "pakan",
                        "product_type": "pakan",
                        "tenor": 2
                }]
        }
},
                         headers={'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE5NTkxODEyMDAsImp0aSI6IkhJZERxWEtXbVRGTVFsY1ciLCJpc3MiOiJlZmlzaGVyeS1zZXJ2aWNlLWF1dGgiLCJpZCI6MCwidXVpZCI6IjdlOTY0N2VlLThiYjEtNDJhNC1hZDQ0LTUzMjYwODVmZjMzZiIsInN1YiI6MCwiZW1haWwiOiJtb2hhbWFkLmhhbmlmYW5AZWZpc2hlcnkuY29tIiwibmFtZSI6ImhhbmlmYW5tIiwicGhvbmUiOiIiLCJpc0FkbWluIjowLCJzdGF0dXMiOiIiLCJpc19uYmlvdCI6ZmFsc2UsInN1YmRpc3RyaWN0X2lkIjoiIiwicHJvdl9jb2RlIjowLCJjdXN0b21lcl9udW1iZXIiOiIiLCJhcHBfdXNlcl9pZCI6MCwidXNlcm5hbWUiOiIiLCJhZGRyZXNzIjoiIiwicGljdHVyZSI6IiIsImNvbXBhbnlfbmFtZSI6IiIsImNyZWF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsInVwZGF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsImxvY2F0aW9uIjoiIiwiaW50ZXJlc3QiOiIiLCJ2ZXJzaW9uIjoyLCJsZWFkX2lkIjoiIiwibGVhZF9uYW1lIjoiaGFuaWZhbm0iLCJpYXQiOjE2NTMyOTUyNzJ9.k0nXJCXWSAIflN4tIiSZlwV-IHKGSYkd8xFsN5dCL1g'})
    
class apply_order_cash_with_promo(HttpUser):
    
    wait_time = between(0.1, 2000)


    @task
    def apply_order_cash_with_promo(self):
        print("apply_order_cash_with_promo is starting")


        self.client.request_name = "Apply order cash with promo"
        self.client.post('/apply-promo',json=
                            
    {
        "order": {
                "order_type": "member",
                "no_pks": "2821/MTN-LEG/EXT/VII/2021",
                "lead_id": "513qwy9ap6hu",
                "point_id": 6,
                "order_date": "2022-12-15T16:54:52+07:00",
                "client_code": "feedhub",
                "order_details": [{
                        "product_id": 1425,
                        "qty": 20,
                        "unit": "sak",
                        "detil_pakan_jumlah_kg": 600,
                        "unit_price_petani": 398700,
                        "subtotal_petani": 7974000,
                        "jenis_barang": "pakan",
                        "product_type": "pakan",
                        "tenor": 0
                }]
        }
},
                         headers={'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE5NTkxODEyMDAsImp0aSI6IkhJZERxWEtXbVRGTVFsY1ciLCJpc3MiOiJlZmlzaGVyeS1zZXJ2aWNlLWF1dGgiLCJpZCI6MCwidXVpZCI6IjdlOTY0N2VlLThiYjEtNDJhNC1hZDQ0LTUzMjYwODVmZjMzZiIsInN1YiI6MCwiZW1haWwiOiJtb2hhbWFkLmhhbmlmYW5AZWZpc2hlcnkuY29tIiwibmFtZSI6ImhhbmlmYW5tIiwicGhvbmUiOiIiLCJpc0FkbWluIjowLCJzdGF0dXMiOiIiLCJpc19uYmlvdCI6ZmFsc2UsInN1YmRpc3RyaWN0X2lkIjoiIiwicHJvdl9jb2RlIjowLCJjdXN0b21lcl9udW1iZXIiOiIiLCJhcHBfdXNlcl9pZCI6MCwidXNlcm5hbWUiOiIiLCJhZGRyZXNzIjoiIiwicGljdHVyZSI6IiIsImNvbXBhbnlfbmFtZSI6IiIsImNyZWF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsInVwZGF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsImxvY2F0aW9uIjoiIiwiaW50ZXJlc3QiOiIiLCJ2ZXJzaW9uIjoyLCJsZWFkX2lkIjoiIiwibGVhZF9uYW1lIjoiaGFuaWZhbm0iLCJpYXQiOjE2NTMyOTUyNzJ9.k0nXJCXWSAIflN4tIiSZlwV-IHKGSYkd8xFsN5dCL1g'})

class apply_order_kabayan_with_promo(HttpUser):
    
    wait_time = between(1, 5)    


    @task
    def apply_order_kabayan_with_promo(self):
        print("apply_order_kabayan_with_promo is starting")


        self.client.request_name = "Apply order kabayan with promo"
        self.client.post('/apply-promo',json=
                            
    {
        "order": {
                "order_type": "kabayan",
                "no_pks": "2821/MTN-LEG/EXT/VII/2021",
                "lead_id": "513qwy9ap6hu",
                "point_id": 6,
                "order_date": "2022-12-15T16:54:52+07:00",
                "client_code": "feedhub",
                "order_details": [{
                        "product_id": 1425,
                        "qty": 20,
                        "unit": "sak",
                        "detil_pakan_jumlah_kg": 600,
                        "unit_price_petani": 406674,
                        "subtotal_petani": 8133480,
                        "jenis_barang": "pakan",
                        "product_type": "pakan",
                        "tenor": 2
                }]
        }
},
                         headers={'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE5NTkxODEyMDAsImp0aSI6IkhJZERxWEtXbVRGTVFsY1ciLCJpc3MiOiJlZmlzaGVyeS1zZXJ2aWNlLWF1dGgiLCJpZCI6MCwidXVpZCI6IjdlOTY0N2VlLThiYjEtNDJhNC1hZDQ0LTUzMjYwODVmZjMzZiIsInN1YiI6MCwiZW1haWwiOiJtb2hhbWFkLmhhbmlmYW5AZWZpc2hlcnkuY29tIiwibmFtZSI6ImhhbmlmYW5tIiwicGhvbmUiOiIiLCJpc0FkbWluIjowLCJzdGF0dXMiOiIiLCJpc19uYmlvdCI6ZmFsc2UsInN1YmRpc3RyaWN0X2lkIjoiIiwicHJvdl9jb2RlIjowLCJjdXN0b21lcl9udW1iZXIiOiIiLCJhcHBfdXNlcl9pZCI6MCwidXNlcm5hbWUiOiIiLCJhZGRyZXNzIjoiIiwicGljdHVyZSI6IiIsImNvbXBhbnlfbmFtZSI6IiIsImNyZWF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsInVwZGF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsImxvY2F0aW9uIjoiIiwiaW50ZXJlc3QiOiIiLCJ2ZXJzaW9uIjoyLCJsZWFkX2lkIjoiIiwibGVhZF9uYW1lIjoiaGFuaWZhbm0iLCJpYXQiOjE2NTMyOTUyNzJ9.k0nXJCXWSAIflN4tIiSZlwV-IHKGSYkd8xFsN5dCL1g'})

class apply_order_cash_with_spesific_promo_lead_id(HttpUser):
    
    wait_time = between(0.1, 2000)


    @task
    def apply_order_cash_with_spesific_promo_lead_id(self):
        print("apply_order_cash_with_spesific_promo_lead_id is starting")


        self.client.request_name = "Apply order cash with spesific promo lead id"
        self.client.post('/apply-promo',json=
                            
    {
        "order": {
                "order_type": "member",
                "no_pks": "2821/MTN-LEG/EXT/VII/2021",
                "lead_id": "513qwy9ap6hu",
                "point_id": 6,
                "order_date": "2022-12-15T16:54:52+07:00",
                "client_code": "feedhub",
                "order_details": [{
                        "product_id": 1425,
                        "qty": 20,
                        "unit": "sak",
                        "detil_pakan_jumlah_kg": 600,
                        "unit_price_petani": 398700,
                        "subtotal_petani": 7974000,
                        "jenis_barang": "pakan",
                        "product_type": "pakan",
                        "tenor": 0
                }]
        }
},
                         headers={'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE5NTkxODEyMDAsImp0aSI6IkhJZERxWEtXbVRGTVFsY1ciLCJpc3MiOiJlZmlzaGVyeS1zZXJ2aWNlLWF1dGgiLCJpZCI6MCwidXVpZCI6IjdlOTY0N2VlLThiYjEtNDJhNC1hZDQ0LTUzMjYwODVmZjMzZiIsInN1YiI6MCwiZW1haWwiOiJtb2hhbWFkLmhhbmlmYW5AZWZpc2hlcnkuY29tIiwibmFtZSI6ImhhbmlmYW5tIiwicGhvbmUiOiIiLCJpc0FkbWluIjowLCJzdGF0dXMiOiIiLCJpc19uYmlvdCI6ZmFsc2UsInN1YmRpc3RyaWN0X2lkIjoiIiwicHJvdl9jb2RlIjowLCJjdXN0b21lcl9udW1iZXIiOiIiLCJhcHBfdXNlcl9pZCI6MCwidXNlcm5hbWUiOiIiLCJhZGRyZXNzIjoiIiwicGljdHVyZSI6IiIsImNvbXBhbnlfbmFtZSI6IiIsImNyZWF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsInVwZGF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsImxvY2F0aW9uIjoiIiwiaW50ZXJlc3QiOiIiLCJ2ZXJzaW9uIjoyLCJsZWFkX2lkIjoiIiwibGVhZF9uYW1lIjoiaGFuaWZhbm0iLCJpYXQiOjE2NTMyOTUyNzJ9.k0nXJCXWSAIflN4tIiSZlwV-IHKGSYkd8xFsN5dCL1g'})

class apply_order_kabayan_with_spesific_promo_lead_id(HttpUser):
    
    wait_time = between(0.1, 2000)


    @task
    def apply_order_kabayan_with_spesific_promo_lead_id(self):
        print("apply_order_kabayan_with_spesific_promo_lead_id is starting")


        self.client.request_name = "Apply order kabayan with spesific promo lead id"
        self.client.post('/apply-promo',json=
                            
    {
        "order": {
                "order_type": "kabayan",
                "no_pks": "2821/MTN-LEG/EXT/VII/2021",
                "lead_id": "513qwy9ap6hu",
                "point_id": 6,
                "order_date": "2022-12-15T16:54:52+07:00",
                "client_code": "feedhub",
                "order_details": [{
                        "product_id": 1425,
                        "qty": 20,
                        "unit": "sak",
                        "detil_pakan_jumlah_kg": 600,
                        "unit_price_petani": 406674,
                        "subtotal_petani": 8133480,
                        "jenis_barang": "pakan",
                        "product_type": "pakan",
                        "tenor": 2
                }]
        }
},
                         headers={'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE5NTkxODEyMDAsImp0aSI6IkhJZERxWEtXbVRGTVFsY1ciLCJpc3MiOiJlZmlzaGVyeS1zZXJ2aWNlLWF1dGgiLCJpZCI6MCwidXVpZCI6IjdlOTY0N2VlLThiYjEtNDJhNC1hZDQ0LTUzMjYwODVmZjMzZiIsInN1YiI6MCwiZW1haWwiOiJtb2hhbWFkLmhhbmlmYW5AZWZpc2hlcnkuY29tIiwibmFtZSI6ImhhbmlmYW5tIiwicGhvbmUiOiIiLCJpc0FkbWluIjowLCJzdGF0dXMiOiIiLCJpc19uYmlvdCI6ZmFsc2UsInN1YmRpc3RyaWN0X2lkIjoiIiwicHJvdl9jb2RlIjowLCJjdXN0b21lcl9udW1iZXIiOiIiLCJhcHBfdXNlcl9pZCI6MCwidXNlcm5hbWUiOiIiLCJhZGRyZXNzIjoiIiwicGljdHVyZSI6IiIsImNvbXBhbnlfbmFtZSI6IiIsImNyZWF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsInVwZGF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsImxvY2F0aW9uIjoiIiwiaW50ZXJlc3QiOiIiLCJ2ZXJzaW9uIjoyLCJsZWFkX2lkIjoiIiwibGVhZF9uYW1lIjoiaGFuaWZhbm0iLCJpYXQiOjE2NTMyOTUyNzJ9.k0nXJCXWSAIflN4tIiSZlwV-IHKGSYkd8xFsN5dCL1g'})


class apply_order_cash_with_spesific_promo_point_lead_id_513qwy9ap6hu(HttpUser):
    
    wait_time = between(0.1, 2000)


    @task
    def apply_order_cash_with_spesific_promo_point_lead_id_513qwy9ap6hu(self):
        print("apply_order_cash_with_spesific_promo_point_lead_id_513qwy9ap6hu is starting")


        self.client.request_name = "Apply order cash with spesific promo point lead id 513qwy9ap6hu"
        self.client.post('/apply-promo',json=
                            
    {
        "order": {
                "order_type": "member",
                "no_pks": "2821/MTN-LEG/EXT/VII/2021",
                "lead_id": "513qwy9ap6hu",
                "point_id": 6,
                "order_date": "2022-12-15T16:54:52+07:00",
                "client_code": "feedhub",
                "order_details": [{
                        "product_id": 1425,
                        "qty": 20,
                        "unit": "sak",
                        "detil_pakan_jumlah_kg": 600,
                        "unit_price_petani": 398700,
                        "subtotal_petani": 7974000,
                        "jenis_barang": "pakan",
                        "product_type": "pakan",
                        "tenor": 0
                }]
        }
},
                         headers={'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE5NTkxODEyMDAsImp0aSI6IkhJZERxWEtXbVRGTVFsY1ciLCJpc3MiOiJlZmlzaGVyeS1zZXJ2aWNlLWF1dGgiLCJpZCI6MCwidXVpZCI6IjdlOTY0N2VlLThiYjEtNDJhNC1hZDQ0LTUzMjYwODVmZjMzZiIsInN1YiI6MCwiZW1haWwiOiJtb2hhbWFkLmhhbmlmYW5AZWZpc2hlcnkuY29tIiwibmFtZSI6ImhhbmlmYW5tIiwicGhvbmUiOiIiLCJpc0FkbWluIjowLCJzdGF0dXMiOiIiLCJpc19uYmlvdCI6ZmFsc2UsInN1YmRpc3RyaWN0X2lkIjoiIiwicHJvdl9jb2RlIjowLCJjdXN0b21lcl9udW1iZXIiOiIiLCJhcHBfdXNlcl9pZCI6MCwidXNlcm5hbWUiOiIiLCJhZGRyZXNzIjoiIiwicGljdHVyZSI6IiIsImNvbXBhbnlfbmFtZSI6IiIsImNyZWF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsInVwZGF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsImxvY2F0aW9uIjoiIiwiaW50ZXJlc3QiOiIiLCJ2ZXJzaW9uIjoyLCJsZWFkX2lkIjoiIiwibGVhZF9uYW1lIjoiaGFuaWZhbm0iLCJpYXQiOjE2NTMyOTUyNzJ9.k0nXJCXWSAIflN4tIiSZlwV-IHKGSYkd8xFsN5dCL1g'})

class apply_order_kabayan_with_spesific_promo_point_lead_id_513qwy9ap6hu(HttpUser):
    
    wait_time = between(0.1, 2000)


    @task
    def apply_order_kabayan_with_spesific_promo_point_lead_id_513qwy9ap6hu(self):
        print("apply_order_kabayan_with_spesific_promo_point_lead_id_513qwy9ap6hu is starting")


        self.client.request_name = "Apply order kabayan with spesific promo point lead id 513qwy9ap6hu"
        self.client.post('/apply-promo',json=
                            
    {
        "order": {
                "order_type": "kabayan",
                "no_pks": "2821/MTN-LEG/EXT/VII/2021",
                "lead_id": "513qwy9ap6hu",
                "point_id": 6,
                "order_date": "2022-12-15T16:54:52+07:00",
                "client_code": "feedhub",
                "order_details": [{
                        "product_id": 1425,
                        "qty": 20,
                        "unit": "sak",
                        "detil_pakan_jumlah_kg": 600,
                        "unit_price_petani": 406674,
                        "subtotal_petani": 8133480,
                        "jenis_barang": "pakan",
                        "product_type": "pakan",
                        "tenor": 2
                }]
        }
},
                         headers={'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE5NTkxODEyMDAsImp0aSI6IkhJZERxWEtXbVRGTVFsY1ciLCJpc3MiOiJlZmlzaGVyeS1zZXJ2aWNlLWF1dGgiLCJpZCI6MCwidXVpZCI6IjdlOTY0N2VlLThiYjEtNDJhNC1hZDQ0LTUzMjYwODVmZjMzZiIsInN1YiI6MCwiZW1haWwiOiJtb2hhbWFkLmhhbmlmYW5AZWZpc2hlcnkuY29tIiwibmFtZSI6ImhhbmlmYW5tIiwicGhvbmUiOiIiLCJpc0FkbWluIjowLCJzdGF0dXMiOiIiLCJpc19uYmlvdCI6ZmFsc2UsInN1YmRpc3RyaWN0X2lkIjoiIiwicHJvdl9jb2RlIjowLCJjdXN0b21lcl9udW1iZXIiOiIiLCJhcHBfdXNlcl9pZCI6MCwidXNlcm5hbWUiOiIiLCJhZGRyZXNzIjoiIiwicGljdHVyZSI6IiIsImNvbXBhbnlfbmFtZSI6IiIsImNyZWF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsInVwZGF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsImxvY2F0aW9uIjoiIiwiaW50ZXJlc3QiOiIiLCJ2ZXJzaW9uIjoyLCJsZWFkX2lkIjoiIiwibGVhZF9uYW1lIjoiaGFuaWZhbm0iLCJpYXQiOjE2NTMyOTUyNzJ9.k0nXJCXWSAIflN4tIiSZlwV-IHKGSYkd8xFsN5dCL1g'})

class apply_order_cash_with_spesific_promo_pakan_lead_id_513qwy9ap6hu(HttpUser):
    
    wait_time = between(0.1, 2000)


    @task
    def apply_order_cash_with_spesific_promo_pakan_lead_id_513qwy9ap6hu(self):
        print("apply_order_cash_with_spesific_promo_pakan_lead_id_513qwy9ap6hu is starting")


        self.client.request_name = "Apply order cash with spesific promo pakan lead id 513qwy9ap6hu"
        self.client.post('/apply-promo',json=
                            
    {
        "order": {
                "order_type": "member",
                "no_pks": "2821/MTN-LEG/EXT/VII/2021",
                "lead_id": "513qwy9ap6hu",
                "point_id": 6,
                "order_date": "2022-12-15T16:54:52+07:00",
                "client_code": "feedhub",
                "order_details": [{
                        "product_id": 1425,
                        "qty": 20,
                        "unit": "sak",
                        "detil_pakan_jumlah_kg": 600,
                        "unit_price_petani": 398700,
                        "subtotal_petani": 7974000,
                        "jenis_barang": "pakan",
                        "product_type": "pakan",
                        "tenor": 0
                }]
        }
},
                         headers={'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE5NTkxODEyMDAsImp0aSI6IkhJZERxWEtXbVRGTVFsY1ciLCJpc3MiOiJlZmlzaGVyeS1zZXJ2aWNlLWF1dGgiLCJpZCI6MCwidXVpZCI6IjdlOTY0N2VlLThiYjEtNDJhNC1hZDQ0LTUzMjYwODVmZjMzZiIsInN1YiI6MCwiZW1haWwiOiJtb2hhbWFkLmhhbmlmYW5AZWZpc2hlcnkuY29tIiwibmFtZSI6ImhhbmlmYW5tIiwicGhvbmUiOiIiLCJpc0FkbWluIjowLCJzdGF0dXMiOiIiLCJpc19uYmlvdCI6ZmFsc2UsInN1YmRpc3RyaWN0X2lkIjoiIiwicHJvdl9jb2RlIjowLCJjdXN0b21lcl9udW1iZXIiOiIiLCJhcHBfdXNlcl9pZCI6MCwidXNlcm5hbWUiOiIiLCJhZGRyZXNzIjoiIiwicGljdHVyZSI6IiIsImNvbXBhbnlfbmFtZSI6IiIsImNyZWF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsInVwZGF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsImxvY2F0aW9uIjoiIiwiaW50ZXJlc3QiOiIiLCJ2ZXJzaW9uIjoyLCJsZWFkX2lkIjoiIiwibGVhZF9uYW1lIjoiaGFuaWZhbm0iLCJpYXQiOjE2NTMyOTUyNzJ9.k0nXJCXWSAIflN4tIiSZlwV-IHKGSYkd8xFsN5dCL1g'})

class apply_order_kabayan_with_spesific_promo_pakan_lead_id_513qwy9ap6hu(HttpUser):
    
    wait_time = between(0.1, 2000)


    @task
    def apply_order_kabayan_with_spesific_promo_pakan_lead_id_513qwy9ap6hu(self):
        print("apply_order_kabayan_with_spesific_promo_pakan_lead_id_513qwy9ap6hu is starting")


        self.client.request_name = "Apply order kabayan with spesific promo pakan lead id 513qwy9ap6hu"
        self.client.post('/apply-promo',json=
                            
    {
        "order": {
                "order_type": "kabayan",
                "no_pks": "2821/MTN-LEG/EXT/VII/2021",
                "lead_id": "513qwy9ap6hu",
                "point_id": 6,
                "order_date": "2022-12-15T16:54:52+07:00",
                "client_code": "feedhub",
                "order_details": [{
                        "product_id": 1425,
                        "qty": 20,
                        "unit": "sak",
                        "detil_pakan_jumlah_kg": 600,
                        "unit_price_petani": 406674,
                        "subtotal_petani": 8133480,
                        "jenis_barang": "pakan",
                        "product_type": "pakan",
                        "tenor": 2
                }]
        }
},
                         headers={'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE5NTkxODEyMDAsImp0aSI6IkhJZERxWEtXbVRGTVFsY1ciLCJpc3MiOiJlZmlzaGVyeS1zZXJ2aWNlLWF1dGgiLCJpZCI6MCwidXVpZCI6IjdlOTY0N2VlLThiYjEtNDJhNC1hZDQ0LTUzMjYwODVmZjMzZiIsInN1YiI6MCwiZW1haWwiOiJtb2hhbWFkLmhhbmlmYW5AZWZpc2hlcnkuY29tIiwibmFtZSI6ImhhbmlmYW5tIiwicGhvbmUiOiIiLCJpc0FkbWluIjowLCJzdGF0dXMiOiIiLCJpc19uYmlvdCI6ZmFsc2UsInN1YmRpc3RyaWN0X2lkIjoiIiwicHJvdl9jb2RlIjowLCJjdXN0b21lcl9udW1iZXIiOiIiLCJhcHBfdXNlcl9pZCI6MCwidXNlcm5hbWUiOiIiLCJhZGRyZXNzIjoiIiwicGljdHVyZSI6IiIsImNvbXBhbnlfbmFtZSI6IiIsImNyZWF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsInVwZGF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsImxvY2F0aW9uIjoiIiwiaW50ZXJlc3QiOiIiLCJ2ZXJzaW9uIjoyLCJsZWFkX2lkIjoiIiwibGVhZF9uYW1lIjoiaGFuaWZhbm0iLCJpYXQiOjE2NTMyOTUyNzJ9.k0nXJCXWSAIflN4tIiSZlwV-IHKGSYkd8xFsN5dCL1g'})

class apply_order_cash_with_spesific_promo_point_lead_id_5123wk33h57x(HttpUser):
    
    wait_time = between(0.1, 2000)


    @task
    def apply_order_cash_with_spesific_promo_point_lead_id_5123wk33h57x(self):
        print("apply_order_cash_with_spesific_promo_point_lead_id_5123wk33h57x is starting")


        self.client.request_name = "Apply order cash with spesific promo point lead id 5123wk33h57x"
        self.client.post('/apply-promo',json=
                            
    {
        "order": {
                "order_type": "member",
                "no_pks": "6620/MTN-LEG/EXT/XII/2021",
                "lead_id": "5123wk33h57x",
                "point_id": 6,
                "order_date": "2022-12-15T16:54:52+07:00",
                "client_code": "feedhub",
                "order_details": [{
                        "product_id": 1425,
                        "qty": 20,
                        "unit": "sak",
                        "detil_pakan_jumlah_kg": 600,
                        "unit_price_petani": 398700,
                        "subtotal_petani": 7974000,
                        "jenis_barang": "pakan",
                        "product_type": "pakan",
                        "tenor": 0
                }]
        }
},
                         headers={'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE5NTkxODEyMDAsImp0aSI6IkhJZERxWEtXbVRGTVFsY1ciLCJpc3MiOiJlZmlzaGVyeS1zZXJ2aWNlLWF1dGgiLCJpZCI6MCwidXVpZCI6IjdlOTY0N2VlLThiYjEtNDJhNC1hZDQ0LTUzMjYwODVmZjMzZiIsInN1YiI6MCwiZW1haWwiOiJtb2hhbWFkLmhhbmlmYW5AZWZpc2hlcnkuY29tIiwibmFtZSI6ImhhbmlmYW5tIiwicGhvbmUiOiIiLCJpc0FkbWluIjowLCJzdGF0dXMiOiIiLCJpc19uYmlvdCI6ZmFsc2UsInN1YmRpc3RyaWN0X2lkIjoiIiwicHJvdl9jb2RlIjowLCJjdXN0b21lcl9udW1iZXIiOiIiLCJhcHBfdXNlcl9pZCI6MCwidXNlcm5hbWUiOiIiLCJhZGRyZXNzIjoiIiwicGljdHVyZSI6IiIsImNvbXBhbnlfbmFtZSI6IiIsImNyZWF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsInVwZGF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsImxvY2F0aW9uIjoiIiwiaW50ZXJlc3QiOiIiLCJ2ZXJzaW9uIjoyLCJsZWFkX2lkIjoiIiwibGVhZF9uYW1lIjoiaGFuaWZhbm0iLCJpYXQiOjE2NTMyOTUyNzJ9.k0nXJCXWSAIflN4tIiSZlwV-IHKGSYkd8xFsN5dCL1g'})

class apply_order_kabayan_with_spesific_promo_point_lead_id_5123wk33h57x(HttpUser):
    
    wait_time = between(0.1, 2000)


    @task
    def apply_order_kabayan_with_spesific_promo_point_lead_id_5123wk33h57x(self):
        print("apply_order_kabayan_with_spesific_promo_point_lead_id_5123wk33h57x is starting")


        self.client.request_name = "Apply order kabayan with spesific promo point lead id 5123wk33h57x"
        self.client.post('/apply-promo',json=
                            
    {
        "order": {
                "order_type": "kabayan",
                "no_pks": "6620/MTN-LEG/EXT/XII/2021",
                "lead_id": "5123wk33h57x",
                "point_id": 6,
                "order_date": "2022-12-15T16:54:52+07:00",
                "client_code": "feedhub",
                "order_details": [{
                        "product_id": 1425,
                        "qty": 20,
                        "unit": "sak",
                        "detil_pakan_jumlah_kg": 600,
                        "unit_price_petani": 406674,
                        "subtotal_petani": 8133480,
                        "jenis_barang": "pakan",
                        "product_type": "pakan",
                        "tenor": 2
                }]
        }
},
                         headers={'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE5NTkxODEyMDAsImp0aSI6IkhJZERxWEtXbVRGTVFsY1ciLCJpc3MiOiJlZmlzaGVyeS1zZXJ2aWNlLWF1dGgiLCJpZCI6MCwidXVpZCI6IjdlOTY0N2VlLThiYjEtNDJhNC1hZDQ0LTUzMjYwODVmZjMzZiIsInN1YiI6MCwiZW1haWwiOiJtb2hhbWFkLmhhbmlmYW5AZWZpc2hlcnkuY29tIiwibmFtZSI6ImhhbmlmYW5tIiwicGhvbmUiOiIiLCJpc0FkbWluIjowLCJzdGF0dXMiOiIiLCJpc19uYmlvdCI6ZmFsc2UsInN1YmRpc3RyaWN0X2lkIjoiIiwicHJvdl9jb2RlIjowLCJjdXN0b21lcl9udW1iZXIiOiIiLCJhcHBfdXNlcl9pZCI6MCwidXNlcm5hbWUiOiIiLCJhZGRyZXNzIjoiIiwicGljdHVyZSI6IiIsImNvbXBhbnlfbmFtZSI6IiIsImNyZWF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsInVwZGF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsImxvY2F0aW9uIjoiIiwiaW50ZXJlc3QiOiIiLCJ2ZXJzaW9uIjoyLCJsZWFkX2lkIjoiIiwibGVhZF9uYW1lIjoiaGFuaWZhbm0iLCJpYXQiOjE2NTMyOTUyNzJ9.k0nXJCXWSAIflN4tIiSZlwV-IHKGSYkd8xFsN5dCL1g'})

class apply_order_cash_with_spesific_promo_pakan_lead_id_512h4gjt4rrk(HttpUser):
    
    wait_time = between(0.1, 2000)


    @task
    def apply_order_cash_with_spesific_promo_pakan_lead_id_512h4gjt4rrk(self):
        print("apply_order_cash_with_spesific_promo_pakan_lead_id_512h4gjt4rrk is starting")


        self.client.request_name = "Apply order cash with spesific promo pakan lead id 512h4gjt4rrk"
        self.client.post('/apply-promo',json=
                            
    {
        "order": {
                "order_type": "member",
                "no_pks": "11272/MTN-LEG/EXT/VI/2022",
                "lead_id": "512h4gjt4rrk",
                "point_id": 6,
                "order_date": "2022-12-15T16:54:52+07:00",
                "client_code": "feedhub",
                "order_details": [{
                        "product_id": 1425,
                        "qty": 20,
                        "unit": "sak",
                        "detil_pakan_jumlah_kg": 600,
                        "unit_price_petani": 398700,
                        "subtotal_petani": 7974000,
                        "jenis_barang": "pakan",
                        "product_type": "pakan",
                        "tenor": 0
                }]
        }
},
                         headers={'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE5NTkxODEyMDAsImp0aSI6IkhJZERxWEtXbVRGTVFsY1ciLCJpc3MiOiJlZmlzaGVyeS1zZXJ2aWNlLWF1dGgiLCJpZCI6MCwidXVpZCI6IjdlOTY0N2VlLThiYjEtNDJhNC1hZDQ0LTUzMjYwODVmZjMzZiIsInN1YiI6MCwiZW1haWwiOiJtb2hhbWFkLmhhbmlmYW5AZWZpc2hlcnkuY29tIiwibmFtZSI6ImhhbmlmYW5tIiwicGhvbmUiOiIiLCJpc0FkbWluIjowLCJzdGF0dXMiOiIiLCJpc19uYmlvdCI6ZmFsc2UsInN1YmRpc3RyaWN0X2lkIjoiIiwicHJvdl9jb2RlIjowLCJjdXN0b21lcl9udW1iZXIiOiIiLCJhcHBfdXNlcl9pZCI6MCwidXNlcm5hbWUiOiIiLCJhZGRyZXNzIjoiIiwicGljdHVyZSI6IiIsImNvbXBhbnlfbmFtZSI6IiIsImNyZWF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsInVwZGF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsImxvY2F0aW9uIjoiIiwiaW50ZXJlc3QiOiIiLCJ2ZXJzaW9uIjoyLCJsZWFkX2lkIjoiIiwibGVhZF9uYW1lIjoiaGFuaWZhbm0iLCJpYXQiOjE2NTMyOTUyNzJ9.k0nXJCXWSAIflN4tIiSZlwV-IHKGSYkd8xFsN5dCL1g'})

class apply_order_kabayan_with_spesific_promo_pakan_lead_id_512h4gjt4rrk(HttpUser):
    
    wait_time = between(0.1, 2000)


    @task
    def apply_order_kabayan_with_spesific_promo_pakan_lead_id_512h4gjt4rrk(self):
        print("apply_order_kabayan_with_spesific_promo_pakan_lead_id_512h4gjt4rrk is starting")


        self.client.request_name = "Apply order kabayan with spesific promo pakan lead id 512h4gjt4rrk"
        self.client.post('/apply-promo',json=
                            
    {
        "order": {
                "order_type": "kabayan",
                "no_pks": "11272/MTN-LEG/EXT/VI/2022",
                "lead_id": "512h4gjt4rrk",
                "point_id": 6,
                "order_date": "2022-12-15T16:54:52+07:00",
                "client_code": "feedhub",
                "order_details": [{
                        "product_id": 1425,
                        "qty": 20,
                        "unit": "sak",
                        "detil_pakan_jumlah_kg": 600,
                        "unit_price_petani": 406674,
                        "subtotal_petani": 8133480,
                        "jenis_barang": "pakan",
                        "product_type": "pakan",
                        "tenor": 2
                }]
        }
},
                         headers={'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE5NTkxODEyMDAsImp0aSI6IkhJZERxWEtXbVRGTVFsY1ciLCJpc3MiOiJlZmlzaGVyeS1zZXJ2aWNlLWF1dGgiLCJpZCI6MCwidXVpZCI6IjdlOTY0N2VlLThiYjEtNDJhNC1hZDQ0LTUzMjYwODVmZjMzZiIsInN1YiI6MCwiZW1haWwiOiJtb2hhbWFkLmhhbmlmYW5AZWZpc2hlcnkuY29tIiwibmFtZSI6ImhhbmlmYW5tIiwicGhvbmUiOiIiLCJpc0FkbWluIjowLCJzdGF0dXMiOiIiLCJpc19uYmlvdCI6ZmFsc2UsInN1YmRpc3RyaWN0X2lkIjoiIiwicHJvdl9jb2RlIjowLCJjdXN0b21lcl9udW1iZXIiOiIiLCJhcHBfdXNlcl9pZCI6MCwidXNlcm5hbWUiOiIiLCJhZGRyZXNzIjoiIiwicGljdHVyZSI6IiIsImNvbXBhbnlfbmFtZSI6IiIsImNyZWF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsInVwZGF0ZWRfYXQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwWiIsImxvY2F0aW9uIjoiIiwiaW50ZXJlc3QiOiIiLCJ2ZXJzaW9uIjoyLCJsZWFkX2lkIjoiIiwibGVhZF9uYW1lIjoiaGFuaWZhbm0iLCJpYXQiOjE2NTMyOTUyNzJ9.k0nXJCXWSAIflN4tIiSZlwV-IHKGSYkd8xFsN5dCL1g'})
