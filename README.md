![Unit tests](https://github.com/meanthadar-p/hackerRank/workflows/Unit%20tests/badge.svg)
# HackerRank
Amount
```
EASY: 6
MEDIUM: 2
```


# Unit Tests
using pytest library https://docs.pytest.org/en/stable/

``` 
$ pytest
============================= test session starts ==============================
platform linux -- Python 3.8.3, pytest-5.4.3, py-1.8.2, pluggy-0.13.1
rootdir: /home/runner/work/hacker-rank-practice/hacker-rank-practice
collected 33 items

Easy/CatsAndaMouse/test_CatsAndaMouse.py ...                             [  9%]
Easy/CountingValleys/test_CountingValleys.py ..                          [ 15%]
...
lib/QuickSort/test_QuickSort.py ..                                       [100%]

============================== 33 passed in 0.12s ==============================
```

please aware
1. Verify that all files with test cases start with 'test_' word.
2. Verify that all test cases names also start with 'test_' word.


### Noted
```
[WARN] couldn't commit pytest_cache folder or init.py files, it make unit tests failure when run with git actions.
```
