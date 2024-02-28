# Generated by Django 5.0.2 on 2024-02-28 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('start', models.DateField(blank=True, null=True)),
                ('finish', models.DateField(blank=True, null=True)),
                ('img', models.TextField(blank=True, null=True)),
                ('link', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=20)),
                ('subject', models.CharField(blank=True, max_length=200, null=True)),
                ('facility', models.CharField(blank=True, max_length=300, null=True)),
                ('mon', models.CharField(blank=True, max_length=20, null=True)),
                ('tue', models.CharField(blank=True, max_length=20, null=True)),
                ('wed', models.CharField(blank=True, max_length=20, null=True)),
                ('thu', models.CharField(blank=True, max_length=20, null=True)),
                ('fri', models.CharField(blank=True, max_length=20, null=True)),
                ('sat', models.CharField(blank=True, max_length=20, null=True)),
                ('sun', models.CharField(blank=True, max_length=20, null=True)),
                ('note', models.CharField(blank=True, max_length=200, null=True)),
                ('page1', models.CharField(blank=True, max_length=200, null=True)),
                ('page2', models.CharField(blank=True, max_length=200, null=True)),
                ('page3', models.CharField(blank=True, max_length=200, null=True)),
                ('tel', models.CharField(blank=True, max_length=20, null=True)),
                ('tag', models.CharField(blank=True, max_length=400, null=True)),
                ('region', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('lat', models.CharField(blank=True, max_length=20, null=True)),
                ('lon', models.CharField(blank=True, max_length=20, null=True)),
                ('img', models.TextField(blank=True, null=True)),
            ],
        ),
    ]