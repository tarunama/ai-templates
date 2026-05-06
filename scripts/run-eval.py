#!/usr/bin/env python3
"""Summarize AI evaluation cases from a Markdown table.

The script is intentionally dependency-free so agents can run it before opening a PR
and paste the Markdown output into the PR's evaluation section.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

REQUIRED_SECTIONS = [
    "## 1. 評価概要",
    "## 2. 評価実行情報",
    "## 3. 評価指標",
    "## 4. テストケース",
    "## 5. 総合結果",
    "## 6. 次アクション",
]

PASS_VALUES = {"pass", "passed", "ok", "成功", "合格", "○", "✅"}
FAIL_VALUES = {"fail", "failed", "ng", "失敗", "不合格", "×", "❌"}
PENDING_VALUES = {"pending", "todo", "未実施", "未評価", "保留", "-", "—"}


@dataclass
class EvalSummary:
    eval_file: str
    total_cases: int
    passed: int
    failed: int
    pending: int
    pass_rate: float | None
    missing_sections: list[str]
    status: str


def normalize_cell(value: str) -> str:
    value = value.strip().strip("`*").lower()
    value = re.sub(r"\s+", " ", value)
    return value


def split_markdown_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def iter_test_rows(lines: list[str]) -> Iterable[dict[str, str]]:
    in_table = False
    headers: list[str] = []

    for line in lines:
        if line.startswith("## 4. テストケース"):
            in_table = True
            continue
        if in_table and line.startswith("## "):
            break
        if not in_table or not line.lstrip().startswith("|"):
            continue

        cells = split_markdown_row(line)
        if not cells:
            continue
        if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            continue
        if not headers:
            headers = cells
            continue
        if len(cells) != len(headers):
            continue
        yield dict(zip(headers, cells))


def classify_result(value: str) -> str:
    normalized = normalize_cell(value)
    if not normalized:
        return "pending"
    if normalized in PASS_VALUES:
        return "passed"
    if normalized in FAIL_VALUES:
        return "failed"
    if normalized in PENDING_VALUES:
        return "pending"
    return "pending"


def evaluate(eval_file: Path, allow_template: bool) -> EvalSummary:
    text = eval_file.read_text(encoding="utf-8")
    lines = text.splitlines()
    missing_sections = [section for section in REQUIRED_SECTIONS if section not in text]

    rows = list(iter_test_rows(lines))
    result_column = next(
        (
            header
            for header in rows[0].keys()
            if "判定" in header or normalize_cell(header) in {"result", "status"}
        ),
        None,
    ) if rows else None

    counts = {"passed": 0, "failed": 0, "pending": 0}
    for row in rows:
        result = classify_result(row.get(result_column, "") if result_column else "")
        counts[result] += 1

    total_cases = len(rows)
    completed = counts["passed"] + counts["failed"]
    pass_rate = round((counts["passed"] / completed) * 100, 2) if completed else None

    if missing_sections:
        status = "fail"
    elif counts["failed"]:
        status = "fail"
    elif total_cases == 0 or counts["pending"]:
        status = "warning" if allow_template else "fail"
    else:
        status = "pass"

    return EvalSummary(
        eval_file=str(eval_file),
        total_cases=total_cases,
        passed=counts["passed"],
        failed=counts["failed"],
        pending=counts["pending"],
        pass_rate=pass_rate,
        missing_sections=missing_sections,
        status=status,
    )


def render_markdown(summary: EvalSummary) -> str:
    pass_rate = "未算出" if summary.pass_rate is None else f"{summary.pass_rate:.2f}%"
    lines = [
        "## 評価結果",
        "",
        f"- 評価ファイル: `{summary.eval_file}`",
        f"- ステータス: `{summary.status}`",
        f"- 合計ケース数: {summary.total_cases}",
        f"- Pass / Fail / Pending: {summary.passed} / {summary.failed} / {summary.pending}",
        f"- Pass率: {pass_rate}",
    ]
    if summary.missing_sections:
        lines.append(f"- 不足セクション: {', '.join(summary.missing_sections)}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="評価ケースMarkdownからPR貼り付け用の評価結果を生成します。")
    parser.add_argument("--eval-file", default="docs/templates/eval-cases.md", help="評価ケースMarkdownのパス")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown", help="出力形式")
    parser.add_argument(
        "--allow-template",
        action="store_true",
        help="未記入テンプレートやPendingが残る場合も警告扱いで終了コード0にします。",
    )
    args = parser.parse_args()

    eval_file = Path(args.eval_file)
    if not eval_file.exists():
        print(f"評価ファイルが見つかりません: {eval_file}", file=sys.stderr)
        return 2

    summary = evaluate(eval_file, args.allow_template)
    if args.format == "json":
        print(json.dumps(asdict(summary), ensure_ascii=False, indent=2))
    else:
        print(render_markdown(summary))

    if summary.status == "pass":
        return 0
    if summary.status == "warning" and args.allow_template:
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
