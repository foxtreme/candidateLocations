# Generated by Django 3.1.7 on 2021-03-09 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restApi', '0002_auto_20210309_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Economy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unemployment_rate', models.DecimalField(decimal_places=2, max_digits=2, verbose_name='Unemployment Rate')),
                ('activities', models.TextField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restApi.city')),
            ],
        ),
    ]
