from flask import url_for
from flask_testing import TestCase

import blinkwink

class TestTestCase(TestCase):

    def create_app(self):
        return blinkwink.create_app("test")

    def setUp(self):
        self.client = self.app.test_client()

    def test_can_connect_to_main(self):
        response = self.client.get(url_for("main.index"))
        assert response.status_code == 200
