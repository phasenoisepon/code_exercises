```
$ cat results.txt
PASS
ERROR 70
ERROR 1
PASS
ERROR 325
ERROR 1
ERROR 1
ERROR 1
ERROR 70
PASS
```

> Parse the following log file, and present a report on which errors were seen 
and how many of each error."""

```python
def main()
    with open("results.txt") as file_handle:
        pass_count = 0
        error_count = {}
        lines = file_handle.readlines()
        for line in lines:
            if "PASS" in line:
                pass_count += 1
                pass
            if "ERROR" in line:
                split_line = line.split(' ')
                assert len(split_line)==2
                # get the error'ing test ID
                error_test = split_line[1]
                # attempt to get test from dict and add 1 to the value
                # if DNE, create that key in the dict and set value to 1
                if error_count.get(error_test) is None:
                    error_count.add(error_test, 1)
                else:
                    error_count.update(error_test, error_count[error_test]+1)
                    
    print("Test Summary: {} pass results".format(pass_count))
    print("Error Tests:")
    for (key,value) in error_count:
        print("Test Name: {test_id}, Fail Count:{fail_count}".format(test_id=key, fail_count=value))
    
    
if __name__ == "__main__":
    main()
```