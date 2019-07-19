import yaml
service_directory = '..services/'


class Provider:
    def __init__(self, service_name):
        self.service_name = service_name

    def make(self, response):
        return response

    def validate_contact(self, response):
        contract_keys = self.get_contract().keys()
        contract_items = self.get_contract().items()

    def get_contract(self) -> dict:
        with open(self.contract_path(), 'r') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def contract_path(self):
        return service_directory + self.service_name + "/contract.yml"
