
from PIL import Image, ImageDraw
from pathlib import Path
import random

out = Path("output")
out.mkdir(exist_ok=True)

scenes = [
    ("सुनसान गाँव", "रात के बारह बजे पूरा गाँव सो रहा था।"),
    ("पुरानी हवेली", "अचानक हवेली का दरवाज़ा अपने आप खुल गया।"),
    ("डरावना रास्ता", "रवि को पीछे से किसी के चलने की आवाज़ आई।"),
    ("काली परछाईं", "अँधेरे में एक लंबी परछाईं दिखाई दी।"),
    ("बंद कमरा", "कमरे के अंदर से आवाज़ आई—मुझे बाहर निकालो!"),
    ("खौफनाक अंत", "रवि ने पीछे देखा, वहाँ उसका ही भूत खड़ा था!")
]

story = []

for i, (title, line) in enumerate(scenes, 1):
    img = Image.new("RGB", (1280, 720), (12, 12, 22))
    draw = ImageDraw.Draw(img)

    draw.ellipse((900, 70, 1030, 200), fill=(170, 170, 185))
    draw.rectangle((380, 280, 850, 650), fill=(35, 32, 43))
    draw.polygon(
        [(330, 280), (615, 100), (900, 280)],
        fill=(55, 40, 55)
    )
    draw.rectangle((550, 420, 680, 650), fill=(5, 5, 10))

    for _ in range(100):
        x = random.randint(0, 1279)
        y = random.randint(200, 719)
        draw.point((x, y), fill=(70, 75, 85))

    draw.text((50, 40), f"SCENE {i}", fill=(230, 50, 50))
    draw.text((50, 90), title, fill="white")
    img.save(out / f"scene{i}.png")
    story.append(f"{title}\n{line}")

(out / "story.txt").write_text(
    "\n\n".join(story), encoding="utf-8"
)

print("6 horror scene images and story created!")

