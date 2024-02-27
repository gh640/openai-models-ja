# OpenAI 社が提供するモデルの一覧（日本語）

**最終更新日: 2024/02/27**

OpenAI 社が提供するモデルの一覧です。
基本的に最新のものが各表の一番上に並んでいます。

可能なときに更新していきます。
最終更新日が古い場合は公式にあたってください。

---

## 継続的なモデルアップグレード

以下のモデルはそのときどきの最新版のモデルを指す。

- `gpt-3.5-turbo`
- `gpt-4`
- `gpt-4-turbo-preview`

実際に使われたモデルの情報はレスポンスオブジェクトに含まれている（例: `gpt-3.5-turbo-0613` ）。

> ## ChatGPT upgrades
>
> We are constantly improving our ChatGPT models, and want to make these enhancements available to developers as well. Developers who use the `gpt-3.5-turbo model will always get our recommended stable model, while still having the flexibility to opt for a specific model version. For example, today we’re releasing `gpt-3.5-turbo-0301`, which will be supported through at least June 1st, and we’ll update `gpt-3.5-turbo` to a new stable release in April. The models page will provide switchover updates.
> >
> https://openai.com/blog/introducing-chatgpt-and-whisper-apis#:~:text=Chat%20guide.-,ChatGPT%20upgrades,-We%20are%20constantly

## GPT-4 と GPT-4 Turbo

GPT-3.5 を改善した、自然言語やコードを理解・生成できるモデル群。

| モデル | 説明 | コンテキストウィンドウ | トレーニングデータ |
| --- | --- | --- | --- |
| `gpt-4-0125-preview` | **New**<br>最新の **GPT-4 Turbo** モデル。 [詳細](https://openai.com/blog/new-embedding-models-and-api-updates) | 128,000 トークン | 2023/12 まで |
| `gpt-4-turbo-preview` | 現在 `gpt-4-0125-preview` を指す。 | 128,000 トークン | 2023/12 まで |
| `gpt-4-1106-preview` | GPT-4 Turbo モデル。プロダクショントラフィック向けではない。 [詳細](https://openai.com/blog/new-models-and-developer-products-announced-at-devday) | 128,000 トークン | 2023/04 まで |
| `gpt-4-vision-preview` | 画像の理解能力のある GPT-4 。プロダクショントラフィック向けではない。 [詳細](https://openai.com/blog/new-models-and-developer-products-announced-at-devday) | 128,000 トークン | 2023/04 まで |
| `gpt-4` | 現在 `gpt-4-0613` を指す。 | 8,192 トークン | 2021/09 まで |
| `gpt-4-0613` | `gpt-4` の 2023/06/13 時点のスナップショット。ファンクションコーリングサポートの改善あり。 | 8,192 トークン | 2021/09 まで |
| `gpt-4-32k` | 現在 `gpt-4-32k-0613` を指す。 GPT-4 Turbo が優先されたため広く展開されなかった。 | 32,768 トークン | 2021/09 まで |
| `gpt-4-32k-0613` | `gpt-4-32k` の 2023/06/13 時点のスナップショット。ファンクションコーリングサポートの改善あり。 GPT-4 Turbo が優先されたため広く展開されなかった。 | 32,768 トークン | 2021/09 まで |

### 料金

| モデル | インプット（ 1k トークン） | アウトプット（ 1k トークン） |
| --- | --- | --- |
| `gpt-4-0125-preview` | $0.01 | $0.03 |
| `gpt-4-1106-preview` | $0.01 | $0.03 |
| `gpt-4-1106-vision-preview` | $0.01 | $0.03 |
| `gpt-4` | $0.03 | $0.06 |
| `gpt-4-32k` | $0.06 | $0.12 |

後発の `gpt-4-turbo` が `gpt-4` よりも単価が低いのは間違いではありません。

> GPT-4 Turbo is more capable and has knowledge of world events up to April 2023. It has a 128k context window so it can fit the equivalent of more than 300 pages of text in a single prompt. We also optimized its performance so we are able to offer GPT-4 Turbo at a 3x cheaper price for input tokens and a 2x cheaper price for output tokens compared to GPT-4.
>
> [New models and developer products announced at DevDay](https://openai.com/blog/new-models-and-developer-products-announced-at-devday)

画像生成は 150px x 150px で $0.00255 。

多くの基本的なタスクでは GPT-4 と GPT-3.5 の差は大きくない。しかし、より複雑な推論状況では GPT-4 はこれまでのどのモデルよりもはるかに能力が高い。

## GPT-3.5 Turbo

GPT-3.5 を改善した、自然言語やコードを理解・生成できるモデル群。

| モデル | 説明 | コンテキストウィンドウ | トレーニングデータ |
| --- | --- | --- | --- |
| `gpt-3.5-turbo-0125` | **New**<br>最新の **GPT 3.5 Turbo** モデル。 [詳細](https://openai.com/blog/new-embedding-models-and-api-updates#:~:text=Other%20new%20models%20and%20lower%20pricing) | 16,385 トークン | 2021/09 まで |
| `gpt-3.5-turbo` | 現在 `3.5-turbo-0613` を指す。 2024/02/16 に `3.5-turbo-0125` に変更される。 | 4,096 トークン | 2021/09 まで |
| `gpt-3.5-turbo-1106` | GPT-3.5 Turbo モデル。インストラクションへの対応・ JSON モード・再現可能な出力・パラレルファンクションコーリングなどの改善あり。 [詳細](https://openai.com/blog/new-models-and-developer-products-announced-at-devday) | 16,385 トークン | 2021/09 まで |
| `gpt-3.5-turbo-instruct` | GPT-3 時代と近い能力。レガシー Completions エンドポイントとの互換性あり、 Chat Completions との互換性なし。 | 4,096 トークン | 2021/09 まで |
| `gpt-3.5-turbo-16k` | **Legacy**<br>現在 `gpt-3.5-turbo-16k-0613` を指す。 | 16,385 トークン | 2021/09 まで |
| `gpt-3.5-turbo-0613` | **Legacy**<br>`gpt-3.5-turbo` の 2023/06/13 時点のスナップショット。 2024/06/13 に deprecated 予定。 | 4,096 トークン | 2021/09 まで |
| `gpt-3.5-turbo-16k-0613` | **Legacy**<br>`gpt-3.5-16k-turbo` の 2023/06/13 時点のスナップショット。 2024/06/13 に deprecated 予定。 | 16,385 トークン | 2021/09 まで |

### 料金

| モデル | インプット（ 1k トークン） | アウトプット（ 1k トークン） |
| --- | --- | --- |
| `gpt-3.5-turbo-0125` | $0.0005 | $0.0015 |
| `gpt-3.5-turbo-instruct` | $0.0015 | $0.0020 |

## アシスタント API

アシスタント API では各チャットモデルが利用できます。

### 料金

| ツール | インプット |
| --- | --- |
| Code interpreter | $0.03 / セッション |
| Retieval | $0.20 / GB / アシスタント / 日（ 2024/03/01 まで無料） |

## DALL·E

自然言語のプロンプトを与えて画像を生成・編集できるモデル。

| モデル | 説明 |
| --- | --- |
| `dall-e-3` | **New**<br>最新の **DALL·E 3** モデル。 2023/11 リリース。 [詳細](https://openai.com/blog/new-models-and-developer-products-announced-at-devday) |
| `dall-e-2` | ひとつ前の DALL·E モデル。 2022/11 リリース。オリジナルモデルよりも 4 倍以上の解像度のリアルで精確な第 2 世代 DALL·E モデル。 |

### 料金

| モデル | 品質 | 解像度 | 料金（ 1 画像） |
| --- | --- | --- | --- |
| `dall-e-3` | Standard | 1024×1024 | $0.040 |
|  | Standard | 1024×1792, 1792×1024 | $0.080 |
|  | HD | 1024×1024 | $0.080 |
|  | HD | 1024×1792, 1792×1024 | $0.120 |
| `dall-e-2` |  | 1024×1024 | $0.020 |
|  |  | 512×512 | $0.018 |
|  |  | 256×256 | $0.016 |

## TTS

テキストを自然な発話データに変換できるモデル群。
TTS は Text-To-Speech の略。

| モデル | 説明 |
| --- | --- |
| `tts-1` | **New**<br>最新の **Text-to-Speech 1** モデル。リアルタイム生成向けでスピード優先。 |
| `tts-1-hd` | **New**<br>最新の text-to-Speech 1 HD** モデル。品質優先。 |

### 料金

| モデル | 料金 |
| --- | --- |
| `tts-1` |	$0.015 / 1K 文字 |
| `tts-1-hd` | $0.030 / 1K 文字 |

## Whisper

音声をテキストに変換できるモデル。
マルチタスクで多言語音声認識・音声翻訳・言語識別も可能。
現在モデル名 `whisper-1` で Whisper v2-large モデルが利用可能。

| モデル | 説明 |
| --- | --- |
| `whisper-1` | Whisper v2-large モデル。 |

現在オープンソースバージョンと OpenAI の API で利用できるバージョンに違いは無いが、 API の方は推論過程の最適化により高速化されている。

### 料金

| モデル | 料金 |
| --- | --- |
| `whisper-1` |	$0.006 / 分（端数は近い秒に丸められる） |

## Embeddings

テキストを数値形式に変換できるモデル群。
最新のモデルについては [告知のブログ投稿](https://openai.com/blog/new-embedding-models-and-api-updates) に詳細あり。

| モデル | 説明 | 出力の次元 |
| --- | --- | --- |
| `text-embedding-3-large` | **New**<br>**Embedding V3 large** <br>英語とその他の言語の両方で最も能力の高い embedding モデル。 [詳細](https://openai.com/blog/new-embedding-models-and-api-updates) | 3,072 |
| `text-embedding-3-small` | **New**<br>**Embedding V3 small** <br>第 2 世代の ada embedding モデルからパフォーマンスを改善。 [詳細](https://openai.com/blog/new-embedding-models-and-api-updates) | 1,536 |
| `text-embedding-ada-002` | 第 2 世代で最も能力の高い embedding モデル。 16 個の第 1 世代モデルの置き換え。 [詳細](https://openai.com/blog/new-and-improved-embedding-model) | 1,536 |

### 料金

| モデル | 使用（ 1k トークン） |
| --- | --- |
| `text-embedding-3-large` | $0.00013 |
| `text-embedding-3-small` | $0.00002 |
| `ada v2` | $0.00010 |

## Moderation

テキストがセンシティブであったり安全でなかったりするかを検出できるファインチューンされたモデル。

| モデル | 説明 | 最大トークン |
| --- | --- | --- |
| `text-moderation-latest` | 現在 `text-moderation-007` を指す。 | 32,768 |
| `text-moderation-stable` | 現在 `text-moderation-007` を指す。 | 32,768 |
| `text-moderation-007` | すべてのカテゴリーで最も能力の高い moderation モデル。 [詳細](https://openai.com/blog/new-embedding-models-and-api-updates) | 32,768 |

## GPT base

自然言語やコードを理解・生成できるがインストラクションでの学習ができないモデル群。
オリジナルの GPT-3 ベースモデルの置き換えとして作られた。
レガシーな COmpletions API を使う。
ほとんどのユーザーにはこれらではなく GPT-3.5 か GPT-4 の利用が推奨される。

| モデル | 説明 | 最大トークン | トレーニングデータ |
| --- | --- | --- | --- |
| `babbage-002` | GPT-3 `ada` と `babbage` ベースモデルの置き換え。 | 16,384 トークン | 2021/09 まで |
| `davinci-002` | GPT-3 `curie` と `davinci` ベースモデルの置き換え。  | 16,384 トークン | 2021/09 まで |

### 料金

| モデル | 使用（ 1k トークン） |
| --- | --- |
| `davinci-002` | $0.0020 |
| `babbage-002` | $0.0004 |


## データの使用ポリシー

2023/03/01 時点で（明示的にオプトインしないかぎり） OpenAI API に送信されたデータは OpenAI のモデルのトレーングには使わない、とのこと。
ただし、不正使用の特定のためにデータは最長 30 日間保持されることがある。

**注: デフォルトの使用ポリシーはエンドポイントごとに異なるため公式ドキュメンテーションを参考してください。**

このデータポリシーは API 経由ではない ChatGPT や DALL·E Labs のサービスには適用されない（つまり、 ChatGPT や DALL·E Labs でユーザーが送信したデータはモデルのトレーニングに使用されることがある）。

> ## Your data is your data.
>
> As of March 1, 2023, data sent to the OpenAI API will not be used to train or improve OpenAI models (unless you explicitly opt in). One advantage to opting in is that the models may get better at your use case over time.
>
> To help identify abuse, API data may be retained for up to 30 days, after which it will be deleted (unless otherwise required by law). For trusted customers with sensitive applications, zero data retention may be available. With zero data retention, request and response bodies are not persisted to any logging mechanism and exist only in memory in order to serve the request.
>
> Note that this data policy does not apply to OpenAI's non-API consumer services like [ChatGPT(https://chat.openai.com/)] or [DALL·E Labs](https://labs.openai.com/).
>
> https://platform.openai.com/docs/models/how-we-use-your-data

## Deprecated

非推奨となったモデルの全リストと代替案。

**注: シャットダウン日が過ぎているものは除外しています。**

### 2023/11/06: チャットモデルのアップデート

| モデル | 推奨される移行先 | シャットダウン日 |
| --- | --- | --- |
| `gpt-3.5-turbo-0613` | `gpt-3.5-turbo-1106` | 2024/06/13 |
| `gpt-3.5-turbo-16k-0613` | `gpt-3.5-turbo-1106` | 2024/06/13 |

### 2023/06/13: チャットモデルのアップデート

| モデル | 推奨される移行先 | シャットダウン日 |
| --- | --- | --- |
| `gpt-3.5-turbo-0301` | `gpt-3.5-turbo-0613` | 早ければ 2024/06/13 |
| `gpt-4-0314` | `gpt-4-0613` | 早ければ 2024/06/13 |
| `gpt-4-32k-0314` | `gpt-4-32k-0613` | 早ければ 2024/06/13 |

## 公式ページ

- [Models - OpenAI API](https://platform.openai.com/docs/models)
- [Deprecations - OpenAI API](https://platform.openai.com/docs/deprecations)
- [Pricing](https://openai.com/pricing)

## その他参考文献

- [OpenAI - Wikipedia](https://en.wikipedia.org/wiki/OpenAI)

