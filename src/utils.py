import os
import time
import uuid
import cv2
import logging
import tensorflow as tf

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_image(x):
    byte_img = tf.io.read_file(x)
    img = tf.io.decode_jpeg(byte_img)
    return img


def create_folder(path):
    if not os.path.exists(path):
        logger.info(f"Creating folder en ... {path}")
        os.makedirs(path)
    else:
        logger.info(f"Folder in {path} is already created...")


def capture_picture(num_images: int, IMAGES_PATH: str):
    cap = cv2.VideoCapture(1)
    for img_num in range(num_images):
        logger.info(f'Collecting imagen: {img_num}')
        ret, frame = cap.read()
        img_name = os.path.join(IMAGES_PATH, f"{str(uuid.uuid1())}.jpg")
        cv2.imwrite(img_name, frame)
        cv2.imshow('frame', frame)
        time.sleep(1)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
