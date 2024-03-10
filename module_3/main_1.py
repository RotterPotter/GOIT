from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import os


def sort_folder(folder_path): #creating a thread
    with ThreadPoolExecutor() as executor:
        executor.submit(thread_function, folder_path)
        print('starting thread')

def thread_function(some_folder):
    for f in os.listdir(some_folder):
        f_path = Path(f'{some_folder}/{f}')

        if os.path.isfile(f_path):
            f_format = f.split('.')[-1]
            folder_name = f_format.upper()
            folder_path = Path(f'{root_folder_path}/{folder_name}')
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
            os.rename(f_path, Path(f'{folder_path}/{f}'))
        else:
            sort_folder(f_path)
            if not os.listdir(f_path):
                os.rmdir(f_path)


if __name__ == '__main__':
    root_folder_path = input('>>>')
    sort_folder(root_folder_path)