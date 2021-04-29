import os
import sys

path = "C:\\F1"
print(f"Start in {path}")

files = os.listdir(path)

musics = []
videos = []
documents = []
pictures = []
extension_с = []
others = []

for file in files:
    if file.endswith(".mp3") or file.endswith(".ogg") or file.endswith(".wav") or file.endswith(".amr"):
        musics.append(file)
                       
    elif file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".jpg"):
        pictures.append(file)
    
    elif file.endswith(".doc") or file.endswith(".docx") or file.endswith(".txt"):
        documents.append(file)
    
    elif file.endswith(".avi") or file.endswith(".mp4") or file.endswith(".mov"):
        videos.append(file)
    else:
        others.append(file)

    extension = file.split(".")
    extension_с.append(extension[-1])
    
print(f'Музыка: {musics}')   
print(f'Видео: {videos}')
print(f'Изображения: {pictures}')
print(f'Документы: {documents}')
print(f'Прочие файлы: {others}')
print(f'Расширения в папке: {extension_с}')