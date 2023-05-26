from django.db import models

class PictureModel(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  author = models.CharField(max_length=100)
  # 画像をアップロード時にはpillowライブラリが使われるので、pipでインストールする必要あり
  # 前提としてブランクの時にはデフォルトでどこに保存するかの設定をsettings.pyに書き込む必要あり
  images = models.ImageField(upload_to='') # upload_toはどこのディレクトリに画像をアップロードするかの設定
  good = models.IntegerField()
  read = models.IntegerField()
  readtext = models.CharField(max_length=200)

# class Category(models.Model):
#     name = models.CharField(
#         max_length=255,
#         blank=False,
#         null=False,
#         unique=True)
    
#     def __str__(self):
#         return self.name


# class Tag(models.Model):
#     name = models.CharField(
#         max_length=255,
#         blank=False,
#         null=False,
#         unique=True)
    
#     def __str__(self):
#         return self.name


# class Post(models.Model):
#     created = models.DateTimeField(
#         auto_now_add=True,
#         editable=False,
#         blank=False,
#         null=False)
    
#     updated = models.DateTimeField(
#         auto_now=True,
#         editable=False,
#         blank=False,
#         null=False)
        
#     title = models.CharField(
#         max_length=255,
#         blank=False,
#         null=False)
        
#     body = models.TextField(
#         blank=True,
#         null=False)

#     category = models.ForeignKey(
#         Category,
#         on_delete=models.CASCADE)
        
#     tags = models.ManyToManyField(
#         Tag,
#         blank=True)

#     def __str__(self):
#         return self.title