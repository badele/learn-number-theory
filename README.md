# number-theory
The number theory

# Found during my personal analyzes (by order found)
- [A121326 - Primes of the form 4*k^2 + 1](https://oeis.org/A121326)
- [A002061 - Central polygonal numbers](https://oeis.org/A002061)
- [A001844 - Centered square numbers](https://oeis.org/A001844)
- [A272850 - Square sum numbers](https://oeis.org/A272850)
- [A017197 - a(n) = 9*n + 3](https://oeis.org/A017197)
- [A051369 - a(n+1) = a(n) + sum of digits of a(n)^2](https://oeis.org/A017197)
- [A007953 - Digital sum (i.e., sum of digits) of n; also called digsum(n).](https://oeis.org/A007953)
- [A010888 - Digital root of n (repeatedly add the digits of n until a single digit is reached)](https://oeis.org/A010888)

## Theory
- [A000040](oeis/A000040_prime_numbers.py) Compute a prime numbers
- [A000396](oeis/A000396_perfect_numbers.py) Compute a perfect numbers

## Cool theory
- Divisible by 3
  - Consecutive three number: 15,16,17 151617 is divisible by 3
  - Sum of digit % 3 == 0, the number is divisible by 3: ex 456 = 15, 15 is divisible by 3. Therefore 456 is divisible by 3

### Math tool
- [divisors](lib/math.py) Compute a divisors for a number
- [sum_divisors](lib/math.py) Compute a sum divisors for a number

## Install
```
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt

## Generate numbers

```
python pandas_numbers_generator.py -n 100
```

## Mesuring performance

```
time python3 A000396_perfect_numbers.py -n5
/usr/lib/python3.7/profile.py -s cumtime A000396_perfect_numbers.py -n5
```
