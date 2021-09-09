import os

ENV_ACCESS_TOKEN = 'B_ACCESS_TOKEN'
class Configuration:
    def __init__(self):
        self.access_token = os.environ[ENV_ACCESS_TOKEN]

    def get_access_token(self) -> str:
        return self.access_token