import pickle
from Command.command_helpers import get_config_root_command
from Configuration.configuration_factory import ConfigurationFactory
from Connectors.github_connector import GithubConnector

UPDATE_FROM_REPO = False

configuration = ConfigurationFactory.create_configuration('prod')

def update_autoconf_file():
    github_connector = GithubConnector(configuration)

    read_data = github_connector.get_boilerplates_structure() 
    with open(configuration.boilerplates_file, "w+b") as fp:
        pickle.dump(read_data, fp)


def get_from_autoconf_file() -> list:
    read_data = None
    try:
        with open(configuration.boilerplates_file, "r+b") as fp:
            read_data = pickle.load(fp)
    except:
        raise(Exception(f'file {configuration.boilerplates_file} does not exist'))

    return read_data

def run_program():
    if UPDATE_FROM_REPO:
        update_autoconf_file()

    read_data = get_from_autoconf_file()
    root_command = get_config_root_command(read_data)

    # Printing all commands
    print(root_command.print_all_commands())

    command_to_get = input('type the command you want \n')
    path = root_command.get_path(command_to_get.split())

    print(path)

def __main__():
    run_program()

if __name__ == "__main__":
    __main__()
