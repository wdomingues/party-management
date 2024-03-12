from django.db import models

class Guest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    cellphone = models.CharField(max_length=20)
    companion_qty = models.IntegerField(default=0)
    companion_names = models.CharField(max_length=100) #TODO improve with new fields by qty
    confirmed_1 = models.BooleanField(default=False)
    confirmed_2 = models.BooleanField(default=False)
    confirmed_3 = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name+((" e " + self.companion_names) if self.companion_names else "")
    