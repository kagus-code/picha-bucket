from django.test import TestCase
from .models import Location, Category, Image
import datetime as dt

# Create your tests here.


class LocationTestClass(TestCase):

   # Set up method
    def setUp(self):
        self.location = Location(
            name='Africa', )

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))


    #Testing save method 
    def test_save_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)   

    def test_delete_method(self):
        self.location.save_location()
        Location.delete_location(Location, name='Africa')
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)     

    def test_update_location(self):
        self.location.save_location()
        Location.update_location(name='Africa', new_name='Asia')
        self.assertTrue(Location.objects.get(name='Asia'))


    def test_get_location_id(self):
        self.location.save_location()
        location_id = Location.get_location_id(id=self.location.id)
        self.assertEqual(location_id,self.location)

    def tearDown(self):
        Location.objects.all().delete()    

class CategoryTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.category = Category(
            name='nature', )

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))


    #Testing save method 
    def test_save_method(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)       

    def test_delete_method(self):
        self.category.save_category()
        Category.delete_category(Category, name='nature')
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)     

    def test_update_location(self):
        self.category.save_category()
        Category.update_category(name='nature', new_name='travel')
        self.assertTrue(Category.objects.get(name='travel'))    

    def tearDown(self):
        Category.objects.all().delete()   





class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new Location and saving it
    
        self.location = Location(
            name='Africa', )

        # Creating a new Category and saving it
        self.category = Category(
            name='nature', )

        self.new_image = Image(image ='gallery/',
            image_name='Machu pichu', image_description='This is a random test description', location=self.location)
            
     # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image, Image))

    
    #Testing save method 
    def test_save_method(self):
        self.location.save()
        self.category.save()
        self.new_image.save_image()

        images = Image.objects.all()
        self.assertTrue(len(images) > 0)       

    def test_delete_method(self):
        self.location.save()
        self.category.save()
        self.new_image.save_image()
        Image.delete_image(Image, name='Machu pichu')
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)     

    def test_update_image(self):
        self.location.save()
        self.category.save()
        self.new_image.save_image()
        Image.update_image(name='Machu pichu', new_name='maldives')
        self.assertTrue(Image.objects.get(image_name='maldives'))  

    def test_get_image(self):
        self.location.save()
        self.category.save()
        self.new_image.save_image()  

        images = Image.get_image(id=self.new_image.id)
        self.assertEqual(images,self.new_image)      
    







    def tearDown(self):
        Location.objects.all().delete()  
        Category.objects.all().delete()   
        Image.objects.all().delete()


