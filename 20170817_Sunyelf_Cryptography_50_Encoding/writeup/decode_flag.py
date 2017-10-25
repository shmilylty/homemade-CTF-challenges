from bubblepy import BubbleBabble

bb = BubbleBabble()
with open('flag.enc', 'r') as f:
    print bb.decode(f.read())
