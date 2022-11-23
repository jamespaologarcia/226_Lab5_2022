from django.test import TestCase
from django.utils.html import strip_tags

import game.models
# Create your tests here.
class PlayerTestCase(TestCase):
    def test_create(self):
        response = self.client.get("/game/get/1")
        output = strip_tags(response._container[0].decode())
        assert output == 'Welcome player 1! It is  your turn________________________________________________________________'
     


