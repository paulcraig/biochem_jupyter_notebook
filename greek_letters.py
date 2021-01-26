"""
Short cut for Greek letters
"""

_lowercase = [chr(x) for x in range(945, 970)]
_uppercase = [chr(x) for x in range(913, 938)]

_lowercase_names = [
    "alpha",
    "beta",
    "gamma",
    "delta",
    "epsilon",
    "zeta",
    "eta",
    "theta",
    "iota",
    "kappa",
    "Lambda",
    "mu",
    "nu",
    "xi",
    "omicron",
    "pi",
    "rho",
    "sigma_alt",
    "sigma",
    "tau",
    "upsilon",
    "phi",
    "chi",
    "psi",
    "omega"
]

_uppercase_names = [x.upper() for x in _lowercase_names]

for i in range(len(_lowercase_names)):
    vars()[f"{_lowercase_names[i]}"] = _lowercase[i]
    vars()[f"{_uppercase_names[i]}"] = _uppercase[i]
