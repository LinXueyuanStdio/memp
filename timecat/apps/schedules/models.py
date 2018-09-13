from django.db import models

# 引入Enum类型
from enum import Enum
from enumfields import EnumIntegerField

from apps.users.models import CustomUser

class Label(Enum):
    IMPORTANT_URGENT = 0
    IMPORTANT_NOT_URGENT = 1
    NOT_IMPORTANT_URGENT = 2
    NOT_IMPORTANT_NOT_URGENT = 3

class Task(models.Model):
    """
    Model: 任务/日程
    Fields: 创建时间(created), 创建者(owner), 任务标题(title), 任务详情(detail),
            任务日期时间(date), 是否完成(isDone)
    """
    user = models.ForeignKey(CustomUser, verbose_name='用户', blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField('标题', max_length=100, blank=True, default='新任务')
    content = models.TextField('内容', blank=True, default='')
    
    label = EnumIntegerField(Label, verbose_name='重要紧急标签', default=Label.IMPORTANT_URGENT)

    created_datetime = models.DateTimeField('创建时间', auto_now_add=True)
    update_datetime = models.DateTimeField('修改时间', auto_now=True)
    
    is_archived = models.BooleanField('是否归档', default=False)

    is_finished = models.BooleanField('是否完成', default=False)
    finished_datetime = models.DateTimeField('完成时间', blank=True, null=True, default=None)

    is_all_day = models.BooleanField('是否全天', default=True)
    begin_datetime = models.DateTimeField('开始时间', blank=True, null=True, default=None)
    end_datetime = models.DateTimeField('结束时间', blank=True, null=True, default=None)

    class Meta:
        db_table = "schedules"
        ordering = ('update_datetime', )