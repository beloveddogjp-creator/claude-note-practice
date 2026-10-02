# Claude Code /rewindの確認用サンプル

2026-10-02確認。架空の文章と標準Pythonによる比較だけを収録しています。
Claude Codeの対話実行・推敲・巻き戻しは未実施です。CLIの確認は2.1.278のバージョン表示まで。
必要環境はPython 3と、すでにセットアップしたClaude Code。料金やアカウント条件は読者の環境に従います。

ZIPを新しい空のフォルダへ展開し、rewind-practiceフォルダでターミナルを開きます。
既存の原稿や設定のあるフォルダへ重ねて展開しないでください。

```bash
cp -n draft.md draft.before.md
claude
```

draft.before.mdが既にある場合は続行せず、新しい展開先でやり直します。
Claude Codeで次の依頼文を送ります。

```text
draft.mdの「作業を行う」を2か所とも「作業をする」へ置き換えてください。
組み込みのファイル編集ツールでdraft.mdだけを変更してください。
Bash、別のagent、スキルは使わず、expected.mdとdraft.before.mdは変更しないでください。
それ以外の文字と改行は保ってください。
```

別のターミナルを同じフォルダで開いて確認します。

```bash
python3 check_files.py edited
```

一致しなければ、その状態を確認してから巻き戻しの練習へ進みます。エラーは成功にしません。
Claude Codeで/rewindを入力し、編集を頼んだpromptを選び、Restore codeを選びます。
追跡対象の変更がなければRestore codeは表示されません。Restore conversationだけではファイルは戻りません。

```bash
python3 check_files.py restored
```

PASSならdraft.mdと手元の変更前コピーが一致しています。これだけで外部処理の取り消しや長期バックアップは保証しません。
Bashが行ったファイル変更、外部の公開操作、symlink/hardlinkは巻き戻せる対象として扱いません。
通常の独立したファイルを、別の同時セッションから編集しない条件で試してください。
元原稿を守るには別の保存先やGitの履歴も用意します。

一次資料: https://code.claude.com/docs/en/checkpointing
