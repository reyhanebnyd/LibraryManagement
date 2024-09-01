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


# class BookFilter(models.Model):  
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)  
#     filter_date = models.DateField(null=True, blank=True)  
#     filter_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  

#     def __str__(self):  
#         return f"Filter for {self.book.title}"

