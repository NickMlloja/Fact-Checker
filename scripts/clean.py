import subprocess


def format():
    # Format using Black

    print("Formatting with Black...")
    result = subprocess.run(
        ["poetry", "run", "black", "--quiet", "scripts", "src"],
        stderr=subprocess.PIPE,
    )
    if result.stderr:
        print(result.stderr.decode())
    else:
        print("Formatting Completed\n")


def lint():
    # Lint using Flake8

    print("Linting with Flake8...")
    result = subprocess.run(
        ["poetry", "run", "flake8", "scripts", "src"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.stderr:
        print(result.stderr.decode())
    else:
        output = result.stdout.decode()
        print(output, end="")
        print("Linting Completed\n")


if __name__ == "__main__":
    format()
    lint()
