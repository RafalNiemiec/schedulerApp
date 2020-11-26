import _sqlite3
from pulp import *
from .models import *

def createVariables(): #DONE
    global countTime, countGroups, countLessons, countTeachers, countClassrooms
    global shiftTime, shiftGroups, shiftLessons, shiftTeachers, shiftClassrooms
    global timeSpan, groupSpan, lessonSpan, teacherSpan, classroomSpan
    global planId
    planId = 1

    countTime = Time.objects.using('schoolsDB').filter(planId_id=planId).count()
    countGroups = Group.objects.using('schoolsDB').filter(planId_id=planId).count()
    countLessons = Lesson.objects.using('schoolsDB').filter(planId_id=planId).count()
    countTeachers = Teacher.objects.using('schoolsDB').filter(planId_id=planId).count()
    countClassrooms = Classroom.objects.using('schoolsDB').filter(planId_id=planId).count()

    shiftTime = Time.objects.filter(planId_id=planId).using('schoolsDB')[0].id
    shiftGroups = Group.objects.filter(planId_id=planId).using('schoolsDB')[0].id
    shiftLessons = Lesson.objects.filter(planId_id=planId).using('schoolsDB')[0].id
    shiftTeachers = Teacher.objects.filter(planId_id=planId).using('schoolsDB')[0].id
    shiftClassrooms = Classroom.objects.filter(planId_id=planId).using('schoolsDB')[0].id

    timeSpan = Time.objects.filter(planId_id=planId).using('schoolsDB')
    groupSpan = Group.objects.filter(planId_id=planId).using('schoolsDB')
    lessonSpan = Lesson.objects.filter(planId_id=planId).using('schoolsDB')
    teacherSpan = Teacher.objects.filter(planId_id=planId).using('schoolsDB')
    classroomSpan = Classroom.objects.filter(planId_id=planId).using('schoolsDB')

    #variables
    variables = LpVariable.dicts("Choice",
                                 #hour, class, lesson, teacher, classroom
                                 [(h, g, l, t, c)  for h in range(countTime)
                                                    for g in range(countGroups)
                                                    for l in range(countLessons)
                                                    for t in range(countTeachers)
                                                    for c in range(countClassrooms)],
                                 0, 1, LpInteger)
    return variables


def notDoubleConstraints(variables):
    constraints = list()

    for h in range(countTime):
        for g in range(countGroups):
            constraints.append(lpSum(variables[(h, g, l, t, c)]    for l in range(countLessons)
                                                                    for t in range(countTeachers)
                                                                    for c in range(countClassrooms)) == (1 or 0))
        for t in range(countTeachers):
            constraints.append(lpSum(variables[(h, g, l, t, c)]    for g in range(countGroups)
                                                                    for l in range(countLessons)
                                                                    for c in range(countClassrooms)) == (1 or 0))
        for c in range(countClassrooms):
            constraints.append(lpSum(variables[(h, g, l, t, c)]    for g in range(countGroups)
                                                                    for l in range(countLessons)
                                                                    for t in range(countTeachers)) == (1 or 0))
    return constraints


#Allowance constraints

def timeAllowance(variables):
    constraints = list()

    """
    timeSpan = Time.objects.filter(id=planId).using('schoolsDB')
    groupSpan = Group.objects.filter(id=planId).using('schoolsDB')
    lessonSpan = Lesson.objects.filter(id=planId).using('schoolsDB')
    teacherSpan = Teacher.objects.filter(id=planId).using('schoolsDB')
    classroomSpan = Classroom.objects.filter(id=planId).using('schoolsDB')
    """

    #(h, g, l, t, c)
    for h in timeSpan:
        hourPosition = h.id - shiftTime

        for g in groupSpan:
            if not h.Time.objects.filter(groups=g).exist():
                groupPosition = g.id - shiftGroups
                constraints.append(variables[(hourPosition, groupPosition, l, t, c)]   for l in range (countLessons)
                                                                                       for t in range(countTeachers)
                                                                                       for c in range(countClassrooms) == 0)
        for l in lessonSpan:
            if not h.Time.objects.filter(lesson=l).exist():
                lessonPosition = l.id - shiftLessons
                constraints.append(variables[(hourPosition, g, lessonPosition, t, c)]   for g in range(countGroup)
                                                                                        for t in range(countTeachers)
                                                                                        for c in range(countClassrooms) == 0)
        for t in teacherSpan:
            if not h.Time.objects.filter(teacher=t).exist():
                teacherPosition = t.id - shiftTeachers
                constraints.append(variables[(hourPosition, g, l, teacherPosition, c)]  for g in range(countGroups)
                                                                                        for l in range (countLessons)
                                                                                        for c in range(countClassrooms) == 0)
        for c in classroomSpan:
            if not h.Time.objects.filter(classrooms=c).exist():
                classroomPosition = c.id - shiftClassrooms
                constraints.append(variables[(hourPosition, g, l, t, classroomPosition)]    for g in range(countGroups)
                                                                                            for l in range(countLessons)
                                                                                            for t in range(countTeachers) == 0)
    return constraints


def teacherAllowance(variables):
    constraints = list()

    """
    teacherSpan = Teacher.objects.filter(id=planId).using('schoolsDB')[0]
    groupSpan = Group.objects.filter(id=planId).using('schoolsDB')
    lessonSpan = Lesson.objects.filter(id=planId).using('schoolsDB')
    classroomSpan = Classroom.objects.filter(id=planId).using('schoolsDB')
    """

    #(h, g, l, t, c)
    for t in range(countTeachers):
        for g in range(countGroups):
            if not teacherSpan[t] in groupSpan[g].classroom.all():
                constraints.append(lpSum(variables[(h, g, l, t, c)]     for h in range(countTime)
                                                                        for l in range(countLessons)
                                                                        for c in range(countClassrooms)) == 0)
        for l in range(countLessons):
            if not lessonSpan[l] in teacherSpan[t].lesson.all():
                constraints.append(lpSum(variables[(h, g, l, t, c)]     for h in range(countTime)
                                                                        for g in range(countGroups)
                                                                        for c in range(countClassrooms)) == 0)
        for c in range(countClassrooms):
            if not classroomSpan[c] in teacherSpan[t].classroom.all():
                constraints.append(lpSum(variables[(h, g, l, t, c)]     for l in range(countLessons)
                                                                        for g in range(countGroups)
                                                                        for h in range(countTime)) == 0)
        for h in range(countTime):
            if not timeSpan[h] in teacherSpan[t].time.all():
                constraints.append(lpSum(variables[(h, g, l, t, c)]     for l in range(countLessons)
                                                                        for g in range(countGroups)
                                                                        for c in range(countClassrooms)) == 0)
    return constraints


def groupAllowance(variables):
    constraints = list()
    """
    groupSpan = Group.objects.filter(id=planId).using('schoolsDB')
    lessonSpan = Lesson.objects.filter(id=planId).using('schoolsDB')
    classroomSpan = Classroom.objects.filter(id=planId).using('schoolsDB')
    """
    #(h, g, l, t, c)
    for g in range(countGroups):
        for l in range(countLessons):
            if not lessonSpan[l] in groupSpan[g].lesson.all():
                constraints.append(lpSum(variables[(h, g, l, t, c)]   for h in range(countTime)
                                                                for t in range(countTeachers)
                                                                for c in range(countClassrooms)) == 0)
        for c in range(countClassrooms):
            if not classroomSpan[c] in groupSpan[g].lesson.all():
                constraints.append(lpSum(variables[(h, g, l, t, c)]   for h in range(countTime)
                                                                for t in range(countTeachers)
                                                                for l in range(countLessons)) == 0)
        for h in range(countTime):
            if not timeSpan[h] in groupSpan[g].time.all():
                constraints.append(lpSum(variables[(h, g, l, t, c)]     for l in range(countLessons)
                                                                        for t in range(countTeachers)
                                                                        for c in range(countClassrooms)) == 0)
        print(60*'{}', 'added groups constraints')
        return constraints

def classroomAllowance(variables):
    constraints = []

    for c in range(countClassrooms):
        for l in range(countLessons):
            if not classroomSpan[c] in lessonSpan[l].classrooms.all():
                constraints.append(lpSum(variables[(h, g, l, t, c)]     for h in range(countTime)
                                                                        for t in range(countTeachers)
                                                                        for g in range(countGroups)) == 0)
        for h in range(countTime):
            if not timeSpan[h] in classroomSpan[c].time.all():
                constraints.append(lpSum(variables[(h, g, l, t, c)]     for l in range(countLessons)
                                                                         for t in range(countTeachers)
                                                                         for g in range(countGroups)) == 0)
    return constraints

def lessonAllowance(variables):
    constraints = list()
    """
    lessonSpan = Lesson.objects.filter(id=planId).using('schoolsDB')
    classroomSpan = Classroom.objects.filter(id=planId).using('schoolsDB')
    """
    #(h, g, l, t, c)
    for l in range(countLessons):
        for h in range(countTime):
            if not timeSpan[h] in lessonSpan[l].time.all():
                constraints.append(lpSum(variables[(h, g, l, t, c)]     for c in range(countClassrooms)
                                                                        for t in range(countTeachers)
                                                                        for g in range(countGroups)) == 0)
    return constraints



def maxWeeklyHoursConstrains(variables):
    constraints = []
    """
    timeSpan = Time.objects.filter(id=planId).using('schoolsDB')
    groupSpan = Group.objects.filter(id=planId).using('schoolsDB')
    lessonSpan = Lesson.objects.filter(id=planId).using('schoolsDB')
    teacherSpan = Teacher.objects.filter(id=planId).using('schoolsDB')
    classroomSpan = Classroom.objects.filter(id=planId).using('schoolsDB')
    """
    for t in teacherSpan:
        teacherPosition = t.id - shiftTeacher
        constraints.append(lpSum(variables[(h, g, l, teacherPosition, c)]    for h in range(countTime)
                                                                             for g in range(countGroups)
                                                                             for l in range(countTeachers)
                                                                             for c in range(countClassrooms) <= t.maxWeeklyHours))
    return constraints

def minWeeklyHoursConstrains(variables):
    constraints = []
    teacherSpan = Teacher.objects.filter(id=planId).using('schoolsDB')

    for t in teacherSpan:
        teacherPosition = t.id - shiftTeachers
        constraints.append(lpSum(variables[(h, g, l, teacherPosition, c)]    for h in range(countTime)
                                                                             for g in range(countGroups)
                                                                             for l in range(countTeachers)
                                                                             for c in range(countClassrooms) >= t.minWeeklyHours))
    return constraints


def numberOfLessons(variables):
    constraints = []
    """
    lessonSpan = Lesson.objects.filter(planId_id=planId).using('schoolsDB')
    groupSpan = Group.objects.filter(planId_id=planId).using('schoolsDB')
    """
    for g in groupSpan:
        print(g)
        for l in lessonSpan:
            if l in g.lesson.all():
                print('found pair', g, l)
            #if g.lesson.objects.filter(group=l).exist():
                con = GroupLesson.objects.using('schoolsDB').filter(lesson=l)[0].lessonAmount
                print(100*'{}')
                print(con)
            #if l.Lesson.objects.filter(group=g).exist():
                #con = int(l.Lesson.objects.filter(group=g).lessonAmmount)
                groupPosition = g.id - shiftGroups
                lessonPosition = l.id - shiftLessons
                constraints.append(lpSum(variables[(h, groupPosition, lessonPosition, t, c)]    for h in range(countTime)
                                                                                                for t in range(countTeachers)
                                                                                                for c in range(countClassrooms)) == con)

    return constraints

def create_linear_programming_problem(linear_constraints):
        """
        Function creates linear programming problem in Pulp. Returns LpProblem object
        :param linear_constraints: list of constraints
        :return: LpProblem object
        """
        linear_problem = LpProblem('lessonPlan', LpMinimize)  # LpMaximize #LpMinimize
        for i in linear_constraints:
            linear_problem += i
        return linear_problem


def solve_linear_problem():
    """
    Solves linear problem, returns problem, objective and solver status
    :param linear_problem: LpProblem object
    :return: linear problem, objective, solver status
    """

    variables = createVariables()

    constraints = list()
    constraints.append(notDoubleConstraints(variables)) #DONE

    #Allowance constraints
    #constraints.append(timeAllowance(variables))
    constraints.append(teacherAllowance(variables))    #DONE
    constraints.append(groupAllowance(variables))       #DONE
    constraints.append(classroomAllowance(variables))   #DONE
    constraints.append(lessonAllowance(variables))      #DONE


    #constraints.append(maxWeeklyHoursConstrains(variables))
    #constraints.append(minWeeklyHoursConstrains(variables))w
    constraints.append(numberOfLessons(variables))
    a = list()
    for i in constraints:
        for j in i:
            a.append(j)

    problem = create_linear_programming_problem(a)
    #create_linear_programming_problem(constraints)
    #linear_problem.solve()
    problem.solve()

    return variables, problem, problem.objective, problem.status
    #return variables, linear_problem, linear_problem.objective, linear_problem.status

#variables = createVariables()
#notDouble = notDoubleConstraints()

#a = list()
#problem = create_linear_programming_problem(a)
#problem.solve()

#Minimalizacja całkowitego czasu wykonywanych zadań


#createPlan("luuupi")