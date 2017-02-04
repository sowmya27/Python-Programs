Problem:

You are given a dictionary (dictionary.txt), containing a list of words, one per line. Imagine you have seven tiles. Each tile is either blank or contains a single lowercase letter (a-z).Please list all the words from the dictionary that can be produced by using some or all of the seven tiles, in any order. A blank tile is a wildcard, and can be used in place of any letter.1. Find all of the words that can be formed if you don't have to deal with blank tiles. 2. Find all of the words that can be formed, including those where blank tiles are used as wildcards.3. Please bear in mind you will need to process several hundred of 7-tile sets with the same dictionary.



Explanation:

step 1: compute the powerset (set of all subsets) of the 7 letters (this represents all combinations and is only 2^7 = 128 groups of letters)
step 2: check the dictionary for this each word from the subset. If found add it to a list.
If there are blanks in 7 tiles, then use the blank as wildcard i.e., use a regex to provide all possible combinations with blank.
step 3: Put these into a final set which represents the result.




Run program:

$ python3.5 search.py 
Enter 7 tiles with alphabets or _ for blank tiles without any spaces:appears
Done.Check out_file.txt file




