import pytest

import server.settings as config
    
def test_staticfiles():
    assert config.STATIC_URL == '/static/'
    assert 'whitenoise' in config.MIDDLEWARE[1].lower()
    
def test_allowed_hosts():
    assert config.ALLOWED_HOSTS == ['*']
