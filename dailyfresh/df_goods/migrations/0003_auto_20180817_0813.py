# Generated by Django 2.0.7 on 2018-08-17 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0002_auto_20180815_0149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='gclick',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gpic',
            field=models.ImageField(upload_to='static/df_goods'),
        ),
        migrations.AlterField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_goods.TypeInfo'),
        ),
    ]
