from django.db import models
from datetime import date
from .advisor import Advisor


class Client(models.Model):
    advisor = models.ForeignKey(to=Advisor, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(
        "First Name", 
        max_length=240)
    last_name = models.CharField(
        "Last Name", 
        max_length=240)
    middle_name = models.CharField(
        "Middle Name",
        max_length=240,
        default="")
    birth_year = models.IntegerField(
        "Birth Year",
        default=date.today().year)
    email = models.EmailField(
        "Email")
    city = models.CharField(
        "City",
        max_length=100,
        default="Philadelphia")
    state = models.CharField(
        "State",
        max_length=100,
        default="PA")
    gross_income = models.DecimalField(
        "Gross Income",
        max_digits=8,
        decimal_places=2,
        default=0.0)
    after_taxes_income = models.DecimalField(
        "After Taxes Income",
        max_digits=8,
        decimal_places=2,
        default=0.0)

    def __str__(self):
        attrs = vars(self)
        return '\n'.join('%s: %s' % item for item in attrs.items())
