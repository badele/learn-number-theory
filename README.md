# number-theory
The number theory

## Theory

### Prime numbers (nb divisors)
- [A008578](https://oeis.org/A008578) A number has two divisors is a prime number
- [](https://oeis.org/) A number has odd divisors, contain primary number

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
