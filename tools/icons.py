from PIL import Image, ImageDraw
import sys, os
out = sys.argv[1]
def make(S):
    k = 4  # supersampling
    N = S * k
    im = Image.new('RGB', (N, N), '#123A5E')
    d = ImageDraw.Draw(im)
    step = N // 16
    for i in range(0, N + 1, step):
        c = '#1B4C78' if (i // step) % 4 else '#256392'
        d.line([(i, 0), (i, N)], fill=c, width=max(1, N // 256))
        d.line([(0, i), (N, i)], fill=c, width=max(1, N // 256))
    cx, cy = N / 2, N * 0.60
    w = N * 0.17   # medio ancho de arista en x
    h = w * 0.5
    H = N * 0.30   # altura del edificio
    top = [(cx, cy - H - h), (cx + w, cy - H), (cx, cy - H + h), (cx - w, cy - H)]
    left = [(cx - w, cy - H), (cx, cy - H + h), (cx, cy + h), (cx - w, cy)]
    right = [(cx + w, cy - H), (cx, cy - H + h), (cx, cy + h), (cx + w, cy)]
    # sombra
    d.polygon([(cx - w * 1.15, cy + h * 0.2), (cx, cy + h * 1.25), (cx + w * 1.15, cy + h * 0.2), (cx, cy - h * 0.9)], fill='#0D2D49')
    d.polygon(left, fill='#FFFFFF')
    d.polygon(right, fill='#8FA6BC')
    d.polygon(top, fill='#F2B705')
    d.line(top + [top[0]], fill='#C48F00', width=max(2, N // 120))
    # ventanas azules
    for row in range(4):
        for col in range(2):
            u0 = 0.14 + col * 0.42; u1 = u0 + 0.28
            v0 = 0.10 + row * 0.22; v1 = v0 + 0.13
            def L(u, v):
                x = cx - w + w * u; yb = cy - H + h * u
                return (x, yb + H * v)
            def R(u, v):
                x = cx + w * u; yb = cy - H + h - h * u
                return (x, yb + H * v)
            d.polygon([L(u0, v0), L(u1, v0), L(u1, v1), L(u0, v1)], fill='#2C6AA3')
            d.polygon([R(u0, v0), R(u1, v0), R(u1, v1), R(u0, v1)], fill='#2C6AA3')
    return im.resize((S, S), Image.LANCZOS)
for s in (180, 192, 512):
    make(s).save(os.path.join(out, f'icon-{s}.png'))
print('ok')
