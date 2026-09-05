#!/usr/bin/env python3
"""講座概要Markdownの必須見出しとタイムテーブル合計を検証する。"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_HEADINGS = [
    "講座の概要",
    "章構成",
    "タイムテーブル",
    "ポイント",
    "注意点",
]

BANNED_PROCESS_NOTES = [
    "PDFの構成をもとに、3時間枠へ仮配分しています",
    "受講生が操作する演習時間は、未確定の場合のみ5分を仮置きしています",
]


def clean_cell(value: str) -> str:
    return value.strip().replace("**", "").replace("`", "")


def parse_minutes(value: str) -> int | None:
    match = re.fullmatch(r"(\d+)分", clean_cell(value))
    return int(match.group(1)) if match else None


def timetable_lines(lines: list[str]) -> list[str]:
    start = next(
        (index for index, line in enumerate(lines) if line.strip() == "## タイムテーブル"),
        None,
    )
    if start is None:
        return []

    result: list[str] = []
    for line in lines[start + 1 :]:
        if line.startswith("## "):
            break
        result.append(line)
    return result


def validate(path: Path) -> tuple[list[str], list[str]]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    errors: list[str] = []
    warnings: list[str] = []

    positions: list[int] = []
    for heading in REQUIRED_HEADINGS:
        marker = f"## {heading}"
        matches = [index for index, line in enumerate(lines) if line.strip() == marker]
        if not matches:
            errors.append(f"必須見出しがありません: {marker}")
        else:
            positions.append(matches[0])
    if len(positions) == len(REQUIRED_HEADINGS) and positions != sorted(positions):
        errors.append("必須見出しの順序が正しくありません。")

    rows: list[list[str]] = []
    for line in timetable_lines(lines):
        stripped = line.strip()
        if not (stripped.startswith("|") and stripped.endswith("|")):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if len(cells) < 4 or all(set(cell) <= {"-", ":", " "} for cell in cells):
            continue
        rows.append(cells)

    if not rows:
        errors.append("タイムテーブルの表が見つかりません。")
    else:
        durations: list[int] = []
        declared_total: int | None = None
        for cells in rows[1:]:
            if "合計" in clean_cell(" ".join(cells)):
                declared_total = parse_minutes(cells[-1])
                continue
            minutes = parse_minutes(cells[-1])
            if minutes is not None:
                durations.append(minutes)

        if declared_total is None:
            errors.append("タイムテーブルの合計時間が見つかりません。")
        elif sum(durations) != declared_total:
            errors.append(
                f"タイムテーブルの行合計{sum(durations)}分と記載合計{declared_total}分が一致しません。"
            )

        course_hours = re.search(r"講座時間：\s*(\d+)時間", text)
        if course_hours and declared_total is not None:
            expected = int(course_hours.group(1)) * 60
            if declared_total != expected:
                errors.append(
                    f"講座時間{expected}分とタイムテーブル合計{declared_total}分が一致しません。"
                )

    provisional = re.findall(r"（演習・仮：\d+分）", text)
    if provisional:
        warnings.append(f"未確定の演習時間が{len(provisional)}件あります。")

    for phrase in BANNED_PROCESS_NOTES:
        if phrase in text:
            errors.append(f"成果物へ載せない作業過程の注記が含まれています: {phrase}")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("markdown", type=Path, help="検証する講座概要Markdown")
    args = parser.parse_args()

    if not args.markdown.is_file():
        print(f"ERROR: ファイルが見つかりません: {args.markdown}", file=sys.stderr)
        return 2

    errors, warnings = validate(args.markdown)
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)

    if errors:
        return 1
    print("OK: 必須見出しとタイムテーブルを確認しました。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
