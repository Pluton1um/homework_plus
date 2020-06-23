from django.db import models


# 学校
class school(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)


# 专业
class spciality(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)

    school = models.ForeignKey("school", on_delete=models.CASCADE)


# 老师
class teacher(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=50, null=False)

    name = models.CharField(max_length=20, null=False)

    school = models.ForeignKey("school", on_delete=models.SET_NULL, null=True)
    spciality = models.ManyToManyField("spciality")


# 学生
class student(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=50, null=False)

    name = models.CharField(max_length=20, null=False)
    class_f = models.CharField(max_length=50, null=True)
    selfinfo = models.TextField(null=True)
    sexuality = models.CharField(max_length=50, null=True)  # 性别
    age = models.IntegerField(null=True)

    school = models.ForeignKey("school", on_delete=models.SET_NULL, null=True)
    spciality = models.ForeignKey("spciality", on_delete=models.SET_NULL, null=True)
    subject = models.ManyToManyField("subject")


# 课程
class subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    grade = models.CharField(max_length=100, null=False)

    teacher = models.ForeignKey("teacher", on_delete=models.CASCADE)


# 学生某门课的整体信息
class score_report(models.Model):
    id = models.AutoField(primary_key=True)
    subject_score = models.CharField(max_length=10)  # 学生某门课总成绩

    subject = models.ForeignKey("subject", on_delete=models.CASCADE)
    student = models.ForeignKey("student", on_delete=models.CASCADE)


# 老师布置的某次作业信息
class assigment(models.Model):
    id = models.AutoField(primary_key=True)
    start_time = models.DateTimeField(null=True)  # 作业开始的时间
    end_time = models.DateTimeField(null=True)  # 作业截至的时间
    submit_num = models.IntegerField(null=True)  # 已提交的作业数量
    num = models.IntegerField(null=False)  # 这是第几次作业
    text = models.TextField(null=True)  # 内容

    subject = models.ForeignKey("subject", on_delete=models.CASCADE)


# 学生提交的作业及相关信息
class homework(models.Model):
    id = models.AutoField(primary_key=True)
    submit_time = models.DateTimeField(null=True)  # 提交时间
    whether_submit = models.BooleanField(null=True)  # 作业是否提交
    whether_correct = models.BooleanField(default=False)  # 作业是否被老师批改
    remark = models.TextField(null=True)  # 老师评语
    score = models.CharField(max_length=10)  # 作业成绩

    assigment = models.ForeignKey("assigment", on_delete=models.CASCADE)
    student = models.ForeignKey("student", on_delete=models.CASCADE)


class photo(models.Model):
    id = models.AutoField(primary_key=True)
    photo = models.ImageField()  # 作业照片

    homework = models.ForeignKey("homework", on_delete=models.CASCADE)
