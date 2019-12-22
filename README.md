# Bloom Filter : Probabilistic Data Structures

A Bloom Filter is a space efficient probabilistic data structure, conceived by Burton Howard in 1970.

It is used to quickly check wether or not an element is a member of a set.

The probabilistic nature of Bloom Filter means, there might be some False positive.

When you look up an element in a Bloom Filter, the possible answer are:
  - It's definitely not in the set. (True negative)
  - It might be in the set.(False positive or True positive)

We can control the probability of getting a False positive by controlling the size of the Bloom Filter.

More space means fewer False positive.
