# Generated by Django 4.1.4 on 2023-02-25 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_alter_notifications_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='type',
            field=models.CharField(choices=[('response', 'Отклик'), ('chat', 'Чат'), ('registration', 'Регистрация'), ('adding_student', 'Добавление ученика'), ('review', 'Отзыв')], max_length=200, verbose_name='Пол'),
        ),
    ]
