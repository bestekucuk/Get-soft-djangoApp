# Generated by Django 4.1.3 on 2023-04-06 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_remove_course_category_course_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='isHome',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='isActive',
            field=models.BooleanField(default=False),
        ),
    ]