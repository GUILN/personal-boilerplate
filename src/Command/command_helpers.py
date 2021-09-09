from .command import Command


PATH_PROPERTY = 'path'
ROOT_COMMAND_NAME = '*'

def traverse_config_file(config_file, root_command: 'Command'):
    if not isinstance(config_file, dict) and not isinstance(config_file, list):
        return

    if isinstance(config_file, dict):
        for d in config_file:
            if isinstance(d, dict) or isinstance(d, list):
                traverse_config_file(config_file, root_command)

            if PATH_PROPERTY in d:
                root_command.set_path(config_file[d])
            else:
                new_command = Command(d, root_command)
                root_command.set_children(new_command)
                root_command = new_command

            traverse_config_file(config_file[d], root_command)

    elif isinstance(config_file, list):
        for d in config_file:
            if not (isinstance(d, dict) or isinstance(d, list)):
                new_command = Command(d, root_command)
                root_command.set_children(new_command)
                root_command = new_command

            traverse_config_file(d, root_command)


def get_config_root_command(config_data: dict) -> Command:
    root_command = Command(ROOT_COMMAND_NAME)
    traverse_config_file(config_data, root_command)
    return root_command
