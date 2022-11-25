import json
import uuid

from locust import HttpUser,  between, task, SequentialTaskSet

headers = {
    "X-App-Token":"DSQYPS3c6emppJJ6x80JKYrZ9J3LNHtO",
}


def _get_pdf_part(file_path, file_content_type='application/pdf'):
    import os
    file_name = os.path.basename(file_path)
    file_content = open(file_path, 'rb')
    return file_name, file_content, file_content_type


class ProcessTask(SequentialTaskSet):

    document_id = ""

    @task
    def post_esign(self):
        # docusign limit 75
        self.document_id = uuid.uuid4()
        print("--- First Task " + str(self.document_id))
        payload = {
            "document_id": str(self.document_id),
            "users": json.dumps([
                {
                    "email": "erwanakse@mail.local",
                    "name": "erwan akse",
                    "participant_id": "1",
                    "phone": "089689636352",
                    "callback_url": "http://localhost/callback",
                    "return_url": "http://localhost/return",
                    "tab_position": {
                        "anchorString": "Page 3"
                    }
                },
                {
                    "email": "asep@mail.local",
                    "name": "Asep",
                    "participant_id": "2",
                    "phone": "087689636352",
                    "callback_url": "http://localhost/callback2",
                    "return_url": "http://localhost/return2",
                    "tab_position": {
                        "anchorString": "Harga"
                    }
                }
            ]),
            "meta_data": json.dumps({
                "email_subject": "Please Sign Here",
                "email_blurb": "EFishery"
            }),
            "participant_id": "1"
        }
        files = {
            "document": _get_pdf_part("/mnt/locust/locustfiles/signature/rfc.pdf")
        }
        response = self.client.post(
            '/esign/document', data=payload, files=files, headers=headers)
        print(response.text)

    @task
    def get_health(self):
        print("--- Health Check Task " + str(self.document_id))
        response = self.client.get("/health")
        print(response.text)

    @task
    def get_docment(self):
        # docusign limit 250
        print("--- Second Task " + str(self.document_id))
        response = self.client.get(
            "/esign/" + str(self.document_id), headers=headers)
        print(response.text)

    # @task
    # def get_callback(self):
    #     print("--- third Task " + str(self.document_id))
    #     response = self.client.get(
    #         "/esign/callback?document_id="+str(self.document_id)+"&participant_id=1&event=signing_complete")
    #     print(response.text)


class TestSignature(HttpUser):
    wait_time = between(0.5, 2.5)
    tasks = [ProcessTask]
