import asyncio
from aiopath import AsyncPath
import concurrent.futures
import os
import pathlib
import shutil
import time



video_folder = {".avi" : "Видео/", ".mov" : "Видео/", ".mp4" : "Видео/"}
music_folder = {".mp3" : "Музыка/", ".ogg": "Музыка/", ".arm" : "Музыка/", ".wav" : "Музыка/"}
pic_folder = {".jpg" : "Изображения/", ".png" : "Изображения/", ".jpeg" : "Изображения/"}
doc_folder = {".doc" : "Документы/", ".docx" : "Документы/", ".txt" : "Документы/", ".pdf" : "Документы/"}

def normalize(string):
    legend = {
    ord('а'):'a', ord('б'):'b', ord('в'):'v', ord('г'):'g', ord('д'):'d', ord('е'):'e', ord('ё'):'yo', ord('ж'):'zh', ord('з'):'z',
    ord('и'):'i', ord('й'):'y', ord('к'):'k', ord('л'):'l', ord('м'):'m', ord('н'):'n', ord('о'):'o', ord('п'):'p', ord('р'):'r',
    ord('с'):'s', ord('т'):'t', ord('у'):'u', ord('ф'):'f', ord('х'):'h', ord('ц'):'ts', ord('ч'):'ch', ord('ш'):'sh', ord('щ'):'shch',
    ord('ъ'):'y', ord('ы'):'y', ord('ь'):"'", ord('э'):'e', ord('ю'):'yu', ord('я'):'ya', ord('А'):'A', ord('Б'):'B', ord('В'):'V',
    ord('Г'):'G', ord('Д'):'D', ord('Е'):'E', ord('Ё'):'Yo', ord('Ж'):'Zh', ord('З'):'Z', ord('И'):'I', ord('Й'):'Y', ord('К'):'K',
    ord('Л'):'L', ord('М'):'M', ord('Н'):'N', ord('О'):'O', ord('П'):'P', ord('Р'):'R', ord('С'):'S', ord('Т'):'T', ord('У'):'U',
    ord('Ф'):'F', ord('Х'):'H', ord('Ц'):'Ts', ord('Ч'):'Ch', ord('Ш'):'Sh', ord('Щ'):'Shch', ord('Ъ'):'Y', ord('Ы'):'Y', ord('Ь'):"'",
    ord('Э'):'E', ord('Ю'):'Yu', ord('Я'):'Ya', ord('!'):'_', ord(','):'_', ord('?'):'_', ord('/'):'_', ord('\\'):'_', ord('@'):'_',
    ord('$'):'_', ord('%'):'_', ord('+'):'_', ord('*'):'_', ord('='):'_', ord(':'):'_', ord('-'):'_', ord(';'):'_', ord('#'):'_',
    ord('№'):'_', ord(')'):'_', ord('('):'_'
    }

    result_string = str.translate(string, legend)
    return result_string

async def run_file(name_folder, name):
    path = r"C:\F1"
    dirs = os.walk(path)

    for path_from_top, subdirs, files_dirs in dirs:
        for name_file in files_dirs:
            for name_format in name_folder:
                if name_file.endswith(name_format):
                    print(f'start {name}')
                    os.makedirs(path + "\\" + name, exist_ok=True)
                    shutil.move(path_from_top + "\\" + name_file, path + "\\" + name + "\\" + normalize(name_file))
                else:
                    continue
                await asyncio.sleep(1)
                print(f"{name} finished")


async def main():

    print(f"started at {time.strftime('%X')}")

    await run_file(music_folder, "Music")
    await run_file(pic_folder, "Picture")
    await run_file(video_folder, "Video")
    await run_file(doc_folder, "Document")

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
