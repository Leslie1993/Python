#12343
import sys

def func():
    print(100)


for i in range(1, 100):
    func()
for item in sys.path:
    print(item)

print(454)
