def sortedSquArr(arr):
    squ = [0 for _ in arr]; 
    for idx in range(len(arr)):
        value = arr[idx]
        squ[idx] = value * value
    squ.sort()
    print(squ)

array = [1,2,3,5,6,8,9]

sortedSquArr(array)

def optimalFreelancing(jobs):
  LENGTH_OF_WEEK = 7
  print([0])
  timeLine = [0] * LENGTH_OF_WEEK

  jobs.sort(key=lambda job: job['payment'], reverse=True)

  for job in jobs: 
    maxTime = min(job['deadline'], LENGTH_OF_WEEK);

    for time in reversed(range(maxTime)):
        if timeLine[time] == 0:
            timeLine[time] = job['payment']
            break

  return sum(timeLine)

optimalFreelancing([{'payment': 1, 'deadline': 1}, {'payment': 2, 'deadline': 2}])