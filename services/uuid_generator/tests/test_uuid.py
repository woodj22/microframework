import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(os.path.join(parent_dir, 'src'))
test_dir = os.path.join(parent_dir, 'tests')

from generate_uuid import uuid1


def test_it_can_generate_a_uuid_string():
    uuid = uuid1()
    assert type(uuid) is str
