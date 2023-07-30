from django.db import models


class Advertisement(models.Model):
    title = models.CharField("заголовок", max_length=60)
    description = models. TextField("описание")
    price = models.DecimalField("цена", max_digits=10, decimal_places=2)
    is_auction = models.BooleanField("уместен ли торг", help_text="отметьте, если уместен торг")
    updated_at = models.DateTimeField("дата обновления", auto_now=True)
    created_at = models.DateTimeField("дата публикации", auto_now_add=True)
    