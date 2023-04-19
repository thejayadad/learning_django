from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse



# Create your models here.

#post model
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=150)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    #publication date
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #approving comments
    def approve_comments(self):
        return self.comments.filter(approved_comments=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


    #string representation
    def __str__(self):
        return self.title


#Create comments class
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)


    #approve method
    def approve(self):
        self.approved_comment = True
        self.save()

    #redirect after typing comment
    def get_absolute_url(self):
        return reverse("post_list", kwargs={"pk": self.pk})
    

    #string rep of comment
    def __str__(self):
        return self.text