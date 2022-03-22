# Generated by Django 4.0.2 on 2022-03-22 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinroom',
            name='room_num',
            field=models.ForeignKey(db_column='roomnum', on_delete=django.db.models.deletion.CASCADE, to='scheduler.room', unique=True),
        ),
        migrations.AlterField(
            model_name='userinroom',
            name='user_num',
            field=models.ForeignKey(db_column='usernum', on_delete=django.db.models.deletion.CASCADE, to='scheduler.user', unique=True),
        ),
    ]
