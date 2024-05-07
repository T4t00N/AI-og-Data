import cv2 as cv
import numpy as np

# Image path
image_path = "banan.jpg"

# Read the image
image = cv.imread(image_path)

# Read the image in greyscale
grey_img = cv.imread(image_path, cv.IMREAD_GRAYSCALE)

def add_salt_pepper_noise(image, salt_ratio=0.2, pepper_ratio=0.2):
    row, col = image.shape
    salt = np.random.rand(row, col) < salt_ratio
    pepper = np.random.rand(row, col) < pepper_ratio
    noisy_image = np.copy(image)
    noisy_image[salt] = 255
    noisy_image[pepper] = 0
    return noisy_image

def add_gaussian_noise(image, sigma):
    row, col = image.shape
    mean = 0
    gauss = np.random.normal(mean, sigma, (row, col))
    noisy_image = np.clip(image + gauss, 0, 255)
    return noisy_image.astype(np.uint8)

# def add_gaussian_noise(image):
#     noisy_image = cv.GaussianBlur(image, (5,5),64)
#     return noisy_image

def apply_median_filter(image):
    filtered_image = cv.medianBlur(image, 3) # Applying median filter with 3x3 kernel
    return filtered_image

def apply_mean_value_filter(image):
    filtered_image = cv.blur(image, (3,3)) # Applying median filter with 3x3 kernel
    return filtered_image

# Add salt and pepper noise to the grayscale image
# noisy_image = add_salt_pepper_noise(grey_img, sigma=25)
sigma = 20
noisy_image = add_gaussian_noise(grey_img, sigma)

# Apply median filter
mean_filter_image = apply_mean_value_filter(noisy_image)
median_filter_image = apply_median_filter(noisy_image)

# Display the images
cv.imshow("Noisy Image", noisy_image)
cv.waitKey(0)
cv.imshow("Filtered Image", mean_filter_image)
cv.waitKey(0)
cv.imshow("Median Filtered Image", median_filter_image)
cv.waitKey(0)

cv.destroyAllWindows()
