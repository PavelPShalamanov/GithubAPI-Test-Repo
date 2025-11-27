from github import Github, Auth


class RepoCollaboratorManager:
    def __init__(self, token: str, repo_full_name: str):
        """
        :param token: Personal Access Token
        :param repo_full_name: "owner/repo"
        """
        self.github = Github(auth=Auth.Token(token))
        self.repo = self.github.get_repo(repo_full_name)

    def add_collaborator(self, username: str, permission: str = "push"):
        """
        Add a collaborator to the repository.
        permission can be: 'pull', 'triage', 'push', 'maintain', 'admin'
        """
        self.repo.add_to_collaborators(username, permission=permission)
        print(f"Added collaborator: {username} with permission: {permission}")

    def remove_collaborator(self, username: str):
        """Remove a collaborator from the repository."""
        self.repo.remove_from_collaborators(username)
        print(f"Removed collaborator: {username}")

    def list_collaborators(self):
        """List collaborators."""
        return [collab.login for collab in self.repo.get_collaborators()]
