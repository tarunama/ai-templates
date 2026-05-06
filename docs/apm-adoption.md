# APM導入 Phase 0 調査

## 目的
Microsoft APM（Agent Package Manager）をこのリポジトリへ導入できるかを、設定追加前に確認します。

## 参照情報
- 参照URL: <https://github.com/microsoft/apm>
- 確認日: 2026-05-06
- 確認時点の最新リリース表示: v0.12.2（2026-05-05）

## Phase 0 の範囲
Phase 0 では、APMの実設定ファイルはまだ追加せず、導入可否と制約を整理します。

| 観点 | 確認結果 | 初期判断 |
|---|---|---|
| 目的適合性 | APMはエージェント設定を `apm.yml` と lockfile で再現可能にするツールです。 | このリポジトリのテンプレート運用と相性があります。 |
| 導入単位 | instructions、skills、prompts、plugins、MCP servers などを管理できます。 | 初期導入では外部依存を追加しない方針にします。 |
| 再現性 | `apm.lock.yaml` に解決済み依存関係を固定できます。 | Phase 1 で lockfile を生成し、管理対象にするか確認します。 |
| セキュリティ | install / audit による内容検査や、MCP server の信頼境界が用意されています。 | MCP は許可基準を決めるまで追加しません。 |
| CI連携 | CIでの audit 利用が想定されています。 | Phase 0 では追加せず、Phase 4 で判断します。 |

## このリポジトリでの導入方針
1. 既存の `AGENTS.md`、`README.md`、`docs/templates/` 配下のテンプレート運用を優先します。
2. Phase 1 では、外部packageやMCP serverを含まない最小 `apm.yml` を検討します。
3. `apm.lock.yaml` は、生成内容と差分が安定することを確認してからコミット対象にします。
4. APM関連ファイルを変更した場合は、`docs/templates/change-log.md` に `APM/AgentConfig` または `Docs` として記録します。
5. CIへの組み込みは、ローカル検証が安定してから判断します。

## Phase 1 実装結果
- 最小 `apm.yml` をリポジトリ直下に追加しました。
- 外部APM packageとMCP serverは追加していません。
- `apm_modules/` は生成物として `.gitignore` に追加しました。
- `apm.lock.yaml` は、APM CLIで `apm install` が安定して成功した後に生成差分を確認してコミットします。

## Phase 1 検証結果
| 項目 | 結果 | 補足 |
|---|---|---|
| APM CLI導入手順 | 完了 | 公式手順は `curl -sSL https://aka.ms/apm-unix \| sh` または `pip install apm-cli` です。 |
| 最小manifest | 完了 | `apm.yml` に空の `dependencies.apm` と `dependencies.mcp` を定義しました。 |
| 外部依存なしの検証 | 一部未完了 | この環境ではPyPIへの接続がプロキシ制限で失敗したため、APM CLI実行は未完了です。 |
| lockfile方針 | 完了 | `apm.lock.yaml` はCLI実行成功後に生成し、レビュー対象にします。 |

## Phase 2 実装結果
- READMEにAPMの位置づけ、初回セットアップ手順、関連ファイル更新ルールを追加しました。
- `docs/templates/README.md` に、APM利用時も既存テンプレート利用順を優先する補足を追加しました。
- Phase 2では外部package、MCP server、CI設定は追加していません。

## Phase 2 運用ルール
| 対象 | ルール |
|---|---|
| 既存テンプレート | `docs/templates/README.md` の利用順を優先します。 |
| `apm.yml` | 変更時は `apm install --dry-run` と `apm install` の確認を行います。 |
| `apm.lock.yaml` | 生成または更新された場合は差分を確認し、再現性のためにコミット対象にします。 |
| 外部依存/MCP | Phase 3の安全基準が完了するまで追加しません。 |
| 変更履歴 | `docs/templates/change-log.md` に `APM/AgentConfig` または `Docs` として記録します。 |

## Phase 1以降のIssue下書き
Phase 1以降の作業は、GitHub Issueとして登録できるよう `docs/issues/` に分割して管理します。

- Phase 1: `docs/issues/apm-phase-1-poc.md`
- Phase 2: `docs/issues/apm-phase-2-docs.md`
- Phase 3: `docs/issues/apm-phase-3-safety.md`
- Phase 4: `docs/issues/apm-phase-4-ci.md`
- Phase 5: `docs/issues/apm-phase-5-rollout.md`

## 未決事項
- `apm.yml` にこのリポジトリ固有の instructions をどこまで含めるか。
- Codex、GitHub Copilot、Claude Code など複数エージェント向けの出力をどこまでサポートするか。
- `apm audit --ci` を必須チェックにするか、警告運用から始めるか。
