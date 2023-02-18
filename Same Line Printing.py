from time import sleep
i = 100
line_up = '\033[1A'
line_clear = '\x1b[2K'
print("Starting", end="")
sleep(0.5)
for _ in range(3):
    print(".", end="")
    sleep(0.5)
print(line_clear, end="\r")
print("Continuing", end="")
sleep(1)
for _ in range(3):
    print(".", end="")
    sleep(1)
print(line_clear, end="\r")
print("Done")