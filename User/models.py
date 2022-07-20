from django.db import models

# Create your models here.

# User class 
class User(models.Model):
    # MOROCCO CITY
    CITY_CHOICES = (
        (1,"Rabat"),
        (2,"Kenitra"),
        (3,"Tanger"),
        (4,"Oriental"),
        (5,"Souss"),
        (6,"Fes"),
        (7,"Marrakech"),
        (8,"Meknes"),
        (9,"Agadir"),
        (10,"Tetouan"),
        (11,"Safi"),
        (12,"Settat"),
        (13,"Khouribga"),
        (14,"Sale"),
        (15,"Oujda"),
        (16,"Taza"),
        (17,"Tiznit")
    )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50,choices=CITY_CHOICES,default="Kenitra")
    zipcode = models.CharField(max_length=20)



    def __str__(self):
        return f'{self.first_name} {self.last_name}'





# Contact class
class Contact(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.name}'