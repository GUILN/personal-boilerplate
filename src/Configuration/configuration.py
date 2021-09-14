import os

ENV_ACCESS_TOKEN = 'B_PLATE_ACCESS_TOKEN'
ENV_REPO_NAME = 'B_PLATE_REPO_NAME'

home_dir = os.environ.get('HOME')
repo_name = os.environ.get(ENV_REPO_NAME)
token = os.environ.get(ENV_ACCESS_TOKEN)


class Configuration:
    def __init__(self):
        self.access_token = token
        self.boilerplate_repo_name = repo_name
        self.boilerplates_file = f"{home_dir}/.boilerplates.autoconf"

