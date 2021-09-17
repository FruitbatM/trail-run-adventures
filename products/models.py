from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Level(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField(max_length=800)

    def __str__(self):
        return self.name


class Itinerary(models.Model):

    class Meta:
        verbose_name_plural = 'itineraries'

    name = models.CharField(max_length=254, null=True)
    holiday = models.OneToOneField('Product', null=True, blank=True,
                                   on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ItineraryDay(models.Model):
    itinerary = models.ForeignKey('Itinerary', null=True, blank=True,
                                  on_delete=models.CASCADE)
    day_1 = models.CharField(max_length=254, null=True)
    day_1_overview = models.TextField(max_length=800)
    day_1_data = models.TextField(max_length=400)
    day_2 = models.CharField(max_length=254, null=True)
    day_2_overview = models.TextField(max_length=800)
    day_2_data = models.TextField(max_length=400)
    day_3 = models.CharField(max_length=254, null=True)
    day_3_overview = models.TextField(max_length=800)
    day_3_data = models.TextField(max_length=400)
    day_4 = models.CharField(max_length=254, null=True)
    day_4_overview = models.TextField(max_length=800)
    day_4_data = models.TextField(max_length=400)
    day_5 = models.CharField(max_length=254, null=True)
    day_5_overview = models.TextField(max_length=800)
    day_5_data = models.TextField(max_length=400)
    day_6 = models.CharField(max_length=254, null=True)
    day_6_overview = models.TextField(max_length=800)
    day_6_data = models.TextField(max_length=400)
    day_7 = models.CharField(max_length=254, null=True)
    day_7_overview = models.TextField(max_length=800)
    day_7_data = models.TextField(max_length=400)
    day_8 = models.CharField(max_length=254, null=True)
    day_8_overview = models.TextField(max_length=800)
    day_8_data = models.TextField(max_length=400)

    def __str__(self):
        return self.day_1


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    country = models.CharField(max_length=80)
    holiday_header_image = models.ImageField(null=True, blank=True)
    header_paragraph = models.TextField(max_length=800)
    duration = models.IntegerField(null=True, blank=True,
                                   validators=[MinValueValidator(1),
                                               MaxValueValidator(10)])
    distance = models.IntegerField(null=True, blank=True,
                                   validators=[MinValueValidator(10),
                                               MaxValueValidator(200)])
    level = models.ForeignKey('Level', null=True, blank=True,
                              on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2,
                                validators=[MinValueValidator(0.01)])
    single_supplement = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=2, decimal_places=1,
                                 null=True, blank=True,
                                 validators=[MinValueValidator(0),
                                             MaxValueValidator(5)])
    number_of_runners = models.IntegerField(null=True, blank=True,
                                            validators=[MinValueValidator(5),
                                                        MaxValueValidator(14)])
    age = models.IntegerField(null=True, blank=True,
                              validators=[MinValueValidator(16),
                                          MaxValueValidator(76)])
    start_date = models.DateField(auto_now=False, auto_now_add=False,
                                  null=True)
    end_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    guide = models.CharField(max_length=80)
    overview_paragraph_1 = models.TextField(max_length=500)
    overview_paragraph_2 = models.TextField(max_length=800)
    overview_paragraph_3 = models.TextField(max_length=800)
    running_days = models.IntegerField(null=True, blank=True,
                                       validators=[MinValueValidator(1),
                                                   MaxValueValidator(10)])
    min_elavation = models.IntegerField(null=True, blank=True,
                                        validators=[MinValueValidator(1),
                                                    MaxValueValidator(3000)])
    max_elavation = models.IntegerField(null=True, blank=True,
                                        validators=[MinValueValidator(1),
                                                    MaxValueValidator(5000)])
    elevation_gain = models.IntegerField(null=True, blank=True,
                                         validators=[MinValueValidator(100),
                                                     MaxValueValidator(12000)])
    is_holiday = models.BooleanField(default=False)
    image_1 = models.ImageField(null=True, blank=True)
    image_2 = models.ImageField(null=True, blank=True)
    image_3 = models.ImageField(null=True, blank=True)
    route_image = models.ImageField(blank=True)
    description = models.TextField(max_length=800)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name
