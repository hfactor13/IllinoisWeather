import pytest
import os

def test_credentials():
    assert os.environ["GOOGLE_APPLICATION_CREDENTIALS"] is not None