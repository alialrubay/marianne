# Generated by Django 4.1.2 on 2022-10-18 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('how_iam', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField()),
                ('Signature', models.CharField(blank=True, max_length=255, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='my_photos/')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
