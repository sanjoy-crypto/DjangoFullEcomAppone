# Generated by Django 3.2 on 2021-05-06 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0006_auto_20210506_1319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rightimage',
            old_name='image',
            new_name='imageone',
        ),
        migrations.AddField(
            model_name='rightimage',
            name='imagetwo',
            field=models.ImageField(blank=True, upload_to='slider/'),
        ),
    ]
