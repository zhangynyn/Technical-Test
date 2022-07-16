# Runtime versions
Python 3.9.5


# How to run command
- Navigate to /Technical Test/ folder
- Run command `python app.py <number_of_items> <unit_price> <province>`
    + the value of `number_of_items` should be non-negative integer
    + the value of `unit_price` should be non-negative float
    + the value of `province` should be on of `AB`, `ON`, `QC`, `MI`

Here are a few examples:

```
python app.py 500 1.00 ON
>>> $565.00
```

```
python app.py 3600 2.25 MI
>>> $7984.98

```

# How to run unit tests
- Navigate to /Technical Test/ folder
- RUN `python -m unittest test_app.py`
