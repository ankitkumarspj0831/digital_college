# Generated by Django 2.1.2 on 2018-11-18 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='announcements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('message', models.CharField(max_length=250)),
                ('college_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Registered_College')),
            ],
        ),
    ]