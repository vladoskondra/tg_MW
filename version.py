import git

def main():
    repo = git.Repo(".git")
    commit = repo.head.commit
    print(commit)

if __name__== "__main__":
    main()
