"""
2 questions

1. you are given a function f that returns a list of (story, score), you need to implement
 the function top5stories(cutoff: int) which returns a list in descending order of first 5
stories whose score is >= cutoff.

Note: function f doesn't necesarily return all what you need from the first time you call it.
Meaning, you might need to call f several times until you get the top 5 stories

Note 2: If f return a story already seen, the score of the story is the sum of all values seen

2. Given 2 csv files about dinosoaurs which had something like
name, leg_length, type
name, something about length, another value

read them, calculate the speed which is a function that depends on all values and return the
top 10 dinosaurs that run the fastest according to speed

Seen the above exercise before, the idea is to see if you know how to read files, you consider
border cases, you think if the file doesn't fit in memory, bla bla
"""
