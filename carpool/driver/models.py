from django.db import models
from django.contrib.auth.models import User


# Driver model.
class Driver(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(blank = True,max_length = 30)
    destination= models.TextField(max_length=100)
    avatar = models.ImageField(upload_to = 'avatar/')
    
    def __str__(self):
        return self.name

    def save_driver(self):
        self.save()
        
    @classmethod
    def update_driver(cls,id,new_name):
        cls.objects.filter(id=id).update(name = new_name)

    @classmethod
    def delete_driver(cls,id):
        cls.objects.filter(id).delete()

