## A better solution to the 100 prisoners riddle

The strategy involves a simple change: When prisoners do not find their card, they report the number found in the last box.

At 100 it's still an improvement of around 2%: 31% vs 33%. The odds are much improved with a smaller sample, at 10 prisoners/boxes it gives 52% odds.


### Program output for validation:

Begin hacking with 100,000 loops ...    
10 boxes:    
35.52% victory without last card strategy    
52.17% victory with last card strategy    
20 boxes:    
33.37% victory without last card strategy    
42.21% victory with last card strategy    
40 boxes:    
31.93% victory without last card strategy    
36.71% victory with last card strategy    
50 boxes:    
31.61% victory without last card strategy    
35.80% victory with last card strategy    
100 boxes:    
30.93% victory without last card strategy    
33.21% victory with last card strategy


### Explanation

For chains of length 51, and only for chains of length 51, that answer will always be correct. This only improves the odds, by about 2% (33% vs 31%) in a 100 sample size, but all the way up to 52% for a sample of 10, compared to about 35-36% without the last card strategy.

So it goes:    
	- In every sequence below 51, you will always find your number in one of the boxes.    
	- In any sequence above 51, you will never find it, with or without the strategy.    
	- In a sequence of 51, once you open the last box with the number of the 51th box in the sequence, you don't need to know what's in it, because in that sequence it can only be your number, the one that points to the first box you opened, as otherwise the sequence length would be above 51. QED.


### Acknowledgements

Thanks to Derek at Veritasium, his video (https://youtu.be/iSNsgj1OCLA) on this puzzle led me to this solution.
