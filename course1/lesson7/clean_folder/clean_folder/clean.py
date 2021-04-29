import glob
import logging
import os
import pathlib
import sys
import shutil


video_folder = {".avi" : "Видео/", ".mov" : "Видео/", ".mp4" : "Видео/"}
music_folder = {".mp3" : "Музыка/", ".ogg": "Музыка/", ".arm" : "Музыка/", ".wav" : "Музыка/"}
pic_folder = {".jpg" : "Изображения/", ".png" : "Изображения/", ".jpeg" : "Изображения/"}
doc_folder = {".doc" : "Документы/", ".docx" : "Документы/", ".txt" : "Документы/", ".pdf" : "Документы/"}
archives_folder = {".rar" : "Архив/", ".zip" : "Архив/"}
archives_types = ('*.rar', '*.zip')

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


def arhive(path):

    for files in archives_types:
        arh_files = pathlib.Path(path + "\\" + 'Archives').rglob(files)

    while True:
        try:
            path_arh = next(arh_files)
        except StopIteration:
            break
        except PermissionError:
            logging.exception("permission error")
        else:
            extract_dir = path_arh.with_name(path_arh.stem)
            shutil.unpack_archive(str(path_arh), str(extract_dir), "zip" or "rar")


def drop_empty_folders(path):

    for dirpath, dirnames, filenames in os.walk(path, topdown=False):
        if not dirnames and not filenames:
            os.rmdir(dirpath)


def main():
    path = r"C:\Users\Iryna\Desktop\project-Python-GOIT"
    dirs = os.walk(path)

    for path_from_top, subdirs, files_dirs in dirs:
        for name_file in files_dirs:
            for music_format in music_folder:
                if name_file.endswith(music_format):
                    os.makedirs(path + "\\" + 'Music', exist_ok=True)
                    shutil.move(path_from_top + "\\" + name_file, path + "\\" + 'Music'+ "\\" + normalize(name_file))
                else:
                    continue

            for pic_format in pic_folder:
                if name_file.endswith(pic_format):
                    os.makedirs(path + "\\" + 'Pictures', exist_ok=True)
                    shutil.move(path_from_top + "\\" + name_file, path + "\\" + 'Pictures'+ "\\" + normalize(name_file))
                else:
                    continue       

            for doc_format in doc_folder:
                if name_file.endswith(doc_format):
                    os.makedirs(path + "\\" + 'Documents', exist_ok=True)
                    shutil.move(path_from_top + "\\" + name_file, path + "\\" + 'Documents'+ "\\" + normalize(name_file))
                else:
                    continue

            for video_format in video_folder:
                if name_file.endswith(video_format):
                    os.makedirs(path + "\\" + 'Video', exist_ok=True)
                    shutil.move(path_from_top + "\\" + name_file, path + "\\" + 'Video'+ "\\" + normalize(name_file))
                else:
                    continue

            for archives_format in archives_folder:
                if name_file.endswith(archives_format):
                    os.makedirs(path + "\\" + 'Archives', exist_ok=True)
                    shutil.move(path_from_top + "\\" + name_file, path + "\\" + 'Archives'+ "\\" + normalize(name_file))
                else:
                    continue                    
    
    arhive(path)
    
    drop_empty_folders(path)


if __name__ == "__main__":
    main() 
