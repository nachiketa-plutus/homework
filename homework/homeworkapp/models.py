from django.db import models
# from multiselectfield import MultiSelectField

# Create your models here.


class Cities(models.Model):
    city_name = models.CharField(max_length=200)

    def __str__(self):
        return self.city_name


class Cleaner(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    quality_score = models.FloatField(5)
    # cities = models.ManyToManyField(Cities, MultiSelectField(Cities), null=True)

    def __str__(self):
        return str(self.first_name) + " " + str(self .last_name)


class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)


class Booking(models.Model):
    customer = models.ForeignKey(Customer)
    cleaner = models.ForeignKey(Cleaner)
    city_id = models.IntegerField(null=False)
    book_date = models.DateTimeField()

    def __str__(self):
        return str(self.customer.first_name) + " " + str(self.customer.last_name)