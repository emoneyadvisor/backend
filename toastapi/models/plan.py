import uuid
from decimal import Decimal

from computedfields.models import ComputedFieldsModel, computed
from django.db import models

from .client import Client


class Plan(ComputedFieldsModel):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    client = models.OneToOneField(
        to=Client,
        on_delete=models.CASCADE)
    emergency_savings_factor_upper = models.DecimalField(
        "Emergency Savings Factor Upper",
        max_digits=15,
        decimal_places=2,
        default=Decimal('6.00'))
    emergency_savings_factor_lower = models.DecimalField(
        "Emergency Savings Factor Lower",
        max_digits=15,
        decimal_places=2,
        default=Decimal('3.00'))
    budget_savings_factor = models.DecimalField(
        "Budget Savings Factor",
        max_digits=15,
        decimal_places=2,
        default=Decimal('0.20'))
    budget_fixed_expenses_factor = models.DecimalField(
        "Budget Fixed Expenses Factor",
        max_digits=15,
        decimal_places=2,
        default=Decimal('0.50'))
    budget_spending_factor = models.DecimalField(
        "Budget Spending Factor",
        max_digits=15,
        decimal_places=2,
        default=Decimal('0.30'))
    debt_repayment_factor = models.DecimalField(
        "Debt Repayment Factor",
        max_digits=15,
        decimal_places=2,
        default=Decimal('0.36'))

    @computed(models.DecimalField(
        'Retirement Factor',
        max_digits=15,
        decimal_places=2,
        default=Decimal('1.00')),
        depends=[['client', ['age']]])
    def retirement_factor(self):
        client_age = self.client.age
        if client_age < 39:
            return Decimal('1.00')
        if 40 <= client_age <= 49:
            return Decimal('3.00')
        if 50 <= client_age <= 59:
            return Decimal('6.00')
        if 60 <= client_age <= 66:
            return Decimal('8.00')
        if client_age >= 67:
            return Decimal('10.0')
        return Decimal('1.00')  # pragma: no cover

    @computed(models.BooleanField(
        'Debt On Track', default=False),
        depends=[['client', ['total_monthly_debt_amount']], ['self', ['recommended_monthly_maximum_debt_amount']]])
    def on_track(self):
        return self.client.total_monthly_debt_amount <= self.recommended_monthly_maximum_debt_amount

    @computed(models.DecimalField(
        'Protection Factor',
        max_digits=15,
        decimal_places=2,
        default=Decimal('20.0')),
        depends=[['client', ['age']]])
    def protection_factor(self):
        client_age = self.client.age
        if client_age < 30:
            return Decimal('20.0')
        if 30 <= client_age <= 39:
            return Decimal('20.0')
        if 40 <= client_age <= 49:
            return Decimal('12.0')
        if 50 <= client_age <= 59:
            return Decimal('6.00')
        if client_age >= 60:
            return Decimal('6.00')
        return Decimal('20.0')  # pragma: no cover

    # Recommended Retirement
    @computed(models.DecimalField(
        'Recommended Retirement Value',
        max_digits=20,
        decimal_places=2,
        default=0.0),
        depends=[['client', ['total_annual_income']], ['self', ['retirement_factor']]])
    def recommended_retirement_value(self):
        return self.retirement_factor * self.client.total_annual_income

    # Recommended Debt
    @computed(models.DecimalField(
        'Recommended Monthly Maximum Debt Amount',
        max_digits=20,
        decimal_places=2,
        default=Decimal('0.00')),
        depends=[['client', ['total_annual_income']], ['self', ['debt_repayment_factor']]])
    def recommended_monthly_maximum_debt_amount(self):
        return Decimal(self.client.total_annual_income) * Decimal(self.debt_repayment_factor) / Decimal('12.0')

    # Recommended emergency savings upper range
    @computed(models.DecimalField(
        'Recommended Emergency Savings Range Upper',
        max_digits=20,
        decimal_places=2,
        default=Decimal('0.00')),
        depends=[['client', ['total_annual_income']], ['self', ['emergency_savings_factor_upper']]])
    def recommended_emergency_savings_range_upper(self):
        return Decimal((self.client.total_annual_income / 12) * Decimal(self.emergency_savings_factor_upper))

    # Recommended emergency savings lower range
    @computed(models.DecimalField(
        'Recommended Emergency Savings Range Lower',
        max_digits=20,
        decimal_places=2,
        default=Decimal('0.00')),
        depends=[['client', ['total_annual_income']], ['self', ['emergency_savings_factor_lower']]])
    def recommended_emergency_savings_range_lower(self):
        return Decimal((self.client.total_annual_income / 12) * Decimal(self.emergency_savings_factor_lower))

    # Recommended Budget Saving Value
    @computed(models.DecimalField(
        'Recommended Budget Savings Value',
        max_digits=20,
        decimal_places=2,
        default=Decimal('0.00')),
        depends=[['client', ['total_annual_income']], ['self', ['budget_savings_factor']]])
    def recommended_budget_savings_value(self):
        return Decimal((self.client.total_annual_income / 12) * Decimal(self.budget_savings_factor))

    # Recommended Budget Fixed Expenses Value
    @computed(models.DecimalField(
        'Recommended Budget Fixed Expenses Value',
        max_digits=20,
        decimal_places=2,
        default=Decimal('0.00')),
        depends=[['client', ['total_annual_income']], ['self', ['budget_fixed_expenses_factor']]])
    def recommended_budget_fixed_expenses_value(self):
        return Decimal((self.client.total_annual_income / 12) * Decimal(self.budget_fixed_expenses_factor))

    # Recommended Budget Spending Value
    @computed(models.DecimalField(
        'Recommended Budget Spending Value',
        max_digits=20,
        decimal_places=2,
        default=Decimal('0.00')),
        depends=[['client', ['total_annual_income']], ['self', ['budget_spending_factor']]])
    def recommended_budget_spending_value(self):
        return Decimal((self.client.total_annual_income / 12) * Decimal(self.budget_spending_factor))

    # Recommended Protection Value
    @computed(models.DecimalField(
        'Recommended Protection Value',
        max_digits=20,
        decimal_places=2,
        default=Decimal('0.00')),
        depends=[['client', ['total_annual_income']], ['self', ['protection_factor']]])
    def recommended_protection_value(self):
        return Decimal((self.client.total_annual_income) * Decimal(self.protection_factor))

    def __str__(self):
        attrs = vars(self)  # pragma: no cover
        return '\n'.join('%s: %s' % item for item in attrs.items())  # pragma: no cover
