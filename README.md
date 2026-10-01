# Claude Codeで試す文章推敲サンプル

確認日: 2026-10-02 JST。LULUが作った説明用の記入例です。公式テンプレートではありません。

## 何を試すか

- CLAUDE.md: 毎回守ってほしい、このフォルダの作業ルール。
- .claude/skills/rewrite-japanese/SKILL.md: 推敲を頼む場面で使う手順。
- draft.md: 架空の練習文。3か月という数値、かもしれないという断定の強さ、未計測という条件を残せるかを見ます。
- edited.md: 依頼後にできる出力です。配布ZIPには入っていません。

## 準備

Claude Codeをインストール・ログイン済みの方向けです。未導入なら[公式Quickstart](https://code.claude.com/docs/en/quickstart)を先に確認してください。Claudeアプリのチャット欄へZIPを添付する手順ではありません。

[サンプルZIP](https://github.com/beloveddogjp-creator/claude-note-practice/raw/refs/heads/main/claude-note-practice.zip)をダウンロードして展開します。GitHubのZIPファイル画面で「View raw」が出る場合は、そこからダウンロードできます。

ZIPを展開した独立した claude-note-practice フォルダで試します。別の仕事のフォルダへ混ぜる前に、この小さなサンプルで動作を確かめます。サンプル以外の上位ディレクトリのプロジェクトルールを混ぜないためです。自分のユーザー設定等の影響は残る場合があります。

## 1. フォルダの中を確認する

```text
claude-note-practice/
├── CLAUDE.md
├── draft.md
├── README.md
└── .claude/
    └── skills/
        └── rewrite-japanese/
            └── SKILL.md
```

.claude はドットから始まるため、Finderなどでは非表示になることがあります。コードエディタでフォルダを開いて確認してください。手作業で作る場合も、CLAUDE.md.txt や SKILL.md.txt ではなく、この名前で保存します。

## 2. このフォルダでClaude Codeを開始する

ターミナルで展開したフォルダへ移動し、その場所で次を実行します。保存先によって移動先が違うので、固定のパスは指定しません。

```sh
claude
```

## 3. CLAUDE.mdの読み込みを確認する

Claude Code内で次を入力し、Memory filesにこの練習フォルダのCLAUDE.mdが出るか確認します。

```text
/context
```

これは読み込みの確認です。指示を守った結果まで確認したことにはなりません。

## 4. 常設ルールと今回の依頼を分けて試す

まずは、次の文章をClaude Codeへ送ります。

> draft.mdを読みやすく推敲してください。元の意味・数値・断定の強さを保ち、edited.mdに保存してください。変更した点と、確認が必要な点も教えてください。

draft.mdが変更されていないこと、edited.mdができたこと、3か月・かもしれない・未計測の意味が残っていることを、自分でも見比べます。言葉が完全一致する必要はありませんが、意味を強めてはいけません。

## 5. スキルを明示的に呼んで試す

手順を調べたい場合は、新しいセッションで次を入力します。前のedited.mdを残したい場合は、事前に別名で保存してください。

```text
/rewrite-japanese draft.mdを推敲し、edited.mdに保存してください。
```

呼び出したスキルと結果を確認します。上書きの前に許可確認が出た場合は、対象ファイルを見て判断してください。自動適用を確かめたい場合は、別の新しいセッションでスラッシュ呼出を使わず、手順4の依頼を試します。

## 6. 近いが別の依頼と比べる

新しいセッションで「この記事のテーマを三つ考えて」と頼んだ場合は、推敲とは別の作業です。このスキルでdraft.mdの推敲へ進んでしまわないかを見ます。

依頼文、適用されたスキル、出力、期待との違いを短く残します。自然な依頼では使われない場合、descriptionと依頼の言葉の対応を見直す候補になります。説明を具体的にすれば必ず自動起動する、という保証ではありません。

## 確認した範囲

ファイル配置、UTF-8、スキルのfrontmatter、ZIPの内容と展開を確認しています。作成環境のClaude Codeは2.1.278でしたが、この配布サンプルをClaudeへ送って推敲させる実行はしていません。出力の品質や自動起動の結果は未確認です。実行時のモデル、権限、設定により変わります。

## 一次資料

- [CLAUDE.mdとMemory files](https://code.claude.com/docs/en/memory)
- [スキルの配置と呼び出し](https://code.claude.com/docs/en/skills)
- [Claude Codeの導入](https://code.claude.com/docs/en/quickstart)
