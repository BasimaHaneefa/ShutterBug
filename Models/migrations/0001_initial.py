# Generated by Django 5.0.2 on 2024-02-14 04:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_mchat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_content', models.CharField(max_length=500)),
                ('chat_time', models.DateTimeField()),
                ('chat_file', models.FileField(upload_to='ChatFiles/')),
                ('model_from', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='model_from', to='Guest.tbl_model')),
                ('model_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='model_to', to='Guest.tbl_model')),
                ('photographer_from', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photographer_receiveid', to='Guest.tbl_photographer')),
                ('photographer_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photographer_sentid', to='Guest.tbl_photographer')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_modelpic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_image', models.FileField(upload_to='Modelpics/')),
                ('post_caption', models.CharField(max_length=100)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_model')),
            ],
        ),
    ]