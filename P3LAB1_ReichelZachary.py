r = int(input())
g = int(input())
b = int(input())

gray = r
if g < gray:
   gray = g

if b < gray:
   gray = b

if r >= gray:
   r = r - gray
if g >= gray:
   g = g - gray
if b >= gray:
   b = b - gray

print((r), (g), (b))
