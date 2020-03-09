# number-theory
The number theory

## Theory
- [A000040](oeis/A000040_prime_numbers.py) Compute a prime numbers
- [A000396](oeis/A000396_perfect_numbers.py) Compute a perfect numbers

### Math tool
- [divisors](lib/math.py) Compute a divisors for a number
- [sum_divisors](lib/math.py) Compute a sum divisors for a number

## Install
```
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt

## Demonstration

```
python3 export_column.py -q "select * from numbers where nb_divisors=4' -c divisors -i 5

MAX_NB_DIVISORS=7
NB_DIVISORS=$(python3 export_column.py -q "select count(*) as count from numbers where nb_divisors=${MAX_NB_DIVISORS}" -c count)
python3 export_column.py -o list -q "select * from numbers where nb_divisors=2 limit ${NB_DIVISORS}" -c num
python3 export_column.py -o list -q "select * from numbers where nb_divisors=3 limit ${NB_DIVISORS}" -c divisors -i 1
python3 export_column.py -o list -q "select * from numbers where nb_divisors=5 limit ${NB_DIVISORS}" -c divisors -i 1
python3 export_column.py -o list -q "select * from numbers where nb_divisors=7 limit ${NB_DIVISORS}" -c divisors -i 1

python3 export_column.py -o list -q "select * from numbers where nb_divisors=2 limit ${NB_DIVISORS}" -c num
python3 export_column.py -o list -q "select * from numbers where nb_divisors=3 limit ${NB_DIVISORS}" -c num
python3 export_column.py -o list -q "select * from numbers where nb_divisors=5 limit ${NB_DIVISORS}" -c num
python3 export_column.py -o list -q "select * from numbers where nb_divisors=7 limit ${NB_DIVISORS}" -c num

sqlite3 nums.db ".head on" ".mode column" "select * from numbers limit 10"
```

## Mesuring performance

```
time python3 A000396_perfect_numbers.py -n5
/usr/lib/python3.7/profile.py -s cumtime A000396_perfect_numbers.py -n5
```
