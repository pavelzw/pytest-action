# GitHub Action for pytest

This GitHub Action allows you to run `pytest` and output [GitHub Job Summaries](https://github.blog/2022-05-09-supercharging-github-actions-with-job-summaries/). For creating the job summaries, this action uses [pytest-md](https://github.com/hackebrot/pytest-md) and [pytest-emoji](https://github.com/hackebrot/pytest-emoji).

```yaml
- name: Run pytest
  uses: pavelzw/pytest-action@v1
  with:
    verbose: true
    emoji: true
    job-summary: true
    custom-arguments: '-q'
    click-to-expand: true
    report-title: 'Test Report'
```

You need to have Python as well as `pytest` installed in your pipeline before you can run this action. If `job-summary` is set to `true`, you also need to install `pytest-md`. If `emoji` is set to `true`, you need to install `pytest-emoji`.

If you want to change the time zone of the job summary, you may want to use the [szenius/set-timezone](https://github.com/marketplace/actions/set-timezone) action:
```yaml
- name: Set timezone
  uses: szenius/set-timezone@v1
  with:
    timezone: 'Europe/Berlin'
```

When `job-summary` is set to `true`, the action will output a Job Summary.
![Example Job Summary](https://user-images.githubusercontent.com/29506042/170843320-2bb104c5-5284-4fff-a83c-525da58a1a7f.png)

## Activating `conda` environments

This action uses `bash -l {0}` as the shell to run `pytest` in, 
i.e., the login shell that also sources your `.bashrc`. 
When using `bash` in GitHub Actions, it doesn't source your `.bashrc` by default. 
If you want to use a `conda` environment, you need to make sure to add it into your `.bashrc` s.t. 
the `conda` environment automatically gets activated. 
[mamba-org/provision-with-micromamba](https://github.com/mamba-org/provision-with-micromamba) 
does this automatically for you.

```bash
- uses: mamba-org/provision-with-micromamba@main
  with:
    environment-name: myenv
    channels: conda-forge
    environment-file: false
    extra-specs: |
      python=3.7
      pytest
      numpy
- run: pip install pytest-md pytest-emoji
  shell: bash -l {0}
- uses: pavelzw/pytest-action@v2
```

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
      - name: Install dependencies
        run: pip install pytest pytest-md pytest-emoji
      - uses: pavelzw/pytest-action@v2
        with:
          emoji: false
          verbose: false
          job-summary: true
```
