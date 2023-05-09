# Generated by Django 4.1.3 on 2023-03-24 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_course_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='Category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courses.category'),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, default='', editable=False, unique=True),
        ),
    ]
