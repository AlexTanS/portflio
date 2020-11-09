from django.db import models
from django.contrib.auth.models import User

from .utilites import get_timestamp_path


# Model for stories (secondary to User)
# [rus] Модель для рассказов (вторична для User)
class Story(models.Model):
    # link to the author
    # [rus] ссылка на автора
    stories = models.ForeignKey(User, on_delete=models.CASCADE,
                                verbose_name="Автор рассказа")
    # story name (unique, indexed by field)
    # [rus] имя рассказа (уникально, создан индекс по полю)
    title_story = models.TextField(max_length=50, unique=True,
                                   verbose_name="Название")
    # first 1000 characters from the story (optional)
    # [rus] первые 1000 символов из рассказа (необязательно)
    text_small = models.TextField(max_length=1000, blank=True,
                                  verbose_name="Предпросмотр")
    # unloaded file with story content (path: "stories/%Y/%m/%d/", name: "time.file_type")
    # [rus] выгружаемый файл с содержимым рассказа (путь: "stories/%Y/%m/%d/", имя: "время.тип_файла")
    text_file = models.FileField(upload_to=get_timestamp_path,
                                 verbose_name="Рассказ")
    # picture for the story (optional)
    # [rus] картинка к рассказу (необязательно)
    image_story = models.ImageField(upload_to=get_timestamp_path, blank=True,
                                    verbose_name="Обложка")

    class Meta:
        verbose_name = "Рассказ"
        verbose_name_plural = "Рассказы"
