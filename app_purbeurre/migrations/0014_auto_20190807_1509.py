# Generated by Django 2.0 on 2019-08-07 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_purbeurre', '0013_commentary_com_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentaryProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='commentary',
        ),
        migrations.RemoveField(
            model_name='user',
            name='commentary',
        ),
        migrations.AddField(
            model_name='commentary',
            name='users_com',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_purbeurre.User'),
        ),
        migrations.AlterField(
            model_name='commentary',
            name='com',
            field=models.CharField(max_length=400),
        ),
        migrations.AddField(
            model_name='commentaryproduct',
            name='com',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_purbeurre.Commentary'),
        ),
        migrations.AddField(
            model_name='commentaryproduct',
            name='prod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_purbeurre.Product'),
        ),
    ]
