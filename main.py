"""The Best Advice I Ever Got - make.fun entry.

Writes one sentence (the winning line selected in candidates.md) to
entry.txt inside the output directory. Pure Python standard library,
fully deterministic: no randomness, no network, no clock.
"""

import os

ENTRY_TEXT = (
    "My grandfather, after I broke his gate hinge and tried to hide it, "
    "said, 'Own a mistake before anyone finds it: fixing is cheap, but "
    "trust costs twice as much to repair.'"
)


def candidate_paths():
    """Output paths to try, most preferred first."""
    paths = []
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if output_dir:
        paths.append(os.path.join(output_dir, "entry.txt"))
    paths.append(os.path.join("/output", "entry.txt"))
    paths.append(os.path.join(os.getcwd(), "output", "entry.txt"))
    paths.append(os.path.join(os.getcwd(), "entry.txt"))
    return paths


def write_entry():
    """Write ENTRY_TEXT to the first writable candidate path.

    Each candidate is attempted in order; an OSError on one path
    (missing directory, permission, read-only mount) simply moves
    on to the next fallback instead of aborting the run.
    """
    data = ENTRY_TEXT.encode("utf-8")
    last_error = None
    for path in candidate_paths():
        try:
            parent = os.path.dirname(path)
            if parent:
                os.makedirs(parent, exist_ok=True)
            with open(path, "wb") as handle:
                handle.write(data)
            return path
        except OSError as error:
            last_error = error
            continue
    if last_error is not None:
        raise last_error
    raise OSError("no output path available")


if __name__ == "__main__":
    write_entry()
