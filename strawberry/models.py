from django.db import models

flavour_choices = (('Strawberry', 'Strawberry'), ('Chocolate', 'Chocolate'), ('Mixed', 'Mixed'), ('Special', 'Special'), ('Jack Fruit', 'Jack Fruit'), ('Pineapple', 'Pineapple'))


class Size(models.Model):
    title = models.CharField(max_length=120)

    def __str__(self):
        return self.title


class Flavour(models.Model):
    flavour = models.CharField(max_length=120, choices=flavour_choices, default='Strawberry')
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

    def __str__(self):
        return self.flavour




