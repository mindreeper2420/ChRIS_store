# Generated by Django 2.1.4 on 2020-02-12 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plugins', '0008_auto_20190607_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='defaultpathparameter',
            name='plugin_param',
        ),
        migrations.AlterField(
            model_name='pluginparameter',
            name='type',
            field=models.CharField(choices=[('string', 'String values'), ('float', 'Float values'), ('boolean', 'Boolean values'), ('integer', 'Integer values'), ('path', 'Path values'), ('unextpath', 'Unextracted path values')], default='string', max_length=10),
        ),
        migrations.DeleteModel(
            name='DefaultPathParameter',
        ),
    ]