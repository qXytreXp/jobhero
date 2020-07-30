import requests
from bs4 import BeautifulSoup
import collections
import time


def search_links(job):
    url = 'https://hh.ru/search/vacancy?clusters=true&enable_snippets=true&salary=&st=searchVacancy&fromSearch=true&text='+ job +'&from=suggest_post'
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'

    html = requests.get(url, headers={'User-agent':user_agent}).content
    soup = BeautifulSoup(html, 'lxml')
    link = soup.find_all('a', class_='bloko-link HH-LinkModifier')

    arr_links = []

    for links in link:
        if len(arr_links) == 20:
            break

        arr_links.append(links['href'])

    return arr_links


def requirements(job):
        arr_skills = []
        links = search_links(job)

        for link in links:
            try:
                user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'

                html = requests.get(link, headers={'User-agent':user_agent}).content
                soup = BeautifulSoup(html, 'lxml')
                skill = soup.find_all('span', class_='bloko-tag__section bloko-tag__section_text')

                for skills in skill:
                    if skills.text != '':
                        arr_skills.append(skills.text)

            except AttributeError:
                pass

        return arr_skills


def requirements_skills(job):
    res = []
    count_skills = []
    arr_skills = requirements(job)

    c = collections.Counter(arr_skills)

    for arr_skill in arr_skills:
        count_skills.append(c[arr_skill])

    for count_skill in arr_skills:
        if c[count_skill] > max(count_skills) // 4:
            res.append(count_skill)

    return set(res)


