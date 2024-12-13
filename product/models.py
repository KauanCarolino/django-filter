from django.db import models

class Category(models.Model):
    name = models.CharField(verbose_name=("Nome"), max_length=100)
    def __str__(self):

        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey("Category", verbose_name=("Categoria"), on_delete=models.CASCADE)
    date = models.DateField(("Data Cadastro"), auto_now_add=False)
    price = models.DecimalField(verbose_name=("Preço"), max_digits=10, decimal_places=2)
    available = models.BooleanField(verbose_name=("Disponivel?"), default=True)

    def __str__(self):
        return self.name