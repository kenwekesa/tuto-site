# Generated by Django 3.2.10 on 2022-05-03 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_assignment_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, default='Pending', max_length=15, null=True),
        ),
    ]
