# Generated by Django 4.1.7 on 2023-10-05 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuariosHilo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=150, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('url', models.CharField(max_length=200)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]