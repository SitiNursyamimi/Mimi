import cv2
import os
import numpy as np
from PIL import Image

# Path for face image database
path = 'dataset'
recognizer = cv2.face_LBPHFaceRecognizer.create()