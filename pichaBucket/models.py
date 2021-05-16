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


class Location(models.Model):
  name = models.CharField(max_length=50)


  def save_location(self):
        self.save()

  def delete_location(self, name):
     self.objects.filter(name=name).delete()       


  @classmethod
  def update_location(cls,name,new_name):
    update = Location.objects.filter(name=name).update(name=new_name)
    return update    


  def __str__(self):
        return self.name  



class Image(models.Model):
  image= models.ImageField(upload_to = 'gallery/', null=True)
  image_name = models.CharField(max_length=50)
  image_description= models.TextField()
  pub_date = models.DateTimeField(auto_now_add=True)
  location = models.ForeignKey('Location', on_delete=models.CASCADE)
  category = models.ManyToManyField('Category')




  def save_image(self):
    self.save()

  def delete_image(self, name):
     self.objects.filter(image_name=name).delete()

  @classmethod
  def update_image(cls,name,new_name):
    update = Image.objects.filter(image_name=name).update(name=new_name)
    return update

  @classmethod   
  def get_image(cls,id):
    image = Image.objects.get(pk=id)

    return image

  @classmethod
  def search_by_category(cls,search_term):
        images = cls.objects.filter(category__name__icontains=search_term)
        return images  

  @classmethod
  def  get_image_by_location(cls,location):
    image = Image.objects.filter(location=location)

    return image





  def __str__(self):
        return self.image_name


    



