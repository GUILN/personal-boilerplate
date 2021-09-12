from github import Github, Repository
from github.GithubException import GithubException



class GithubConnector:
    def __init__(self, config):
        self.config = config
        self.git = Github(config.access_token)


    def get_boilerplates_structure(self) -> list:
        git = Github(self.config.access_token)

        boilerplates_repo = git.get_user().get_repo(self.config.boilerplate_repo_name)

        boilerplate_dict = self.__traverse_repo(boilerplates_repo, '')
        return [boilerplate_dict]

    def download_boilerplate(self, path_to_boilerplate: str):
        pass

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
