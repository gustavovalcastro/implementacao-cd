import numpy as np
import cv2
import random


def DA_brigthnessIncrease(image_input, image_output):
    image = cv2.imread(image_input)
    bright = np.ones(image.shape, dtype=np.uint8) * 60  # Increase brightness by 50
    bright_image = cv2.add(image, bright)
    cv2.imwrite(image_output, bright_image)


def DA_brigthnessDecrease(image_input, image_output):
    image = cv2.imread(image_input)
    dark = np.ones(image.shape, dtype=np.uint8) * 60  # Decrease brightness by 50
    dark_image = cv2.subtract(image, dark)
    cv2.imwrite(image_output, dark_image)


def DA_contrastIncrease(image_input, image_output):
    image = cv2.imread(image_input)
    alpha = 1.5  # Contrast control (1.0-3.0)
    beta = 0  # Brightness control (0-100)
    contrast_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    cv2.imwrite(image_output, contrast_image)


def DA_contrastDecrease(image_input, image_output):
    image = cv2.imread(image_input)
    alpha = 0.5  # Contrast control (1.0-3.0)
    beta = 0  # Brightness control (0-100)
    contrast_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    cv2.imwrite(image_output, contrast_image)


def DA_resize(image_input, image_output):
    image = cv2.imread(image_input)
    resized_image = cv2.resize(image, (320, 320))
    cv2.imwrite(image_output, resized_image)


def DA_randomNoise(image_input, image_output):
    image = cv2.imread(image_input)
    noise = np.random.randint(0, 256, image.shape, dtype=np.uint8)
    noisy_image = cv2.add(image, noise)
    cv2.imwrite(image_output, noisy_image)


def DA_gaussianBlur(image_input, image_output):
    image = cv2.imread(image_input)
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
    cv2.imwrite(image_output, blurred_image)


def DA_flipHorizontal(image_input, image_output):
    image = cv2.imread(image_input)
    flipped_image = cv2.flip(image, 1)  # 1 for horizontal flip
    cv2.imwrite(image_output, flipped_image)


def DA_flipVertical(image_input, image_output):
    image = cv2.imread(image_input)
    flipped_image = cv2.flip(image, 0)  # 0 for vertical flip
    cv2.imwrite(image_output, flipped_image)


def DA_heavyShapening(image_input, image_output):
    image = cv2.imread(image_input)
    sharpening = np.array([[-1, -1, -1], [-1, 10, -1], [-1, -1, -1]])
    sharpened = cv2.filter2D(image, -1, sharpening)
    for _ in range(500):
        sharpened = cv2.filter2D(sharpened, -1, sharpening)
    cv2.imwrite(image_output, sharpened)
