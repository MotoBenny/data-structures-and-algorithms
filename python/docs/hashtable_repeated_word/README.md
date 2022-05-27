# Challenge Summary
Find repeated words

## Whiteboard Process
[whiteboard](python/docs/hashtable_repeated_word/whiteboard.jpeg)

## Approach & Efficiency
O(n) since we iterate through all the words until we find a match.
This means we potentially need to check every word in the words list, if the
last word is our positive match.

## Solution
The code uses regex to strip any non character letters from the words
it then lowers all characters to ignore word case. And uses split to split
the words at all whitespace.

We then simply work through the words adding any words not in our set to our set.
if we hit a iteration where the word is in our set, we return that word.

```python
import re


def first_repeated_word(word):
    # separate the words at the spaces
    pattern = re.compile('[^a-zA-Z ]')
    stripped = pattern.sub('', word)
    words = stripped.lower().split()
    # print(stripped)
    check_set = set()

    for word in words:
        if word in check_set:
            return word
        else:
            check_set.add(word)




```
