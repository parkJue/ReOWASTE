# Generated by Django 4.1.3 on 2024-02-28 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0003_alter_question_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='region',
            field=models.CharField(blank=True, choices=[('부산', '부산'), ('경북', '경북'), ('대구', '대구'), ('서울', '서울'), ('경기', '경기'), ('전북', '전북'), ('세종', '세종'), ('충남', '충남'), ('인천', '인천'), ('경남', '경남'), ('강원', '강원'), ('충북', '충북'), ('광주', '광주'), ('울산', '울산'), ('제주', '제주'), ('대전', '대전'), ('전남', '전남')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='status',
            field=models.CharField(blank=True, choices=[('예약중', '예약중'), ('나눔중', '나눔중'), ('완료', '완료')], max_length=100, null=True),
        ),
    ]
