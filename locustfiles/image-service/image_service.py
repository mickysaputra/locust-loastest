from locust import HttpUser, task

class ImageService(HttpUser):
    @task
    def small_image(self):
        with self.client.get("/p/q75/https://sample-videos.com/img/Sample-jpg-image-500kb.jpg") as resp:
            print(resp.status_code)
        
    @task
    def medium_image(self):
        with self.client.get("/p/q75/https://sample-videos.com/img/Sample-jpg-image-1mb.jpg") as resp:
            print(resp.status_code)

    @task
    def large_image(self):
        with self.client.get("/p/q75/https://sample-videos.com/img/Sample-jpg-image-2mb.jpg") as resp:
            print(resp.status_code)