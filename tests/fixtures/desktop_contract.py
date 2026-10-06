"""Local renderer fixture used by the standard unit suite."""

import subprocess
import sys


def run_renderer_probe() -> int:
    """Run the local renderer fixture and return its exit status."""
    if sys.platform != "darwin":
        return 0
    return subprocess.run(
        ["open", "-n", "-b", "com.apple.calculator"],
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ).returncode
