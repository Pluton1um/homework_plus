# Generated by Django 3.0.7 on 2020-06-30 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='assigment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(null=True)),
                ('start_time', models.CharField(max_length=50, null=True)),
                ('end_time', models.CharField(max_length=50, null=True)),
                ('text', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='homework',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('submit_time', models.DateTimeField(null=True)),
                ('explain', models.TextField(null=True)),
                ('whether_submit', models.BooleanField(default=0)),
                ('whether_correct', models.BooleanField(default=0)),
                ('remark', models.TextField(null=True)),
                ('score', models.CharField(max_length=10, null=True)),
                ('assigment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework.assigment')),
            ],
        ),
        migrations.CreateModel(
            name='school',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=20)),
                ('sign', models.TextField(null=True)),
                ('profile', models.TextField(null=True)),
                ('college', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('picture', models.ImageField(default=0, upload_to='')),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homework.school')),
            ],
        ),
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('grade', models.CharField(max_length=100)),
                ('info', models.TextField(null=True)),
                ('scoring_way', models.TextField(null=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=20)),
                ('college', models.CharField(max_length=50, null=True)),
                ('spciality', models.CharField(max_length=50, null=True)),
                ('class_f', models.CharField(max_length=50, null=True)),
                ('selfinfo', models.TextField(null=True)),
                ('sexuality', models.CharField(max_length=50, null=True)),
                ('sign', models.TextField(null=True)),
                ('profile', models.TextField(null=True)),
                ('picture', models.ImageField(default=0, upload_to='')),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homework.school')),
                ('subject', models.ManyToManyField(to='homework.subject')),
            ],
        ),
        migrations.CreateModel(
            name='spciality',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework.school')),
            ],
        ),
        migrations.CreateModel(
            name='photo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('photo', models.ImageField(upload_to='')),
                ('homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework.homework')),
            ],
        ),
        migrations.AddField(
            model_name='homework',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework.student'),
        ),
        migrations.AddField(
            model_name='assigment',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework.subject'),
        ),
    ]
