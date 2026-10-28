#!/usr/bin/env python3
"""Optional example of text generation with the OpenAI Responses API.

This script was NOT used to generate the committed samples. It demonstrates an
API-based workflow for future experiments. Keep API credentials in the
OPENAI_API_KEY environment variable; never hard-code keys in source control.
"""

import os
import sys

try:
    from openai import OpenAI
except ImportError as exc:
    raise SystemExit(
        "The OpenAI SDK is missing. Install dependencies with: "
        "python -m pip install -r requirements.txt"
    ) from exc


def main() -> int:
    prompt = " ".join(sys.argv[1:]).strip()
    if not prompt:
        prompt = input("Enter a prompt: ").strip()
    if not prompt:
        print("Error: a non-empty prompt is required.", file=sys.stderr)
        return 2

    if not os.environ.get("OPENAI_API_KEY"):
        print(
            "Error: set OPENAI_API_KEY in your environment before using the API example.",
            file=sys.stderr,
        )
        return 2

    model = os.environ.get("OPENAI_MODEL", "gpt-6-luna")
    client = OpenAI()
    response = client.responses.create(model=model, input=prompt)
    print(response.output_text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
