# Generated by Django 3.2.3 on 2021-05-15 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pichaBucket', '0002_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery/')),
                ('image_name', models.CharField(max_length=50)),
                ('image_description', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(to='pichaBucket.Category')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pichaBucket.location')),
            ],
        ),
    ]
