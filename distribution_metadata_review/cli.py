"""Command-line entry point for distribution metadata review."""

from .report import build_report


def main() -> int:
    report = build_report(
        name="distribution-metadata-review",
        version="1.1.0",
        python_requires=">=3.9",
        dependencies=(),
        scripts=("dist-meta-review",),
        classifiers=(
            "Programming Language :: Python :: 3",
            "Topic :: Software Development :: Quality Assurance",
        ),
    )
    print("\n".join(report.lines()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
