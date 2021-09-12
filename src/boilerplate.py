import pickle
import fire
from Command.command import Command
from Command.command_helpers import get_config_root_command
from Configuration.configuration_factory import ConfigurationFactory
from Connectors.github_connector import GithubConnector

UPDATE_FROM_REPO = True

configuration = ConfigurationFactory.create_configuration('prod')

def update_autoconf_file():
    github_connector = GithubConnector(configuration)

    print('Fetching github boilerplate repo...')
    read_data = github_connector.get_boilerplates_structure() 
    print('Updating boilerplate data...')
    with open(configuration.boilerplates_file, "w+b") as fp:
        pickle.dump(read_data, fp)
    print('Boilerplates has been updated!')


def get_from_autoconf_file() -> list:
    read_data = None
    try:
        with open(configuration.boilerplates_file, "r+b") as fp:
            read_data = pickle.load(fp)
    except:
        raise(Exception(f'file {configuration.boilerplates_file} does not exist'))

    return read_data

def display_boilerplates_list():
    root_command = get_root_command()    # Printing all commands
    print(root_command.print_all_commands())

def get_boilerplate(boilerplate_path: str):
    boilerplate_path = f'*-{boilerplate_path}'
    root_command = get_root_command()
    path = root_command.get_path(boilerplate_path.split('-'))
    print(path)

def get_root_command() -> Command:
    read_data = get_from_autoconf_file()
    return get_config_root_command(read_data)

class Boilerplate(object):
    def get(self, path_separated_by_dash):
        get_boilerplate(path_separated_by_dash)

    def update(self):
        update_autoconf_file()

    def list(self):
        display_boilerplates_list()

def __main__():
    fire.Fire(Boilerplate)
    #run_program()

if __name__ == "__main__":
    __main__()
