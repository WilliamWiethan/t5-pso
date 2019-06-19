import sys
import os
#import imp

import pytest

import server.settings as config
import produtos.tests as testProd
    
def test_staticfiles():
    #imp.reload(config)
    assert config.STATIC_URL == '/static/'
    assert 'whitenoise' in config.MIDDLEWARE[1].lower()
    
def test_allowed_hosts():
    #imp.reload(config)
    assert config.ALLOWED_HOSTS == ['*']

def test_produtos():
    assert testProd.HomePageTests.test_home_page_status_code == 200
    assert testProd.HomePageTests.test_view_url_by_name == 200
    assert testProd.HomePageTests.test_home_page_contains_correct_html
    assert testProd.HomePageTests.test_home_page_does_not_contain_incorrect_html
