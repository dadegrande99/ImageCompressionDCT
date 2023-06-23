import numpy as np
import matplotlib.pylab as plt
import utils as u
from datetime import datetime
from scipy.fftpack import dct

# plot setting
plt.style.use('seaborn')
plt.rcParams['figure.figsize'] = [9, 6]
plt.rcParams['figure.dpi'] = 100


dimensions = [200, 500, 1000, 2000]

timing = {
    "HomeMade": [],  # timing with our method
    "FFT": []  # timing with scipy method
}
results = {
    "HomeMade": [],  # results with our method
    "FFT": []  # results with scipy method
}

for n in dimensions:
    matrix = np.random.randint(0, 256, size=(n, n))
    t1 = datetime.now()
    results["FFT"].append(dct(matrix))
    t2 = datetime.now()
    # results["HomeMade"].append(dct(matrix))
    # timing["HomeMade"].append(datetime.now() - t2)
    timing["FFT"].append(t2 - t1)

for i in range(len(dimensions)):
    # timing["HomeMade"][i] = int(timing["HomeMade"][i].total_seconds() * 1e6)
    timing["FFT"][i] = int(timing["FFT"][i].total_seconds() * 1e6)


type = "FFT"
# for type in timing:
if type == "FFT":
    col = "green"
elif type == "HomeMade":
    col = "blue"
plt.plot(dimensions, timing[type], color=col, label=type)
for i in range(len(dimensions)):
    plt.plot(dimensions[i], timing[type][i], color='red', marker='o')
    plt.text(dimensions[i], timing[type][i], u.printTime(
        timing[type][i]), color='black', ha='left', va="bottom", rotation=45)

plt.xlabel('Dimensions')
plt.ylabel('Times')
plt.title('Comparing different DCT')
plt.legend()
plt.show()
