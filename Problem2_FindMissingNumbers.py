'''
Given a set of arrays of scrambled integers, your goal is to find which numbers were lost from each of the sequences.

Numbers are only lost from the middle of a (properly ordered) sequence: the first integer in the sequence l and last integer r are never lost.

For this problem, a properly ordered sequence of numbers is to be in strictly increasing order: [l, l + 1, l + 2, ... , r - 2, r - 1, r].

Your task, for each of the given arrays, is to print a string containing all of the missing numbers from the sequence in increasing order.

Input definition

An input file for this problem will contain an arbitrary number of lines. The first line will contain an integer, m, the number of tests in the input file. The next m lines will each contain multiple space-separated integers. For each line, generate a string containing the missing integers from the input sequence in increasing order.

Output definition

Your output file should contain m lines.

Each line should contain a string containing the missing integers from the corresponding input sequence, separated by spaces and in increasing order. If the sequence is complete, i.e. no numbers are missing, your output line for that input should be an empty string/blank line.

Example input

11
28 50 45 35 42 32 48 55 30 51 31 41 53 37 36 29 38 46 44 43 47 34 33 49 40 39 56
20 37 21 46 23 27 25 29 51 26 24 43 41 39 35 47 48 49 44 36 31 40 22 34 30 32 42 38 28 45 52
26 44 65 41 34 69 68 46 54 53 70 28 35 49 56 37 52 55 71 29 40 67 64 60 57 30 59 39 38 32 72
19 35 31 40 68 66 27 60 29 45 59 72 71 70 26 38 47 21 52 46 56 57 48 73 74 76 51 39 55 63 28 69 64 77
21 27 48 38 52 30 60 42 47 63 36 64 32 31 39 55 66 61 67 53 25 59 58 22 35 33 41 62 23 40 51 49 46 28 56 54 43 29 37 44 68 34 45 65 69
22 41 33 38 42 48 39 32 23 47 45 40 24 27 37 31 26 43 51
14 34 40 52 36 27 65 56 39 46 29 57 35 60 15 20 24 66 38 21 48 32 64 31 26 18 28 55 59 49 53 19 41 23 22 37 42 61 50 44 45 17 47 16 33 30 63 43 54 67
12 19 42 29 31 51 35 41 50 39 57 54 53 44 21 46 13 14 38 20 58 15 45 24 16 36 32 26 49 27 52 17 33 40 60
10 32 13 56 40 39 57 34 35 43 61 23 25 62 30 22 51 20 63 55 58 44 54 16 66 11 60 19 42 46 52 59 29 36 18 47 41 33 26 31 14 15 49 28 65 53 12 50 48 38 45 64 27 37 67
15 50 26 24 25 20 59 29 33 40 30 66 31 36 41 55 46 60 48 64 51 39 43 67 56 70 17 58 44 37 35 34 68 16 61 19 49 47 63 18 32 23 27 21 45 52 53 38 65 57 54 69 62 28 22 71
10 34 28 30 40 52 49 15 25 32 57 19 27 44 17 22 56 31 54 13 29 48 42 21 11 47 37 51 33 63
Example output

52 54
33 50
27 31 33 36 42 43 45 47 48 50 51 58 61 62 63 66
20 22 23 24 25 30 32 33 34 36 37 41 42 43 44 49 50 53 54 58 61 62 65 67 75
24 26 50 57
25 28 29 30 34 35 36 44 46 49 50
25 51 58 62
18 22 23 25 28 30 34 37 43 47 48 55 56 59
17 21 24
42
12 14 16 18 20 23 24 26 35 36 38 39 41 43 45 46 50 53 55 58 59 60 61 62
'''

from itertools import imap, chain
from operator import sub


n=int(raw_input())

for i in range(n):
    a=map(int, (raw_input().split()))
    a=sorted(a)

    m= list(chain.from_iterable((a[j] + d for d in xrange(1, diff))
                        for j, diff in enumerate(imap(sub, a[1:], a))
                        if diff > 1))
    print ' '.join(str(x) for x in m)
