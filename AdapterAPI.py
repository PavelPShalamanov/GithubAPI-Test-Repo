import os
from github import Github, Auth
from dotenv import load_dotenv
from ColaboratorManager import RepoCollaboratorManager
from CommitStatusManager import RepoStatusManager

load_dotenv()
myPAT : str = os.getenv("MY_PAT")
myRepo : str = "PavelPShalamanov/GithubAPI-Test-Repo"
myDesc : str = "This repository was created via the GitHub API"
collabManager : RepoCollaboratorManager = RepoCollaboratorManager(myPAT, myRepo)
statusManager : RepoStatusManager = RepoStatusManager(myPAT, myRepo)

def create_repo(PAT : str, repo_name : str, repo_desc : str):
    # Authenticate with a personal access token
    g = Github(auth=Auth.Token(PAT))

    # Get the authenticated user
    user = g.get_user()

    # Create a new repository
    repo = user.create_repo(
        name=repo_name,
        description=repo_desc,
        private=True,  # True = private, False = public
        auto_init=True  # Creates README.md
    )

    print(f"Repository created: {repo.clone_url}")

def manage_collaborator(action : str, username : str):
    if action.lower() == "add":
        collabManager.add_collaborator(username)
    elif action.lower == "remove":
        collabManager.remove_collaborator(username)

def manage_statuses(action : str,
                    sha : str, 
                    state : str = "",
                    context : str = "",
                    description : str = "",
                    target_url : str = "" , 
                    ):
    if action.lower() == "set":
        statusManager.set_commit_status(sha, state, context, description, target_url)
    elif action.lower() == "list":
        statusManager.list_commit_statuses(sha)
    elif action.lower() == "get":
        statusManager.get_combined_status(sha)

# manage_collaborator("remove", "cursed144")
manage_statuses("set", )

