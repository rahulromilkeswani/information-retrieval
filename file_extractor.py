def extract_files(): 
    import zipfile as zf
    files = zf.ZipFile("citeseer.zip", 'r')
    files.extractall()
    files.close()