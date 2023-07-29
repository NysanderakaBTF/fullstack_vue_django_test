from django.db import models


class BannerCard(models.Model):
    top_text = models.CharField(max_length=20, verbose_name="Верхний текст")
    main_text = models.CharField(max_length=6, verbose_name="Главный средний текст")
    bottom_text = models.CharField(max_length=20, verbose_name="Нижний текст")


class NavbarLink(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название ссылки")
    url = models.CharField(verbose_name="Сслылка")
