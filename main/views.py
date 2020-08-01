from django.shortcuts import render
from . import parserhh


def view(requests):
    requirements_skills = []
    if requests.method == 'POST':
        job = requests.POST['job']
        if ' ' in job:
            requirements_skills = {'Текст не може бути пустим'} 
        elif job != '' and type(job) == str:
            parser = parserhh.ParserHH()
            requirements_skills = parser.requirements_skills(job)

    return render(requests, 'main.html', {'skills': list(requirements_skills)})
