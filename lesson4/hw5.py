
import sys
import pathlib


def print_path(path, depth=0, margin_sumbol=" "):
    
    margin = margin_sumbol * depth

    if path.is_dir():

        print(margin*2 + path.name + "/")
        for element in path.iterdir():
            print_path(element, depth=depth+1, margin_sumbol=margin_sumbol)

    else:

        if path.suffix == ".mp3" or path.suffix == ".ogg" or path.suffix == ".wav" or path.suffix == ".amr":
            musics.append(path.name)
            print(margin*3 + f'Музыка: {musics}') 
        elif path.suffix == ".jpeg" or path.suffix == ".png" or path.suffix == ".jpg":
            pictures.append(path.name)
            print(margin*3 + f'Изображения: {pictures}')
        elif path.suffix == ".doc" or path.suffix == ".docx" or path.suffix == ".txt":
            documents.append(path.name)
            print(margin*3 + f'Документы: {documents}')
        elif path.suffix == ".avi" or path.suffix == ".mp4" or path.suffix == ".mov":
            videos.append(path.name)
            print(margin*3 + f'Видео: {videos}')
        else:
            others.append(path.name)
            print(margin*3 + f'Прочие файлы: {others}')

        extension = path.suffix
        extension_с.append(extension)
         

documents = []
musics = []
videos = []
pictures = []
extension_с = []
others = []

def der_path():
    path = "C:\\F1"
    path = pathlib.Path(path)
    print_path(path)
    print(f'\nРасширения в папкax: {extension_с}\n')

der_path()



