import helpers
service_directory = '../../services/'

class Consume:
    def __init__(self, service_name):
        self.service_name = service_name

    def get(self):
        function_entry_path = get_contract(self.contract_path())['entry']
        self.call_provider(function_entry_path)


    def call_provider(self, function_entry_path):
        exit(function_entry_path)

    def contract_path(self):
        return service_directory + self.service_name + '/contract.yml'

