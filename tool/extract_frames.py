import cv2
import numpy as np
import os
from pathlib import *
import argparse
from vad_path import getVADPath

# Config
def get_configs():
    parser = argparse.ArgumentParser(description="Extract_frames")
    parser.add_argument("--dataset", type=str, default="custom")
    parser.add_argument("--phase", type=str, default='test', choices=['train', 'test'])
    args = parser.parse_args()

    return args


def extract(args):
    path_videos = f"{getVADPath}custom/{args.phase}ing/videos/"
    path_frames = f"{getVADPath}custom/{args.phase}ing/frames/"

    films = list()
    files = (x for x in Path(path_videos).iterdir() if x.is_file())
    for file in files:
        print(str(file.name).split(".")[0], "is a file!")
        films.append(file)

    for i, film in enumerate(films):
        count = 0
        vidcap = cv2.VideoCapture(str(film))
        success, image = vidcap.read()
        mapp = str(film.name).split(".")[0]
        while success:
            name = f"{path_frames}{mapp}/{count}.jpg"
            if not os.path.isdir(f"{path_frames}{mapp}"):
                os.mkdir(f"{path_frames}{mapp}")
            cv2.imwrite(name, image)  # save frame as JPEG file
            success, image = vidcap.read()
            count += 1


if __name__ == '__main__':
    args = get_configs()
    extract(args)