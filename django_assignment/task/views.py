import requests
from bs4 import BeautifulSoup
from django.shortcuts import render

from django.http import HttpResponse


from .models import Order


def index(request):
    return render(request, 'index.html')

# Question 1

def question_1(request):
    CNN_URL = 'https://www.cnn.com/'
    try:
        response = requests.get(CNN_URL)
        if response.status_code == 200: 
            soup = BeautifulSoup(response.content, 'html.parser')
            headlines = soup.find_all('div', class_='container__item')
            news = []

            for n in headlines:
                d = {}
                link = n.find('a')
                if link:
                    d['url'] = "https://edition.cnn.com" + link['href']
                    # d['title'] = link.get_text()
                    # d['title'] = link.find('span')
                    span = link.find('span', class_='container__headline-text')
                    if span:
                        d['title'] = span.get_text() 
                    else:
                        # d['title'] = link.get_text() 
                        continue

                    news.append(d)

            return render(request, 'que_1.html', {'news': news})
        else:
            error = "Failed to retrieve the news, status code: {}".format(response.status_code)
            return render(request, 'que_1.html', {'error': error})
    except Exception as e:
        error = "An error occurred: {}".format(str(e))
        return render(request, 'que_1.html', {'error': error})

# Question 2
from .que_2 import cleaned_csv


def question_2(request):
    if request.method == "POST":
        user_data = r'..\user_data.csv'
        cleaned_data = cleaned_csv(user_data)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="cleaned_user_data.csv"'

        cleaned_data.to_csv(path_or_buf=response, index=False)

        return response

    return render(request, 'que_2.html')

    

# Question 3

def all_customers(request):
    customers = Order.objects.all()
    return render(request, 'all_customers.html', {'customers': customers})

def question_3(request):
    customers = Order.top_customers()
    return render(request, 'que_3.html', {'customers': customers})


# Question 4

import time
from threading import Lock

class RateLimiter:
    def __init__(self, max_requests=5, time_window=60):
        self.max_requests = max_requests
        self.time_window = time_window
        self.user_requests = {}
        self.lock = Lock()

    def allow_request(self, user_id):
        current_time = time.time()
        with self.lock:
            if user_id not in self.user_requests:
                self.user_requests[user_id] = []
            
            requests = self.user_requests[user_id]
            requests = [req for req in requests if current_time - req < self.time_window]
            self.user_requests[user_id] = requests

            if len(requests) < self.max_requests:
                self.user_requests[user_id].append(current_time)
                return True
            else:
                return False

rate_limiter = RateLimiter()


def question_4(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        return rate_limiter_view(request, user_id)
    else:
        return render(request, 'que_4.html')



def rate_limiter_view(request, user_id):
    if rate_limiter.allow_request(user_id):
        remaining_requests = rate_limiter.max_requests - len(rate_limiter.user_requests[user_id])
        return render(request, 'que_4.html', {'remaining_requests': remaining_requests, 'user_id': user_id})
        # return {'remaining_requests': remaining_requests, 'user_id': user_id}
    else:
        # return HttpResponse(f"Rate limit exceeded for user {user_id}")
        error_message = f"Rate limit exceeded for user {user_id}"
        return render(request, 'que_4.html', {'error_message':error_message, 'user_id':user_id})



# Question 5


from typing import List, Dict, Callable
from .que_5 import *

def aggregate_data(data:List[Dict], key:str, aggregator: Callable):
    if aggregator == 'count':
        print('hhhh')
        rs = aggregate_count(data, key)
        print(rs)
    elif aggregator == 'sum':
        rs = aggregate_sum(data, key)
    elif aggregator == 'avg':
        rs = aggregate_avg(data, key)
    elif aggregator == 'max':
        rs = aggregate_max(data, key)
    elif aggregator == 'min':
        rs = aggregate_min(data, key)
    else:
        rs = "Valid Correct Input"

    return rs

def question_5(request):
    data = [
        {'A':10, 'B':20, 'C':30, 'D':40},
        {'A':15, 'B':20, "C":25, 'D':50},
        {'A':25, 'B':50},
        {'C':55, 'D':70},
    ]
    if request.method == "POST":
        key = request.POST['key']
        aggregator_function = request.POST['aggregator_function']

        rs = aggregate_data(data, key, aggregator=aggregator_function)

        return render(request, 'que_5.html', {'rs':rs})
    else:
        return render(request, 'que_5.html')

# Question 6

def find_duplicate(n, nums):
    for i in range(1, n):
        if i in nums:
            nums.remove(i)
    return nums[0]

def question_6(request):
    if request.method == "POST":
        n = int(request.POST['n'])
        nums = request.POST['nums']

        nums = list(map(int, nums.split(',')))

        duplicate = find_duplicate(n, nums)

        return render(request, 'que_6.html', {"duplicate": duplicate})

    return render(request, 'que_6.html')
