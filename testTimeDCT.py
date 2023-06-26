import numpy as np
import matplotlib.pylab as plt
import utils as u
from datetime import datetime
from scipy.fftpack import dct
import cv2
from DCT import custom_dct2

# plot setting
plt.style.use('seaborn')
plt.rcParams['figure.figsize'] = [9, 6]
plt.rcParams['figure.dpi'] = 100


dimensions = [20, 40, 80, 160]

timing = {
    "HomeMade": [],  # timing with our method
    "FFT-c": [],  # timing with cv2 method
    "FFT-s": []  # timing with scipy method
}
timing2 = {
    "HomeMade": [],  # timing with our method
    "FFT-c": [],  # timing with cv2 method
    "FFT-s": []  # timing with scipy method
}
results = {
    "HomeMade": [],  # results with our method
    "FFT-c": [],  # results with cv2 method
    "FFT-s": []  # results with scipy method
}

for n in dimensions:
    matrix = np.random.randint(0, 256, size=(n, n))
    t0 = datetime.now()
    results["FFT-s"].append(dct(matrix, type=2))
    t1 = datetime.now()
    results["FFT-c"].append(cv2.dct(np.float32(matrix)))
    t2 = datetime.now()
    results["HomeMade"].append(custom_dct2(matrix))
    t3 = datetime.now()

    timing2["HomeMade"].append(t3 - t2)
    timing2["FFT-c"].append(t2 - t1)
    timing2["FFT-s"].append(t1 - t0)

for i in range(len(dimensions)):
    timing["HomeMade"].append(
        int(timing2["HomeMade"][i].total_seconds() * 1e6))
    timing["FFT-c"].append(int(timing2["FFT-c"][i].total_seconds() * 1e6))
    timing["FFT-s"].append(int(timing2["FFT-s"][i].total_seconds() * 1e6))

for type in timing:
    if type == "FFT-s":
        col = "green"
    elif type == "FFT-c":
        col = "yellow"
    elif type == "HomeMade":
        col = "blue"
    plt.semilogy(timing[type], dimensions, color=col, label=type)

plt.xlabel('Times')
plt.ylabel('Dimensions')
plt.title('Comparing different DCT')
plt.legend()
plt.show()
