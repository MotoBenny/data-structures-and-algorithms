# Hashtables
Implement a Hashtable Class with the following methods:

### set
Arguments: key, value\
Returns: nothing\
This method should hash the key, and set the key and value pair \
in the table, handling collisions as needed.
Should a given key already exist, \
replace its value from the value argument given to this method.

### get
Arguments: key\
Returns: Value associated with that key in the table

### contains
Arguments: key\
Returns: Boolean, indicating if the key exists in the table already.\
keys\
Returns: Collection of keys

### hash
Arguments: key\
Returns: Index in the collection for that key


## Approach & Efficiency
The Hashtable is O(1) in the best case, But this isnt normally the case. But a hashtables efficiency is tied to
the types of data stored. Since we are beholden to their efficiency as well.


