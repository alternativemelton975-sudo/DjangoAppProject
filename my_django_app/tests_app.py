from django.test import TestCase

from django.conf import settings
from django.apps import apps

def test_smoke():
    assert True

def test_settings_loaded():
    assert hasattr(settings, "SECRET_KEY")
    assert settings.SECRET_KEY is not None

def test_app_is_installed():
    assert apps.is_installed("config")  # replace if your app name differs
