import zipfile as zf
import tarfile
def extract_files(filename): 
    if(filename.endswith(".zip")) : 
        files = zf.ZipFile(filename, 'r')
        files.extractall()
        files.close()
    if(filename.endswith(".tar.gz")) : 
        tar = tarfile.open(filename)
        tar.extractall()
        tar.close()