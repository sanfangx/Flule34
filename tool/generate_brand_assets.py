from math import cos, pi, sin
from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
MASTER_SIZE = 1024
OUTPUT_SIZES = {
    "mipmap-mdpi": 48,
    "mipmap-hdpi": 72,
    "mipmap-xhdpi": 96,
    "mipmap-xxhdpi": 144,
    "mipmap-xxxhdpi": 192,
}


def scaled(points: list[tuple[float, float]]) -> list[tuple[int, int]]:
    return [
        (round(x * MASTER_SIZE / 108), round(y * MASTER_SIZE / 108))
        for x, y in points
    ]


def build_master() -> Image.Image:
    image = Image.new("RGBA", (MASTER_SIZE, MASTER_SIZE), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle(
        (0, 0, MASTER_SIZE - 1, MASTER_SIZE - 1),
        radius=round(MASTER_SIZE * 24 / 108),
        fill="#F7F2E8",
    )
    draw.rectangle(scaled([(50, 0), (58, 108)]), fill="#A92DAF")
    draw.polygon(
        scaled(
            [
                (19, 24),
                (33, 24),
                (33, 48),
                (50, 48),
                (50, 60),
                (33, 60),
                (33, 84),
                (19, 84),
            ]
        ),
        fill="#E53935",
    )

    bowl = [(58, 30), (76, 30)]
    bowl.extend(
        (76 + 12 * sin(pi * step / 24), 42 - 12 * cos(pi * step / 24))
        for step in range(1, 25)
    )
    bowl.append((58, 54))
    draw.line(
        scaled(bowl),
        fill="#E53935",
        width=round(MASTER_SIZE * 12 / 108),
        joint="curve",
    )
    draw.line(
        scaled([(71, 54), (89, 84)]),
        fill="#E53935",
        width=round(MASTER_SIZE * 14 / 108),
    )
    return image


def main() -> None:
    master = build_master()
    branding = ROOT / "assets" / "branding"
    branding.mkdir(parents=True, exist_ok=True)
    master.save(branding / "haru_icon_master.png", optimize=True)

    resources = ROOT / "android" / "app" / "src" / "main" / "res"
    for directory, size in OUTPUT_SIZES.items():
        output = resources / directory / "ic_launcher.png"
        output.parent.mkdir(parents=True, exist_ok=True)
        master.resize((size, size), Image.Resampling.LANCZOS).save(
            output,
            optimize=True,
        )


if __name__ == "__main__":
    main()
