import os
import base64
from github import Github, Repository
from github.GithubException import GithubException
from .file_helper import write_out_file


class GithubConnector:
    def __init__(self, config):
        self.config = config
        self.git = Github(config.access_token)
        self.boilerplate_repository = self.git.get_user().get_repo(self.config.boilerplate_repo_name)


    def get_boilerplates_structure(self) -> list:
        boilerplate_dict = self.__traverse_repo(self.boilerplate_repository, '')
        return [boilerplate_dict]

    def download_boilerplate(self, path_to_boilerplate: str):
        contents = self.boilerplate_repository.get_contents(path_to_boilerplate)

        for content in contents:
            print(f'Downloading {content}...')
            if content.type == 'dir':
                self.download_boilerplate(content.path)
            else:
                try:
                    print(f'Downloading file {content.name}')
                    print(f'path is {content.path}')
                    file_content = self.boilerplate_repository.get_contents(content.path)
                    file_data = base64.b64decode(file_content.content)
                    write_out_file(content.name, file_data.decode())
                except (GithubException, IOError) as e:
                    raise(Exception(f'Error in download_boilerplate when processing: {content.path} - {e}'))

    def __traverse_repo(self, repo, dir_name: str, root_name: str = "*") -> dict:
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
                root_dict[root_name].append(self.__traverse_repo(repo, new_dir_to_traverse, dir.name))

        return root_dict
