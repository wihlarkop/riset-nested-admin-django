# Generated by Django 3.2.9 on 2021-11-09 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nested_admin_django', '0004_auto_20211109_1212'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusEmot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emot', models.CharField(max_length=20)),
                ('attachment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nested_admin_django.attachment')),
            ],
        ),
    ]
