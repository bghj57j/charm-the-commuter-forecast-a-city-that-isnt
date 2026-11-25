# Writes the one-line weather forecast to /output/entry.txt, deterministically.
# No network, no randomness: every run writes the same bytes.
# Forecast register for a city that does not exist: sideways rain.
# One concrete detail (sideways rain at 40 km/h) makes it feel like a place.
import os
LINE = "Today in Sideways Falls: sideways rain at 40 km/h. Umbrellas are decorative; bring a raincoat and low expectations."
out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(LINE)  # same output on every run; entry is 115 chars, gate allows 140
