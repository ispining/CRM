# Generated by Django 4.1.3 on 2022-12-02 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0005_stock_delete_clients_remove_lead_age_lead_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='langs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20)),
                ('lang', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Texts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_id', models.CharField(max_length=20)),
                ('ru', models.CharField(max_length=1500)),
                ('en', models.CharField(max_length=1500)),
                ('he', models.CharField(max_length=1500)),
            ],
        ),
        migrations.AlterField(
            model_name='lead',
            name='address',
            field=models.CharField(default='', max_length=50),
        ),
    ]