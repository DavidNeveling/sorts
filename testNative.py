import random, time, sys

size = int(sys.argv[1])
list = [random.randrange(1, size) for i in range(size)]
start = time.clock()
list = sorted(list)
end = time.clock()
print("time elapsed = " + str(end - start))
