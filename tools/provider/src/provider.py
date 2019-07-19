from os.path import join

import yaml
service_directory = '../../services/'


class Provider:
    def __init__(self, service_name):
        self.service_name = service_name

    def make(self, response):
        return self.validated_contact(response)

    def validated_contact(self, response: dict):
        contract_keys = self.get_contract().keys()

        # Add type validation ?
        # contract_items = self.get_contract().items()
        diff = set(contract_keys - response.keys())

        if len(diff):
            raise Exception('The {0} Key(s) not found in contract. Please update the contract or remove the key from the response.'.format(''.join(diff)))

        return response

    def get_contract(self) -> dict:
        with open(self.contract_path(), 'r') as stream:
            try:
                return yaml.safe_load(stream)['api']
            except yaml.YAMLError as exc:
                print(exc)

    def contract_path(self):
        return service_directory + self.service_name + "/contract.yml"
