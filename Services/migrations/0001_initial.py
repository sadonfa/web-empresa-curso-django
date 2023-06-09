# Generated by Django 4.1.1 on 2022-09-30 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('subtitle', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(default='null', upload_to='')),
                ('created_ad', models.DateTimeField(auto_now_add=True)),
                ('updated_ad', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
                'ordering': ['-title'],
            },
        ),
    ]
