import time

start = time.time()

count = 0
for i in range(1000000000):
    count += 1

end = time.time()

print(end - start, 'sec')

# Results on my PC: 73.83807063102722 sec
# My PC Characteristics:
# CPU: Intel Core I5 11th Gen (2.40 GHz)
# RAM: 8 GB
# OS: Windows 10 - 64x
