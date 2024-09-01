from django.db import models

class Author(models.Model):  
    name = models.CharField(max_length=255)  

    def __str__(self):  
        return self.name  

class Book(models.Model):  
    title = models.CharField(max_length=255)  
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  
    publication_date = models.DateField()  
    price = models.DecimalField(max_digits=10, decimal_places=2)  

    def __str__(self):  
        return self.title



