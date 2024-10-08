# Complete the 'getMinCost' function below.
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY crew_id
#  2. INTEGER_ARRAY job_id
# len(crew_id) = len(job_id)
# It needs to return the minimum distance for the crew to travel to the available jobs


def getMinCost(crew_id, job_id):
    crew_id.sort()
    job_id.sort()
    res = 0
    for i in range(len(crew_id)):
        res += abs(crew_id[i] - job_id[i])
    return res
