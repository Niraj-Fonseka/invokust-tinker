# -*- coding: utf-8 -*-

from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(0, 0)

    def get_hello(self):
        """
        Gets /hello
        """
        response = self.client.get("/hello")
