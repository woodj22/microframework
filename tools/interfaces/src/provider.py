from os.path import join

import yaml
from .helpers import get_contract
service_directory = '../../services/'


class Provider:
    def __init__(self, service_name):
        self.service_name = service_name

    def make(self, response):
        return self.validated_contact(response)

    def validated_contact(self, response: dict):
        contract_keys = get_contract().keys()

        # Add type validation ?
        # contract_items = self.get_contract().items()
        diff = set(contract_keys - response.keys())

        if len(diff):
            raise Exception('The {0} Key(s) not found in contract. Please update the contract or remove the key from the response.'.format(''.join(diff)))

        return response

    def contract_path(self):
        return service_directory + self.service_name + "/contract.yml"
