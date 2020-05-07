
# python skills

- data struct in data struct
- reversed(range(5)):

## from collections import OrderedDict

- index
- from collections import Counter
- cnt = Counter([iterable-or-mapping])
- cnt.elements() # All elements
- cnt.most_common() # Specify a parameter n, - - list the first n elements, and list all without specifying parameters
- cnt.subtract([iterable-or-mapping]) # Subtract the original element from the new element
- cnt.update([iterable-or-mapping])

## string

- join(iterable)
- replace(old, new[, count])
- count(sub[, start[, end]])
- startswith(prefix[, start[, end]])
- endswith(suffix[, start[, end]])
- s[0:i] without i

## List

- l.sort(\*, key=None, reverse=False)
- l.append(val) # It can also be lst = lst + [val]
- l.clear()
- l.count(val)
- l.pop(val=lst[-1])
- l.remove(val)
- l.reverse()
- l.insert(i, val)

## import random

- choice random.choice(d.keys())
- random.randrange(10))

# defaultdict

d = collections.defaultdict(list) //value of key beg=come list
for key, value in ditems():
d[k].append(v) (for list in value in Dict)

- list(d.items())
- [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
- students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
- sorted(students, key=lambda s: s[2])
- d = {'a': 'zapple', 'b': 'aberry', 'c': 'qcherry'}
- ds = sorted(d.items(), key=lambda x: x[1])
  map-> key ->string int tuple

## from collections import deque

- queue = deque([iterable[, maxlen]])
- queue.append(val) # Add an element to the right
- queue.popleft()
- queue.reverse() # Queue reversal
- queue.remove(val) # Delete the specified element
- queue.appendleft(val) # Add an element to the left
- queue.clear() # ClearQueue
- queue.count(val) # Returns the number of occurrences of

- set(str)
- add(elem) # Adding data to a collection
- update(\*others) # Increasing iteratively
- clear() # Empty Set
- discard(elem)

- import collections
- s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

## Java vs Python

Java programming is statically typed means that one has to explicitly mention the data type of variable if datatype (int, float, double, character) does not mention then the error will occur in the program.
Python is dynamically typed means one has directly assigned a value to a variable at the runtime it will assume data type.
create class before you do anything

fast speed then java need JVM which is portable allow it to run on many different device , python is an interpreter and it will assume data type of a variable at runtime due to which it becomes slower than java.

Java architecture: -JVM (Java Virtual Machine) is an engine that gives a runtime environment to operate the Java Code. It turns Java bytecode into machine language. JVM is a chunk of JRE (Java Run Environment).

