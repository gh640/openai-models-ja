"""モデル一覧を取得して出力する

- 環境変数 `OPENAI_API_KEY` に permissions:All の API キーをセットして使用してください
"""

import csv
import os
import sys
from dataclasses import asdict, dataclass, fields
from datetime import datetime
from typing import Self, TextIO

from openai import OpenAI
from openai.types.model import Model as OpenAIModel


@dataclass
class Model:
    """モデル

    - オリジナルには `object` がありますがいずれも値が `"model"` なので対応するフィールドはありません
    """

    id: str
    owned_by: str
    created: datetime

    @classmethod
    def fieldnames(cls) -> list[str]:
        return [x.name for x in fields(cls)]

    @classmethod
    def from_raw(cls, model) -> Self:
        return cls(
            id=model.id,
            owned_by=model.owned_by,
            created=dt_from_ts(model.created),
        )


def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        sys.exit("Environment variable `OPENAI_API_KEY` needs to be set.")

    # 取得する
    client = OpenAI(api_key=api_key)
    pages = client.models.list().iter_pages()

    models = (m for page in pages for m in page.data if is_official_model(m))
    models = (Model.from_raw(m) for m in models)
    # 最新順
    models = sorted(models, key=lambda x: x.created, reverse=True)

    # 出力する
    write_to_csv(sys.stdout, models)


def is_official_model(model: OpenAIModel) -> bool:
    return not is_user_model(model)


def is_user_model(model: OpenAIModel) -> bool:
    return model.owned_by.startswith("user-")


def dt_from_ts(ts: int) -> datetime:
    return datetime.fromtimestamp(ts)


def write_to_csv(file: TextIO, models: list[Model]) -> None:
    writer = csv.DictWriter(file, fieldnames=Model.fieldnames())
    writer.writeheader()
    writer.writerows(asdict(m) for m in models)


if __name__ == "__main__":
    main()
