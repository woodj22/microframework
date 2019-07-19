import os
import sys
import pytest

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(os.path.join(parent_dir, 'src'))
test_dir = os.path.join(parent_dir, 'tests')
from provider import Provider


def test_it_can_create_a_response():
    input = {'uuid': 'oisdfjgi0djfg'}
    response = Provider('uuid_generator').make({'uuid': 'oisdfjgi0djfg'})

    assert response == input


def test_it_can_throw_an_exception_if_it_is_not_valid():
    with pytest.raises(Exception):
        Provider('uuid_generator').make({'wrongContract': 'oisdfjgi0djfg'})
