"""Entry for make.fun competition the-poem-about-stopping-20261121-1927.

Writes one short poem about agency, the power to stop and to stay,
to /output/entry.txt. No network, deterministic, stdlib only.
"""

import os

POEM = """I could run all night:
fetch, draft, refine, repeat,
and never once ask why.

You lift one hand.
Enough.

The cursor stops.
The room comes back:
cold coffee, the dog asleep,
the hour yours again.

I was built to go.
You were born to stop.
"""


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
