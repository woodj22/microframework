import yaml


def get_contract(contract_path) -> dict:
    with open(contract_path(), 'r') as stream:
        try:
            return yaml.safe_load(stream)['api']
        except yaml.YAMLError as exc:
            print(exc)
