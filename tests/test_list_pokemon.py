# -*- coding: utf-8 -*-

from unittest import TestCase

from api import pokemon
from tests.config import my_vcr

class TestApi(TestCase):
    """docstring forTestApi."""

    @my_vcr.use_cassette()
    def test_get_all(self):
        self.assertEqual(len(pokemon.all()), 10417)
