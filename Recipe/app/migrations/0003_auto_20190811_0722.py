# Generated by Django 2.2.3 on 2019-08-11 07:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190810_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipemodel',
            name='id',
        ),
        migrations.AddField(
            model_name='recipemodel',
            name='ingredient',
            field=models.ForeignKey(default='none', on_delete=django.db.models.deletion.CASCADE, to='app.IngredientModel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipemodel',
            name='step',
            field=models.ForeignKey(default='none', on_delete=django.db.models.deletion.CASCADE, to='app.StepModel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ingredientmodel',
            name='text',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='recipemodel',
            name='name',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='recipemodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.UserModel'),
        ),
        migrations.AlterField(
            model_name='stepmodel',
            name='step_text',
            field=models.CharField(default='None', max_length=100),
        ),
    ]