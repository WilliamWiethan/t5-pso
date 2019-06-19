import sys
import os
#import imp

import pytest

import server.settings as config
    
def test_staticfiles():
    #imp.reload(config)
    assert config.STATIC_URL == '/static/'
    assert 'whitenoise' in config.MIDDLEWARE[1].lower()
    
def test_allowed_hosts():
    #imp.reload(config)
    assert config.ALLOWED_HOSTS == ['*']
