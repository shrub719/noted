import sys, markdown
from pathlib import Path

TEMPLATE_PATH = Path("/home/andrei/notes/build/template.html")
MD_EXT = [
    "extra"
]
OUTPUT_PATH = Path("/home/andrei/notes/view")

def convert(file):
    lines = file.read_text(encoding="utf-8").splitlines(keepends=True)

    id = file.stem
    md = "".join(lines).replace("\\", "&#92;")
    body = markdown.markdown(
        md,
        extensions=MD_EXT
    )
    template = TEMPLATE_PATH.read_text(encoding="utf-8")

    html = template.format(
        id=id,
        body=body
    )

    (OUTPUT_PATH / f"{id}.html").write_text(html, encoding="utf-8")

    print("noted: " + id)

if __name__ == "__main__":
    convert(Path(sys.argv[1]))

