from math import copysign, cos, pi, sin
from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
MASTER_SIZE = 1024
ADAPTIVE_SCALE = 2 / 3
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


def adaptive(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    return [
        (
            54 + (x - 54) * ADAPTIVE_SCALE,
            54 + (y - 54) * ADAPTIVE_SCALE,
        )
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


def build_adaptive_layers() -> Image.Image:
    image = Image.new("RGBA", (MASTER_SIZE, MASTER_SIZE), "#F7F2E8")
    draw = ImageDraw.Draw(image)
    draw.rectangle(
        scaled(
            [
                (54 + (50 - 54) * ADAPTIVE_SCALE, 0),
                (54 + (58 - 54) * ADAPTIVE_SCALE, 108),
            ]
        ),
        fill="#A92DAF",
    )
    draw.polygon(
        scaled(
            adaptive(
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
            )
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
        scaled(adaptive(bowl)),
        fill="#E53935",
        width=round(MASTER_SIZE * 12 / 108 * ADAPTIVE_SCALE),
        joint="curve",
    )
    draw.line(
        scaled(adaptive([(71, 54), (89, 84)])),
        fill="#E53935",
        width=round(MASTER_SIZE * 14 / 108 * ADAPTIVE_SCALE),
    )
    return image


def build_adaptive_preview() -> Image.Image:
    layers = build_adaptive_layers()
    tile_size = 320
    margin = 48
    preview = Image.new(
        "RGB",
        (tile_size * 3 + margin * 4, tile_size + margin * 2),
        "#202124",
    )
    inset = round(MASTER_SIZE * 18 / 108)
    bounds = (inset, inset, MASTER_SIZE - inset, MASTER_SIZE - inset)

    masks: list[Image.Image] = []
    circle = Image.new("L", (MASTER_SIZE, MASTER_SIZE), 0)
    ImageDraw.Draw(circle).ellipse(bounds, fill=255)
    masks.append(circle)

    rounded = Image.new("L", (MASTER_SIZE, MASTER_SIZE), 0)
    ImageDraw.Draw(rounded).rounded_rectangle(
        bounds,
        radius=round((MASTER_SIZE - inset * 2) * 0.22),
        fill=255,
    )
    masks.append(rounded)

    squircle = Image.new("L", (MASTER_SIZE, MASTER_SIZE), 0)
    center = MASTER_SIZE / 2
    radius = (MASTER_SIZE - inset * 2) / 2
    points = []
    for step in range(256):
        angle = 2 * pi * step / 256
        x = center + radius * copysign(abs(cos(angle)) ** 0.5, cos(angle))
        y = center + radius * copysign(abs(sin(angle)) ** 0.5, sin(angle))
        points.append((round(x), round(y)))
    ImageDraw.Draw(squircle).polygon(points, fill=255)
    masks.append(squircle)

    for index, mask in enumerate(masks):
        masked = Image.new("RGBA", (MASTER_SIZE, MASTER_SIZE), (0, 0, 0, 0))
        masked.paste(layers, (0, 0), mask)
        icon = masked.crop(bounds).resize(
            (tile_size, tile_size),
            Image.Resampling.LANCZOS,
        )
        preview.paste(icon, (margin + index * (tile_size + margin), margin), icon)
    return preview


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

    preview = ROOT / "build" / "branding" / "haru_adaptive_masks.png"
    preview.parent.mkdir(parents=True, exist_ok=True)
    build_adaptive_preview().save(preview, optimize=True)


if __name__ == "__main__":
    main()
