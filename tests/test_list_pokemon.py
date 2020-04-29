# -*- coding: utf-8 -*-

from unittest import TestCase

from api import pokemon
from tests.config import MY_VRC

class TestApi(TestCase):
    """docstring forTestApi."""

    @MY_VRC.use_cassette()
    def test_get_all(self):
        self.assertEqual(len(pokemon.all()), 10417)
