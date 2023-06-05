import uuid

import pytest
from django.core.cache import cache
from rest_captcha import VERSION
from rest_captcha.utils import get_cache_key


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    yield APIClient()


@pytest.fixture()
def captcha_data():
    key_uuid = str(uuid.uuid4())
    key = get_cache_key(key_uuid)
    value = "TEST"

    cache.set(key, value, 60 * 60 * 24)
    yield {
        "captcha_key": key_uuid,
        "captcha_value": value,
    }
