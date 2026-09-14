import random

print("random programmer")

print("Random program at the top")

for _ in range(100):
    code = ''
    for _ in range(random.randint(1, 5)):
        code += random.choice('print("Hello, world!");\n')
    print(code)