__author__ = 'annapurnaannadatha'

#############################################################################
##                               README                                    ##
##                                                                         ##
##     This program takes 7 tiles as input with lowercase alphabets and    ##
##     underscore ("_") for blank. It produces list  of all the words      ##
##     from the dictionary.txt that can be produced by using some or all   ##
##     of the seven tiles. Underscore is used as the wild card.            ##
##     Output is text file.                                                ##
##     Run Program : python3.5 search.py                                   ##
##                                                                         ##
#############################################################################


from itertools import chain, combinations
from sys import exit
import fnmatch
import re


def powerset(iterable):
    # to make list of all combinations
    s = list(iterable)
    return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))

def wildcard_match(comb_list,content):
    result=[]
    for word in comb_list:
        if "_" in word:
            word = word.replace("_","?")
            # wildcard matching
            for new_word in content:
                 if fnmatch.fnmatch(new_word,word):
                     result.append(new_word)
        else:
            if word in content:
                result.append(word)
    return result


if __name__=='__main__':
    # Taking input
    tiles = input("Enter 7 tiles with alphabets or _ for blank tiles without any spaces:")

    # check if there are 7 tiles and lowercase or exit
    if len(tiles)!=7:
        print("Need exactly 7 tiles ")
        exit()
    elif not re.match("^[a-z_]*$", tiles):
        print("Only lowercase alphabets and underscores allowed")
        exit()

    # reading dictionary into list
    with open("dictionary.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    # making list of all possible combinations with the tiles
    comb_list = list(map(''.join,powerset(tiles)))
    # check if there is blank
    if "_" in tiles:
        result = wildcard_match(comb_list,content)
    else:
        result = list(set(comb_list)&set(content))

    #print("\n".join(result))
    #writing list to a text file
    with open("out_file.txt", 'w') as file_handler:
        for item in result:
            file_handler.write("{}\n".format(item))
    print("Done.Check out_file.txt file")
