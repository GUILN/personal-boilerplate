import yaml
from github import Github, Repository

from Command.command_helpers import get_config_root_command
from Configuration.configuration_factory import ConfigurationFactory
from Connectors.github_connector import GithubConnector

# consts
GH_REPO = "ghRepo"
BOILERPLATE_FOLDER = "../boilerplates.yml"
ROOT_COMMAND_NAME = "root"



def run_program():
    #with open(BOILERPLATE_FOLDER) as fh:
    #    read_data = yaml.safe_load(fh)

    configuration = ConfigurationFactory.create_configuration('prod')
    github_connector = GithubConnector(configuration)

    read_data = github_connector.get_boilerplates_structure() #get_configured_boilerplates("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", "boilerplates")
    print(read_data)
    root_command = get_config_root_command(read_data)
    # Printing all commands
    print(root_command.print_all_commands())

    command_to_get = input('type the command you want \n')
    path = root_command.get_path(command_to_get.split())

    print(path)

def __main__():
    #play_with_github()

    #print(configuration.get_access_token())
    run_program()

if __name__ == "__main__":
    __main__()
