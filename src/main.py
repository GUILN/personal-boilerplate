import yaml
from Command.CommandHelpers import get_config_root_command

# consts
GH_REPO = "ghRepo"
BOILERPLATE_FOLDER = "../boilerplates.yml"
ROOT_COMMAND_NAME = "root"


def run_program():
    with open(BOILERPLATE_FOLDER) as fh:
        read_data = yaml.safe_load(fh)
    print(read_data)
    root_command = get_config_root_command(read_data['boilerplates'])
    # Printing all commands
    print(root_command.print_all_commands())

    command_to_get = input('type the command you want \n')
    path = root_command.get_path(command_to_get.split())

    print(path)


def __main__():
    run_program()

if __name__ == "__main__":
    __main__()
