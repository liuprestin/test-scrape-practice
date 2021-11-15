"""
Copyright © 2021 Prestin Liu

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the “Software”), to deal in the
 Software without restriction, including without limitation the rights to use,
 copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the
 Software, and to permit persons to whom the Software is furnished to do so,
 subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
# API practice sheet response
# to use this script in the command line
# python ./test-scrape.py

import requests
from bs4 import BeautifulSoup

# Question 1 - write a python program to test if a given page is found or not
# on this server: https://en.wikipedia.org/robots.txt

robot_res = requests.get('https://en.wikipedia.org/robots.txt')

def test_connect_site(res):
    if res.status_code == 200:
        print("Connection Worked - retrieved information")
    else:
        print("double check the request object it returned: " + str(res))
    return None

test_connect_site(robot_res)

# Question 2 - write a python program to down and display the content of
# robot.txt from Question 1

#lets save this as well 
with open('wikipedia_robot.txt', "w") as robot_txt:
    robot_txt.writelines(robot_res.text)

print(robot_res.text)

# Question 3 - write a python program to extract h1 tags from http://www.example.com

res = requests.get('http://www.example.com')
soup = BeautifulSoup(res.text, 'html.parser')

ex_header = soup.select('h1')
print(ex_header)

# ------------------------------------------------------------------
# The next set of questions requires accessing www.python.org

py_res = requests.get('https://www.python.org')
py_soup = BeautifulSoup(py_res.text, 'lxml')

# Question 4 - write a python program to find all h2 tags and list the first four
# from https://www.python.org

def python_site_h2_headers():
    h2_pyheaders = py_soup.find_all('h2')
    counter = 0
    while counter < 4:
        print(h2_pyheaders[counter].getText())
        counter += 1
    return h2_pyheaders

python_site_h2_headers()

# Question 5 - write a python program to find all h1,h2,h3 tags from
# https://www.python.org

def python_site_headers():
    h1_h2_h3_pyheaders = py_soup.find_all(['h1','h2','h3'])
    print(h1_h2_h3_pyheaders)
    return h1_h2_h3_pyheaders

python_site_headers()

# Question 6 - write a python program to retrieve the children of the html tag
# from https://www.python.org

#returns soup object

def python_site_html_children():
    py_html = py_soup.find('html')
    children = py_html.findChildren()
    print(children)
    return children

python_site_html_children()
