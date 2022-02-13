# import the necessary packages
import os
import sys
import requests
import ssl
from flask import Flask
from flask import request
from flask import jsonify
from flask import send_file
from app_utils import download
from app_utils import generate_random_filename
from app_utils import clean_me
from app_utils import clean_all
from app_utils import create_directory
from app_utils import get_model_bin
from app_utils import convertToJPG

from os import path
import torch

import fastai
from deoldify.visualize import *
from pathlib import Path
import traceback


# Handle switch between GPU and CPU
if torch.cuda.is_available():
    torch.backends.cudnn.benchmark = True
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"
else:
    del os.environ["CUDA_VISIBLE_DEVICES"]

global video_colorizer
video_colorizer = get_video_colorizer()
video = video_colorizer.colorize_from_file_name("video.mp4", render_factor=30)
