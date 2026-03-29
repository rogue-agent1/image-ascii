#!/usr/bin/env python3
"""Image to ASCII - Convert PBM/PGM images to ASCII art."""
import sys

CHARS = " .:-=+*#%@"

def pgm_to_ascii(data, width=80):
    lines = data.strip().split("\n")
    magic = lines[0]
    idx = 1
    while lines[idx].startswith("#"): idx += 1
    w, h = map(int, lines[idx].split()); idx += 1
    maxval = int(lines[idx]); idx += 1
    pixels = []
    for line in lines[idx:]:
        pixels.extend(int(x) for x in line.split())
    scale_x = max(1, w // width); scale_y = max(1, h // (width // 2))
    result = []
    for y in range(0, h, scale_y):
        row = ""
        for x in range(0, w, scale_x):
            if y < h and x < w:
                v = pixels[y * w + x]
                idx_c = int(v / maxval * (len(CHARS) - 1))
                row += CHARS[idx_c]
        result.append(row)
    return "\n".join(result)

def gradient_demo(width=70, height=20):
    lines = []
    for y in range(height):
        row = ""
        for x in range(width):
            v = (x / width + y / height) / 2
            row += CHARS[int(v * (len(CHARS) - 1))]
        lines.append(row)
    return "\n".join(lines)

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            print(pgm_to_ascii(f.read()))
    else:
        print("=== Image to ASCII ===\n")
        print("Gradient demo:")
        print(gradient_demo())
        print(f"\nCharset: {''.join(CHARS)} (dark to light)")
        print("Usage: image_ascii.py <file.pgm> [width]")

if __name__ == "__main__":
    main()
