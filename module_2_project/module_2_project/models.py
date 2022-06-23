from django.db import models

class Vulnes(models.Model):
    class Meta():
        verbose_name_plural = "vuln"

    vuln = models.CharField(max_length=255, verbose_name="Vuln ID")
    description = models.TextField(verbose_name="Description", blank=True)
    score = models.FloatField(verbose_name="Score")

    def __str__(self):
        return f"{self.vuln} {self.score}"


