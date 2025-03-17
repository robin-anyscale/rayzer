# Rayzer

Rayzer is an interactive CLI tool for Ray cluster and job management.

## Quick Installation

Install and run Rayzer with a single command:

```bash
curl -sSL https://raw.githubusercontent.com/robin-anyscale/rayzer/main/install.sh | bash -s -- --run
```

Or install without running immediately:

```bash
curl -sSL https://raw.githubusercontent.com/robin-anyscale/rayzer/main/install.sh | bash
```

## Features

- Launch Ray jobs
- Create Ray services
- Deploy Ray clusters locally, on AWS, or on Anyscale

## Requirements

- Python 3.9 or higher
- Bash shell
- Git (for installation)

## Manual Installation

If you prefer to install manually:

1. Clone this repository: `git clone git@github.com:robin-anyscale/rayzer.git`
2. Change to the repository directory: `cd rayzer`
3. Create a virtual environment: `uv venv`
4. Install dependencies: `uv pip install typer questionary`
5. Run the application: `python main.py rayzer`

## License

[Add your license information here]
