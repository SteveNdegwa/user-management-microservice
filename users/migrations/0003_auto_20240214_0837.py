# Generated by Django 3.2.12 on 2024-02-14 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='emailverified',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='MailOtp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customuser')),
            ],
        ),
    ]