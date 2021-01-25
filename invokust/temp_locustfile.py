from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(0, 0)

    @task(1)
    def get_about(self):
        """
        Gets /about
        """
        response = self.client.get("/hello")