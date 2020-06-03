# Generated by Django 3.0 on 2020-06-03 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackinfo2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('teamname', models.CharField(max_length=255)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('statusid', models.AutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=255)),
                ('contact', models.IntegerField()),
                ('college', models.CharField(max_length=300)),
                ('yearofstudy', models.CharField(max_length=10)),
                ('branch', models.CharField(max_length=40)),
                ('github', models.URLField(default='', max_length=250)),
                ('linkedin', models.URLField(default='', max_length=250)),
                ('travel', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
