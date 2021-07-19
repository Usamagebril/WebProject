from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    
class BookBorrowModel(models.Model):
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    book =models.OneToOneField(Book,null=True,on_delete=models.CASCADE)
    period=models.PositiveIntegerField(default=0)
    def __str__(self):
        return str(self.book)
