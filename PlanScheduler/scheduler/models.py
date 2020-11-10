from django.db import models

# Create your models here.

"""

class Time(models.Model):
    timeWindow = models.IntegerField()
    class Meta:
        db_table = 'time'

class Classroom(models.Model):
    classroomName = models.CharField(max_length=30)
    building = models.CharField(max_length=30)
    #Relations
    time = models.ManyToManyField(Time)
    class Meta:
        db_table = 'classroom'

class Lesson(models.Model):
    lessonName = models.CharField(max_length=30)
    # Relations
    classrooms = models.ManyToManyField(Classroom)
    time = models.ManyToManyField(Time)
    class Meta:
        db_table = 'lesson'

class Teacher(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    #Relations
    lesson = models.ManyToManyField(Lesson)
    classroom = models.ManyToManyField(Classroom)
    time = models.ManyToManyField(Time)
    class Meta:
        db_table = 'teacher'

#School tables
class Group(models.Model):
    groupName = models.CharField(max_length=30)
    #Relations
    teacher = models.ManyToManyField(Teacher)
    lesson = models.ManyToManyField(Lesson)
    classroom = models.ManyToManyField(Classroom)
    time = models.ManyToManyField(Time)
    class Meta:
        db_table = 'group'

"""


class PlansPermission(models.Model):
    userNumber = models.CharField(max_length=60)
    planName = models.CharField(max_length=60)
    class Meta:
        db_table = 'plansPermission'


"""
#Connects

#Groups
class GroupTeacher(models.Model):
    groupId = models.IntegerField()
    teacherId = models.IntegerField()
    class Meta:
        db_table = 'groupTeacher'

class GroupLesson(models.Model):
    groupId = models.IntegerField()
    lessonId = models.IntegerField()
    class Meta:
        db_table = 'groupLesson'

class GroupClassroom(models.Model):
    groupId = models.IntegerField()
    classroomId = models.IntegerField()
    class Meta:
        db_table = 'groupClassroom'

class GroupTime(models.Model):
    groupId = models.IntegerField()
    timeId = models.IntegerField()
    class Meta:
        db_table = 'groupTime'

#Teachers
class TeacherLesson(models.Model):
    teacherId = models.IntegerField()
    lessonId = models.IntegerField()
    class Meta:
        db_table = 'teacherLesson'

class TeacherClassroom(models.Model):
    teacherId = models.IntegerField()
    classroomId = models.IntegerField()
    class Meta:
        db_table = 'teacherClassroom'

class TeacherTime(models.Model):
    teacherId = models.IntegerField()
    timeId = models.IntegerField()
    class Meta:
        db_table = 'teacherTime'

#Lesson
class LessonClassroom(models.Model):
    lessonId = models.IntegerField()
    classroomId = models.IntegerField()
    class Meta:
        db_table = 'lessonClassroom'

class LessonTime(models.Model):
    lessonId = models.IntegerField()
    timeId = models.IntegerField()
    class Meta:
        db_table = 'lessonTime'

#Classroom
class ClassroomTime(models.Model):
    classroomId = models.IntegerField()
    timeId = models.IntegerField()
    class Meta:
        db_table = 'classroomTime'
        
"""
