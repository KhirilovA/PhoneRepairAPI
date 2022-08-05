# Generated by Django 3.2.15 on 2022-08-05 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_invoice_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Not started'), (2, 'In progress'), (3, 'Done')], default=1),
        ),
    ]