from django import forms
# from django.forms.widgets import Select, HiddenInput
from .models import Story
from .validators import validate_file_extension


# Form for adding a story
# [rus] Форма добавления рассказа
class StoryForm(forms.ModelForm):
    text_file = forms.FileField(validators=[validate_file_extension])

    class Meta:
        model = Story  # the model used
        fields = ("title_story", "text_file", "image_story")  # displayed fields in the form
        labels = {"title_story": "Название рассказа", "text_file": "Файл TXT с рассказом",
                  "image_story": "Иллюстрация к рассказу"}
        # widgets = {"stories": forms.HiddenInput}
