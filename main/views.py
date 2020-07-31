from django.shortcuts import render
from . import parserhh


def view(requests):
    requirements_skills = []
    if requests.method == 'POST':
        job = requests.POST['job']
        if ' ' in job:
            requirements_skills = {'Текст не може бути пустим'} 
        elif job != '' and type(job) == str:
<<<<<<< HEAD
            parser = parserhh.ParserHH()
            requirements_skills = parser.requirements_skills(job)
=======
            requirements_skills = parserhh.requirements_skills(job)
>>>>>>> b9f5dcff4b361722d80e61da84d85811b9864a6c

    return render(requests, 'main.html', {'skills': list(requirements_skills)})