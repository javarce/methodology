# Generated by Django 2.0.3 on 2018-04-03 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buysell', '0008_message_received'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('time', models.DateTimeField(verbose_name='time sent')),
                ('name', models.CharField(max_length=200)),
                ('post_identifier', models.IntegerField(blank=True)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buysell.Account')),
            ],
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.RenameField(
            model_name='received',
            old_name='sender',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='received',
            old_name='time_sent',
            new_name='time',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
