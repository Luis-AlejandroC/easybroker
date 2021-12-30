from django import urls
from django.contrib.auth import get_user_model

import sys
sys.path.insert(1, str('..'))
import pytest

@pytest.mark.parametrize('param', [
    ('home')
])
def test_render_views(client, param):
    temp_url = urls.reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 200