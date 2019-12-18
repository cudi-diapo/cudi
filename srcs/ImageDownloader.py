import os
import re
import time
import random
import urllib.request
import multiprocessing

link_image_regex = re.compile(r"content\=\"(http(?:s)?:\/\/[0-9]*\.media\.tumblr\.com\/.*(?:.jpg|.jpeg|.png))\">")


def get_image(p_name, num):
    def _get_image_link(number):
        source = urllib.request.urlopen("http://archillect.com/" + number).read().decode('utf-8')
        print(f"{p_name} | http://archillect.com/{number}")
        try:
            return str(link_image_regex.findall(source)[0])
        except IndexError as e:  # no image found or gif found
            print(f"{p_name} | {e} number = {number} | link = {_get_image_link(number)}")
            _get_image_link(str(random.randint(0, 250000)))
    try:
        urllib.request.urlretrieve(_get_image_link(str(random.randint(0, 230000))), f"media/archillect{num}.jpg")
    except TypeError:
        print(f"{p_name} | Error while getting the url: number = {num} | image = {_get_image_link(num)}")
        get_image(p_name, num)


def image_controler(process_id, min_img, max_img, timer):
    while True:
        for x in range(min_img, max_img):
            get_image(f"Process-{process_id}", x)
            if timer != -1:
                time.sleep(float(timer) - 0.500)


class ImageDownloader:
    timer = -1
    nb_img: int = 200
    nb_process: int = 10
    process_list: list

    def init_processes(self):
        img_range = int(self.nb_img / self.nb_process)
        for x in range(self.nb_process):
            self.process_list.append(multiprocessing.Process(target=image_controler,
                                                             args=(x, img_range * x, self.nb_img, self.timer)))

    def __init__(self, addr_menu):
        self.process_list = []
        self.addr_menu = addr_menu
        if not os.path.isdir("./media"):
            os.mkdir("./media")
        self.init_processes()

    def __str__(self):
        return f"class ImageDownloader:\n" \
               f"\t\t{'nb_img =':20}{self.nb_img}\n\t\t{'nb_thread =':20}{self.nb_process}\n"

    def start_processes(self):
        try:
            for process in self.process_list:
                process.start()
        except Exception as e:
            print(e)

    def kill_process(self):
        for process in self.process_list:
            process.terminate()
        print("All processes killed")

    def change_process_param(self):
        self.kill_process()
        self.start_processes()

    def __change_timer(self):
        try:
            self.timer = self.addr_menu.img_params["timer"]
        except Exception:
            pass

    def __change_nb_process(self):
        try:
            self.nb_process = self.addr_menu.img_params["nb_process"]
        except Exception:
            pass

    def __change_nb_img(self):
        try:
            self.nb_img = self.addr_menu.img_params["nb_img"]
        except Exception:
            pass

    def update_processes(self):
        self.__change_timer()
        self.__change_nb_process()
        self.__change_nb_img()
        self.change_process_param()

