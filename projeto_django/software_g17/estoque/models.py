from django.db import models

class Brinquedo(models.Model) :
    brinquedo = models.CharField(max_length=50)
    descricao = models.TextField()
    passo_a_passo = models.TextField()

    def __str__(self) :
        return self.brinquedo

class material_de_um_brinquedo(models.Model) :
    brinquedo = models.ForeignKey(Brinquedo, on_delete=models.CASCADE, related_name='Brinquedo', null=True)
    material = models.CharField(max_length=20)
    quantidade = models.IntegerField()

    def __str__(self) :
        return self.material

class Material(models.Model) :
    material = models.CharField(max_length=20)
    quantidade = models.IntegerField()
    preco = models.FloatField()
    date_added = models.DateTimeField(null=True)

    def __str__(self):
        return self.material
