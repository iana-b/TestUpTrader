from django.db import models


class Menu(models.Model):
    name = models.CharField('Название', max_length=50)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField('Название', max_length=50)
    url = models.CharField('Ссылка', max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_items')

    def __str__(self):
        return self.name
