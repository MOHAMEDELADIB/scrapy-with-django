# Generated by Django 2.2.4 on 2019-08-20 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190819_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrapyitem',
            name='contents',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='scrapyitem',
            name='title',
            field=models.TextField(blank=True),
        ),
    ]