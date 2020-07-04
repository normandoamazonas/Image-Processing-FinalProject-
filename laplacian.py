# SCC0251 - Processamento de Imagens (Turma 1 - Semestre 1 - 2020)
# 11561949 - Normando de Campos Amazonas Filho
# 8632563 - Robson Marques Pessoa

# Laplacian Filtering

# Gitlab Repository: https://gitlab.com/robsonpessoa-scc0251/t02-image-enhancement-and-filtering

import imageio
import numpy as np


def create_matrix(width, height, func):
    return apply(np.zeros((width, height)), func)


def create_spatial_matrix(size, func):
    return create_matrix(size, size, func)


def apply(matrix, func):
    m = np.array(matrix, copy=True).astype(np.float)

    width, height = matrix.shape

    a = int((width - 1) / 2)
    b = int((height - 1) / 2)

    for i in range(width):
        signal_x = -1 if i < a else 1
        x = int(np.abs(a - i) * signal_x)
        for j in range(height):
            signal_y = -1 if j < b else 1
            y = int(np.abs(b - j) * signal_y)
            m[i, j] = func(x, y, matrix[i, j])
    return m


def euclidean_equation(x, y):
    return np.sqrt(x ** 2 + y ** 2)


def gaussian_kernel_equation(x, sigma):
    return (1 / (2 * np.pi * sigma ** 2)) * np.exp((-1 * x ** 2) / (2 * sigma ** 2))


def gaussian_range_component(matrix, sigma):
    size = len(matrix)
    center = int(np.floor(size / 2))
    component = apply(matrix.astype(np.float),
                      lambda x, y, value: gaussian_kernel_equation(value - matrix[center, center], sigma))
    return component


def bilateral_normalization(original, matrix):
    W = np.sum(matrix)
    I = np.sum(np.multiply(matrix, original))
    return I / W


def scale(matrix):
    min_value = np.min(matrix)
    max_value = np.max(matrix)
    matrix = np.subtract(matrix, np.full(matrix.shape, min_value))
    matrix = np.multiply(matrix, np.full(matrix.shape, 255))
    matrix = np.divide(matrix, np.full(matrix.shape, max_value - min_value))
    return matrix.astype(np.uint8)


# The following method was taken from the class materials
def image_convolution(image, filter_matrix):
    N, M = image.shape
    n, m = filter_matrix.shape

    a = int((n - 1) / 2)
    b = int((m - 1) / 2)

    # new image to store filtered pixels
    # copies the original image 'image' so that border pixels remain the same
    g = np.array(image, copy=True).astype(np.float)

    # for every pixel
    for x in range(a, N - a):
        for y in range(b, M - b):
            # gets subimage
            neighbourhood = image[x - a: x + a + 1, y - b:y + b + 1]
            modified_neighbourhood = np.multiply(filter_matrix, neighbourhood).astype(np.uint8)
            g[x, y] = np.sum(neighbourhood, modified_neighbourhood)

    return g


def add_border(image, matrix):
    a = int((matrix.shape[0] - 1) / 2)
    return np.pad(image, a, mode='constant')


def remove_border(image, matrix):
    length = int((matrix.shape[0] - 1) / 2)
    size = image.shape
    height = size[0]
    width = size[1]
    return image[length:width - length, length:height - length]


def laplacian_filtering(img, c, kernel):
    kernel_1 = np.full((3, 3), -1)
    kernel_1[1, 1] = 4
    indexes = np.meshgrid([0, 2], [0, 2])
    kernel_1[tuple(indexes)] = 0

    kernel_2 = np.full((3, 3), -1)
    kernel_2[1, 1] = 8

    matrix = kernel_1 if kernel == 1 else kernel_2

    padded_img = add_border(img, matrix)
    filtered_img = image_convolution(padded_img, matrix)
    filtered_img = remove_border(filtered_img, matrix)

    filtered_img = scale(filtered_img)

    filtered_img = np.multiply(filtered_img, np.full(filtered_img.shape, c))
    filtered_img = np.add(filtered_img, img)

    filtered_img = scale(filtered_img)

    return filtered_img


def comparison(transformed_img, original_img):
    power_matrix = np.full(transformed_img.shape, 2)
    matrix = np.power(np.subtract(transformed_img.astype(np.float), original_img.astype(np.float)), power_matrix)
    return np.sqrt(np.sum(matrix))


def apply_filter(img):
    output = np.array(img, copy=True).astype(np.uint32)

    # Laplacian Filtering
    c = 0.5
    kernel = 1

    output[:,:,0] = laplacian_filtering(np.array(np.clip(img[:,:,0], 0, 255)), c, kernel)
    output[:,:,1] = laplacian_filtering(np.array(np.clip(img[:,:,1], 0, 255)), c, kernel)
    output[:,:,2] = laplacian_filtering(np.array(np.clip(img[:,:,2], 0, 255)), c, kernel)

    return img


def save_image(value):
    return value == 1


input_img = imageio.imread("LANDSAT2000.png")
output_img = apply_filter(input_img)
imageio.imwrite("LANDSAT2000_1.png", output_img)
print("%.4f" % comparison(output_img, input_img))

input_img = imageio.imread("LANDSAT2017.png")
output_img = apply_filter(input_img)
imageio.imwrite("LANDSAT2017_1.png", output_img)
print("%.4f" % comparison(output_img, input_img))
