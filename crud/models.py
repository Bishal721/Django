from django.db import models

# Create your models here.
class Blog(models.Model):
    title =  models.CharField(max_length=150)
    subtitle = models.CharField(max_length=200,default="This is the Sub Heading")
    description = models.TextField()


    def __str__(self) -> str:
        return self.title

class Contact(models.Model):
    name =  models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()


    def __str__(self) -> str:
        return self.name
    
    # @classmethod
    # def create(cls,name,message,email):
    #     contact = cls(name=name,message=message,email=email)
    #     return contact
