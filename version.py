import git

def checkVersion():
    repo = git.Repo(".git")
    commit = repo.head.commit
    return commit

