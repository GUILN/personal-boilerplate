import yaml
from Command.CommandHelpers import get_config_root_command

# consts
GH_REPO = "ghRepo"
BOILERPLATE = "boilerplates"
ROOT_COMMAND_NAME = "ROOT"

def run_program(file_name: str):
    with open(f'../{file_name}.yml') as fh:
        read_data = yaml.safe_load(fh)

    root_command = get_config_root_command(read_data[BOILERPLATE])
    # Printing all commands
    print(root_command.print_all_commands())

    command_to_get = input('type the command you want \n')
    path = root_command.get_path(command_to_get.split())

    print(path)


def __main__():
    run_program('boilerplates')

if __name__ == "__main__":
    __main__()
