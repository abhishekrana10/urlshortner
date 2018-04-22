# Generated by Django 2.0.3 on 2018-04-17 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('short_url', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='recap',
            fields=[
                ('short_url', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('ttl', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='url_stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('browser', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('hit_time', models.IntegerField()),
                ('short_url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='short_url.url_mapping')),
            ],
        ),
        migrations.RemoveField(
            model_name='short_url_info',
            name='short_code',
        ),
        migrations.DeleteModel(
            name='Short_url_info',
        ),
    ]