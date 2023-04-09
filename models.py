from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 
import datetime
from datetime import date
from bpa_social import settings



class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank  = True, null = True)


    post_type = models.TextField(max_length = 95, blank = True, null = True)
    # The post images

    image1 = models.CharField(max_length=800, blank = True, null = True)
    image2 = models.CharField(max_length=800, blank = True, null = True)
    image3 = models.CharField(max_length=800, blank = True, null = True)
    image4 = models.CharField(max_length=800, blank = True, null = True)
    image5 = models.CharField(max_length=800, blank = True, null = True)


    # The number of likes and comments the post has (add comments functionality later)
    likes = models.IntegerField(default=0)

    comments_amount = models.IntegerField(default=0)


    # The caption of the post

    caption = models.TextField(max_length = 95)

    # The date and time that the post was created at

    created_at = models.DateTimeField(auto_now_add=True, null = True)


    # User post settings (checkbox)

    hide_likes = models.BooleanField(default=True)
    privacy = models.BooleanField(default=False)


    #User who created the post

    username = models.TextField(max_length = 40, blank = True, null = True)


    #If they want to type out their post instead
    text_content = models.TextField(max_length = 1000, blank = True, null = True)




class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)
        self.post.comments_amount += 1
        self.post.save()



class Blog(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank  = True, null = True)


    title = models.TextField(max_length = 95)

    body = models.TextField(max_length = 2000, blank = True, null = True)

    image1 = models.CharField(max_length=800, blank = True, null = True)
    image2 = models.CharField(max_length=800, blank = True, null = True)
    image3 = models.CharField(max_length=800, blank = True, null = True)
    image4 = models.CharField(max_length=800, blank = True, null = True)
    image5 = models.CharField(max_length=800, blank = True, null = True)


    username = models.TextField(max_length = 40, blank = True, null = True)

    created_at = models.DateTimeField(auto_now_add=True, null = True)



    # User post settings (checkbox)

    likes = models.IntegerField(default=0)

    post_type = models.TextField(max_length = 95, blank = True, null = True)





class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank = True, null = True)

    profile_pic = models.CharField(max_length=800, default = "http://res.cloudinary.com/hfg9s7ggn/image/upload/v1674747457/v58y8htlxkb7esrxdudl.jpg")

    bio = models.TextField(max_length = 95, blank = True)

    following = models.TextField(max_length = 10000, blank = True)

    followers = models.TextField(max_length = 10000, blank = True)

class LikePost(models.Model):
    post_id = models.CharField(max_length = 500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username