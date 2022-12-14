from django.db import models


class News(models.Model):
    title = models.CharField(max_length=256, verbose_name='Title')
    preambule = models.CharField(max_length=1024, verbose_name='Preambule')
    body = models.TextField(blank=True, null=True, verbose_name='Body')
    body_as_markdown = models.BooleanField(default=False, verbose_name='As markdown')
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Created')
    update = models.DateTimeField(auto_now = True, editable=False, verbose_name='Updated')
    deleted = models.BooleanField(default=False, verbose_name='Deleted')

    def __str__(self):
        return f"{self.pk}--->{self.title}"

    def delete(self):
        self.deleted = True
        self.save()

class CoursesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class Courses(models.Model):
    objects = CoursesManager()
    name = models.CharField(max_length=256, verbose_name='Name')
    description = models.TextField(blank='True', null='True', verbose_name='Description')
    description_as_markdown = models.BooleanField(default=False, verbose_name='As markdown')
    cost = models.DecimalField(max_digits=8, decimal_places=2, default = 0, verbose_name='Cost')
    cover = models.CharField(max_length=25, default='no_image.svg', verbose_name='Cover')
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, editable=False, verbose_name='Updated')
    deleted = models.BooleanField(default=False, verbose_name='Deleted')

    def __str__(self):
        return f"{self.pk}--->{self.name}"

    def delete(self):
        self.deleted = True
        self.save()


class Lesson(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    num = models.PositiveIntegerField(verbose_name='Lesson number')
    title = models.CharField(max_length=256, verbose_name='Title')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    description_as_markdown=models.BooleanField(default=False, verbose_name='As markdown')
    created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')
    deleted = models.BooleanField(default=False, verbose_name='Deleted')

    def __str__(self):
        return f"{self.course.name} {self.num} {self.title}"

    def delete(self):
        self.deleted = True
        self.save()

    class Meta:
        ordering = ('course', 'num')


class CourseTeachers(models.Model):
    course = models.ManyToManyField(Courses)
    name_first = models.CharField(max_length=128, verbose_name="Name")
    name_second = models.CharField(max_length=128, verbose_name="Surname")
    day_birth = models.DateField(verbose_name="Birth date")
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return "{0:0>3} {1} {2}".format(self.pk, self.name_second, self.name_first)

    def delete(self, *args):
        self.deleted = True
        self.save()
