from git_repo import clone_repo
from source_tree import get_repo_tree
def main():
    repo_url = "https://github.com/PKU-YuanGroup/Open-Sora-Plan"
    repo_name = clone_repo(repo_url)
    print(f"Cloned repo folder name: {repo_name}")
    repo_tree = get_repo_tree(repo_name)
    with open('repo_structure.txt', 'w') as f:
        f.write(repo_tree)
    print(f"Repo tree written to repo_structure.txt")

if __name__ == "__main__":
    main()