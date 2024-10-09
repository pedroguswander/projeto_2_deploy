from django.db import models

class Material(models.Model) :
    material = models.CharField(max_length=20)
    quantidade = models.IntegerField()
    preco = models.FloatField()
    date_added = models.DateTimeField(null=True)

    def __str__(self):
        return self.material
