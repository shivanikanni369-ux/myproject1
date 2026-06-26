from django.shortcuts import render
from .forms import StudentForm
from .models import Course

def register_student(request):
    form = StudentForm()
    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'myapp/register.html', {'form': form})


def course_students(request):
    courses = Course.objects.all()
    students = None

    if 'course' in request.GET:
        course_id = request.GET.get('course')
        course = Course.objects.get(id=course_id)
        students = course.student_set.all()

    return render(request, 'myapp/course_students.html', {
        'courses': courses,
        'students': students
    })