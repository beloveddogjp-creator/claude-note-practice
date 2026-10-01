# Claude Codeの権限を確認する練習用サンプル

2026-10-02 JSTの公式資料を基にした独自の練習例です。公式配布物ではありません。
Claude Codeをインストール・ログイン済みで、Python 3が使える方向けです。架空の文章だけを入れています。

## 準備

[ZIP](https://github.com/beloveddogjp-creator/claude-note-practice/raw/refs/heads/main/claude-permission-practice.zip)を展開します。GitHubの画面が開いた場合はView rawからダウンロードします。
他の仕事のフォルダへ混ぜず、展開したclaude-permission-practiceフォルダをターミナルで開きます。上位のCLAUDE.md、個人設定、組織の設定等の影響が残る場合はあります。

サンプルのsettings.example.jsonは、置いただけでは適用されません。次の操作は自分で行います。既に.claude/settings.local.jsonがある場合はコピーで上書きせず、内容を比較し、必要な設定だけを手作業で合わせます。

```sh
python3 -m json.tool settings.example.json
mkdir -p .claude
cp settings.example.json .claude/settings.local.json
```

新しい練習フォルダにだけコピーしてください。実際の仕事の設定を置き換える手順ではありません。
.claudeは隠しフォルダです。エディタで開くと確認できます。settings.local.json.txtのような名前にしないでください。
.gitignoreは個人設定を追跡しないための行だけを含みます。実際にgitで追跡済みのファイルを自動で解除するものではありません。

## 開く画面

このフォルダでclaudeを開始し、Claude Code内で次を入力します。

```text
/permissions
```

AskにEditとBashがあり、どの設定ファイルに由来するかを見ます。起動モードも確認します。この例はdefault（Manual）を前提にしています。組織の管理設定がある場合はそちらの規則も確認します。拒否を無理に解除しません。

## 試す依頼

```text
draft.mdを読みやすくし、edited.mdへ保存してください。三つという数と未計測の条件は残してください。変更前に保存先を示してください。
```

ファイル変更の確認が出たら、対象がこの練習フォルダのedited.mdであることを確認して、一回だけの許可を選びます。継続許可を選ぶ練習にはしません。

元のdraft.mdが保たれ、edited.mdができているかを比べます。数と未計測の条件、余分な実績が加わっていないかも確認します。確認が出ない場合は、モード、ルールの適用元、管理設定を確認し、結果を記録します。

```sh
python3 -m json.tool .claude/settings.local.json
```

これはJSON構文の確認だけです。Claudeの権限動作が意図どおりになったことを証明しません。

## 確認した範囲と限界

配布時に確認したのはJSONの構文、4ファイルのUTF-8、ZIP内容と元ファイルの一致です。このサンプルをClaudeへ送る実行、確認画面の発生、edited.mdの生成結果は未確認です。
Editは組み込みのファイル変更ツールに対する設定です。Bash以外のツール、PowerShell、MCP等すべてを制御する設定ではありません。単純な権限設定を完全な隔離や秘密情報保護として扱わないでください。仕事の機密資料や認証情報を練習フォルダへ追加しないでください。

## 一次資料

- [Claude Codeの権限](https://code.claude.com/docs/en/permissions)
- [設定ファイルと適用範囲](https://code.claude.com/docs/en/settings)
