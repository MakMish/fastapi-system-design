from locust import HttpUser,between,task,wait_time
class work(HttpUser):
    host="http://127.0.0.1:8000/user"
    wait_time=between(1,3)
    @task
    def sata(self):
        self.client.post("/login",data={
            "username": "jasj@gmail.com",
            "password": "1235"
        })