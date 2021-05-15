from django.db import models


# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length =50)


  def save_category(self):
    self.save()

  def delete_category(self, name):
     self.objects.filter(name=name).delete()

  @classmethod
  def update_category(cls,name,new_name):
    update = Category.objects.filter(name=name).update(name=new_name)
    return update

  def __str__(self):
        return self.name  


    



