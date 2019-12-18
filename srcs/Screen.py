from srcs.Menu import Menu
from srcs.EnvCudi import EnvCudi
from srcs.ImageDownloader import ImageDownloader


class Screen:
    def __init__(self, os_param):
        self.os = os_param['os']
        self.menu = Menu(os_param)
        self.cudi = EnvCudi(self.menu)
        self.img_dl = ImageDownloader(self.menu)

    def launch(self):
        self.img_dl.start_processes()
        print(f"-------Debug on start-------\n{self}")
        import time
        time.sleep(1)
        self.img_dl.kill_process()

    def __str__(self):
        return f"class Screen:\n" \
               f"\t{'os:':20}{self.os}\n\n\t{self.menu}\n\t{self.cudi}\n\t{self.img_dl}"
