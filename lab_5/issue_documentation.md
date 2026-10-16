\# Lab 5: Static Code Analysis — Issue Documentation



\## Issues Identified and Fixes Applied



| No. | Issue | Type | Original Line(s) | Description | Fix Approach |

|---:|---|---|---|---|---|

| 1 | Missing module docstring | Pylint — C0114 | 1 | The Python module did not have a descriptive docstring. | Added a module-level docstring describing the program. |

| 2 | Missing function docstrings | Pylint — C0116 | 11, 16, 19, 23, 33, 37, 45 | Functions did not explain their purpose. | Added descriptive docstrings to the functions. |

| 3 | Mutable default argument | Pylint — W0102 | 11 | Using `logs=\[]` as a default could cause data to be shared between calls. | Changed the default to `None` and initialized a new list inside the function. |

| 4 | String formatting | Pylint — C0209 | 13 | Regular string formatting could be simplified. | Used an f-string. |

| 5 | Bare exception handler | Pylint — W0702; Bandit — B110; Flake8 — E722 | 29 | A bare `except` with `pass` could silently hide errors. | Removed the silent exception handling and used explicit validation and error handling. |

| 6 | Function naming convention | Pylint — C0103 | 33 | `assignDriver` did not follow Python's snake\_case naming convention. | Renamed the function to `assign\_driver`. |

| 7 | Unused function argument | Pylint — W0613 | 33 | The `route\_id` argument was unused. | Used the route ID to validate that the requested route exists. |

| 8 | Global statement | Pylint — W0603 | 38 | The function modified global route data using a `global` statement. | Updated the existing route dictionary in place instead of rebinding the global variable. |

| 9 | Missing file encoding | Pylint — W1514 | 39, 42 | Files were opened without explicitly specifying an encoding. | Specified UTF-8 encoding. |

| 10 | File resource management | Pylint — R1732 | 39, 42 | File handles were not managed using a context manager. | Used `with` statements to open and close files safely. |

| 11 | Insecure random selection warning | Bandit — B311 | 35 | `random.choice` was flagged by Bandit. | Replaced it with `secrets.choice`. |

| 12 | Blank lines before functions | Flake8 — E302 | 11, 16, 19, 23, 33, 37, 45 | Functions did not have the required two blank lines before their definitions. | Corrected spacing between top-level definitions. |

| 13 | Line too long | Flake8 — E501 | 13 | A line exceeded the configured 79-character limit. | Split the line across multiple lines. |

| 14 | Blank lines after function definition | Flake8 — E305 | 60 | There was insufficient spacing after a function definition. | Corrected the spacing before the next top-level statement. |

| 15 | Empty route handling | Functional robustness | Not limited to one reported line | Averaging an empty trip list could cause a division-by-zero error. | Returned `0` when a route has no recorded trips. |

| 16 | Invalid or missing route handling | Functional robustness | Multiple locations | Unknown routes could cause lookup errors. | Added route validation and clear error messages. |

| 17 | Invalid passenger counts | Input validation | Trip logging function | Negative or non-integer passenger counts were not rejected. | Added validation for non-negative integer passenger counts. |



\## Validation Results



| Tool | Before | After |

|---|---|---|

| Pylint | Score: 6.25/10 | Score: 10.00/10 |

| Bandit | 2 reported issues | No issues identified |

| Flake8 | Multiple formatting issues | No findings |



\*Line numbers refer to the original script and baseline reports. Functional robustness items describe additional fixes in the updated code.\*



