# GitHub Action for pytest

This GitHub Action allows you to run pytest and output [GitHub Job Summaries](https://github.blog/2022-05-09-supercharging-github-actions-with-job-summaries/). For creating the job summaries, this action uses [pytest-md](https://github.com/hackebrot/pytest-md) and [pytest-emoji](https://github.com/hackebrot/pytest-emoji).

```yaml
- name: Run pytest
  uses: pavelzw/pytest-action@v1
  with:
    verbose: true
    emoji: true
    job_summary: true
    custom_arguments: '-q'
```

You need to have Python installed in your pipeline before you can run this action.

If you want to change the time zone of the job summary, you may want to use the [szenius/set-timezone](https://github.com/marketplace/actions/set-timezone) action:
```yaml
- name: Set timezone
  uses: szenius/set-timezone@v1
  with:
    timezone: 'Europe/Berlin'
```

When `job_summary` is set to `true`, the action will output a Job Summary.
![Example Job Summary](https://user-images.githubusercontent.com/29506042/170843320-2bb104c5-5284-4fff-a83c-525da58a1a7f.png)

## Example Usage

```yaml
name: Run Python tests

on: [push]

jobs:
  build:
    name: Run tests
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.6", "3.7", "3.8", "3.9"]

    steps:
      - uses: szenius/set-timezone@v1.0
        with:
          timezoneLinux: "Europe/Berlin"
      - uses: actions/checkout@v3
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v3
        with:
          python-version: ${{ matrix.python-version }}
      - uses: pavelzw/pytest-action@test
        with:
          emoji: false
          verbose: false
          job_summary: true
```
