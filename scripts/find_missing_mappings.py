import glob
import os
from pathlib import Path
import yaml

link_map = {}

for path in glob.glob("arcticons-light/scalable/**/*.svg", recursive=True):
    try:
        # SYMLINK

        icon_source_path = os.readlink(path)

        icon_name = Path(icon_source_path).stem

        formatted_path = path.removeprefix("arcticons-light/scalable/").removesuffix(".svg")

        if icon_name not in link_map:
            link_map[icon_name] = []

        link_map[icon_name].append(formatted_path)

    except:
        icon_name = Path(path).stem

        formatted_path = path.removeprefix("arcticons-light/scalable/").removesuffix(".svg")

        if icon_name not in link_map:
            link_map[icon_name] = []

        link_map[icon_name].append(formatted_path)


for name, links in link_map.items():
    print(f"{name}:")
    for link in links:
        print(f"- {link}")
