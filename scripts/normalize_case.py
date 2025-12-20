import os

def rename_to_lowercase(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        # Ignore les dossiers sensibles
        if ".venv" in dirpath or "__pycache__" in dirpath:
            continue

        for filename in filenames:
            old_path = os.path.join(dirpath, filename)
            new_filename = filename.lower()
            new_path = os.path.join(dirpath, new_filename)
            if old_path != new_path:
                try:
                    os.rename(old_path, new_path)
                except PermissionError:
                    pass

        for dirname in dirnames:
            if dirname in [".venv", "__pycache__"]:
                continue
            old_dir = os.path.join(dirpath, dirname)
            new_dirname = dirname.lower()
            new_dir = os.path.join(dirpath, new_dirname)
            if old_dir != new_dir:
                try:
                    os.rename(old_dir, new_dir)
                except PermissionError:
                    pass

