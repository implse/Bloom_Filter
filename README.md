# Bloom Filter : Probabilistic Data Structures

A `Bloom Filter` is a space efficient probabilistic data structure, conceived by Burton Howard in 1970.

It is used to quickly check whether or not an element is a member of a set.

The probabilistic nature of `Bloom Filter` means, there might be some `False positive`.

When you look up an element in a `Bloom Filter`, the possible answer are:

  - It's definitely not in the set. `True negative`
  - It might be in the set. `False positive` or `True positive`

We can control the probability of getting a `False positive` by controlling the size of the `Bloom Filter`.

More space means fewer `False positive`.

The base data structure of a `Bloom filter` is a `Bit Vector`.

Useful in cases:

- the data to be searched is large.

- the memory available on the system is limited/ low.

#### Strengths
  - Space efficient : `Bloom Filter` takes `O(1)` space, regardless of the number of elements inserted. (Accuracy goes down as more elements are added)

  - Fast : Insert and Lookup operations are both `O(1)` time.

#### Weakness
  - Probabilistic : `Bloom Filter` can only definitively identify True negative, they cannot identify True positives. (False positive or True positive)

  - Limited Interface : `Bloom Filter` only support the insert and lookup operations. You can't iterate through the items in the set or delete items.


#### Applications

- Weak password detection
- Internet Cache Protocol
- Safe browsing in Google Chrome
- Wallet synchronization in Bitcoin
- Hash based IP Traceback
- Cyber security like virus scanning
