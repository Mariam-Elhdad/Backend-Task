import os


class Renamefiles:
    def __init__(self):
        self.path = os.getcwd()

    def user_input_dir(self):
        print("Input the directory, please : ")
        self.path = input()
        return self.path

    def change_dir(self):
        os.chdir(self.path)

    def get_files(self):
        return os.listdir(self.path)

    def renamer(self):
        files = self.get_files()
        cnt = 0
        for file in files:
            new_file_name = f"Renamed_{cnt}"
            os.rename(file, new_file_name)
            cnt += 1


newpath = Renamefiles()
newpath.user_input_dir()
newpath.change_dir()
newpath.renamer()
print(newpath.get_files())
