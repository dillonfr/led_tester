#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `led_tester` package."""
import sys
sys.path.append('.')
import pytest
from click.testing import CliRunner
from ledtester import ledtester
from ledtester import cli
from ledtester import utils


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    ifile = "./data/test_data.txt"
    N, instructions = utils.parseFile(ifile)
    assert N is not None
    
def test_http():
    ifile = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
    N, instructions = utils.parseFile(ifile)
    assert N is not None
    assert instructions is not None
    
def test_class():
    Lights = cli.LightTester(20)
    assert len(Lights.lights) == 20
    
def test_count():
    Lights = cli.LightTester(5)
    Lights.lights[0][0] = True
    assert Lights.count() == 1
    
def test_turn_on():
    Lights = cli.LightTester(10)
    Lights.apply("turn on", 3, 3, 9, 9)
    assert Lights.count() > 5
    
def test_switch():
    Lights = cli.LightTester(10)
    Lights.apply("switch", 0, 0, 9, 9)
    assert Lights.count() == 100
    
def test_spell_error():
    Lights = cli.LightTester(10)
    Lights.apply("turn on", 5, 5, 9, 9)
    Lights.apply("tuzn of", 5, 5, 9, 9)
    assert Lights.count() > 5
    
    
