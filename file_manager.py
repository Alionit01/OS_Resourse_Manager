class File:
    def __init__(self, name, content="", permission="read-write"):
        self.name = name
        self.content = content
        self.permission = permission

class Directory:
    def __init__(self, name):
        self.name = name
        self.files = {}
        self.subdirectories = {}

class FileSystem:
    def __init__(self):
        self.root = Directory("root")

    def create_file(self, path, file_name, permission="read-write"):
        directory = self._navigate_to(path)
        if file_name not in directory.files:
            directory.files[file_name] = File(file_name, "", permission)
            print(f"[CREATE] File '{file_name}' created at '{path}'.")
        else:
            print(f"[SKIP] File '{file_name}' already exists at '{path}'.")

    def write_file(self, path, file_name, content):
        directory = self._navigate_to(path)
        if file_name in directory.files:
            file = directory.files[file_name]
            if file.permission == "read-write":
                file.content = content
                print(f"[WRITE] Written to file '{file_name}'.")
            else:
                print(f"[DENIED] File '{file_name}' is read-only.")
        else:
            print(f"[ERROR] File '{file_name}' not found at '{path}'.")

    def read_file(self, path, file_name):
        directory = self._navigate_to(path)
        if file_name in directory.files:
            print(f"[READ] Content of '{file_name}': {directory.files[file_name].content}")
        else:
            print(f"[ERROR] File '{file_name}' not found at '{path}'.")

    def delete_file(self, path, file_name):
        directory = self._navigate_to(path)
        if file_name in directory.files:
            del directory.files[file_name]
            print(f"[DELETE] File '{file_name}' deleted from '{path}'.")
        else:
            print(f"[ERROR] File '{file_name}' not found at '{path}'.")

    def create_folder(self, path, folder_name):
        directory = self._navigate_to(path)
        if folder_name not in directory.subdirectories:
            directory.subdirectories[folder_name] = Directory(folder_name)
            print(f"[FOLDER] Folder '{folder_name}' created inside '{path}'.")
        else:
            print(f"[SKIP] Folder '{folder_name}' already exists.")

    def _navigate_to(self, path):
        parts = path.strip("/").split("/")
        current = self.root
        for part in parts:
            if part:
                current = current.subdirectories.get(part, None)
                if current is None:
                    raise Exception(f"[ERROR] Path '{path}' not found.")
        return current

# --- Example usage ---
if __name__ == "__main__":
    fs = FileSystem()

    fs.create_folder("/", "docs")
    fs.create_file("/docs", "notes.txt", "read-write")
    fs.write_file("/docs", "notes.txt", "Hello OS World!")
    fs.read_file("/docs", "notes.txt")

    fs.create_file("/docs", "readonly.txt", "read-only")
    fs.write_file("/docs", "readonly.txt", "You can't write this.")

    fs.delete_file("/docs", "notes.txt")
    fs.read_file("/docs", "notes.txt")
