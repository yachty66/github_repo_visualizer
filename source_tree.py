import os

def get_repo_tree(repo_path):
    tree = []
    repo_name = os.path.basename(repo_path)

    def generate_tree(directory, prefix=""):
        entries = sorted(os.scandir(directory), key=lambda e: e.name)
        for i, entry in enumerate(entries):
            is_last = i == len(entries) - 1
            node = "└── " if is_last else "├── "
            tree.append(f"{prefix}{node}{entry.name}")
            
            if entry.is_dir() and not entry.name.startswith('.'):
                new_prefix = prefix + ("    " if is_last else "│   ")
                generate_tree(entry.path, new_prefix)

    tree.append(repo_name)
    generate_tree(repo_path)
    return "\n".join(tree)

# This allows the function to be imported and used in other Python files
if __name__ == "__main__":
    # If run as a script, you can test it here
    import sys
    if len(sys.argv) > 1:
        repo_path = sys.argv[1]
        print(get_repo_tree(repo_path))
    else:
        print("Please provide the repository path as an argument.")