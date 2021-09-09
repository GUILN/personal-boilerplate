from .configuration import Configuration
PROD = 'prod'
TEST = 'test'

class ConfigurationFactory:
    @staticmethod
    def create_configuration(environment: str) -> Configuration:
        return Configuration()