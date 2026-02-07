# generate_marc_math_mega.py
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import random

W, H = A4
M = 18*mm
TOTAL = 20

# Font cu diacritice (DejaVu)
pdfmetrics.registerFont(TTFont("DejaVu", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))

OUT = "Marc_Matematica_1-10_Mega_Aerisite_Setul_1.pdf"
c = canvas.Canvas(OUT, pagesize=A4)

BOTTOM_RESERVED = 55*mm
TOP_AFTER_HEADER = 62*mm

def bg():
    c.setFillColor(colors.whitesmoke)
    c.rect(0, 0, W, H, stroke=0, fill=1)

def header(page_no, subtitle):
    bg()
    c.setFillColor(colors.black)
    c.setFont("DejaVu-Bold", 18)
    c.drawString(M, H-22*mm, "Marc • Matematică (1–10) • MEGA AERISIT")
    c.setFont("DejaVu", 11.5)
    c.drawString(M, H-30*mm, subtitle)

    c.setStrokeColor(colors.black); c.setLineWidth(1.2)
    c.roundRect(M, H-42*mm, 94*mm, 10*mm, 3*mm, stroke=1, fill=0)
    c.roundRect(M+98*mm, H-42*mm, 78*mm, 10*mm, 3*mm, stroke=1, fill=0)
    c.setFont("DejaVu", 9.5)
    c.drawString(M+2*mm, H-38.5*mm, "Nume: ____________________")
    c.drawString(M+100*mm, H-38.5*mm, "Data: ____ / ____ / ____")

    c.setFont("DejaVu", 9)
    c.setFillColor(colors.grey)
    c.drawRightString(W-M, 10*mm, f"Pagina {page_no}/{TOTAL}")
    c.setFillColor(colors.black)

def sticker_area(tip_text):
    y = 18*mm
    c.setFillColor(colors.black)
    c.setFont("DejaVu-Bold", 12)
    c.drawString(M, y+28*mm, "Sticker / recompensă:")
    c.setStrokeColor(colors.black); c.setLineWidth(1.3)
    c.roundRect(M, y, 82*mm, 24*mm, 6*mm, stroke=1, fill=0)
    c.setFont("DejaVu", 10)
    c.drawString(M+88*mm, y+5*mm, "Tip: " + tip_text)

def blocks(n):
    y_top = H - TOP_AFTER_HEADER
    y_bot = BOTTOM_RESERVED
    height = y_top - y_bot
    gap = 8*mm
    block_h = (height - (n-1)*gap) / n
    res = []
    cur_top = y_top
    for _ in range(n):
        top = cur_top
        bottom = cur_top - block_h
        res.append((top, bottom))
        cur_top = bottom - gap
    return res

def section_title(y, text):
    c.setFont("DejaVu-Bold", 14)
    c.setFillColor(colors.black)
    c.drawString(M, y, text)
    c.setStrokeColor(colors.lightgrey); c.setLineWidth(1)
    c.line(M, y-4*mm, W-M, y-4*mm)

def answer_box(x, y, w=38*mm, h=26*mm):
    c.setStrokeColor(colors.black); c.setLineWidth(1.5)
    c.roundRect(x, y, w, h, 4*mm, stroke=1, fill=0)

def dot(x, y, r=4.7*mm, crossed=False):
    c.setStrokeColor(colors.black); c.setLineWidth(1.3)
    c.setFillColor(colors.white)
    c.circle(x, y, r, stroke=1, fill=1)
    if crossed:
        c.setStrokeColor(colors.black); c.setLineWidth(1.3)
        c.line(x-r*0.75, y-r*0.75, x+r*0.75, y+r*0.75)
        c.line(x-r*0.75, y+r*0.75, x+r*0.75, y-r*0.75)

def dot_box(y, n):
    x = M
    w = W - 2*M
    h = 58*mm
    c.setStrokeColor(colors.black); c.setLineWidth(1.3)
    c.roundRect(x, y, w, h, 6*mm, stroke=1, fill=0)
    answer_box(x+w-44*mm, y+(h-26*mm)/2, 38*mm, 26*mm)
    # dot grid (left safe zone)
    left_w = w - 60*mm
    cols, rows = 5, 2
    dx = left_w/(cols+1)
    dy = h/(rows+1)
    pts = []
    for r in range(rows):
        for col in range(cols):
            pts.append((x+10*mm + (col+0.8)*dx, y + (r+1)*dy))
    for i in range(n):
        dot(*pts[i])

def big_eq(y, a, op, b):
    c.setFont("DejaVu-Bold", 34)
    c.setFillColor(colors.black)
    c.drawString(M+16*mm, y, f"{a} {op} {b} =")
    answer_box(M+110*mm, y-8*mm, 42*mm, 28*mm)

random.seed(2026)

# P1
header(1, "Fișa 1 — Start!")
b = blocks(2)
section_title(b[0][0]-10*mm, "Reguli:")
c.setFont("DejaVu", 13.5)
rules = [
    "1) 5–10 minute sunt perfecte.",
    "2) Dacă nu știi, desenează puncte (•) și numără.",
    "3) Greșeala e ok: ștergi și încerci din nou.",
    "4) După fiecare pagină: sticker ⭐",
]
yy = b[0][0]-26*mm
for t in rules:
    c.drawString(M+6*mm, yy, t); yy -= 14*mm
section_title(b[1][0]-10*mm, "Exemple:")
c.setFont("DejaVu-Bold", 34)
c.drawString(M+16*mm, b[1][0]-40*mm, "3 + 2 ="); answer_box(M+110*mm, b[1][0]-48*mm, 42*mm, 28*mm)
c.drawString(M+16*mm, b[1][0]-78*mm, "7 − 4 ="); answer_box(M+110*mm, b[1][0]-86*mm, 42*mm, 28*mm)
sticker_area("termină cu zâmbetul."); c.showPage()

# P2-3 dot count
for p in [2,3]:
    header(p, f"Fișa {p} — Numără punctele")
    c.setFont("DejaVu", 12.5); c.drawString(M, H-58*mm, "2 exerciții, foarte mari.")
    b = blocks(2)
    dot_box(b[0][1]+6*mm, random.randint(1,10))
    dot_box(b[1][1]+6*mm, random.randint(1,10))
    sticker_area("numără cu degetul."); c.showPage()

# P4 add dots (2)
header(4, "Fișa 4 — Adunări cu puncte")
b = blocks(2)
for i,(top,bottom) in enumerate(b, start=1):
    section_title(top-10*mm, f"Exercițiul {i}")
    a = random.randint(1,5); b2 = random.randint(1,5)
    while a+b2 > 10: a = random.randint(1,5); b2 = random.randint(1,5)
    ymid = (top+bottom)/2
    x = M+16*mm
    for k in range(a): dot(x+k*14*mm, ymid, r=4.6*mm)
    c.setFont("DejaVu-Bold", 28); c.drawString(M+90*mm, ymid-10*mm, "+")
    for k in range(b2): dot(M+112*mm+k*14*mm, ymid, r=4.6*mm)
    c.drawString(W-86*mm, ymid-10*mm, "="); answer_box(W-64*mm, ymid-14*mm, 38*mm, 26*mm)
sticker_area("numără toate punctele."); c.showPage()

# P5-6 big additions (3)
for p in [5,6]:
    header(p, f"Fișa {p} — Adunări (max. 10)")
    b = blocks(3)
    for i,(top,bottom) in enumerate(b, start=1):
        section_title(top-10*mm, f"Exercițiul {i}")
        a = random.randint(0,10); b2 = random.randint(0,10-a)
        big_eq((top+bottom)/2-10*mm, a, "+", b2)
    sticker_area("5 + 5 = 10."); c.showPage()

# P7-8 big subtractions (3)
for p in [7,8]:
    header(p, f"Fișa {p} — Scăderi (0–10)")
    b = blocks(3)
    for i,(top,bottom) in enumerate(b, start=1):
        section_title(top-10*mm, f"Exercițiul {i}")
        a = random.randint(1,10); b2 = random.randint(0,a)
        big_eq((top+bottom)/2-10*mm, a, "−", b2)
    sticker_area("0 e ok!"); c.showPage()

# P9-10 make 10 (2)
for p in [9,10]:
    header(p, f"Fișa {p} — Până la 10")
    b = blocks(2)
    for i,(top,bottom) in enumerate(b, start=1):
        section_title(top-10*mm, f"Exercițiul {i}")
        filled = random.randint(1,9)
        y = (top+bottom)/2-18*mm
        # simplu: scrie doar ecuația
        c.setFont("DejaVu-Bold", 30)
        c.drawString(M+16*mm, y, f"{filled} + ____ = 10")
        answer_box(M+120*mm, y-8*mm, 42*mm, 28*mm)
    sticker_area("gândește: 10 - ce ai."); c.showPage()

# P11-12 missing number (3)
for p in [11,12]:
    header(p, f"Fișa {p} — Numărul lipsă")
    b = blocks(3)
    for i,(top,bottom) in enumerate(b, start=1):
        section_title(top-10*mm, f"Exercițiul {i}")
        if i%2==1:
            cval = random.randint(4,10); aval = random.randint(1,cval-1); b2 = cval-aval
            miss = random.choice(["a","b"])
            y = (top+bottom)/2-10*mm
            c.setFont("DejaVu-Bold", 30)
            if miss=="a": answer_box(M+16*mm, y-8*mm, 42*mm, 28*mm)
            else: c.drawString(M+16*mm, y, str(aval))
            c.drawString(M+70*mm, y, "+")
            if miss=="b": answer_box(M+86*mm, y-8*mm, 42*mm, 28*mm)
            else: c.drawString(M+90*mm, y, str(b2))
            c.drawString(M+140*mm, y, "="); c.drawString(M+158*mm, y, str(cval))
        else:
            a = random.randint(4,10); b2 = random.randint(0,a-1); r = a-b2
            y = (top+bottom)/2-10*mm
            c.setFont("DejaVu-Bold", 30)
            answer_box(M+16*mm, y-8*mm, 42*mm, 28*mm)
            c.drawString(M+70*mm, y, "−"); c.drawString(M+90*mm, y, str(b2))
            c.drawString(M+140*mm, y, "="); c.drawString(M+158*mm, y, str(r))
    sticker_area("verifică o dată."); c.showPage()

# P13 compare (4)
header(13, "Fișa 13 — Compară (<, >, =)")
b = blocks(4)
for i,(top,bottom) in enumerate(b, start=1):
    section_title(top-10*mm, f"Exercițiul {i}")
    a = random.randint(1,10); b2 = random.randint(1,10)
    y = (top+bottom)/2-12*mm
    c.setFont("DejaVu-Bold", 38)
    c.drawString(M+30*mm, y, str(a))
    answer_box(M+70*mm, y-10*mm, 44*mm, 28*mm)
    c.drawString(M+130*mm, y, str(b2))
sticker_area("mai mare = mai multe."); c.showPage()

# P14 number line
header(14, "Fișa 14 — Linia numerelor")
c.setFont("DejaVu-Bold", 26)
c.drawString(M+16*mm, H/2, "1, 2, __, 4, 5, __, 7, __, 9, 10")
sticker_area("în ordine e ușor."); c.showPage()

# P15-16 problems (2 each)
for p in [15,16]:
    header(p, f"Fișa {p} — Probleme")
    c.setFont("DejaVu", 14)
    t1 = "Am 3 mere. Mai primesc 2. Câte am?  Răspuns: _______"
    t2 = "Aveam 8 baloane. Dau 5. Câte rămân?  Răspuns: _______"
    if p==16:
        t1 = "Am 4 mașini. Mai vin 1. Câte sunt?  Răspuns: _______"
        t2 = "Am 9 biscuiți. Mănânc 4. Câți rămân?  Răspuns: _______"
    c.drawString(M+10*mm, H-120*mm, "1) " + t1)
    c.drawString(M+10*mm, H-170*mm, "2) " + t2)
    sticker_area("desenele te ajută."); c.showPage()

# P17-18 mini rapid
for p in [17,18]:
    header(p, f"Fișa {p} — Mini-rapid")
    c.setFont("DejaVu-Bold", 24)
    y = H-110*mm
    for _ in range(6):
        a = random.randint(0,10)
        if random.random()<0.5:
            b2 = random.randint(0,10-a); op="+"
        else:
            if a==0: a= random.randint(1,10)
            b2 = random.randint(0,a); op="−"
        c.drawString(M+16*mm, y, f"{a} {op} {b2} = _______")
        y -= 28*mm
    sticker_area("1 minut e suficient."); c.showPage()

# P19 circle answer
header(19, "Fișa 19 — Încercuiește răspunsul")
c.setFont("DejaVu-Bold", 22)
y = H-110*mm
for i in range(4):
    a = random.randint(0,10); b2 = random.randint(0,10-a)
    ans = a+b2
    c.drawString(M+16*mm, y, f"{a} + {b2} =   ({ans-1})   ({ans})   ({ans+1})")
    y -= 32*mm
sticker_area("încercuiește fără grabă."); c.showPage()

# P20 diploma
header(20, "Fișa 20 — Diplomă")
c.setFont("DejaVu-Bold", 18)
c.drawString(M, H-110*mm, "Diplomă de campion la matematică ⭐")
c.setFont("DejaVu", 14)
c.drawString(M, H-140*mm, "Astăzi Marc a fost campion la numărat, adunări și scăderi!")
c.setStrokeColor(colors.black); c.setLineWidth(1.3)
c.roundRect(M, 60*mm, 120*mm, 54*mm, 7*mm, stroke=1, fill=0)
c.setFont("DejaVu-Bold", 13)
c.drawString(M, 120*mm, "Sticker mare aici:")
sticker_area("bravo!"); c.showPage()

c.save()
print("Gata:", OUT)