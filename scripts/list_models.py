"""モデル一覧を取得して出力する

- 環境変数 `OPENAI_API_KEY` に permissions:All の API キーをセットして使用してください
"""

import csv
import sys
from dataclasses import asdict, dataclass, fields
from datetime import datetime

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


def main():
    # 取得する
    client = OpenAI()
    pages = client.models.list().iter_pages()

    models_orig = []
    for p in pages:
        models_orig.extend(filter(is_official_model, p.data))

    models = [
        Model(id=m.id, owned_by=m.owned_by, created=dt_from_ts(m.created))
        for m in models_orig
    ]

    # 最新のものから順に並べる
    models.sort(key=lambda x: x.created, reverse=True)

    # 出力する
    writer = csv.DictWriter(sys.stdout, fieldnames=[x.name for x in fields(Model)])
    writer.writeheader()
    writer.writerows([asdict(m) for m in models])


def is_official_model(model: OpenAIModel) -> bool:
    return not is_user_model(model)


def is_user_model(model: OpenAIModel) -> bool:
    return model.owned_by.startswith("user-")


def dt_from_ts(ts: str) -> datetime:
    return datetime.fromtimestamp(ts)


if __name__ == "__main__":
    main()
