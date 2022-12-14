# Generated by Django 4.1.1 on 2022-09-16 08:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=30)),
                ('client_email', models.EmailField(max_length=254)),
                ('client_mobile', models.CharField(max_length=10)),
                ('client_message', models.TextField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_contacted', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='projectrequest',
            name='is_contacted',
            field=models.BooleanField(default=False),
        ),
    ]
