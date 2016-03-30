from django.db import models

class Users(models.Model):
    login_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    authority = models.IntegerField()
    email = models.EmailField()
    cellphone = models.CharField(max_length=100, blank=True)
    sex = models.IntegerField(blank=True)

class Projects(models.Model):
    # sponsor = models.ForeignKey(Users)
    # start_time = models.DateTimeField(blank=True)
    # end_time = models.DateTimeField(blank=True)
    project_title = models.CharField(max_length=50, blank=True)
    project_objective = models.CharField(max_length=400, blank=True)

class Authority(models.Model):
    operation = models.IntegerField()
    user_authority = models.IntegerField()
    other_request = models.IntegerField()

class Literature(models.Model):
    project = models.ForeignKey(Projects)
    literature_title = models.CharField(max_length=50)
    literature_authors = models.CharField(max_length=50)
    literature_year = models.IntegerField(max_length=4)
    literature_library = CharField(max_length=50)
    SOURCE_TYPE = ((0001,'Manual Search'),
                   (0002,'Automated Search'),
                   (0003,'Snowballing'))
    literature_source = forms.ChoiceField(choices=SOURCE_TYPE)
    literature_volume = models.IntegerField(max_length=5)
    literature_number = models.IntegerField(max_length=10)
    literature_pages = models.IntegerField(max_length=5)
    literature_month = models.IntegerField(max_length=2)
    literature_keywords = models.CharField(max_length=200)
    literature_abstracts = models.TextField(max_length=1000)
    literature_url = models.UrlField()
    LiteratureStatus = ((1001,'Unclassified'),
                        (1002,'Included'),
                        (1003,'Excluded'),
                        (1004,'Extracted'))
    literature_status = models.ChoiceField(choices=LiteratureStatus)
    literature_quality = models.IntegerField(max_length=5)
    literature_label = models.CharField(max_length=50)