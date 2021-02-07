import logging
import os
from pathlib import Path
import sys
from shutil import move
from shutil import unpack_archive

def normalize(string):
    legend = {
    ord('а'):'a',
    ord('б'):'b',
    ord('в'):'v',
    ord('г'):'g',
    ord('д'):'d',
    ord('е'):'e',
    ord('ё'):'yo',
    ord('ж'):'zh',
    ord('з'):'z',
    ord('и'):'i',
    ord('й'):'y',
    ord('к'):'k',
    ord('л'):'l',
    ord('м'):'m',
    ord('н'):'n',
    ord('о'):'o',
    ord('п'):'p',
    ord('р'):'r',
    ord('с'):'s',
    ord('т'):'t',
    ord('у'):'u',
    ord('ф'):'f',
    ord('х'):'h',
    ord('ц'):'ts',
    ord('ч'):'ch',
    ord('ш'):'sh',
    ord('щ'):'shch',
    ord('ъ'):'y',
    ord('ы'):'y',
    ord('ь'):"'",
    ord('э'):'e',
    ord('ю'):'yu',
    ord('я'):'ya',

    ord('А'):'A',
    ord('Б'):'B',
    ord('В'):'V',
    ord('Г'):'G',
    ord('Д'):'D',
    ord('Е'):'E',
    ord('Ё'):'Yo',
    ord('Ж'):'Zh',
    ord('З'):'Z',
    ord('И'):'I',
    ord('Й'):'Y',
    ord('К'):'K',
    ord('Л'):'L',
    ord('М'):'M',
    ord('Н'):'N',
    ord('О'):'O',
    ord('П'):'P',
    ord('Р'):'R',
    ord('С'):'S',
    ord('Т'):'T',
    ord('У'):'U',
    ord('Ф'):'F',
    ord('Х'):'H',
    ord('Ц'):'Ts',
    ord('Ч'):'Ch',
    ord('Ш'):'Sh',
    ord('Щ'):'Shch',
    ord('Ъ'):'Y',
    ord('Ы'):'Y',
    ord('Ь'):"'",
    ord('Э'):'E',
    ord('Ю'):'Yu',
    ord('Я'):'Ya',

    ord('!'):'_',
    ord(','):'_',
    ord('?'):'_',
    ord('/'):'_',
    ord('\\'):'_',
    ord('@'):'_',
    ord('$'):'_',
    ord('%'):'_',
    ord('+'):'_',
    ord('*'):'_',
    ord('='):'_',
    ord(':'):'_',
    ord('-'):'_',
    ord(';'):'_',
    ord('#'):'_',
    ord('№'):'_',
    ord(')'):'_',
    ord('('):'_'
    }

    result_string = str.translate(string, legend)
    return result_string

def drop_empty_folders(directory):

    for dirpath, dirnames, filenames in os.walk(directory, topdown=False):
        if not dirnames and not filenames:
            os.rmdir(dirpath)

video_folder = {".avi" : "Видео/", ".mov" : "Видео/", ".mp4" : "Видео/"}
music_folder = {".mp3" : "Музыка/", ".ogg": "Музыка/", ".arm" : "Музыка/", ".wav" : "Музыка/"}
pic_folder = {".jpg" : "Изображения/", ".png" : "Изображения/", ".jpeg" : "Изображения/"}
doc_folder = {".doc" : "Документы/", ".docx" : "Документы/", ".txt" : "Документы/", ".pdf" : "Документы/"}
archives_folder = {".rar" : "Архив/", ".zip" : "Архив/"}

path = r"C:\F1"
zip_files = Path(r"C:\F1\Archives").rglob("*.zip")
files = os.listdir(path)

for music_format in music_folder:
    for name_file in files:
        if name_file.endswith(music_format):
            result = name_file.split(str(music_format), 1)
            os.makedirs(path + "\\" + 'Music', exist_ok=True)
            move(path + "\\" + result[0] + music_format, path + "\\" + "Music" + "\\" + normalize(result[0]) + music_format)
        
for pic_format in pic_folder:
    for name_file in files:
        if name_file.endswith(pic_format):
            result = name_file.split(str(pic_format), 1)
            os.makedirs(path + "\\" + 'Pictures', exist_ok=True)
            move(path + "\\" + result[0] + pic_format, path + "\\" + "Pictures" + "\\" + normalize(result[0]) + pic_format)

for doc_format in doc_folder:
    for name_file in files:
        if name_file.endswith(doc_format):
            result = name_file.split(str(doc_format), 1)
            os.makedirs(path + "\\" + 'Documents', exist_ok=True)
            move(path + "\\" + result[0] + doc_format, path + "\\" + "Documents" + "\\" + normalize(result[0]) + doc_format)

for video_format in video_folder:
    for name_file in files:
        if name_file.endswith(video_format):
            result = name_file.split(str(video_format), 1)
            os.makedirs(path + "\\" + 'Video', exist_ok=True)
            move(path + "\\" + result[0] + video_format, path + "\\" + "Video" + "\\" + normalize(result[0]) + video_format)            

for archives_format in archives_folder:
    for name_file in files:
        if name_file.endswith(archives_format):
            result = name_file.split(str(archives_format), 1)
            os.makedirs(path + "\\" + 'Archives', exist_ok=True)
            move(path + "\\" + result[0] + archives_format, path + "\\" + "Archives" + "\\" + normalize(result[0]) + archives_format)


while True:
    try:
        path = next(zip_files)
    except StopIteration:
        break
    except PermissionError:
        logging.exception("permission error")
    else:
         extract_dir = path.with_name(path.stem)
         unpack_archive(str(path), str(extract_dir), 'zip')

drop_empty_folders(r"C:\F1")

