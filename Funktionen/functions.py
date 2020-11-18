import os

def list_files(dir):
    list_of_files = []
    all_objects_in_directory = os.scandir(dir)
    for d in all_objects_in_directory:
        if d.is_file:
            full_pathname = d.path
            filename = os.path.basename(full_pathname)
            list_of_files.append(filename)
    return list_of_files

if __name__ == '__main__':
    local_path = os.getcwd()
    files = list_files(local_path)
    print(files)