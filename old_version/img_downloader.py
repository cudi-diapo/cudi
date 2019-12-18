import os
import re
import sys
import time
import random
import urllib.request

link_image_regex = re.compile(r"content\=\"(http(?:s)?:\/\/[0-9]*\.media\.tumblr\.com\/.*(?:.jpg|.jpeg|.png))\">")


def get_image(t_name, num):
    def _get_image_link(number):
        source = urllib.request.urlopen("http://archillect.com/" + number).read().decode('utf-8')
        print(f"{t_name} | http://archillect.com/{number}")
        try:
            return str(link_image_regex.findall(source)[0])
        except IndexError as e:  # no image found or gif found
            print(e)
            _get_image_link(str(random.randint(0, 230000)))

    try:
        urllib.request.urlretrieve(_get_image_link(str(random.randint(0, 230000))), f"media/archillect{num}.jpg")
    except TypeError:
        print("Error while getting the url")
        get_image(t_name, num)


def img_dl(t_name, timer, num_min, num_max):
    print(f"Enter {t_name} - timer = {timer}")
    i = num_min - 1
    while True:
        i += 1
        get_image(t_name, i)
        if timer > 0:
            time.sleep(timer)
        if i == num_max:
            i = num_min - 1

