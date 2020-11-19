import os
import pathlib

from src.Code.Class.Zip import Zip

print(os.path.abspath(__file__))
print(os.path.basename(os.path.abspath(__file__)))
p = pathlib.Path(os.path.abspath(__file__))
print(p.parent)
print(os.path.basename(p.parent))

print(os.path.abspath(p.parent))

tab = ['.py', '.txt']

zip = Zip(p.parent)
zip.setExtensionFileToZip(tab)
zip.zip()