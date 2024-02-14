"""モデル一覧を取得して出力する

- 環境変数 `OPENAI_API_KEY` に permissions:All の API キーをセットして使用してください
"""

import csv
import sys
from dataclasses import asdict, dataclass, fields
from datetime import datetime

from openai import OpenAI


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
    models = []
    for p in pages:
        models.extend(
            Model(
                id=m.id,
                owned_by=m.owned_by,
                created=datetime.fromtimestamp(m.created),
            )
            for m in p.data
        )

    # 最新のものから順に並べる
    models.sort(key=lambda x: x.created, reverse=True)

    # 出力する
    writer = csv.DictWriter(sys.stdout, fieldnames=[x.name for x in fields(Model)])
    writer.writeheader()
    writer.writerows([asdict(m) for m in models])


if __name__ == "__main__":
    main()
