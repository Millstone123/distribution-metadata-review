"""Deterministic metadata report construction."""

from dataclasses import dataclass
from typing import Iterable, Tuple


@dataclass(frozen=True)
class MetadataReport:
    name: str
    version: str
    python_requires: str
    dependency_count: int
    scripts: Tuple[str, ...]
    notes: Tuple[str, ...]

    def lines(self) -> Tuple[str, ...]:
        return (
            "name=%s" % self.name,
            "version=%s" % self.version,
            "python_requires=%s" % self.python_requires,
            "dependencies=%d" % self.dependency_count,
            "scripts=%s" % ",".join(self.scripts),
            "notes=%s" % ";".join(self.notes),
        )


def build_report(
    name: str,
    version: str,
    python_requires: str,
    dependencies: Iterable[str] = (),
    scripts: Iterable[str] = (),
    classifiers: Iterable[str] = (),
) -> MetadataReport:
    dependency_list = tuple(sorted(item.strip() for item in dependencies if item.strip()))
    script_list = tuple(sorted(item.strip() for item in scripts if item.strip()))
    classifier_list = tuple(sorted(item.strip() for item in classifiers if item.strip()))
    notes = []
    if not classifier_list:
        notes.append("no-classifiers")
    if not script_list:
        notes.append("no-console-scripts")
    return MetadataReport(
        name=name.strip(),
        version=version.strip(),
        python_requires=python_requires.strip(),
        dependency_count=len(dependency_list),
        scripts=script_list,
        notes=tuple(notes),
    )
