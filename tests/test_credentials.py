from pathlib import Path
import pytest

def test_credentials():
    credential_path = Path.cwd() / "secrets" / "my_credentials.json"
    assert credential_path.exists()