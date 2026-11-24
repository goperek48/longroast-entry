#!/usr/bin/env python3
"""Long Roast entry: a single satirical sentence about the people who legislate
AI, crypto and the internet while tripping over the humblest task in computing.

The program itself is intentionally unremarkable. All of the craft sits in
the sentence it emits; the code just carries it to /output/entry.txt intact.
One sentence, no extra lines, no trailing newline, no decoration. The joke
is built as a reversal: the subject starts out holding genuine authority
over the technology, and the sentence then strips that authority away with
a routine office chore he cannot perform.
"""

import os
import sys

# The sentence itself: a single sentence of 202 characters, comfortably
# under the 320-character gate. The opening grants the man real authority
# (he runs the AI committee, he signs the bills that govern what chatbots
# may say); the close yanks it away (asked for a PDF, he sends his
# assistant a photograph of a Word document). The sting is in the final
# words, and the screenshot detail is concrete enough to feel observed
# rather than invented.
SENTENCE = (
    "He chairs the committee on artificial intelligence, signs bills that "
    "decide what your chatbot may say, and still emails his assistant a "
    "screenshot of a Word document whenever someone asks him for a PDF."
)


def main() -> int:
    """Write the sentence to /output/entry.txt and exit 0."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
