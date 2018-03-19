
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from .auth import auth_user
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=256)
    nickname = models.CharField(max_length=256, default='Newer')

    profile_picture = models.CharField(max_length=128, default='user04.png')

    email = models.EmailField(null=True)
    register_time = models.DateField(auto_now_add=True)


    role = models.CharField(max_length=256, default='undistributed')
    temp_role = models.CharField(max_length=256, null=True)

    @classmethod
    def login(cls, name, password):
        username = 'xib\\' + name
        ret = auth_user(username, password)

        # password correct
        if ret:
            try:
                user = User.objects.get(name=name)
                return user
            except ObjectDoesNotExist as e:
                user = User()
                user.name = name
                user.save()
                return user

        # password error
        else:
            return None



    class Meta:
        db_table = 'users'

    def __repr__(self):
        return f'Name: {self.name}, Role: {self.role}'

    __str__ = __repr__


class Record(models.Model):
    user = models.ForeignKey(User)

    file = models.CharField(max_length=256, default='blank')
    action = models.CharField(max_length=128, default='')

    message = models.CharField(max_length=512, default='')

    time = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f'User: {self.user.name}, Action: {self.action}, Message: {self.message}'

    __str__ = __repr__

    class Meta:
        db_table = 'records'


class Memo(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=512, default='')
    startday = models.CharField(max_length=128, default='')
    endday = models.CharField(max_length=128, default='')

    def __repr__(self):
        return f'User: {self.user.name}, MemoTitle: {self.title}'

    __str__ = __repr__


    class Meta:
        db_table = 'memos'