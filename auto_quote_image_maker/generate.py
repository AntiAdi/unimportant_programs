import os
import re
import string
import sys
from PIL import Image, ImageDraw, ImageFont

# ===============================
# ======== CONFIG SECTION =======
# ===============================

WIDTH, HEIGHT = 1080, 1350
FONT_PATH = "font.ttf"
FONT_SIZE = 70
LINE_SPACING_MULTIPLIER = 1.78
TEXT_COLOR = (255, 255, 255)
RED_COLOR = (255, 0, 0)
BG_COLOR = (0, 0, 0)
MARGIN_X = 80
MAX_TEXT_WIDTH = WIDTH - 2 * MARGIN_X

# ===============================
# ====== DYNAMIC ARGS ===========
# ===============================

BASE_OUTPUT_DIR = "output"  # Top-level output directory
QUOTE_FILE = "quotes.txt"

# Defaults to subfolder 'default' under 'output'
SUB_OUTPUT_FOLDER = "default"

# Override if passed via CLI
if len(sys.argv) > 1:
    SUB_OUTPUT_FOLDER = sys.argv[1]
if len(sys.argv) > 2:
    QUOTE_FILE = sys.argv[2]

# Create full output path
OUTPUT_DIR = os.path.join(BASE_OUTPUT_DIR, SUB_OUTPUT_FOLDER)
os.makedirs(OUTPUT_DIR, exist_ok=True)

font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

# ===============================
# ===== TEXT CLEANUP FUNC =======
# ===============================

def process_quote(quote):
    quote = quote.strip()
    if not quote.endswith('.'):
        quote += '.'
    quote = re.sub(r'([.,] )([a-z])', lambda m: m.group(1) + m.group(2).upper(), quote)
    return quote

# ===============================
# ===== IMAGE GENERATION ========
# ===============================

def create_image(quote, index):
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    quote = process_quote(quote)
    words = quote.split()

    def measure_line(words_list):
        total_width = 0
        space_width = draw.textlength(' ', font=font)
        for w in words_list:
            core = w[1:] if w.startswith('-') else w
            core = core.rstrip(string.punctuation)
            total_width += draw.textlength(core.upper() if w.startswith('-') else core, font=font) + space_width
        return total_width

    lines = []
    current_line = []

    for word in words:
        test_line = current_line + [word]
        if measure_line(test_line) > MAX_TEXT_WIDTH:
            if current_line:
                lines.append(current_line)
            current_line = [word]
        else:
            current_line = test_line
    if current_line:
        lines.append(current_line)

    line_height = int(FONT_SIZE * LINE_SPACING_MULTIPLIER)
    y = (HEIGHT - len(lines) * line_height) // 2

    for line in lines:
        x = MARGIN_X
        for word in line:
            if word.startswith('-'):
                core = word[1:]
                trailing_punct = ''
                while core and core[-1] in string.punctuation:
                    trailing_punct = core[-1] + trailing_punct
                    core = core[:-1]
                draw.text((x, y), core.upper(), font=font, fill=RED_COLOR)
                x += draw.textlength(core.upper(), font=font)
                if trailing_punct:
                    draw.text((x, y), trailing_punct, font=font, fill=TEXT_COLOR)
                    x += draw.textlength(trailing_punct, font=font)
                x += draw.textlength(" ", font=font)
            else:
                draw_word = word + " "
                draw.text((x, y), draw_word, font=font, fill=TEXT_COLOR)
                x += draw.textlength(draw_word, font=font)
        y += line_height

    watermark_text = "@gl1tch.protocol"
    watermark_font_size = 25
    watermark_font = ImageFont.truetype(FONT_PATH, watermark_font_size)

    img_rgba = img.convert("RGBA")
    watermark_layer = Image.new("RGBA", img_rgba.size, (0, 0, 0, 0))
    draw_watermark = ImageDraw.Draw(watermark_layer)

    text_width = draw_watermark.textlength(watermark_text, font=watermark_font)
    wm_x = (WIDTH - text_width) // 2
    wm_y = HEIGHT - watermark_font_size - 40
    draw_watermark.text((wm_x, wm_y), watermark_text, font=watermark_font, fill=(255, 255, 255, 64))

    final_img = Image.alpha_composite(img_rgba, watermark_layer).convert("RGB")
    final_img.save(os.path.join(OUTPUT_DIR, f"quote_{index}.png"))

# ===============================
# ========= RUN LOOP ============
# ===============================

with open(QUOTE_FILE, "r", encoding="utf-8") as f:
    quotes = [line.strip() for line in f if line.strip()]

for i, quote in enumerate(quotes):
    create_image(quote, i)
    if i % 100 == 0:
        print(f"Generated: {i} images...")

print(f"✅ All quote images generated in folder: {OUTPUT_DIR}")