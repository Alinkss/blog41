from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name="Тег")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        
        

class Post(models.Model):
    title = models.CharField(max_length=30, verbose_name = "Заголовок")
    content = models.TextField(verbose_name = "Описание")
    published_date = models.DateTimeField(auto_created=True, verbose_name = "Дата")
    
    category = models.ForeignKey(Category, on_delete = models.CASCADE, verbose_name = "Категория")
    user = models.ForeignKey(User,on_delete = models.CASCADE, verbose_name = "Автор", default=1)
    tags = models.ManyToManyField(Tag, verbose_name = "Теги", blank = True)
    # image = models.ImageField(upload_to='post_images', default='post_images/900x300.png')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images', default='post_images/900x300.png')
    
    def __str__(self):
        return f"{self.post} - {self.image}"
    
class Comments(models.Model):
    text = models.TextField(max_length = 450)
    avatar = models.URLField(default = "https://as1.ftcdn.net/v2/jpg/03/46/83/96/1000_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg" )
    user = models.ForeignKey(User, on_delete = models.CASCADE, default=1)
    published_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    
    def __str__(self):
       return f"{self.text} - {self.published_date}"
       
    class Meta:
        db_table = 'blog2_custom_comments_new'
        
class SubscribeNewsletter(models.Model):
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.email
    
class Country(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name
    
class City(models.Model):
    name = models.CharField(max_length=40)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name}"
    
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='user_avatar')
    # avatar = models.URLField(default = "https://as1.ftcdn.net/v2/jpg/03/46/83/96/1000_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg")
    telephone = models.CharField(max_length=10)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null= True, blank=True)
    register_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.user.username
    
        
class Adress(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=200)
    private_house_number = models.IntegerField(null= True, blank=True)
    entrance_number = models.CharField(max_length=10, null= True, blank=True)
    flat_num = models.IntegerField(null= True, blank=True)
    profile = models.ForeignKey(Profile, related_name='addresses', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.street}, {self.private_house_number}, {self.entrance_number}, {self.flat_num}"
    
    
