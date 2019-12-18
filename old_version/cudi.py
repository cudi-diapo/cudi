import os
import argparse

from MyThread import MyThread
from exit_cudi import exit_cudi
from img_downloader import img_dl


def parse_args():
    parser = argparse.ArgumentParser(description="Launch CUDI\nEvery parameters are in the app")
    parser.add_argument("-m", "--media", help="Choose the media directory in ./media/", type=str, default="")
    parser.add_argument("-t", "--thread", help="Number of threads (max 10)", type=int, default=1)
    parser.add_argument("-nb", "--number_media", help="Number of images in media source (default 100)", type=int, default=100)
    args = parser.parse_args()
    if not os.path.isdir(f"./media/{args.media}"):
        print(f"'media/{args.media}' is not a directory, media set as the default media directory")
    if args.thread > 10:
        args.thread = 10
    return args


def init_thread(args):
    thread_list = []
    num_max = int(100 / args.thread)
    for i in range(0, args.thread):
        thread_list.append(MyThread(i, f"Thread-{i + 1}", img_dl, 5, num_max - num_max, num_max))
        num_max += num_max
    thread_list.append(MyThread(args.thread, f"Thread-{args.thread + 1}", process_aff, 5, 0, num_max))
    return thread_list


def launch_cudi(args):
    thread_list = init_thread(args)
    try:
        for thread in thread_list:
            thread.start()
        for thread in thread_list:
            thread.join()
        # create screen and launch inside envcudi
    except Exception as e:
        exit_cudi(1)
        print(e)


if __name__ == "__main__":
    """
        To do: - Create a menu class with a thread's stop or a pause
               - Use the Archillect API
               - change speed and image's size while running
               - Apply a filter
               - change media root while running
               - adapt windows size
               - use deezer API 
               - Use SDL instead of pygame
    """
    args = parse_args()
    launch_cudi(args)
