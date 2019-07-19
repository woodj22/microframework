
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(os.path.join(parent_dir, 'src'))
test_dir = os.path.join(parent_dir, 'tests')
from consumer import Consume
# from ..services.uuid import uuid

def test_it_can_retrieve_the_correct_service():
    Consume('uuid_generator').get()