# drills

Interview practice problems in Python, with pytest tests.

- `code/<category>/<problem>.py` — solutions, tested by `test/<category>/test_<problem>.py`
- `code/<category>/<problem>_solutions/` — alternate solutions for a problem
- `misc/algo_experts/` — AlgoExpert problems, each with its own `code/` and `test/`

## Running tests

```sh
pytest                                            # everything
pytest test/hashing                               # one category
pytest test/hashing/test_two_number_sum_map.py    # one problem
```

## Drilling

```sh
./drill.sh                               # list problems
./drill.sh random                        # pick a random problem and start it
./drill.sh hashing/two_number_sum_map    # stub the solution and show its tests
python3 code/hashing/two_number_sum_map.py   # run it with the first example from the tests
./drill.sh test hashing/two_number_sum_map   # run its tests
./drill.sh show hashing/two_number_sum_map   # print the saved solution
./drill.sh reset hashing/two_number_sum_map  # restore the solution
./drill.sh reset-all                     # restore every solution
```
