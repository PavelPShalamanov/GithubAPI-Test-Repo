from github import Github, Auth


class RepoStatusManager:
    def __init__(self, token: str, repo_full_name: str):
        """
        :param token: PAT with repo:status permissions
        :param repo_full_name: 'owner/repo'
        """
        self.github = Github(auth=Auth.Token(token))
        self.repo = self.github.get_repo(repo_full_name)

    def set_commit_status(
        self,
        sha: str,
        state: str,
        context: str,
        description: str = "",
        target_url: str = "",
    ):
        """
        Set a commit status check.
        
        state: 'pending', 'success', 'failure', 'error'
        context: Identifier for your CI job ('ci/test-suite', 'linting', etc.)
        description: Short human-readable message
        target_url: Link to logs or a status page
        """
        status = self.repo.get_commit(sha).create_status(
            state=state,
            target_url=target_url,
            description=description,
            context=context,
        )
        print(f"Set status '{context}' -> {state}")
        return status

    def list_commit_statuses(self, sha: str):
        commit = self.repo.get_commit(sha)
        return list(commit.get_statuses())

    def get_combined_status(self, sha: str):
        return self.repo.get_combined_status(sha)
