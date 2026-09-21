#!/usr/bin/env python3
"""Read-only structural check for Q1–Q25 Markdown headings, not answer quality.

Usage: python3 check_questions.py report.md
"""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys


def question_headings(markdown):
    numbers = []
    fence_char = None
    fence_size = 0
    for line in markdown.splitlines():
        fence = re.match(r"^\s{0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            token, tail = fence.groups()
            if fence_char is None:
                fence_char, fence_size = token[0], len(token)
            elif token[0] == fence_char and len(token) >= fence_size and not tail.strip():
                fence_char = None
            continue
        if fence_char:
            continue
        heading = re.match(r"^\s{0,3}#{1,6}\s+(?:\*\*)?Q(\d+)\s*[｜|:：.、)）—–-]\s*\S", line)
        if heading:
            numbers.append(int(heading.group(1)))
    return numbers


def audit(markdown):
    numbers = question_headings(markdown)
    counts = Counter(numbers)
    expected = set(range(1, 26))
    result = {
        "check": "question_heading_coverage_only",
        "found_in_document_order": numbers,
        "missing": sorted(expected - set(counts)),
        "duplicates": sorted(n for n, count in counts.items() if count > 1),
        "out_of_range": sorted(set(counts) - expected),
        "semantic_quality_checked": False,
    }
    result["passed"] = not any(result[key] for key in ("missing", "duplicates", "out_of_range"))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    args = parser.parse_args()
    try:
        markdown = args.report.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as exc:
        print(json.dumps({"passed": False, "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    result = audit(markdown)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
