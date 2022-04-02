# Generated by Django 3.0.5 on 2022-03-22 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20220320_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.IntegerField(choices=[(2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025), (2026, 2026)], default=2022, max_length=4, verbose_name='year'),
        ),
    ]