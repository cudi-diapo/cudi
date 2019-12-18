class Button:
    """
        Create the function that manage button on the screen in the init
        Create the function that change the state when the button is clicked
    """
    def __init__(self):
        self.button = True

    def change_state(self):
        self.button = False if self.button else True

    def button_state(self):
        return self.button


class Menu:
    min_x: int
    min_y: int
    max_x: int
    max_y: int
    menu_width: int
    menu_height: int
    screen_width: int
    screen_height: int
    refresh_speed: int
    pause_screen: Button
    process_button: Button

    """
        process_menu: CustomMenu -> Choose all the process param & return a dict with params as timer, nb_process or nb_img
                    -> need to check the return dict but the dict can be empty
        pause_screen: Button -> button start/pause that stop the refresh of the screen
        process_button: Button -> button start/pause effect on the thread of img_downloader
        refresh_speed: Slider -> slider that update the delay between screen refresh (a screen refresh  = a new pic)
        filter: CustomMenu -> Mini menu that allow the user to add a filter to the screen (Black/white or old school edge)
        screen_size: CustomMenu -> Mini menu that allow the user to ass from full screen to a custom screen size and vice versa

        deezer_playlist: CustomMenu -> Choose your music / playlist and ( Button to adapt the refresh with the bpm) NOT IN DEV
    """
    def __init_min_max_coord(self):
        self.min_x: int = int(self.screen_width * 0.15)
        self.min_y: int = int(self.screen_height * 0.15)
        self.max_x: int = int(self.screen_width * 0.85)
        self.max_y: int = int(self.screen_height * 0.85)

    def update_screen_size(self, width, height):
        self.screen_width: int = width
        self.screen_height: int = height
        self.__init_min_max_coord()

    def update_menu_size(self, width, height):
        self.menu_width: int = width
        self.menu_height: int = height

    def __init__(self, os_param: dict):
        self.refresh_speed = 1
        self.pause_screen = Button()
        self.thread_button = Button()
        self.screen_width: int = int(os_param['screen_width'])
        self.screen_height: int = int(os_param['screen_height'])
        self.__init_min_max_coord()
        self.update_menu_size(int(self.screen_width / 10), int(self.screen_height / 10))

    def __str__(self):
        return f"class Menu:\n" \
              f"\t\t{'screen_width =':20}{self.screen_width}\n\t\t{'screen_height =':20}{self.screen_height}\n" \
              f"\t\t{'menu_width =':20}{self.menu_width}\n\t\t{'menu_height =':20}{self.menu_height}\n" \
              f"\t\t{'min_x =':20}{self.min_x}\n\t\t{'min_y =':20}{self.min_y}\n" \
              f"\t\t{'max_x =':20}{self.max_x}\n\t\t{'max_y =':20}{self.max_y}\n"
