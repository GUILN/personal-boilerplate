from github import Github, Repository
from github.GithubException import GithubException



class GithubConnector:
    def __init__(self, config):
        self.config = config
        self.git = Github(config.get_access_token())

    def get_repo(self, repo_name: str) -> object:
        repo = self.git.get_user().get_repo(repo_name)
        return repo
