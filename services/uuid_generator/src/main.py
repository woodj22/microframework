
from tools.provider.src.provider import Provider
from .generate_uuid import uuid1


def handle():
    return Provider('uuid_generator').make({'uuid': uuid1()})
