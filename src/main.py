import yaml
from github import Github, Repository

from Command.command_helpers import get_config_root_command
from Configuration.configuration_factory import ConfigurationFactory
from Connectors.github_connector import GithubConnector

# consts
GH_REPO = "ghRepo"
BOILERPLATE_FOLDER = "../boilerplates.yml"
ROOT_COMMAND_NAME = "root"

def traverse_repo(repo, dir_name: str, root_name: str = "*") -> dict:
    file_contents = repo.get_contents(dir_name)
    is_boilerplate = True if len([c for c in file_contents if c.name == '.boilerplate']) > 0 else False
    root_dict = {}
    root_dict[root_name] = []

    if is_boilerplate:
        root_dict[root_name] = {'path': f'{dir_name}'}
        return root_dict
    else:
        inner_dirs = [c for c in file_contents if c.type == 'dir']
        for dir in inner_dirs:
            new_dir_to_traverse = dir_name + f'/{dir.name}'
            root_dict[root_name].append(traverse_repo(repo, new_dir_to_traverse, dir.name))

    return root_dict

def get_configured_boilerplates(pat: str, boilerplate_repo_name: str) -> list:
    git = Github(pat)

    boilerplates_repo = git.get_user().get_repo(boilerplate_repo_name)

    boilerplate_dict = traverse_repo(boilerplates_repo, '')
    return [boilerplate_dict]


def run_program():
    #with open(BOILERPLATE_FOLDER) as fh:
    #    read_data = yaml.safe_load(fh)

    read_data = get_configured_boilerplates("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", "boilerplates")
    print(read_data)
    root_command = get_config_root_command(read_data)
    # Printing all commands
    print(root_command.print_all_commands())

    command_to_get = input('type the command you want \n')
    path = root_command.get_path(command_to_get.split())

    print(path)

def play_with_github():
    configuration = ConfigurationFactory.create_configuration('prod')
    github_connector = GithubConnector(configuration)

    algo_repo = github_connector.get_repo("boilerplates")
    for content_file in algo_repo.get_contents(""):
        print(content_file)

def __main__():
    #play_with_github()

    #print(configuration.get_access_token())
    run_program()

if __name__ == "__main__":
    __main__()
