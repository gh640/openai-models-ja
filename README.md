# OpenAI API モデル一覧（日本語）

**最終更新日: 2026/09/24**

[OpenAI 公式 Models ページ](https://developers.openai.com/api/docs/models) をもとに OpenAI が提供するモデルについて日本語でまとめています。料金や仕様は変更される可能性があるため最新情報は必ず公式サイトでご確認ください。

- 単位 $ はすべて US ドルです

## 目次

- [概要](#概要)
- [フロンティアモデル](#フロンティアモデル)
- [その他フロンティアモデル](#その他フロンティアモデル)
- [特化モデル](#特化モデル)
  - [OpenAI Daybreak](#openai-daybreak)
  - [Life sciences](#life-sciences)
  - [画像](#画像)
  - [動画](#動画)
  - [リアルタイム・音声](#リアルタイム音声)
  - [音声生成](#音声生成)
  - [文字起こし](#文字起こし)
  - [コーディング](#コーディング)
  - [ディープリサーチ](#ディープリサーチ)
  - [オープンウェイト](#オープンウェイト)
  - [Embedding](#embedding)
  - [ChatGPT](#chatgpt)
- [その他](#その他)
- [価格](#価格)
- [利用可能なエンドポイント](#利用可能なエンドポイント)
- [ツール](#ツール)
- [レートリミット](#レートリミット)
- [参考](#参考)

## 概要

OpenAI API は多様なワークロードに対応する複数のモデル群で構成されています。モデルごとに対応モダリティ、推論能力、料金体系、サービスポリシーが異なります。開発用途に応じてモデルを選択し、必要であればファインチューニングやツール連携を組み合わせて利用できます。

| カテゴリ | 概要 |
| --- | --- |
| フロンティアモデル | 公式 Models ページの Flagship models に掲載されている最新世代の汎用モデル。 |
| その他フロンティアモデル | 主要モデル以外の上位版・小型版・旧世代の汎用モデル。 |
| 特化モデル | OpenAI Daybreak、Life sciences、画像、動画、Realtime、音声生成、文字起こし、コーディング、ディープリサーチ、オープンウェイト、Embedding、ChatGPT 向けモデル。 |
| その他 | 公式の More models 相当の既存モデルや、非推奨モデル。 |

## フロンティアモデル

公式 Models ページで主要モデルとして案内されている最新世代の汎用モデルです。GPT-6 シリーズは、最も高性能な Astra、Astra に近い性能とコストのバランスを取る GPT-6.1 Sol、高効率な Luna で構成されます。

### GPT-6 Astra

OpenAI の最も高性能なモデル。複雑な推論、コーディング、コンピュータ操作、調査、ドキュメント作成など、難しいエンドツーエンドの作業向けです。

- モデル ID: `gpt-6-astra`
- Reasoning: `low` / `medium` / `high` / `xhigh` / `max`（推論トークン対応。`none` は非対応）
- 価格（1M トークンあたり）: 入力 $10.00 / キャッシュ入力 $1.00 / キャッシュ書き込み $12.50 / 出力 $50.00
- 272K を超える入力トークンのプロンプト: 入力・キャッシュ料金は 2 倍、出力料金は 1.5 倍
- コンテキストウィンドウ: 1,050,000
- 最大出力トークン: 128,000
- ナレッジカットオフ: 2026/04/30
- 入力モダリティ: テキスト・画像
- 出力モダリティ: テキスト
- 特徴: ストリーミング、function calling、structured outputs に対応。Responses API では web search、file search、image generation、Code Interpreter、computer use、MCP などのツールを利用できます。

### GPT-6.1 Sol

複雑なコーディング、コンピュータ操作、プロフェッショナルワーク向けのモデルです。Astra に近い性能をより低いコストで提供します。

- モデル ID: `gpt-6.1-sol`
- Reasoning: `low` / `medium` / `high` / `xhigh` / `max`（`medium` がデフォルト。`none` と `minimal` は非対応）
- 価格（1M トークンあたり）: 入力 $2.00 / キャッシュ入力 $0.10 / キャッシュ書き込み $2.50 / 出力 $10.00
- 272K を超える入力トークンのプロンプト: 入力・キャッシュ料金は 2 倍、出力料金は 1.5 倍
- コンテキストウィンドウ: 1,050,000
- 最大出力トークン: 128,000
- ナレッジカットオフ: 2026/04/30
- 入力モダリティ: テキスト・画像
- 出力モダリティ: テキスト
- 特徴: ストリーミング、function calling、structured outputs に対応。ツール呼び出しには Responses API を使用します。Chat Completions はツール呼び出しなしで利用できます。

### GPT-6 Luna

集中的なタスクを効率よく大量に処理するための GPT-6 シリーズのモデルです。コスト重視の高ボリュームなワークロードに適しています。

- モデル ID: `gpt-6-luna`
- Reasoning: `none` / `low` / `medium` / `high` / `xhigh` / `max`（`medium` がデフォルト）
- 価格（1M トークンあたり）: 入力 $0.10 / キャッシュ入力 $0.01 / キャッシュ書き込み $0.125 / 出力 $0.50
- 272K を超える入力トークンのプロンプト: 入力・キャッシュ料金は 2 倍、出力料金は 1.5 倍
- コンテキストウィンドウ: 1,050,000
- 最大出力トークン: 128,000
- ナレッジカットオフ: 2026/05/18
- 入力モダリティ: テキスト・画像
- 出力モダリティ: テキスト
- 特徴: ストリーミング、function calling、structured outputs に対応。Responses API で組み込みツールを利用できます。Chat Completions で function calling を使う場合は `reasoning_effort: "none"` が必要です。

### GPT-5.6 Sol

複雑なプロフェッショナルワーク、推論、コーディング向けの GPT-5.6 系フロンティアモデル。 `gpt-5.6` エイリアスはこのモデルにルーティングされます。

- モデル ID: `gpt-5.6-sol`（エイリアス: `gpt-5.6`）
- Reasoning: `none` / `low` / `medium` / `high` / `xhigh` / `max`（`medium` がデフォルト）
- 価格（1M トークンあたり）: 入力 $4.00 / キャッシュ入力 $0.40 / 出力 $20.00
- 272K を超える入力トークンのプロンプト: 入力料金は 2 倍、出力料金は 1.5 倍
- コンテキストウィンドウ: 1,050,000
- 最大出力トークン: 128,000
- ナレッジカットオフ: 2026/02/16
- 入力モダリティ: テキスト・画像
- 出力モダリティ: テキスト
- 特徴: 推論トークン、ストリーミング、function calling、structured outputs をサポート。Responses API では web search、file search、computer use、MCP などのツールを利用できます。

### GPT-5.6 Terra

知能とコストのバランスを取る GPT-5.6 系モデル。従来の GPT-5 系における mini 相当の位置付けです。

- モデル ID: `gpt-5.6-terra`
- Reasoning: `none` / `low` / `medium` / `high` / `xhigh` / `max`（`medium` がデフォルト）
- 価格（1M トークンあたり）: 入力 $2.00 / キャッシュ入力 $0.20 / 出力 $12.00
- 272K を超える入力トークンのプロンプト: 入力料金は 2 倍、出力料金は 1.5 倍
- コンテキストウィンドウ: 1,050,000
- 最大出力トークン: 128,000
- ナレッジカットオフ: 2026/02/16
- 入力モダリティ: テキスト・画像
- 出力モダリティ: テキスト
- 特徴: 推論トークン、ストリーミング、function calling、structured outputs と Responses API の各種ツールをサポート。

### GPT-5.6 Luna

コスト重視かつ高ボリュームのワークロード向けに最適化された GPT-5.6 系モデル。従来の GPT-5 系における nano 相当の位置付けです。

- モデル ID: `gpt-5.6-luna`
- Reasoning: `none` / `low` / `medium` / `high` / `xhigh` / `max`（`medium` がデフォルト）
- 価格（1M トークンあたり）: 入力 $0.20 / キャッシュ入力 $0.02 / 出力 $1.20
- 272K を超える入力トークンのプロンプト: 入力料金は 2 倍、出力料金は 1.5 倍
- コンテキストウィンドウ: 1,050,000
- 最大出力トークン: 128,000
- ナレッジカットオフ: 2026/02/16
- 入力モダリティ: テキスト・画像
- 出力モダリティ: テキスト
- 特徴: 推論トークン、ストリーミング、function calling、structured outputs と Responses API の各種ツールをサポート。

## その他フロンティアモデル

公式カタログの主要モデル以外に掲載されているモデル ID と提供状況です。個別の仕様・料金は公式モデルページを参照してください。

| モデル ID | 状態 |
| --- | --- |
| `gpt-6-sol` | 提供中（GPT-6.1 Sol より前のモデル） |
| `gpt-5.5`, `gpt-5.5-pro` | 提供中 |
| `gpt-5.4`, `gpt-5.4-pro`, `gpt-5.4-mini`, `gpt-5.4-nano` | 提供中 |
| `gpt-5.2`, `gpt-5.2-pro`, `gpt-5.1`, `gpt-5`, `gpt-5-mini`, `gpt-5-nano`, `gpt-5-pro` | 提供中 |
| `gpt-4.1`, `gpt-4.1-mini`, `gpt-4o`, `gpt-4o-mini` | 提供中 |

## 特化モデル

公式 Models ページの Specialized models に掲載されている、用途別のモデル群です。

### OpenAI Daybreak

認可済みの防御目的のサイバーセキュリティ研究・テスト向けモデル群です。利用には別途承認とプロビジョニングが必要です。

#### GPT-5.6 Cyber

高度な脆弱性研究、エクスプロイト検証、セキュリティテスト向けに訓練されたモデルです。

- モデル ID: `gpt-5.6-cyber`
- コンテキストウィンドウ: 400,000
- 最大出力トークン: 128,000
- 入力モダリティ: テキスト・画像
- 出力モダリティ: テキスト

#### Daybreak Red

高度なサイバーセキュリティモデルへのエイリアスです。認可済みの防御者による脆弱性研究、エクスプロイト検証、セキュリティテスト向けです。

- モデル ID: `gpt-daybreak-red-latest`
- 特徴: ストリーミング、function calling、structured outputs、Responses API の各種ツールに対応

#### Daybreak Blue

防御目的のサイバーセキュリティ用途向けに安全策を調整した、フロンティア汎用モデルへのエイリアスです。

- モデル ID: `gpt-daybreak-blue-latest`
- 特徴: ストリーミング、function calling、structured outputs、Responses API の各種ツールに対応

### Life sciences

承認済みの組織によるライフサイエンス研究向けモデルです。

#### GPT-Rosalind

承認された内部ライフサイエンス研究向けの推論モデルです。Trusted Access program を通じた承認が必要です。

- モデル ID: `gpt-rosalind-research`
- 価格（1M トークンあたり）: 入力 $5.00 / キャッシュ入力 $0.50 / 出力 $25.00
- 課金開始日: 2026/10/05
- キャッシュ書き込み料金: 対象外

### 画像

画像生成と編集向けのモデル群です。

#### GPT Image 2.5 Sunburst

画像生成と編集における精度を重視した、GPT Image 2.5 系の最上位モデルです。テキスト・画像入力から画像を生成し、Image API または Responses API の画像生成ツールで利用できます。

- モデル ID: `gpt-image-2.5-sunburst`（スナップショット: `gpt-image-2.5-sunburst-2026-09-08`）
- 品質設定: `low` / `medium` / `high` / `xhigh` / `max` / `auto`
- 価格（1M トークンあたり）:
  - テキストトークン: 入力 $5.00 / キャッシュ入力 $1.25
  - 画像トークン: 入力 $8.00 / キャッシュ入力 $2.00 / 出力 $30.00
- 入力モダリティ: テキスト・画像
- 出力モダリティ: 画像
- 特徴: ストリーミング、function calling、structured outputs には非対応

#### GPT Image 2.5 Flare

日常的な画像生成を高速に行う GPT Image 2.5 系モデルです。テキスト・画像入力から画像を生成し、Image API または Responses API の画像生成ツールで利用できます。

- モデル ID: `gpt-image-2.5-flare`（スナップショット: `gpt-image-2.5-flare-2026-09-08`）
- 品質設定: `low` / `medium` / `high` / `xhigh` / `max` / `auto`
- 価格（1M トークンあたり）:
  - テキストトークン: 入力 $5.00 / キャッシュ入力 $1.25
  - 画像トークン: 入力 $8.00 / キャッシュ入力 $2.00 / 出力 $30.00
- 入力モダリティ: テキスト・画像
- 出力モダリティ: 画像
- 特徴: ストリーミング、function calling、structured outputs には非対応

#### GPT Image 2

`gpt-image-2` は GPT Image 2.5 より前の世代です。公式カタログには引き続き掲載されています。

#### GPT Image 1.5

`gpt-image-1.5` は非推奨です。

#### その他の画像モデル

- `chatgpt-image-latest`, `gpt-image-1`, `gpt-image-1-mini`: 非推奨

### 動画

Sora 2 と Sora 2 Pro（`sora-2`、`sora-2-pro`）は 2026/09/24 に提供終了しました。

### リアルタイム・音声

リアルタイム会話、音声入出力、文字起こし向けのモデル群です。

#### GPT-Live 1

自然で表現力のある音声会話と、滑らかな割り込み処理に対応する全二重音声モデルです。音声を聞きながら同時に話すことができ、推論やツール利用をバックエンドエージェントに委譲できます。

- モデル ID: `gpt-live-1`
- 価格: ライブセッション 1 分あたり $0.05（秒単位で実際に課金。1 分未満を切り上げない）
- 入力モダリティ: テキスト・音声
- 出力モダリティ: テキスト・音声
- エンドポイント: Live API `v1/live/sessions`
- 特徴: ストリーミングと function calling に対応。バックエンドのモデル・ツール利用料は別途発生します。

#### gpt-realtime-2.1

gpt-realtime-2 を更新した、推論対応のリアルタイム音声モデル。英数字の認識、無音・ノイズ処理、中断時の挙動が改善されており、複雑な音声エージェントワークフロー向けに設定可能な推論負荷、指示追従、ツール利用をサポートします。

- Reasoning: 最高（推論トークン対応、推論負荷を調整可能）
- Speed: 高速
- 価格
  - テキストトークン / 1M: 入力 $4.00 / キャッシュ入力 $0.40 / 出力 $24.00
  - 音声トークン / 1M: 入力 $32.00 / キャッシュ入力 $0.40 / 出力 $64.00
  - 画像トークン / 1M: 入力 $5.00 / キャッシュ入力 $0.50
- コンテキストウィンドウ: 128,000
- 最大出力トークン: 32,000
- ナレッジカットオフ: 2024/09/30
- 入力モダリティ: テキスト・音声・画像
- 出力モダリティ: テキスト・音声
- 特徴: 音声対話での認識精度や割り込み処理を改善した gpt-realtime-2 系の上位モデル。Realtime API のほか、Responses API / Chat Completions API などでも利用可能として掲載されています。

#### gpt-realtime-2.1-mini

より高速・低コストなリアルタイム音声対話向けの蒸留推論モデル。 WebRTC / WebSocket / SIP 接続を通じた音声・テキスト入力に対応し、 gpt-realtime-2 より英数字認識が改善されています。

- Reasoning: 高（推論トークン対応）
- Speed: 非常に高速
- 価格
  - テキストトークン / 1M: 入力 $0.60 / キャッシュ入力 $0.06 / 出力 $2.40
  - 音声トークン / 1M: 入力 $10.00 / キャッシュ入力 $0.30 / 出力 $20.00
  - 画像トークン / 1M: 入力 $0.80 / キャッシュ入力 $0.08
- 入力モダリティ: テキスト・音声・画像
- 出力モダリティ: テキスト・音声
- 特徴: 低レイテンシー・低コストの音声エージェント向け。Realtime API のほか、Responses API / Chat Completions API などでも利用可能として掲載されています。

#### gpt-realtime-2

`gpt-realtime-2` は `gpt-realtime-2.1` より前の世代です。公式カタログには引き続き掲載されています。

#### gpt-realtime-1.5

`gpt-realtime-1.5` は現行カタログに掲載されています。最新世代の Realtime モデルではありません。

#### gpt-realtime

`gpt-realtime` は非推奨です。

#### gpt-realtime-mini

`gpt-realtime-mini` は非推奨です。

#### gpt-realtime-translate

ライブ多言語音声体験向けのストリーミング音声翻訳モデル。音声入力を受け取り、入力音声が届いている途中から翻訳済み音声と transcript delta を返します。会話管理やツール呼び出しを行うアシスタントではなく、「人が話した内容を翻訳する」用途向けです。

- Performance: 最高
- Speed: 非常に高速
- 価格: リアルタイム音声 1 分あたり $0.034
- コンテキストウィンドウ: 16,000
- 最大出力トークン: 2,000
- ナレッジカットオフ: 2024/09/30
- 入力モダリティ: 音声
- 出力モダリティ: 音声・テキスト
- 特徴: 専用の Realtime translation endpoint `v1/realtime/translations` で利用します。

#### gpt-audio

`gpt-audio` は非推奨です。

#### gpt-audio-1.5

Chat Completions REST API で利用できる、音声入出力向けの上位モデル。テキストと音声の双方向入出力に対応します。

- 料金
  - テキストトークン / 1M: 入力 $2.50 / 出力 $10.00
  - 音声トークン / 1M: 入力 $32.00 / 出力 $64.00
- コンテキストウィンドウ: 128,000
- 最大出力トークン: 16,384
- ナレッジカットオフ: 2024/09/30
- 入力モダリティ: テキスト・音声
- 出力モダリティ: テキスト・音声

#### gpt-audio-mini

`gpt-audio-mini` は非推奨です。

#### その他のリアルタイム・音声モデル

- gpt-audio
- GPT-4o Transcribe
- GPT-4o mini Transcribe
- TTS-1
- TTS-1 HD
- Whisper

### 文字起こし

#### GPT-4o Transcribe Diarize

`gpt-4o-transcribe-diarize` は旧世代の文字起こしモデルです。後継として `gpt-transcribe` が掲載されています。

#### gpt-realtime-whisper

ライブ音声から低レイテンシーの transcript delta が必要なアプリケーション向けのストリーミング speech-to-text モデル。レイテンシーと精度を調整したいリアルタイム用途のために設計されており、テキストトークンではなく音声時間に基づいて課金されます。

- Performance: 高
- Speed: 非常に高速
- 価格: リアルタイム音声 1 分あたり $0.017
- コンテキストウィンドウ: 16,000
- 最大出力トークン: 2,000
- ナレッジカットオフ: 2024/09/30
- 入力モダリティ: テキスト・音声
- 出力モダリティ: テキスト
- 特徴: Realtime transcription session で `audio.input.transcription.model` に指定して利用します。ファイルやリクエスト・レスポンス型の文字起こし全般の置き換えではなく、ライブ音声での遅延と精度の要件に応じて評価するモデルです。

#### gpt-live-transcribe

ライブ音声から低レイテンシーの transcript delta を取得するストリーミング speech-to-text モデル。レイテンシーを調整でき、非構造化コンテキスト、キーワードヒント、言語ヒントに対応します。

- 価格: リアルタイム音声 1 分あたり $0.017
- 入力モダリティ: テキスト・音声
- 出力モダリティ: テキスト
- 特徴: 低遅延の Realtime transcription 向け。ストリーミングに対応し、function calling と structured outputs には対応していません。

#### gpt-transcribe

高精度な speech-to-text モデル。完了した音声ファイル、ストリーミング中のファイル文字起こし、WebSocket の Realtime セッションで確定したターンの文字起こしに対応します。非構造化コンテキスト、キーワードヒント、言語ヒントも利用できます。

- 価格: 文字起こし音声 1 分あたり $0.0045
- 入力モダリティ: テキスト・音声
- 出力モダリティ: テキスト
- 特徴: ファイル文字起こしと Realtime 入力の確定ターンの文字起こしに対応します。

### 音声生成

テキストを自然な音声へ変換するモデル群です。

#### gpt-4o-mini-tts

GPT-4o Mini を基盤とするテキスト読み上げモデルです。入力テキストから自然な音声を生成します。入力トークンの上限は 2,000 です。

- モデル ID: `gpt-4o-mini-tts`
- 価格（1M トークンあたり）: テキスト入力 $0.60 / 音声出力 $12.00
- 入力モダリティ: テキスト
- 出力モダリティ: 音声

### コーディング

ソフトウェアエンジニアリング向けに最適化されたモデル群です。

#### GPT-5.3-Codex

`gpt-5.3-codex` は公式カタログに掲載中です。仕様・料金は公式モデルページを参照してください。

#### 旧 Codex モデル

| モデル ID | 状態 |
| --- | --- |
| `gpt-5.2-codex` | 2026/07/23 提供終了 |
| `gpt-5.1-codex`, `gpt-5.1-codex-max`, `gpt-5.1-codex-mini`, `gpt-5-codex` | 2026/07/23 提供終了 |

### ディープリサーチ

深い調査タスク向けの旧モデルです。以下はいずれも公式カタログで非推奨とされています。

- `o3-deep-research`
- `o4-mini-deep-research`

### オープンウェイト

Apache 2.0 ライセンスで公開されているモデルウェイト。 HuggingFace から取得し、ローカル/オンプレミスでカスタマイズ・推論可能です。

#### gpt-oss-120b

OpenAI の最も強力なオープンウェイトモデル。 H100 GPU 1枚で動作可能な設計。 117B パラメータ（ 5.1B アクティブ）。

- Reasoning: 非常に高い（推論トークン対応）
- Speed: 中
- 価格: API 課金なし（ダウンロード提供）
- コンテキストウィンドウ: 131,072
- 最大出力トークン: 131,072
- ナレッジカットオフ: 2024/06/01
- 入力モダリティ: テキスト
- 出力モダリティ: テキスト
- 主な特徴:
  - Apache 2.0 ライセンスで自由に利用・再配布可能
  - 推論負荷を調整可能（低／中／高）
  - 推論過程を追跡できる完全な Chain-of-Thought
  - ファインチューニングやエージェント用途（ファンクションコーリング・ウェブブラウジング・ Python コード実行・ Structured outputs 等）に対応

#### gpt-oss-20b

レイテンシの低い、中サイズのオープンウェイトモデル。ローカルや特化したユースケース向き。 21B パラメータ（ 3.6B アクティブパラメータ）。

- Reasoning: 非常に高い（推論トークン対応）
- Speed: 中
- 価格: API 課金なし（オープンウェイト／ダウンロード提供）
- コンテキストウィンドウ: 131,072
- 最大出力トークン: 131,072
- ナレッジカットオフ: 2024/06/01
- 入力モダリティ: テキスト
- 出力モダリティ: テキスト
- 主な特徴:
  - Apache 2.0 ライセンス
  - 推論負荷を調整可能（低／中／高）
  - 推論過程を追跡できる完全な Chain-of-Thought
  - ファインチューニングやエージェント用途（ファンクションコーリング・ウェブブラウジング・ Python コード実行・ Structured outputs 等）に対応

### ChatGPT

公式カタログの ChatGPT models に掲載されているモデルです。ChatGPT 内で使われるモデルで、API 利用は推奨されていません。

#### chat-latest

ChatGPT で使われる Instant モデルのエイリアスです。基盤モデルのスナップショットは固定されず、公式カタログでは API 用途に推奨されていません。

| 旧モデル ID | 状態 |
| --- | --- |
| `gpt-5.3-chat-latest`, `gpt-5.2-chat-latest` | 2026/08/10 提供終了 |
| `gpt-5-chat-latest`, `gpt-5.1-chat-latest` | 2026/07/23 提供終了 |
| `chatgpt-4o-latest` | 2026/02/17 提供終了 |

## その他

上記カテゴリ外の主なモデル ID と公式カタログ上の状態です。

| モデル ID | 状態 |
| --- | --- |
| `o3-pro`, `o3`, `gpt-4.1-mini`, `omni-moderation-latest` | 提供中 |
| `gpt-4.1-nano`, `o4-mini`, `o1-pro`, `computer-use-preview`, `gpt-4o-mini-search-preview`, `gpt-4o-search-preview`, `o3-mini`, `o1`, `o1-mini`, `o1-preview`, `gpt-4.5-preview`, `gpt-3.5-turbo`, `gpt-4`, `gpt-4-turbo`, `text-moderation-latest`, `text-moderation-stable` | 非推奨 |
| `babbage-002`, `davinci-002` | 非推奨（2026/09/28 提供終了） |

### Embedding

テキストをベクトル表現へ変換するモデル群です。

- `text-embedding-3-large`
- `text-embedding-3-small`
- `text-embedding-ada-002`

## 価格

- 多くの料金は 1M トークンあたりです。音声セッション・文字起こしモデルは時間あたりの実際のコストも併記しています。
- 料金は基本的に使用トークン数に基づきます。 Responses API でツールを呼び出す場合はツール呼び出しごとに追加料金が発生することがあります。
- Batch API を利用すると割引料金が適用されます。
- 以下は `Standard` の主な価格です。最新の `Batch` / `Flex` / `Priority` は公式 Pricing ページを参照してください。

### フラッグシップモデル

| モデル | 短コンテキスト入力 | 短コンテキストキャッシュ入力 | 短コンテキスト出力 | 長コンテキスト入力 | 長コンテキストキャッシュ入力 | 長コンテキスト出力 |
| --- | --- | --- | --- | --- | --- | --- |
| GPT-6 Astra (`gpt-6-astra`) | $10.00 | $1.00 | $50.00 | $20.00 | $2.00 | $75.00 |
| GPT-6.1 Sol (`gpt-6.1-sol`) | $2.00 | $0.10 | $10.00 | $4.00 | $0.20 | $15.00 |
| GPT-6 Luna (`gpt-6-luna`) | $0.10 | $0.01 | $0.50 | $0.20 | $0.02 | $0.75 |
| GPT-5.6 Sol (`gpt-5.6`) | $4.00 | $0.40 | $20.00 | $8.00 | $0.80 | $30.00 |
| GPT-5.6 Terra | $2.00 | $0.20 | $12.00 | $4.00 | $0.40 | $18.00 |
| GPT-5.6 Luna | $0.20 | $0.02 | $1.20 | $0.40 | $0.04 | $1.80 |
| GPT-5.5 | $5.00 | $0.50 | $30.00 | $10.00 | $1.00 | $45.00 |
| GPT-5.5 pro | $30.00 | - | $180.00 | - | - | - |
| GPT-5.4 | $2.50 | $0.25 | $15.00 | $5.00 | $0.50 | $22.50 |
| GPT-5.4 mini | $0.75 | $0.075 | $4.50 | - | - | - |
| GPT-5.4 nano | $0.20 | $0.02 | $1.25 | - | - | - |
| GPT-5.4 pro | $30.00 | - | $180.00 | $60.00 | - | $270.00 |

長コンテキスト料金は、入力トークンが 272K を超えるプロンプト全体に適用される倍率（入力・キャッシュ 2 倍、出力 1.5 倍）を反映しています。キャッシュ書き込みは通常の入力料金の 1.25 倍です。

GPT-5.6 Sol の価格はプロモーション価格で、少なくとも 2026/11/21 までは適用されます。

### リアルタイム・音声モデル

| モデル | モダリティ | 入力 | キャッシュ入力 | 出力 |
| --- | --- | --- | --- | --- |
| gpt-realtime-2.1 | Audio | $32.00 | $0.40 | $64.00 |
| gpt-realtime-2.1 | Text | $4.00 | $0.40 | $24.00 |
| gpt-realtime-2.1 | Image | $5.00 | $0.50 | - |
| gpt-realtime-2.1-mini | Audio | $10.00 | $0.30 | $20.00 |
| gpt-realtime-2.1-mini | Text | $0.60 | $0.06 | $2.40 |
| gpt-realtime-2.1-mini | Image | $0.80 | $0.08 | - |
| gpt-realtime-2 | Audio | $32.00 | $0.40 | $64.00 |
| gpt-realtime-2 | Text | $4.00 | $0.40 | $24.00 |
| gpt-realtime-2 | Image | $5.00 | $0.50 | - |
| gpt-realtime-1.5 | Audio | $32.00 | $0.40 | $64.00 |
| gpt-realtime-1.5 | Text | $4.00 | $0.40 | $16.00 |
| gpt-realtime-1.5 | Image | $5.00 | $0.50 | - |
| gpt-realtime-translate | Audio duration | $0.034 / minute | - | - |
| gpt-realtime-whisper | Audio duration | $0.017 / minute | - | - |

### GPT-Live モデル

| モデル | 課金単位 | 実際のコスト | 備考 |
| --- | --- | --- | --- |
| gpt-live-1 | ライブセッション時間 | $0.05 / minute | 秒単位で課金。バックエンドモデル・ツール利用料は別途 |

### 音声生成モデル

| モデル | モダリティ | 入力 | 出力 |
| --- | --- | --- | --- |
| gpt-4o-mini-tts | Text / Audio | $0.60 / 1M tokens | $12.00 / 1M tokens |

### 画像生成モデル

| モデル | モダリティ | 入力 | キャッシュ入力 | 出力 |
| --- | --- | --- | --- | --- |
| gpt-image-2.5-sunburst | Image | $8.00 | $2.00 | $30.00 |
| gpt-image-2.5-sunburst | Text | $5.00 | $1.25 | - |
| gpt-image-2.5-flare | Image | $8.00 | $2.00 | $30.00 |
| gpt-image-2.5-flare | Text | $5.00 | $1.25 | - |
| gpt-image-2 | Image | $8.00 | $2.00 | $30.00 |
| gpt-image-2 | Text | $5.00 | $1.25 | - |

### 動画生成モデル

Sora 2 系モデルは 2026/09/24 に提供終了したため、価格を掲載していません。

### 文字起こしモデル

| モデル | 用途 | 入力 | 出力 | コスト（推定/実際） |
| --- | --- | --- | --- | --- |
| gpt-live-transcribe | Realtime transcription | - | - | 実際: $0.017 / minute |
| gpt-transcribe | Transcription / Realtime input transcription | - | - | 実際: $0.0045 / minute |
| gpt-4o-transcribe | Transcription | $2.50 | $10.00 | 推定: $0.006 / minute |
| gpt-4o-mini-transcribe | Transcription | $1.25 | $5.00 | 推定: $0.003 / minute |

### 特化モデル

| カテゴリ | モデル | 入力 | キャッシュ入力 | 出力 |
| --- | --- | --- | --- | --- |
| ChatGPT | chat-latest | $5.00 | $0.50 | $30.00 |
| Codex | gpt-5.3-codex | $1.75 | $0.175 | $14.00 |

- `gpt-5.5` は 272K を超える入力トークンのプロンプトで、セッション全体に入力 2x / 出力 1.5x の長コンテキスト価格が適用されます。
- `gpt-5.4` と `gpt-5.4-pro` には長コンテキスト価格があります。
- Regional processing（ data residency ）エンドポイントでは、`gpt-5.5` / `gpt-5.5-pro` / `gpt-5.4` / `gpt-5.4-mini` / `gpt-5.4-nano` / `gpt-5.4-pro` に 10% の割増料金が適用されます。

## 利用可能なエンドポイント

いずれも先頭に `v1/` が付きます。

- `chat/completions`
- `responses`
- `realtime` （GPT-5 シリーズは未対応）
- `realtime/translations`
- `realtime/transcription_sessions`
- `assistants`
- `batch`
- `fine-tuning` （GPT-5 シリーズは未対応）
- `embeddings`
- `images/generations`
- `images/edits`
- `audio/speech`
- `audio/transcriptions`
- `audio/translations`
- `moderations`
- `completions` （レガシー）

## ツール

OpenAI API ではモデルと組み合わせて以下のツールや機能を利用できます。対応状況はモデルや API によって異なります。

- Web search （ウェブ検索）
- MCP and Connectors （MCP とコネクタ）
- Skills （スキル）
- Shell （シェル）
- Computer use （コンピューター操作）
- File search and retrieval （ファイル検索と検索拡張）
- Tool search （ツール検索）
- その他
  - Apply Patch （パッチ適用）
  - Local shell （ローカルシェル）
  - Image generation （画像生成）
  - Code interpreter （コードインタプリタ）

## レートリミット

OpenAI の API レートは組織ごとに設定された Usage tier に基づきます。利用額が増えると自動的に次のティアへ昇格し利用上限が引き上げられます。詳細はアカウント設定の limits セクションで確認できます。

| ティア | 条件 | 月間利用上限（月） |
| --- | --- | --- |
| Free | サービス対象地域のユーザー | $100 |
| Tier 1 | $5 支払い済み | $100 |
| Tier 2 | $50 支払い済みかつ初回支払いから 7 日以上経過 | $500 |
| Tier 3 | $100 支払い済みかつ初回支払いから 7 日以上経過 | $1,000 |
| Tier 4 | $250 支払い済みかつ初回支払いから 14 日以上経過 | $5,000 |
| Tier 5 | $1,000 支払い済みかつ初回支払いから 30 日以上経過 | $200,000 |

## 参考

- OpenAI Models: https://developers.openai.com/api/docs/models
- GPT-6.1 Sol: https://developers.openai.com/api/docs/models/gpt-6.1-sol
- Model guidance: https://developers.openai.com/api/docs/guides/latest-model
- Realtime prompting guide: https://developers.openai.com/api/docs/guides/realtime-models-prompting
- Realtime translation: https://developers.openai.com/api/docs/guides/realtime-translation
- Realtime transcription: https://developers.openai.com/api/docs/guides/realtime-transcription
- Pricing: https://developers.openai.com/api/docs/pricing
- Deprecations: https://developers.openai.com/api/docs/deprecations
