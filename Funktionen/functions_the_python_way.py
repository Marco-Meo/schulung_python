import os

def list_files(dir):
    return [os.path.basename(d.path) if d.is_file else None for d in os.scandir(dir)]

if __name__ == '__main__':
    files = list_files(os.getcwd())
    print(files)