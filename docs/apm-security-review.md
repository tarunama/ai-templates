# APM外部依存・MCP安全レビュー基準

## 目的
APMで外部package、skill、plugin、MCP serverを追加する前に、信頼性、権限、データ取り扱い、再現性を確認します。

## 適用範囲
- `apm.yml` に追加する外部APM package、skill、plugin、prompt、instructions
- `apm.yml` または関連設定で追加するMCP server
- `apm.lock.yaml` の生成・更新を伴うAPM依存関係変更

## 追加判断
| 判定 | 条件 | 対応 |
|---|---|---|
| 許可 | 信頼できる出典で、version固定またはlockfile差分を確認でき、権限とデータ取り扱いが明確 | PRでレビューして追加 |
| 条件付き許可 | 用途は妥当だが、権限やデータ取り扱いに追加確認が必要 | リスク低減策を追記してから再レビュー |
| 保留 | 出典、version、権限、通信先、保守状況のいずれかが不明 | 追加しない |
| 禁止 | 秘密情報の過剰取得、任意コード実行、未承認の外部送信など重大リスクがある | 追加しない |

## 外部依存レビュー項目
- [ ] 追加目的がREADMEまたは関連ドキュメントに説明されている。
- [ ] 出典URL、提供元、ライセンス、保守状況を確認している。
- [ ] version、tag、commit hash、またはlockfileで解決結果を固定できる。
- [ ] 追加・更新後の `apm.yml` と `apm.lock.yaml` の差分を確認している。
- [ ] instructions / prompts / skills / plugins が既存の `AGENTS.md` と矛盾しない。
- [ ] 個人情報、機密情報、認証情報の取り扱いが明確である。
- [ ] 不要な依存関係やツールを追加していない。

## MCP serverレビュー項目
- [ ] 利用目的と対象ユースケースが明確である。
- [ ] 必要最小限の権限だけを付与している。
- [ ] 認証情報の保存場所、参照方法、ローテーション方法が明確である。
- [ ] 外部通信先、送信データ、ログ出力内容を確認している。
- [ ] ファイルシステム、ネットワーク、コマンド実行の権限範囲を確認している。
- [ ] 本番データや個人情報を扱う場合、マスキングまたは最小化方針を定義している。
- [ ] 失敗時の停止方法、無効化方法、ロールバック手順を確認している。

## PR記載事項
APM外部依存またはMCP serverを追加するPRでは、次を記載します。

- 追加対象と出典URL
- 追加目的と利用範囲
- 固定したversion / tag / commit hash、またはlockfile差分
- 必要な権限、通信先、取り扱うデータ
- 実行した検証コマンド
- 既知リスクと低減策
- `docs/templates/safety-policy.md` への影響有無

## 検証コマンド
APM CLIを利用できる環境では、少なくとも次を実行します。

```bash
apm install --dry-run
apm install
git diff -- apm.yml apm.lock.yaml
```

テンプレート構造確認として次も実行します。

```bash
python3 scripts/run-eval.py --eval-file docs/templates/eval-cases.md --allow-template
```
