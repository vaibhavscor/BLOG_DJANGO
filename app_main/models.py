from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User




class blog(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    head_img = models.FileField(upload_to="images", default='')
    content_main = RichTextField(blank=True, null=True)
    slug = models.CharField(max_length=1000)
    timestamp = models.DateField(auto_now=True)
    # liked = models.ManyToManyField(User, default=None, blank=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):

        return self.title + 'by' + self.name


#     @property
#     def num_likes(self):
#         return self.liked.all().count()

#     LIKE_CHOICES = (('Like','like'),('unlike','unlike'))


# class  like(model.models):
#     user = models.ForeignKey(User, on_delete=modles.CASCADE)
#     post = models.ForeignKey(blog, on_delete=modles.CASCADE)
#     value = models.CharField(choices=LIKE_CHOICES,default='LIKE',max_length=10)
    

#     __str__(self):
#         return str(self.post)
    













    