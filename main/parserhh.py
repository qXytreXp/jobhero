import requests
from bs4 import BeautifulSoup
import collections
import time
import threading


class ParserHH:
    def __init__(self):
        self.res_thread_search_requirements_one = []
        self.res_thread_search_requirements_two = []
        self.res_thread_search_requirements_three = []
        self.res_thread_search_requirements_four = []
        self.res_thread_search_requirements_five = []
        self.res_thread_search_requirements_six = []
    

    def search_links(self, job):
        url = 'https://hh.ru/search/vacancy?clusters=true&enable_snippets=true&salary=&st=searchVacancy&fromSearch=true&text='+ job +'&from=suggest_post'
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'

        html = requests.get(url, headers={'User-agent':user_agent}).content
        soup = BeautifulSoup(html, 'html.parser')
        link = soup.find_all('a', class_='bloko-link HH-LinkModifier')

        arr_links = []

        for links in link:
        
            arr_links.append(links['href'])


        return arr_links


    def separation_links(self, job):
        links = self.search_links(job)
        res = []
        count = 4
        
        for i in range(0, len(links), count):
            res.append(links[i:i+count])
        
        try:
            part_one = res[0]
            part_two = res[1]
            part_three = res[2]
            part_four = res[3]
            part_five = res[4]
            part_six = res[5]
        except IndexError:
            arr_length = len(links)-1
            number = arr_length // 3

            part_one = links[:-(arr_length-number)]
            part_two = links[(arr_length + 1) // 3:-arr_length // 3]
            part_three = links[arr_length - number:]
            part_four = []
            part_five = []
            part_six = []

        return part_one, part_two, part_three, part_four, part_five, part_six


    def base_thread(self, job):
        part_one, part_two, part_three, part_four, part_five, part_six = self.separation_links(job)

        thread1 = threading.Thread(target=self.thread_search_requirements_one, args=(part_one, job))
        thread2 = threading.Thread(target=self.thread_search_requirements_two, args=(part_two, job))
        thread3 = threading.Thread(target=self.thread_search_requirements_three, args=(part_three, job))
        thread4 = threading.Thread(target=self.thread_search_requirements_four, args=(part_four, job))
        thread5 = threading.Thread(target=self.thread_search_requirements_five, args=(part_five, job))
        thread6 = threading.Thread(target=self.thread_search_requirements_six, args=(part_six, job))

        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        thread5.start()
        thread6.start()
        thread1.join()
        thread2.join()
        thread3.join()
        thread4.join()
        thread5.join()
        thread6.join()
        

    def thread_search_requirements_one(self, links, job):
        links = links
        arr_skills = []

        for link in links:
            try:
                user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'

                html = requests.get(link, headers={'User-agent':user_agent}).content
                soup = BeautifulSoup(html, 'html.parser')
                skill = soup.find_all('span', class_='bloko-tag__section bloko-tag__section_text')

                for skills in skill:
                    if skills.text != '':
                        arr_skills.append(skills.text)

            except AttributeError:
                pass
        self.res_thread_search_requirements_one = arr_skills
    

    def thread_search_requirements_two(self, links, job):
        links = links
        arr_skills = []

        for link in links:
            try:
                user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'

                html = requests.get(link, headers={'User-agent':user_agent}).content
                soup = BeautifulSoup(html, 'html.parser')
                skill = soup.find_all('span', class_='bloko-tag__section bloko-tag__section_text')

                for skills in skill:
                    if skills.text != '':
                        arr_skills.append(skills.text)

            except AttributeError:
                pass
        self.res_thread_search_requirements_two = arr_skills


    def thread_search_requirements_three(self, links, job):
        links = links
        arr_skills = []

        for link in links:
            try:
                user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'

                html = requests.get(link, headers={'User-agent':user_agent}).content
                soup = BeautifulSoup(html, 'html.parser')
                skill = soup.find_all('span', class_='bloko-tag__section bloko-tag__section_text')

                for skills in skill:
                    if skills.text != '':
                        arr_skills.append(skills.text)

            except AttributeError:
                pass

        self.res_thread_search_requirements_three = arr_skills


    def thread_search_requirements_four(self, links, job):
        links = links
        arr_skills = []

        for link in links:
            try:
                user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'

                html = requests.get(link, headers={'User-agent':user_agent}).content
                soup = BeautifulSoup(html, 'html.parser')
                skill = soup.find_all('span', class_='bloko-tag__section bloko-tag__section_text')

                for skills in skill:
                    if skills.text != '':
                        arr_skills.append(skills.text)

            except AttributeError:
                pass

        self.res_thread_search_requirements_four = arr_skills


    def thread_search_requirements_five(self, links, job):
        links = links
        arr_skills = []

        for link in links:
            try:
                user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'

                html = requests.get(link, headers={'User-agent':user_agent}).content
                soup = BeautifulSoup(html, 'html.parser')
                skill = soup.find_all('span', class_='bloko-tag__section bloko-tag__section_text')

                for skills in skill:
                    if skills.text != '':
                        arr_skills.append(skills.text)

            except AttributeError:
                pass

        self.res_thread_search_requirements_five = arr_skills


    def thread_search_requirements_six(self, links, job):
        links = links
        arr_skills = []

        for link in links:
            try:
                user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'

                html = requests.get(link, headers={'User-agent':user_agent}).content
                soup = BeautifulSoup(html, 'html.parser')
                skill = soup.find_all('span', class_='bloko-tag__section bloko-tag__section_text')

                for skills in skill:
                    if skills.text != '':
                        arr_skills.append(skills.text)

            except AttributeError:
                pass

        self.res_thread_search_requirements_six = arr_skills


    def requirements_skills(self, job):
        res = []
        count_skills = []
        self.base_thread(job)
        arr_skills = self.res_thread_search_requirements_one + self.res_thread_search_requirements_two + self.res_thread_search_requirements_three + self.res_thread_search_requirements_four + self.res_thread_search_requirements_five + self.res_thread_search_requirements_six

        c = collections.Counter(arr_skills)

        for arr_skill in arr_skills:
            count_skills.append(c[arr_skill])

        for count_skill in arr_skills:
            if c[count_skill] > max(count_skills) // c[count_skill]:
                res.append(count_skill)

        return set(res)


