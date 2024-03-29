# Generated by Django 4.2.3 on 2023-10-20 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('escribania', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='escribano',
            name='caracter',
            field=models.CharField(choices=[('Titular', 'Titular'), ('Adscripto', 'Adscripto')], default='Titular', max_length=50, verbose_name='Carácter'),
        ),
        migrations.CreateModel(
            name='ActoEscribano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='escribania.actojuridico', verbose_name='Acto Jurídico')),
                ('escribano', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='escribania.escribano', verbose_name='Escribano')),
            ],
        ),
        migrations.AddField(
            model_name='escribano',
            name='actos_juridicos',
            field=models.ManyToManyField(blank=True, through='escribania.ActoEscribano', to='escribania.actojuridico', verbose_name='Actos Jurídicos'),
        ),
    ]
