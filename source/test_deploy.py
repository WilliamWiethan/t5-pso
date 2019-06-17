import sys
import os
import imp

import pytest

import testproject.settings as config
    
def test_staticfiles():
    imp.reload(config)
    
    assert config.STATIC_URL == '/static/'
    assert 'whitenoise' in config.MIDDLEWARE[0].lower()
    

def test_allowed_hosts():
    imp.reload(config)
    
    assert config.ALLOWED_HOSTS == ['*']
    
    
def test_logging():
    imp.reload(config)
    
    assert 'console' in config.LOGGING['handlers']