# itcodegroup-internship

---

## Installation

Before installation, make sure that you have [Python](https://www.python.org/) installed.

1. Clone this repository:
    ``` bash
    git clone https://github.com/ratushnyyvm/itcodegroup-internship.git && cd itcodegroup-internship
    ```

2. Install the program:
   ``` bash
   make setup
   ```

---

## Development

### Dependencies

- python = "^3.11"
- flake8 = "^6.0.0"
- numpy = "^1.24.2"
- pytest = "^7.3.0"

### Makefile Commands

| Command        | Description                              |
|----------------|------------------------------------------|
| `make venv`    | Create and activate virtual environment. |
| `make install` | Install all dependencies of the package. |
| `make lint`    | Check code with flake8 linter.           |
| `make test`    | Run tests.                               |
| `make setup`   | `make venv` + `make install`             |
