import os
from django.core.exceptions import ValidationError


# Validator for the extension of the uploaded file
# [rus] Валидатор расширения загружаемого файла
def validate_file_extension(value):
    # extension of file
    # [rus] получаем расширение файла
    ext = os.path.splitext(value.name)[-1]
    # list of allowed types
    # [rus] список разрешенных типов файлов
    valid_extensions = [".txt"]
    if not ext.lower() in valid_extensions:
        raise ValidationError("Недопустимый тип файла, должен быть .txt")

# Upload File size validator
# [rus] Валидатор размера загружаемого файла
def validate_file_size(value):
    # getting the file size in bytes
    # [rus] получаем размер файла в байтах
    size = value.size
    if size > 5000000:
        raise ValidationError("Размер файла больше 5 Мб")
