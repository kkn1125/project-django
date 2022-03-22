from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    num = models.AutoField(primary_key=True)
    # primary_key를 지정해줘야 ~~.id field error가 나지 않는다.
    profile = models.ImageField(upload_to="", null=True, blank=True)
    nickname = models.CharField(max_length=45, null=False, unique=True)
    email = models.CharField(max_length=45, null=False)
    password = models.CharField(max_length=45, null=False)
    regdate = models.DateTimeField('created', default=timezone.now, editable=False, null=False, blank=False)
    updates = models.DateTimeField('updated', default=timezone.now, editable=False, null=False, blank=False)
    
class Room(models.Model):
    num = models.AutoField(primary_key=True)
    # primary_key를 지정해줘야 ~~.id field error가 나지 않는다.
    master = models.IntegerField(null=False, unique=True)
    title = models.CharField(max_length=45, null=False)
    regdate = models.DateTimeField('created', default=timezone.now, editable=False, null=False, blank=False)
    updates = models.DateTimeField('updated', default=timezone.now, editable=False, null=False, blank=False)
    
class UserInRoom(models.Model):
    num = models.AutoField(primary_key=True)
    # primary_key를 지정해줘야 ~~.id field error가 나지 않는다.
    # room_num = models.IntegerField(null=False, unique=True)
    # user_num = models.IntegerField(null=False, unique=True)
    room_num = models.ForeignKey(Room, on_delete=models.CASCADE, db_column='room_num')
    user_num = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_num')
    regdate = models.DateTimeField('created', default=timezone.now, editable=False, null=False, blank=False)
    updates = models.DateTimeField('updated', default=timezone.now, editable=False, null=False, blank=False)
    
class Calendar(models.Model):
    num = models.AutoField(primary_key=True)
    # primary_key를 지정해줘야 ~~.id field error가 나지 않는다.
    room_num = models.IntegerField(null=False)
    user_num = models.IntegerField(null=False)
    category = models.CharField(max_length=45, null=False)
    title = models.CharField(max_length=50, null=False)
    schedule = models.TextField(blank=True, null=True)
    coworker = models.CharField(max_length=200, null=False)
    start_date = models.DateTimeField('start', null=False, blank=False)
    end_date = models.DateTimeField('end', null=False, blank=False)
    regdate = models.DateTimeField('created', default=timezone.now, editable=False, null=False, blank=False)
    updates = models.DateTimeField('updated', default=timezone.now, editable=False, null=False, blank=False)