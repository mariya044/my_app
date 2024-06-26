# Generated by Django 5.0.6 on 2024-06-26 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('first_name', models.CharField(max_length=100)),
                ('second_name', models.CharField(max_length=100)),
                ('subject', models.CharField(choices=[('English', 'English'), ('Russian', 'Russian'), ('Math', 'Math'), ('History', 'History'), ('Belarusian', 'Belarusian'), ('Chemistry', 'Chemistry'), ('Physics', 'Physics')], default='English', max_length=100)),
                ('about', models.TextField(blank=True, max_length=500, null=True)),
                ('qualification', models.CharField(max_length=200)),
                ('work_experience', models.CharField(max_length=300)),
                ('organizations', models.CharField(max_length=300)),
                ('address', models.CharField(max_length=100)),
                ('online_lessons', models.CharField(choices=[('+', '+'), ('-', '-')], default='+', max_length=100)),
                ('offline_lessons', models.CharField(choices=[('+', '+'), ('-', '-')], default='+', max_length=100)),
                ('lessons_at_home', models.CharField(choices=[('+', '+'), ('-', '-')], default='+', max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('time_of_lesson', models.CharField(choices=[('30', '30'), ('45', '45'), ('60', '60'), ('90', '90')], default='60')),
                ('add_information', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]