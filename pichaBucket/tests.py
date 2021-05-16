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
