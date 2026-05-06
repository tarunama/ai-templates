# APM導入 Phase 1: 最小構成PoC

## 背景
Phase 0で整理した導入方針をもとに、既存のテンプレート運用を壊さない最小構成でAPMを検証します。

## スコープ
- 外部packageやMCP serverを追加しない最小 `apm.yml` の検討
- APM CLI のインストール方法と実行コマンドの確認
- `apm install` または同等の検証コマンドの実行
- `apm.lock.yaml` をコミット対象にするかの判断

## タスク
- [ ] APM CLI の導入手順を確認する
- [ ] 最小 `apm.yml` の候補を作成する
- [ ] 外部依存なしで検証コマンドを実行する
- [ ] lockfile の生成有無と差分を確認する
- [ ] 結果を `docs/apm-adoption.md` または README に反映する
- [ ] `docs/templates/change-log.md` に変更を記録する

## 完了条件
- [ ] 最小構成でAPMを利用できるか判断できている
- [ ] 既存の `AGENTS.md`、README、テンプレート利用順に影響がないことを確認している
- [ ] lockfile の管理方針が決まっている

## 依存関係
- Phase 0調査が完了していること
