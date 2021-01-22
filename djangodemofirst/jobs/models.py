from django.db import models
from django.contrib.auth.models import User


JobTypes = [
    ('0', '技术类'),
    ('1', '产品类'),
    ('2', '运营类'),
    ('3', '设计类'),
]

Cities = [
    ('0', '上海'),
    ('1', '北京'),
    ('2', '深圳'),
]


class Job(models.Model):
    job_type = models.SmallIntegerField(blank=False, choices=JobTypes, verbose_name='职位类别')
    job_name = models.CharField(max_length=250, blank=False, verbose_name='职位名称')
    job_city = models.SmallIntegerField(choices=Cities, blank=False, verbose_name='职位地点')
    job_responsibility = models.TextField(max_length=1024, verbose_name='职位职责')
    job_requirement = models.TextField(max_length=1024, blank=False, verbose_name='职位要求')
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='创建人')
    created = models.DateField(verbose_name='创建时间')
    modified = models.DateField(verbose_name='修改时间')
