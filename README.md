# itcodegroup-internship

---

## Description

| directory   | keywords             |
|-------------|----------------------|
| `lesson_2/` | git, issue, PR, MR   |
| `lesson_3/` | types, functions     |
| `lesson_4/` | aiogram bot          |
| `lesson_5/` | html, css, bootstrap |
| `lesson_6/` | django, ORM          |

---

## Installation

Before installation, make sure that you have [Python](https://www.python.org/) installed.

1. Clone this repository:
    ``` bash
    git clone https://github.com/ratushnyyvm/itcodegroup-internship.git && cd itcodegroup-internship
    ```

2. Create virtual environment:
   ``` bash
   python -m venv venv
   ```

3. Activate virtual environment:
   ``` bash
   source venv/bin/activate
   ```

4. Install all dependencies of the package:
   ``` bash
   make install
   ```

---

## Development

### Dependencies

- python = "^3.11"
- flake8 = "^6.0.0"
- pytest = "^7.3.0"

_lesson_2/_
- numpy = "^1.24.2"

_lesson_4/_
- aiogram = "^2.25.1"
- python-dotenv = "^1.0.0"
- requests = "^2.28.2"

_lesson_6/_
- Django = "^4.2"
- django-taggit = "^3.1.0"



### Makefile Commands

| Command        | Description                              |
|----------------|------------------------------------------|
| `make install` | Install all dependencies of the package. |
| `make lint`    | Check code with flake8 linter.           |
| `make test`    | Run tests.                               |
