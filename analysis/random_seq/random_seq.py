import random
import subprocess
import matplotlib.pyplot as plt
import numpy as np

def GenerateRandomSequence(n, chars=["A", "C", "G", "U"]):
    s = ""
    for _ in range(n):
        s += random.choice(chars)
    return s

# s = GenerateRandomSequence(80)

# subprocess.run(f"echo {s} | drtransformer.py --name rand_50 --outdir analysis/random_seq --logfile", shell=True)
# subprocess.run(f"echo {s} | drtransformer.py --reversed-transcription --name rand_50_rev --outdir analysis/random_seq --logfile", shell=True)

def Compare_53_35(n, seq_len):
    energies = []
    for i in range(n):
        energies.append([None, None])
        s = GenerateRandomSequence(seq_len)
        # call DrTransformer and generate log files
        subprocess.run(f"echo {s} | drtransformer.py --name compare_53_35 --outdir analysis/random_seq --logfile", shell=True)
        subprocess.run(f"echo {s} | drtransformer.py --reversed-transcription --name compare_53_35_rev --outdir analysis/random_seq --logfile", shell=True)
        # parse log files
        with open("analysis/random_seq/compare_53_35.log") as f:
            current_energies = []
            lines = f.readlines()[::-1]
            i = 0
            for line in lines:
                if not line:
                    continue
                words = line.split()
                if words[0] != str(seq_len):
                    break
                current_energies.append(float(words[-5]))
        with open("analysis/random_seq/compare_53_35_rev.log") as f:
            current_energies_rev = []
            lines = f.readlines()[::-1]
            i = 0
            for line in lines:
                if not line:
                    continue
                words = line.split()
                if words[0] != str(seq_len):
                    break
                current_energies_rev.append(float(words[-5]))
        energies[-1][0] = min(current_energies)
        energies[-1][1] = min(current_energies_rev)
    return energies

energies = Compare_53_35(100, 150)
print(energies)
d_energies = [tup[0]-tup[1] for tup in energies]
print(d_energies)
# plot
mi = np.floor(min(d_energies))
ma = np.ceil(max(d_energies))
plt.hist(d_energies, bins=np.arange(mi-0.5, ma+1.5, 1))
plt.title("Comparison of lowest energy at end of simulation\ndE < 0 means: lower energy in 5->3 direction")
plt.xlabel("dE = E(53) - E(35)")
plt.ylabel("Frequency")
plt.savefig("analysis/random_seq/compare_53_35____.png")
plt.close()