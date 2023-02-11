from django.db import models
from django.conf import settings
from accounts.models import User

class JungBo(models.Model):
    # 이름
    name = models.CharField(max_length=30)
    # 학번
    studentid = models.IntegerField()
    # 학년
    grade = models.CharField(max_length=5)
    #재학 여부
    in_university_choices = (('재학', '재학'), ('휴학', '휴학'))
    in_university = models.CharField(max_length=5, choices= in_university_choices, default='')
    # 학과
    Department = models.CharField(max_length=50,  null=False, blank=False,default='Department')
    # 전화번호
    phone = models.CharField(max_length=13)
    # 이메일(개인)
    email = models.EmailField(max_length=30, unique=True, null=False, blank=False)
    #노트북 소지 여부
    notebook_choices = (('있음', '있음'), ('없음', '없음'))
    notebook = models.CharField(max_length=5, choices= notebook_choices, default='')
    # 내용 : 지원동기
    content = models.TextField()
    # 트랙선택
    track_choices = (('기획/디자인', '기획/디자인'), ('프론트엔드', '프론트엔드'), ('백엔드', '백엔드'))
    my_track = models.CharField(max_length=7, choices= track_choices, default='')
    # 트랙선택 이유&경험&성장 기대
    track = models.TextField()
    # 협업 경험
    cooperation = models.TextField(null=True)
    #시간 할애(열정) :    
    spend_time = models.TextField()
    #세션 참석 여부 (선택)
    session_choices = (('참석', '참석'), ('불참', '불참'))
    session = models.CharField(max_length=5, choices= session_choices, default='')
    #github 첨부
    github = models.URLField(null=True)
    # 작성일
    created_at = models.DateTimeField(auto_now_add=True)
    