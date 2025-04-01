import numpy as np
import astropy.units as u
from astropy.time import Time

import time

n = 86400*365
import numpy as np
start = time.time()
res = np.arange(np.datetime64("2024-01-01"), np.datetime64("2024-12-31"), np.timedelta64(1, "s"))
print(len(res))
end = time.time()
print(end - start) #0.057021141052246094

31536000
8.857582092285156

start = time.time()
timeo = Time("2024-01-01T00:00:00Z", scale='utc', format='isot', precision=9)
times = timeo + np.arange(n) * u.second
#times.to_datetime())
print(len(times))
end = time.time()
print(end - start) # 18.311403036117554

import datetime
start = time.time()
test_date = datetime.datetime(2024, 1, 1)
res = [test_date + datetime.timedelta(seconds=idx) for idx in range(int(n))]
print(len(res))
end = time.time()
print(end - start) # 8.857582092285156

#test_date = datetime.datetime(2024, 1, 1, 0, 0, 0)
#print(test_date)
#res = [test_date + datetime.timedelta(seconds=idx) for idx in range(n)]
