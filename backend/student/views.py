from django.shortcuts import render
from student.models import Teacher, Student
from django.db import transaction

# bulk create
teacher_list = [
    Teacher(firstname="Michael", surname="Scott"),
    Teacher(firstname="Dwight", surname="Schrute"),
    Teacher(firstname="Pam", surname="Beesly"),
    Teacher(firstname="Jim", surname="Halpert"),
]

student_list = [
    Student(firstname='Kevin', surname='Malone', age=12, classroom=3, teacher='Micheal'),
    Student(firstname="Angela", surname="Martin", age=14, classroom=1, teacher="Dwight"),
    Student(firstname="Oscar", surname="Martinez", age=13, classroom=2, teacher="Pam"),
    Student(firstname="Ryan", surname="Howard", age=15, classroom=4, teacher="Jim"),
    Student(firstname="Kelly", surname="Kapoor", age=12, classroom=3, teacher="Michael"),
    Student(firstname="Stanley", surname="Hudson", age=14, classroom=1, teacher="Dwight"),
]


def student_bulk_create(request):
    students = Student.objects.bulk_create(student_list)
    teachers = Teacher.objects.bulk_create(teacher_list)
    
    CHUNK_SIZE = 50
    large_student_list = []
    with transaction.atomic():
        for i in range(0, len(large_student_list), CHUNK_SIZE):
            chunk = large_student_list[i : i + CHUNK_SIZE]
            Student.objects.bulk_create(chunk, batch_size=CHUNK_SIZE, ignore_conflicts=True)


def student_list(request):

    return render(request, 'students/student.html')
