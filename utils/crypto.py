from Cryptodome.Hash import SHA256
from typing import Any

import pickle


class Crypto:
    def __init__(self):
        super().__init__()

    @staticmethod
    def get_signature(data: Any) -> bytes:
        hashed_object = SHA256.new(pickle.dumps(data)).hexdigest()
        return hashed_object.encode()
