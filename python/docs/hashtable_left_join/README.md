# hashtable_left_join
Create
## Challenge
Write a function that LEFT JOINs two hashmaps into a single data structure.

Write a function called left join \
Arguments: two hash maps \
The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values. \
The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values. \
Return: The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic

## Approach & Efficiency
We take in the tables as arguments, create a empty list. we use .items() to isolate and view the values from the table. \
If our table_b.get(key) returns truthy we add the value to our empty list. \
else we add 'NONE' to our empty list
we then return our table

## API
No APIs used in the implementation of this challenge
