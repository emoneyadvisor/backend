# Generated by Django 2.2.10 on 2020-05-14 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toastapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='budget_fixed_expenses_value',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='budget_savings_value',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='budget_spending_value',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='emergency_savings_range_lower',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='emergency_savings_range_upper',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='protection_factor_lower',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='protection_factor_upper',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='protection_range_lower',
        ),
        migrations.RemoveField(
            model_name='plan',
            name='protection_range_upper',
        ),
        migrations.AddField(
            model_name='children',
            name='education',
            field=models.CharField(choices=[('In College', 'In College'), ('Going to College', 'Going to College'), ('Other', 'Other')], default='Other', max_length=25),
        ),
        migrations.AddField(
            model_name='client',
            name='total_monthly_debt_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=8, verbose_name='Total Monthly Debt Repayment'),
        ),
        migrations.AddField(
            model_name='plan',
            name='on_track',
            field=models.BooleanField(default=False, editable=False, verbose_name='Debt On Track'),
        ),
        migrations.AddField(
            model_name='plan',
            name='protection_factor',
            field=models.DecimalField(decimal_places=2, default=20.0, editable=False, max_digits=5, verbose_name='Protection Factor'),
        ),
        migrations.AddField(
            model_name='plan',
            name='recommended_budget_fixed_expenses_value',
            field=models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=8, verbose_name='Recommended Budget Fixed Expenses Value'),
        ),
        migrations.AddField(
            model_name='plan',
            name='recommended_budget_savings_value',
            field=models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=8, verbose_name='Recommended Budget Savings Value'),
        ),
        migrations.AddField(
            model_name='plan',
            name='recommended_budget_spending_value',
            field=models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=8, verbose_name='Recommended Budget Spending Value'),
        ),
        migrations.AddField(
            model_name='plan',
            name='recommended_emergency_savings_range_lower',
            field=models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=8, verbose_name='Recommended Emergency Savings Range Lower'),
        ),
        migrations.AddField(
            model_name='plan',
            name='recommended_emergency_savings_range_upper',
            field=models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=8, verbose_name='Recommended Emergency Savings Range Upper'),
        ),
        migrations.AddField(
            model_name='plan',
            name='recommended_protection_value',
            field=models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=8, verbose_name='Recommended Protection Value'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='budget_fixed_expenses_factor',
            field=models.DecimalField(decimal_places=2, default=0.5, max_digits=8, verbose_name='Budget Fixed Expenses Factor'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='budget_savings_factor',
            field=models.DecimalField(decimal_places=2, default=0.2, max_digits=8, verbose_name='Budget Savings Factor'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='budget_spending_factor',
            field=models.DecimalField(decimal_places=2, default=0.3, max_digits=8, verbose_name='Budget Spending Factor'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='emergency_savings_factor_lower',
            field=models.DecimalField(decimal_places=2, default=3.0, max_digits=8, verbose_name='Emergency Savings Factor Lower'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='emergency_savings_factor_upper',
            field=models.DecimalField(decimal_places=2, default=6.0, max_digits=8, verbose_name='Emergency Savings Factor Upper'),
        ),
    ]
