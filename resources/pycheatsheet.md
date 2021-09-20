# Python useful syntax cheatsheet
## Input
Get lines of input until end of file:
```
import sys
for line in sys.stdin:
	# For each line in input
```
Get single line of input:
```
myin = input()
```
Handle input "n k l" where nkl are integers:
```
n, k, l = map(int, input().split())
```
## Give input file to python
```
python main.py < input.txt
```
## Useful algorithms
Count sum of numbers between 1 and n: 
```
sum = (n*(n+1))/2
```
