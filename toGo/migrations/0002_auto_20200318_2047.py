# Generated by Django 3.1 on 2020-03-18 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toGo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=128)),
                ('customer', models.CharField(max_length=128)),
                ('label', models.CharField(max_length=128)),
                ('project_type', models.CharField(max_length=128)),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Labels',
        ),
        migrations.DeleteModel(
            name='Name',
        ),
        migrations.DeleteModel(
            name='ProjectType',
        ),
    ]
