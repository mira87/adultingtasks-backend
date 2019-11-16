from django.db import models

# Create your models here.


class Category(models.Model):
    title=models.CharField(max_length=300,default='Enter Title')




    def __str__(self):
        return self.title

class AdultingTask(models.Model):
    title=models.CharField(max_length=300, default='Enter Title')
    summary=models.CharField(max_length=500, default='Enter Summary')
    details=models.TextField(default='Enter Details')
    taskpic=models.TextField(default='No Picture',null=True,blank=True)
    category=models.ForeignKey(Category, related_name='categories',on_delete=models.CASCADE)

    def __str__(self):
        return self.title


        
        

