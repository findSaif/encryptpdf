import os 
import pikepdf 
from pikepdf import Pdf

password = 'YOURPASSWORD'
path = os.getcwd()

def protect(file, password=password):
  
    pdf = Pdf.open(file)    
    pdf.save(os.path.splitext(file)[0] + '_encrypted.pdf', 
             encryption=pikepdf.Encryption(owner=password, user=password, R=4)) 
    pdf.close()
    print(file, " is successfully encrypted.")
    return

def remove_originals(file):

    if file.endswith(('.pdf', '.PDF')):
        if not file.endswith('_encrypted.pdf'):
            os.remove(file)

#protecting
for folder, subfolders, files in os.walk(path):
    for file in files:
        if file.endswith(('.pdf', '.PDF')):
            protect(os.path.join(folder, file))

#removing originals
for folder, subfolders, files in os.walk(path):
    for file in files:
        if file.endswith(('.pdf', '.PDF')):    
            remove_originals(os.path.join(folder, file))

#renaming the encrypted files to match the original filenames
for folder, subfolders, files in os.walk(path):
    for file in files:
        if file.endswith(('.pdf', '.PDF')):
            os.rename(os.path.join(folder, file), os.path.join(folder, file.replace('_encrypted', '')))