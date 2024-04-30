# Generated by Django 3.2.16 on 2024-04-30 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0005_rename_congratulations_congratulation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=20, verbose_name='Тег')),
            ],
        ),
        migrations.AddField(
            model_name='birthday',
            name='tags',
            field=models.ManyToManyField(blank=True, help_text='Удерживайте Ctrl для выбора нескольких выриантов', to='birthday.Tag', verbose_name='Теги'),
        ),
    ]
