# Generated by Django 4.0.2 on 2022-03-22 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0005_alter_userinroom_room_num_alter_userinroom_user_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinroom',
            name='room_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.room', unique=True),
        ),
        migrations.AlterField(
            model_name='userinroom',
            name='user_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.user', unique=True),
        ),
    ]
