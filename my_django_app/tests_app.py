from django.test import TestCase

from django.conf import settings

def test_settings_loaded():
    assert hasattr(settings, "SECRET_KEY")
    assert settings.SECRET_KEY is not None
