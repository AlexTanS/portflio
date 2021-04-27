"""
To write helper functions.
[rus] Для написания вспомогательных функций.
"""

from django.core.files import File
from datetime import datetime
from os.path import splitext


# reads the first 1000 characters from the file and returns them
# [rus] считывает первые 1000 символов из файла и возвращает их
# FIXME нужно написать и вставить при создании записи, чтобы автоматом заносилось
# FIXME из файла в "text_small" модели "Story"
# FIXME !!!!!!!!!!!!!!!!!!!!!!!!! НЕ СОЗДАВАТЬ ОБЪЕКТОВ МОДЕЛИ "Story"
def thousand_characters(file):
    with open(file, "r", encoding="utf-8") as f:
        temp = f.read()[:1000]
    return temp


# returns the file name in the format: "time.file_extension" (7672886.txt)
# for Story model
# [rus] возвращает имя файла в формате: "время.расширение_файла" (7672886.txt)
# для модели Story
def get_timestamp_path(instance, filename):
    return "stories/" + "%s%s" % (int(datetime.now().timestamp()), splitext(filename)[1])
