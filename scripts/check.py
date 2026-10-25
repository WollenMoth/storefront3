"""Run the same release gates locally and in CI, using isolated test settings."""

import os
import subprocess
import sys
import tempfile
from pathlib import Path


def run(*args):
    print("+", " ".join(args), flush=True)
    subprocess.run(args, check=True)


def main():
    os.chdir(Path(__file__).resolve().parent.parent)
    os.environ["DJANGO_SETTINGS_MODULE"] = "storefront.settings.test"
    run("uv", "lock", "--check")
    run("uv", "pip", "check", "--python", sys.executable)
    run(sys.executable, "manage.py", "check")
    run(sys.executable, "manage.py", "makemigrations", "--check", "--dry-run")
    run(sys.executable, "-m", "pytest")
    # Include optional tooling as well as production dependencies in the audit.
    with tempfile.TemporaryDirectory(prefix="storefront-audit-") as directory:
        requirements = str(Path(directory) / "requirements.txt")
        run(
            "uv",
            "export",
            "--locked",
            "--all-groups",
            "--no-emit-project",
            "--output-file",
            requirements,
            "--quiet",
        )
        run(
            sys.executable,
            "-m",
            "pip_audit",
            "--strict",
            "--disable-pip",
            "--no-deps",
            "-r",
            requirements,
        )


if __name__ == "__main__":
    main()
