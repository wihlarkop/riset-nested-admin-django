# Generated by Django 3.2.9 on 2021-11-09 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nested_admin_django', '0003_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nested_admin_django.comment'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='like',
            field=models.IntegerField(),
        ),
    ]
