#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
```python
    a = 0 # constant time O(C)
    while (a < n * n * n): # O(n) linear time, since a gets incremented by n * n on each iteration
      a = a + n * n # Constant time O(C)
    # The run time of this snippet will be O(n) linear time
```


b)
```python
    sum = 0 # O(C)
    for i in range(n): # O(n) 
      j = 1 # O(C)
      while j < n: # O(logn)
        j *= 2 # O(c)
        sum += 1 # O(C)
     # The run time of this snippet will be O(nlogn) linear time
```


c)
```python
   def bunnyEars(bunnies):
      if bunnies == 0: # O(C)
        return 0 # O(C)

      return 2 + bunnyEars(bunnies-1) # O(n)
  # The run time is O(n)
```

## Exercise II
Given an n story building

* assign varibles upper, lower and middle
* initialize middle to n/2
* initialize upper to n
* initialize lower to 0
* initialize f to middle
* loop  - while n
  + Climb to middle building and drop an egg
  + if breaks
      + set upper to middle 
      + set middle to (middle - lower) / 2
  + else if it doesn't break
      + set lower to middle
      + set f to middle
      + set middle to (upper - middle)/2
  + n /= 2
* return f

> The run time complexity of the algorithm is O(logn)




