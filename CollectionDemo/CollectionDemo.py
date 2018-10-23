# coding:utf-8

from collections import namedtuple

websites = [
    ('Sohu', 'http://www.google.com/', u'张朝阳'),
    ('Sina', 'http://www.sina.com.cn/', u'王志东'),
    ('163', 'http://www.163.com/', u'丁磊')
]
data = []
WebSite = namedtuple('WebSite', 'name, url, founder')
for website in websites:
    website = WebSite._make(website)
    data.append(website)
for d in data:
    print d

Person = namedtuple('Person', 'name age sex')
print type(Person)

person = Person('Lily', 25, 'Female')
dataPerson = []
dataPerson.append(person)
person = Person('Lily', 26, 'Female')
dataPerson.append(person)

for d in dataPerson:
    print d

from collections import deque
import sys
import time

pmd = deque('>---------------------------')
while True:
    print '\r%s' % ''.join(pmd)
    pmd.rotate(1)
    sys.stdout.flush()
    time.sleep(0.08)
