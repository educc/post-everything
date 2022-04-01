import os
from pathlib import Path

from fastapi import FastAPI, Request

app = FastAPI()

OUT_DIR = Path(os.path.realpath(__file__)).parent / "out"
OUT_DIR.mkdir(exist_ok=True)


def create_tree(uri: str) -> Path:
    """
    It creates a directory tree according to the URI paths.
    Example: uri=api/other/person.json
    Result: directory at: out/api/other
    """
    parent_dir = (OUT_DIR / uri).parent
    parent_dir.mkdir(exist_ok=True)
    return parent_dir


@app.post("/{rest_of_path:path}")
async def root(rest_of_path: str, request: Request):
    dir_path: Path = create_tree(rest_of_path)
    abs_path: Path = dir_path / os.path.basename(rest_of_path)

    with abs_path.open("wb") as f:
        data: bytes = await request.body()
        f.write(data)
    return {"message": f"File saved at {abs_path}"}
