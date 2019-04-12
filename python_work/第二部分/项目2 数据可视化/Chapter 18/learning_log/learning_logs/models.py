from django.db import models

# Create your models here.
class Topic(models.Model):
    """
    用户学习的主题
    """

    # 定义模型的两个基本属性
    # text是一个CharField由字符或文本组成的数据，使用CharField属性的时候需要指定数据库预留多少空间，这里设置为200个字符
    text = models.CharField(max_length=200)
    # DateTimeField是一个记录日期和时间的数据，参数表明每当用户创建新主题的时候，都会让Django将这个属性自动设置成当前日期和时间
    date_added = models.DateTimeField(auto_now_add=True)

    # Django调用__str__方法来显示模型的简单表示，它返回存储在属性text中的字符串
    def __str__(self):
        """
        返回模型的字符串表示
        :return:
        """
        return self.text

class Entry(models.Model):
    """学到的有关某个主题的具体知识
    """
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

        def __str__(self):
            """返回模型的字符串表示"""

            return self.text[:50] + "..."