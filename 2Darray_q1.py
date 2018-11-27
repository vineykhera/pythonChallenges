# Complete the hourglassSum function below.
def hourglassSum(arr):
    maxsum = -99
    sumLen = len(arr)-2
    sumarr = [[0 for i in range(sumLen)] for j in range(sumLen)]
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            sumarr[i][j] = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if sumarr[i][j] > maxsum:
                maxsum = sumarr[i][j]
    return maxsum
