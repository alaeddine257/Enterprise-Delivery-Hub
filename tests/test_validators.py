import pytest
import app.validators as validators

def test_validators_exist():
    # Check for actual validator functions
    assert hasattr(validators, 'clean_text')
    assert hasattr(validators, 'require_text')
    assert hasattr(validators, 'parse_float')
    assert hasattr(validators, 'parse_optional_int')
    assert hasattr(validators, 'as_payload')
