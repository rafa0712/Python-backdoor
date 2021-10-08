import tqdm
import time

progress = tqdm.tqdm(range(2048*5), f'Sending filename', unit='8', unit_scale=True, unit_divisor=1024)
print(dir(progress))

for c in range(8):
    time.sleep(0.2)
    progress.update(1000)
progress.close()