from django.db import models


class ProjectsDone(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nazwa projektu")
    description = models.TextField(verbose_name="Opis projektu")
    image = models.ImageField(upload_to='projects_done/', verbose_name="Zdjęcie projektu", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Zakończone projekty"
        verbose_name = "Zakończony projekt"


class ServiceOffers(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nazwa usługi")
    description = models.TextField(verbose_name="Opis usługi")

    class Meta:
        verbose_name_plural = "Usługi"
        verbose_name = "Usługa"


class MessagesFromForm(models.Model):
    name = models.CharField(max_length=30, blank=False, verbose_name="Imię")
    subject = models.CharField(max_length=60, blank=False, verbose_name="Temat")
    email = models.EmailField(blank=False)
    message = models.TextField(blank=False, verbose_name="Wiadomość")
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name="Wysłano")

    class Meta:
        verbose_name_plural = "Wiadomości"
        verbose_name = "Wiadomość"


class FrequentlyAsked(models.Model):
    question = models.CharField(max_length=60, verbose_name="Pytanie")
    answer = models.TextField(verbose_name="Odpowiedź")

    class Meta:
        verbose_name_plural = "Najczęściej zadawane pytania"
        verbose_name = "Pytanie"
