import os


class ChangeDir:
    def __init__(self, path:str):
        self.init_dir = os.getcwd()
        self.path = path

    def __enter__(self):
        os.chdir(self.path)
        return None
    
    def __exit__(self, type, value, traceback):
        os.chdir(self.init_dir)


with ChangeDir('dir1'):
    print(os.listdir())

with ChangeDir('dir2'):
    print(os.listdir())

