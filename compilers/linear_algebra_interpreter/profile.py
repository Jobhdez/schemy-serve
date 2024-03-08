import time
from linear_algebra import Mat, parallel_sq_matrix_mul

m1 = []
for i in range(1, 1001):
    m1.append(i)

m2 = []
for i in range(1000):
    m2.append(m1)

start = time.time()
sq_mul(m2,m2)
end = time.time()

print(f"non parallize matrix sq mul: {end - start}")

start2 = time.time()
parallel_sq_matrix_mul(m2, m2)
end2 = time.time()

print(f"parallize matrix sq mul: {end2-start2}")
