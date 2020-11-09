from django.db import models

# Create your models here.

#class Category(models.Model):
#    name = models.CharField(max_length=128, unique=True)

  #  def __unicode__(self):
  #      return self.name
"""
class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

"""


#School tables
class Group(models.Model):
    groupId = models.IntegerField()
    groupName = models.CharField(max_length=30)

class Teacher(models.Model):
    teacherId = models.IntegerField()
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

class Lesson(models.Model):
    lessonId = models.IntegerField()
    lessonName = models.CharField(max_length=30)

class Classroom(models.Model):
    classroomId = models.IntegerField()
    classroomName = models.CharField(max_length=30)
    building = models.CharField(max_length=30)

class Time(models.Model):
    timeId = models.IntegerField()
    timeWindow = models.IntegerField()

#Connects

#Groups
class GroupTeacher(models.Model):
    groupId = models.IntegerField()
    teacherId = models.IntegerField()

class GroupLesson(models.Model):
    groupId = models.IntegerField()
    lessonId = models.IntegerField()

class GroupClassroom(models.Model):
    groupId = models.IntegerField()
    classroomId = models.IntegerField()

class GroupTime(models.Model):
    groupId = models.IntegerField()
    timeId = models.IntegerField()

#Teachers
class TeacherLesson(models.Model):
    teacherId = models.IntegerField()
    lessonId = models.IntegerField()

class TeacherClassroom(models.Model):
    teacherId = models.IntegerField()
    classroomId = models.IntegerField()

class TeacherTime(models.Model):
    teacherId = models.IntegerField()
    timeId = models.IntegerField()

#Lesson
class LessonClassroom(models.Model):
    lessonId = models.IntegerField()
    classroomId = models.IntegerField()

class LessonTime(models.Model):
    lessonId = models.IntegerField()
    timeId = models.IntegerField()

#Classroom
class ClassroomTime(models.Model):
    classroomId = models.IntegerField()
    timeId = models.IntegerField()
