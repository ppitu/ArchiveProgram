import os
import zipfile
import pathlib

class Zip:
    def __init__(self, path):
        self.path = path
        self.file_path = []
        self.extension_file_to_zip = []

    def setExtensionFileToZip(self, tab):
        self.extension_file_to_zip = tab

    def zip(self):

        print(self.path)

        rootdir = os.path.basename(self.path)

        # writing files to a zipfile
        with zipfile.ZipFile('test.zip', 'w') as m_zip:
            for root, dirs, files in os.walk(self.path):
                for file in files:

                    filepath = os.path.join(root, file)
                    parentpath = os.path.relpath(filepath, self.path)
                    arcname = os.path.join(rootdir, parentpath)

                    if pathlib.Path(filepath).suffix not in self.extension_file_to_zip:
                        continue

                    m_zip.write(filepath, arcname)
