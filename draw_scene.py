"""Original native-vector editorial study; all games/layout are fictional.
No client work, external assets, fonts redistributed, or playtesting claims.
"""
from pathlib import Path
import math, html, json
from PIL import Image, ImageDraw, ImageFont

OUT=Path(__file__).resolve().parent
W,H=1600,900
objects=[]
def rect(x,y,w,h,fill,r=0,stroke=None,sw=1):
    objects.append(dict(t="rect",xy=(x,y,w,h),fill=fill,r=r,stroke=stroke,sw=sw))
def poly(points,fill,stroke=None,sw=1):
    objects.append(dict(t="poly",points=points,fill=fill,stroke=stroke,sw=sw))
def circle(x,y,r,fill):
    objects.append(dict(t="circle",xy=(x,y,r),fill=fill))
def line(points,fill,sw=2):
    objects.append(dict(t="line",points=points,fill=fill,sw=sw))
def text(x,y,s,size,fill="#F4F4EB",bold=False):
    objects.append(dict(t="text",xy=(x,y),s=s,size=size,fill=fill,bold=bold))
def hexagon(x,y,rx,ry,fill):
    poly([(x+rx*math.cos(i*math.pi/3),y+ry*math.sin(i*math.pi/3)) for i in range(6)],fill,"#15252B",3)

rect(0,0,W,H,"#0D2026")
rect(62,60,1476,780,"#122B32",28)
# Decorative grid and distant stars; intentionally quiet behind the type.
for x,y in [(812,152),(1447,204),(1275,147),(1481,468),(735,663)]:
    circle(x,y,3,"#76999A")
line([(99,132),(525,132)],"#638D8F",2)
text(99,88,"ORIGINAL EDITORIAL ART STUDY",18,"#A8C6C4",True)
text(98,194,"TABLETOP",74,bold=True)
text(98,278,"WORLDS",74,bold=True)
text(103,395,"Small pieces.",29,"#BACCC6")
text(103,440,"Room for a bigger story.",29,"#BACCC6")
rect(101,524,304,51,"#E9B66F",25)
text(125,537,"FICTIONAL LANDSCAPE",16,"#15252B",True)
# Stylized game-board coastline made from original hex geometry.
tiles=[
 (895,334,"#638F78"),(1010,334,"#6C9C83"),(1125,334,"#57806E"),
 (837,405,"#527768"),(952,405,"#789E81"),(1067,405,"#719779"),(1182,405,"#83A78A"),
 (895,476,"#739A80"),(1010,476,"#D2B27C"),(1125,476,"#668A72"),(1240,476,"#426958"),
 (952,547,"#668876"),(1067,547,"#91A085"),(1182,547,"#527866"),
]
# Extruded front edge, then tiles.
for x,y,c in tiles:
    hexagon(x,y+22,74,46,"#244B45")
for x,y,c in tiles:
    hexagon(x,y,74,46,c)
# River through the map; no actual product/game geometry is copied.
line([(837,405),(895,433),(952,405),(1010,432),(1067,405),(1125,433),(1182,405)],"#163E49",18)
line([(837,405),(895,433),(952,405),(1010,432),(1067,405),(1125,433),(1182,405)],"#8BC6CB",8)
# Tiny trees.
for x,y in [(895,326),(923,344),(1107,460),(1152,472),(978,540),(1206,397)]:
    rect(x-3,y-8,6,31,"#244A40")
    poly([(x,y-44),(x-20,y-9),(x+20,y-9)],"#173D35")
    poly([(x,y-58),(x-15,y-30),(x+15,y-30)],"#234F40")
# Distant mountain tokens.
for x,y in [(1010,319),(1127,316)]:
    poly([(x,y-81),(x-36,y),(x+39,y)],"#284C4C")
    poly([(x,y-81),(x-36,y),(x-1,y-13)],"#386062")
    poly([(x,y-81),(x-13,y-52),(x+13,y-52)],"#DCE8DB")
# Golden pawn. Abstract original polygon, no game-specific marks.
circle(1190,505,35,"#244940")
poly([(1161,466),(1167,433),(1150,432),(1156,414),(1174,413),(1175,391),(1205,391),(1206,413),(1224,414),(1230,432),(1213,433),(1219,466),(1204,466),(1190,445),(1176,466)],"#EBC47F")
circle(1190,383,17,"#F0CC8D")
# Two dice, drawn as geometric objects.
poly([(1270,585),(1344,560),(1418,592),(1344,619)],"#F0EBDC")
poly([(1270,585),(1344,619),(1344,708),(1270,674)],"#B4C8BD")
poly([(1344,619),(1418,592),(1418,681),(1344,708)],"#DBDED0")
for x,y in [(1314,581),(1372,592)]:
    circle(x,y,5,"#284950")
for x,y in [(1290,614),(1323,657),(1359,641),(1398,630),(1380,676)]:
    circle(x,y,6,"#284950")
circle(1096,661,32,"#16323A")
circle(1093,656,26,"#D28C76")
circle(1093,656,16,"#E2AC91")
line([(1085,656),(1101,656)],"#815749",3)
text(102,728,"A native SVG cover illustration built from original shapes.",18,"#A7C4C0")
text(102,770,"Independent portfolio sample | Fictional scene | Not a client commission",16,"#82A8A7")
text(102,809,"Editable SVG + 1600 x 900 PNG",15,"#82A8A7")

# Render scene to original SVG and a faithful PNG export.
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">',
'<title id="title">Tabletop Worlds — original editorial illustration study</title>',
'<desc id="desc">An original geometric game-board landscape with forest hexagons, a river, mountains, a pawn and dice. Fictional portfolio study, not a client commission.</desc>']
scale=2
im=Image.new("RGB",(W*scale,H*scale)); d=ImageDraw.Draw(im)
def px(v): return round(v*scale)
def pts(pp): return [(px(x),px(y)) for x,y in pp]
fontdir=Path(r"C:\Windows\Fonts")
for o in objects:
    t=o["t"]; c=o["fill"]
    if t=="rect":
        x,y,w,h=o["xy"]; r=o["r"]
        svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{c}"/>')
        d.rounded_rectangle((px(x),px(y),px(x+w),px(y+h)),radius=px(r),fill=c)
    elif t=="poly":
        ps=" ".join(f"{x:.2f},{y:.2f}" for x,y in o["points"])
        stroke=f' stroke="{o["stroke"]}" stroke-width="{o["sw"]}" stroke-linejoin="round"' if o["stroke"] else ""
        svg.append(f'<polygon points="{ps}" fill="{c}"{stroke}/>')
        d.polygon(pts(o["points"]),fill=c)
        if o["stroke"]: d.line(pts(o["points"]+[o["points"][0]]),fill=o["stroke"],width=px(o["sw"]),joint="curve")
    elif t=="circle":
        x,y,r=o["xy"]; svg.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>')
        d.ellipse((px(x-r),px(y-r),px(x+r),px(y+r)),fill=c)
    elif t=="line":
        ps=" ".join(f"{x:.2f},{y:.2f}" for x,y in o["points"])
        svg.append(f'<polyline points="{ps}" fill="none" stroke="{c}" stroke-width="{o["sw"]}" stroke-linejoin="round" stroke-linecap="round"/>')
        d.line(pts(o["points"]),fill=c,width=px(o["sw"]),joint="curve")
    else:
        x,y=o["xy"]; fs=o["size"]; bold=o["bold"]
        svg.append(f'<text x="{x}" y="{y}" dominant-baseline="text-before-edge" font-family="Segoe UI,Arial,sans-serif" font-size="{fs}" font-weight="{700 if bold else 400}" fill="{c}">{html.escape(o["s"])}</text>')
        font=ImageFont.truetype(str(fontdir/("segoeuib.ttf" if bold else "segoeui.ttf")),px(fs))
        d.text((px(x),px(y)),o["s"],font=font,fill=c,anchor="lt")
svg.append("</svg>")
(OUT/"tabletop-worlds-study.svg").write_text("\n".join(svg),encoding="utf-8")
im.resize((W,H),Image.Resampling.LANCZOS).save(OUT/"tabletop-worlds-study.png",optimize=True)
(OUT/"sample-spec.json").write_text(json.dumps({"title":"Tabletop Worlds","kind":"Original native-vector editorial cover study","dimensions":[W,H],"customer_materials":False,"scene":"fictional","client_case":False,"external_assets":[],"embedded_scripts":False,"creator_account":"xtddxsh1","workflow":"Codex-assisted original native-vector code with a PNG rendering; no human-drawn claim","scope_for_sale":"One agreed cover/roundup graphic only; price and brief unconfirmed"},indent=2),encoding="utf-8")
print(json.dumps({"svg":str(OUT/"tabletop-worlds-study.svg"),"png":str(OUT/"tabletop-worlds-study.png"),"bytes":(OUT/"tabletop-worlds-study.png").stat().st_size}))
