# Generated by Django 4.2.1 on 2023-05-23 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_blog_students_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='content',
            field=models.CharField(default=None, max_length=2000000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='students',
            name='branch',
            field=models.CharField(choices=[('BA', 'BA'), ('B.COM', 'B.COM'), ('MBA', 'MBA'), ('CA', 'CA')], default=None, max_length=10),
            preserve_default=False,
        ),
    ]
