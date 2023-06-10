# Generated by Django 4.2.2 on 2023-06-10 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100, verbose_name='Word')),
                ('gender', models.CharField(choices=[('dir', 'Dir'), ('der', 'Der'), ('das', 'Das')], max_length=3, verbose_name='Gender')),
            ],
        ),
    ]