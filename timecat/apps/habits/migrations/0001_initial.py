# Generated by Django 2.0.5 on 2018-09-27 04:14

import apps.habits.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckMark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.IntegerField(default=0, verbose_name='时间戳')),
                ('value', enumfields.fields.EnumIntegerField(default=0, enum=apps.habits.models.CheckMarkLabel, verbose_name='标记状态')),
            ],
            options={
                'db_table': 'CheckMark',
                'ordering': ('timestamp',),
            },
        ),
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='新习惯', max_length=100, verbose_name='标题')),
                ('content', models.TextField(blank=True, default='', verbose_name='内容')),
                ('created_datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_datetime', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_archived', models.BooleanField(default=False, verbose_name='是否归档')),
                ('freqNum', models.IntegerField(default=1, verbose_name='渲染类型')),
                ('freqDen', models.IntegerField(default=1, verbose_name='渲染类型')),
                ('reminderDay', models.IntegerField(default=0, verbose_name='提醒天数')),
                ('reminderHour', models.IntegerField(default=0, verbose_name='提醒小时数')),
                ('reminderMin', models.IntegerField(default=0, verbose_name='提醒分钟数')),
                ('color', models.CharField(blank=True, default='#ffffffff', max_length=9, verbose_name='颜色')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'db_table': 'Habit',
                'ordering': ('update_datetime',),
            },
        ),
        migrations.CreateModel(
            name='Repetition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.IntegerField(default=0, verbose_name='时间戳')),
                ('habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habits.Habit', verbose_name='习惯')),
            ],
            options={
                'db_table': 'Repetition',
                'ordering': ('timestamp',),
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.IntegerField(default=0, verbose_name='时间戳')),
                ('score', models.IntegerField(default=0, verbose_name='分数')),
                ('habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habits.Habit', verbose_name='习惯')),
            ],
            options={
                'db_table': 'Score',
                'ordering': ('timestamp',),
            },
        ),
        migrations.CreateModel(
            name='Streak',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.IntegerField(default=0, verbose_name='开始')),
                ('end', models.IntegerField(default=0, verbose_name='结束')),
                ('length', models.IntegerField(default=0, verbose_name='持续时长')),
                ('habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habits.Habit', verbose_name='习惯')),
            ],
            options={
                'db_table': 'Streak',
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='checkmark',
            name='habit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habits.Habit', verbose_name='习惯'),
        ),
    ]
