import os

def birthdayCakeCandles(candles):
    tallest = max(candles)
    tall_candles = len([x for x in candles if x == tallest])
    return tall_candles


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
