from django.db import models
from django.conf import settings
from accounts.models import User

class JungBo(models.Model):
    # 이름
    name = models.CharField(max_length=30)
    # 학과
    Department = models.CharField(max_length=30,  null=False, blank=False,default='Department')
    # 학번
    studentid = models.IntegerField()
    # 학년
    grade = models.CharField(max_length=5)
    # 전화번호
    phone = models.CharField(max_length=13)
    # 이메일(개인)
    email = models.EmailField(max_length=30, unique=True, null=False, blank=False)
    # 내용 : 지원동기
    content = models.TextField()

    #내용 : 트랙선택 및 관련 경험
    track = models.TextField()
    
    #내용 : 협업 경험
    cooperation = models.TextField(null=True)
    
    #시간 할애(열정) :    
    spend_time = models.TextField()

    # 작성일
    created_at = models.DateTimeField(auto_now_add=True)
    