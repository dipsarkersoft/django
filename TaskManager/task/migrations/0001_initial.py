# Generated by Django 5.1.4 on 2024-12-21 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=20)),
                ('task_desc', models.CharField(max_length=50)),
                ('is_completed', models.BooleanField(default=False)),
                ('task_assain_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
