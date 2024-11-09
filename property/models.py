from django.db import models

# Create your models here.
class RealEstate(models.Model):
    address=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    property_option=(
        ("apartment","apartment"),
        ("house","house"),
        ("land","land")
    )
    property_type=models.CharField(max_length=200,choices=property_option,default="house")
    number_of_bedrooms=models.PositiveIntegerField()
    square_footage=models.PositiveIntegerField()
    location=models.CharField(max_length=200)
    property_image=models.ImageField(upload_to="property_images",null=True)
    contact_details=models.CharField(max_length=200)