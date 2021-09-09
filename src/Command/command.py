class MalformedYamlError(Exception):
    pass


class InvalidCommandException(Exception):
    pass


class CommandDoesNotExistException(InvalidCommandException):
    pass


class CommandDoesNotContainPathPropertyException(InvalidCommandException):
    pass


def get_format_levels(parent_len: int) -> str:
    composed_format = '\n'
    composed_format = composed_format + ' ' * parent_len
    composed_format = composed_format + '|__'
    return composed_format


class Command:
    def __init__(self, command_name: str, parent: 'Command' = None):
        self.name = command_name
        self.parent = parent
        self.children_list = []

    def set_path(self, path: str = None):
        self.path = path

    def get_path(self) -> str:
        return self.path

    def set_children(self, children: 'Command'):
        self.children_list.append(children)

    def get_path(self, command_array: list) -> str:
        if len(command_array) == 0:
            return self.path
        next_command_name = command_array.pop(0)

        next_command = [c for c in self.children_list if c.name == next_command_name][0]
        return next_command.get_path(command_array)

    def print_all_commands(self, space: int = 0) -> str:
        if len(self.children_list) == 0:
            return self.name

        composed = self.name
        for cmd in self.children_list:
            composed_space = len(self.name) + space
            composed = composed + get_format_levels(composed_space)

            composed = composed + ' ' + cmd.print_all_commands(
                composed_space + 3)  # This magic 3 number is to fix the '|__' chars used to separate the paths

        return composed
