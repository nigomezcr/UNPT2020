from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.filters import threshold_li


def show_image(image, title='Image', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()


def save_image(image, fname, title='', cmap_type='gray'):
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.savefig(fname)


base = Path('Images')

for image in base.iterdir():
    # Import image
    im = plt.imread(image)
    # Turn to grayscale
    gray = rgb2gray(im)

    # Calculate threshold (this is an algorithm and may not be the best for every image)
    thresh = threshold_li(gray)
    binary = gray > thresh

    fname = 'processed/' + str(image).split('/')[-1]

    save_image(binary, fname)