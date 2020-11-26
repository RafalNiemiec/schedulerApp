from django.db import models

# Create your models here.

class PlansPermission(models.Model):
    userData = models.CharField(max_length=60, default=' ')
    planName = models.CharField(max_length=60)
    class Meta:
        db_table = 'plansPermission'

class Time(models.Model):
    planId = models.ForeignKey(PlansPermission, on_delete=models.CASCADE)
    timeWindow = models.IntegerField()
    day = models.CharField(max_length=60, default='')
    class Meta:
        db_table = 'time'

class Classroom(models.Model):
    planId = models.ForeignKey(PlansPermission, on_delete=models.CASCADE)
    classroomName = models.CharField(max_length=30)
    building = models.CharField(max_length=30)
    #Relations
    time = models.ManyToManyField(Time)
    class Meta:
        db_table = 'classroom'

class Lesson(models.Model):
    planId = models.ForeignKey(PlansPermission, on_delete=models.CASCADE)
    lessonName = models.CharField(max_length=30)
    # Relations
    classrooms = models.ManyToManyField(Classroom)
    time = models.ManyToManyField(Time)
    class Meta:
        db_table = 'lesson'

class Teacher(models.Model):
    planId = models.ForeignKey(PlansPermission, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    minDailyHours = models.IntegerField(default=2)
    maxDailyHours = models.IntegerField(default=8)
    minWeeklyHours = models.IntegerField(default=10)
    maxWeeklyHours = models.IntegerField(default=40)

    #Relations
    lesson = models.ManyToManyField(Lesson)
    classroom = models.ManyToManyField(Classroom)
    time = models.ManyToManyField(Time)
    class Meta:
        db_table = 'teacher'

    #def __str__(self):
         #return "{0} {1}".format(self.First_Name, self.Last_Name)

class GroupLesson(models.Model):
    group = models.ForeignKey("Group", on_delete=models.CASCADE, default='')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, default='')
    lessonAmount = models.IntegerField(default=1)
    class Meta:
        db_table = "group_lesson"

#School tables
class Group(models.Model):
    planId = models.ForeignKey(PlansPermission, on_delete=models.CASCADE)
    groupName = models.CharField(max_length=30)
    minDailyHoursClass = models.IntegerField(default=1)
    maxDailyHoursClass = models.IntegerField(default=1)

    #Relations
    teacher = models.ManyToManyField(Teacher)
    lesson = models.ManyToManyField(Lesson, blank=True, through=GroupLesson, through_fields=["group", "lesson"])
    classroom = models.ManyToManyField(Classroom)
    time = models.ManyToManyField(Time)
    class Meta:
        db_table = 'group'




#Group.lesson.through._meta.get_field('').column = ''




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
