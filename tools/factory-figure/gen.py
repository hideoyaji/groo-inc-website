# -*- coding: utf-8 -*-
import os
X0, W, DX, DY = 230, 520, 175, -55
CUT = X0 + W          # 750 手前カット位置
BR  = X0 + W + DX     # 925 奥右
BL  = X0 + DX         # 405 奥左

def P(u, v, Y, z=0):
    return (X0 + u + DX*v, Y - 55*v - z)
def f(x): 
    return ("%.2f" % x).rstrip("0").rstrip(".")
def pts(*ps):
    return " ".join(f"{f(x)},{f(y)}" for x, y in ps)

out = []
INDENT = " " * 8   # factory.html 本文と同じ深さ
def w(s):
    for line in s.split("\n"):
        out.append(INDENT + line.strip() if line.strip() else "")

# ---- 階の床レベル (手前エッジ y) ----
B3, B1, F1, F2, F3, F4, RF = 756, 564, 468, 372, 276, 180, 84
GROUND = F1   # 地面 = 1F 床

def slab(Y):
    w(f'          <polygon points="{pts((X0,Y),(CUT,Y),(BR,Y+DY),(BL,Y+DY))}" fill="var(--slab)"/>')
    w(f'          <polygon points="{pts((X0,Y),(CUT,Y),(CUT,Y+12),(X0,Y+12))}" fill="var(--slab-edge)"/>')
    w(f'          <polygon points="{pts((CUT,Y),(BR,Y+DY),(BR,Y+DY+12),(CUT,Y+12))}" fill="var(--slab-edge)"/>')

def walls(Yf, Yc):
    w(f'          <polygon points="{pts((BL,Yf+DY),(BR,Yf+DY),(BR,Yc+DY),(BL,Yc+DY))}" fill="var(--wall-back)"/>')
    w(f'          <polygon points="{pts((X0,Yf),(BL,Yf+DY),(BL,Yc+DY),(X0,Yc))}" fill="var(--wall-left)"/>')

def box(u0,u1,v0,v1,Y,h,fill_top="var(--furn)",fill_front="var(--slab-edge)"):
    a=P(u0,v0,Y); b=P(u1,v0,Y); c=P(u1,v1,Y); d=P(u0,v1,Y)
    w(f'          <polygon points="{pts((a[0],a[1]-h),(b[0],b[1]-h),(b[0],b[1]),(a[0],a[1]))}" fill="{fill_front}"/>')
    w(f'          <polygon points="{pts((a[0],a[1]-h),(b[0],b[1]-h),(c[0],c[1]-h),(d[0],d[1]-h))}" fill="{fill_top}"/>')

def person(u,v,Y,kind="fig",rot=0,sc=1.0,z=0):
    x,y = P(u,v,Y,z)
    t=f'translate({f(x)},{f(y)})'
    if rot: t+=f' rotate({rot})'
    if sc!=1.0: t+=f' scale({sc})'
    w(f'            <g transform="{t}"><use href="#fac-{kind}"/></g>')

def table(u,v,Y,h=28,rx=24,ry=8.5):
    x,y=P(u,v,Y)
    w(f'          <g fill="var(--furn)" stroke="var(--slab-edge)" stroke-width="1">')
    w(f'            <rect x="{f(x-1.5)}" y="{f(y-h)}" width="3" height="{h}"/>')
    w(f'            <ellipse cx="{f(x)}" cy="{f(y-h)}" rx="{rx}" ry="{ry}"/>')
    w(f'          </g>')

def easel(u,v,Y,rot=-9):
    x,y=P(u,v,Y)
    w(f'          <g fill="var(--furn)" stroke="var(--slab-edge)" stroke-width="1">')
    w(f'            <g transform="translate({f(x)},{f(y)}) rotate({rot})">')
    w(f'              <rect x="-15" y="-58" width="30" height="34"/>')
    w(f'              <path d="M-9 -24 l-4 24 h3 l4 -24 z M9 -24 l4 24 h-3 l-4 -24 z"/>')
    w(f'            </g>')
    w(f'          </g>')

def lights(xs, Yceil, drop):
    w('          <g stroke="var(--rule)" stroke-width="1">')
    for x in xs: w(f'            <line x1="{x}" y1="{Yceil}" x2="{x}" y2="{f(Yceil+drop)}"/>')
    w('          </g>')
    w('          <g fill="var(--color-accent)">')
    for i,x in enumerate(xs): w(f'            <circle cx="{x}" cy="{f(Yceil+drop+3+ (i%2)*-4)}" r="4.5"/>')
    w('          </g>')

# ================= 描画本体 =================
w('<svg class="fac-svg" viewBox="30 -8 1200 790" role="img"')
w('     aria-label="地下3階から屋根までを切って描いた FACTORY のコンセプトモデル。地下2階と地下3階は吹き抜けの小劇場、地下1階はクラブで大勢が思い思いの姿勢で踊り、1階はガラス張りのオフィスとアトリエとカフェ、2階はワークショップの輪、3階はインキュベーション、最上階は会員のラウンジ。">')
w('')
w('  <defs>')
w('''    <g id="fac-fig">
      <circle cx="0" cy="-39" r="6.2"/>
      <path d="M-8.2 -32 q8.2 -4.4 16.4 0 l1.4 17 h-19.2 z"/>
      <path d="M-7.4 -14.6 h5.6 l0.6 14.6 h-5.2 z"/>
      <path d="M1.8 -14.6 h5.6 l-1 14.6 h-5.2 z"/>
    </g>
    <g id="fac-figa">
      <use href="#fac-fig"/>
      <path d="M-7.6 -29 l-7.4 -13.6" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round"/>
      <path d="M7.6 -29 l7.4 -13.6" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round"/>
    </g>
    <g id="fac-figs">
      <circle cx="0" cy="-28" r="6"/>
      <path d="M-7.6 -21.5 q7.6 -4.2 15.2 0 l1.2 13.5 h-17.6 z"/>
      <path d="M-2 -8.6 h12.6 v4.7 h-12.6 z"/>
      <path d="M6.6 -4.6 h4.2 v4.6 h-4.2 z"/>
    </g>
    <g id="fac-figg">
      <use href="#fac-fig"/>
      <ellipse cx="10.5" cy="-18" rx="7.6" ry="5.4" transform="rotate(-18 10.5 -18)"/>
      <path d="M15 -23 l11.5 -8.5" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/>
    </g>
    <g id="fac-figd1">
      <use href="#fac-fig"/>
      <path d="M7.6 -30 l8.5 -15" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round"/>
      <path d="M-7.6 -29 l-10.5 7" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round"/>
    </g>
    <g id="fac-figd2">
      <use href="#fac-fig"/>
      <path d="M-7.6 -30.5 l-14 -3.5" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round"/>
      <path d="M7.6 -30.5 l14 -3.5" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round"/>
    </g>
    <g id="fac-figd3">
      <use href="#fac-fig"/>
      <path d="M-7.6 -27 l-9.5 10" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round"/>
      <path d="M7.6 -31 l10.5 -10" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round"/>
    </g>
    <g id="fac-figd4">
      <circle cx="0" cy="-32" r="6.2"/>
      <path d="M-8.2 -25 q8.2 -4.4 16.4 0 l1.4 14 h-19.2 z"/>
      <path d="M-7.4 -11.6 h5.6 l0.6 11.6 h-5.2 z"/>
      <path d="M1.8 -11.6 h5.6 l-1 11.6 h-5.2 z"/>
      <path d="M-7.6 -23 l-12 6.5" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round"/>
      <path d="M7.6 -23 l12 6.5" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round"/>
    </g>
    <g id="fac-figd5">
      <use href="#fac-fig"/>
      <path d="M-7.6 -30 l-4.5 -16.5" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round"/>
      <path d="M7.6 -30 l4.5 -16.5" fill="none" stroke="currentColor" stroke-width="3.4" stroke-linecap="round"/>
    </g>
    <pattern id="fac-earth" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
      <line x1="0" y1="0" x2="0" y2="10" stroke="var(--rule)" stroke-width="1"/>
    </pattern>''')
w('  </defs>')
w('')

# ---------- 地面 ----------
w('  <g>')
w(f'          <rect x="55" y="{GROUND}" width="175" height="22" fill="url(#fac-earth)" opacity="0.55"/>')
w(f'          <line x1="55" y1="{GROUND}" x2="{X0}" y2="{GROUND}" stroke="var(--line)" stroke-width="1.6"/>')
w(f'          <text class="fac-small" x="57" y="{GROUND-8}">地面</text>')
w('  </g>')

# ---------- B2-B3 小劇場 ----------
w('  <!-- B2-B3 小劇場 (2層吹き抜け) -->')
w('  <g>')
slab(B3); walls(B3, B1)
box(90,250,0.20,0.90,B3,22)                       # 舞台
TREAD_U=[275,325,375,425,475,520]; Z=[6,20,34,48,62]
w('          <g fill="var(--furn)" stroke="var(--slab-edge)" stroke-width="1">')
for i,z in enumerate(Z):
    a=P(TREAD_U[i],0.15,B3,z); b=P(TREAD_U[i+1],0.15,B3,z)
    c=P(TREAD_U[i+1],0.95,B3,z); d=P(TREAD_U[i],0.95,B3,z)
    w(f'            <polygon points="{pts(a,b,c,d)}"/>')
w('          </g>')
base=P(TREAD_U[0],0.15,B3)[1]
prof=[]
for i,z in enumerate(Z):
    xa=P(TREAD_U[i],0.15,B3)[0]; xb=P(TREAD_U[i+1],0.15,B3)[0]
    prof += [(xa,base-z),(xb,base-z)]
poly=[(prof[0][0],base)]+prof+[(prof[-1][0],base)]
w(f'          <polygon points="{pts(*poly)}" fill="var(--slab-edge)"/>')
lights([640,712], B1, 32)
w('          <g class="fac-people">')
for u,v,k,r in [(125,0.68,"figd1",-7),(190,0.55,"figd3",9),(140,0.40,"fig",-4)]:
    person(u,v,B3,k,r,0.95,z=22)
SEAT_U=[300,350,400,450,497]
gaps={(1,0.35),(4,0.70)}
for vi in (0.70,0.52,0.35):
    for i,u in enumerate(SEAT_U):
        if (i,vi) in gaps: continue
        person(u,vi,B3,"figs",(3 if i%2 else -3),0.95,z=Z[i])
w('          </g>')
w('  </g>')

# ---------- B1 クラブ ----------
w('  <!-- B1 クラブ -->')
w('  <g>')
slab(B1); walls(B1, F1)
box(300,490,0.70,0.95,B1,14)      # ステージ
box(100,230,0.55,0.70,B1,30)      # バー
lights([520,610,700,790], F1, 16)
CROWD=[(210,.86,"figd2",-11,.92),(270,.84,"figd5",9,.93),
       (165,.75,"fig",0,.93),
       (300,.70,"figd4",-8,.94),(455,.70,"figd2",7,.94),
       (225,.65,"figd1",13,.94),(380,.65,"figd5",-10,.94),(520,.65,"figd3",5,.94),
       (310,.60,"figa",-14,.95),(470,.60,"figd4",10,.95),
       (260,.55,"figd2",-4,.95),(410,.55,"figd1",11,.95),
       (180,.50,"fig",3,.96),(340,.50,"figd5",-12,.96),(505,.50,"figd3",6,.96),
       (150,.45,"figd4",9,.96),(245,.45,"figd1",-7,.96),(400,.45,"figa",14,.96),
       (305,.39,"figd2",-9,.97),(465,.39,"figd5",4,.97),
       (185,.33,"figd3",12,.97),(355,.33,"figd4",-6,.97),(515,.33,"figd1",8,.97),
       (255,.27,"figa",-13,.98),(430,.27,"figd2",5,.98),
       (310,.21,"figd5",10,.98),(490,.21,"figd3",-8,.98),
       (180,.15,"figd1",6,.99),(385,.15,"figd4",-11,.99),
       (275,.09,"figd2",13,1.0),(460,.09,"figa",-5,1.0)]
w('          <g class="fac-people">')
person(350,.82,B1,"figd1",-6,.93,z=14)
person(420,.82,B1,"figd3",12,.93,z=14)
for u,v,k,r,s in CROWD: person(u,v,B1,k,r,s)
w('          </g>')
w('  </g>')

# ---------- 1F オフィス・アトリエ・カフェ ----------
w('  <!-- 1F オフィス / アトリエ / カフェ -->')
w('  <g>')
slab(F1); walls(F1, F2)
box(110,215,0.52,0.66,F1,28)      # カフェカウンター
table(175,0.26,F1)
w('          <g stroke="var(--rule)" stroke-width="1.2" fill="none">')
for u in (280,340,400,460,510):
    x,y=P(u,0.45,F1); w(f'            <line x1="{f(x)}" y1="{f(y)}" x2="{f(x)}" y2="{f(y-90)}"/>')
for u in (280,510):
    x,y=P(u,0.95,F1); w(f'            <line x1="{f(x)}" y1="{f(y)}" x2="{f(x)}" y2="{f(y-90)}"/>')
a=P(280,0.45,F1); b=P(510,0.45,F1); c=P(510,0.95,F1); d=P(280,0.95,F1)
w(f'            <line x1="{f(a[0])}" y1="{f(a[1])}" x2="{f(b[0])}" y2="{f(b[1])}"/>')
w(f'            <line x1="{f(b[0])}" y1="{f(b[1])}" x2="{f(c[0])}" y2="{f(c[1])}"/>')
w(f'            <line x1="{f(a[0])}" y1="{f(a[1])}" x2="{f(d[0])}" y2="{f(d[1])}"/>')
w('          </g>')
easel(305,0.66,F1)
box(390,505,0.52,0.68,F1,26)
box(390,505,0.76,0.92,F1,26)
w('          <g class="fac-people">')
for u,v,k,r,s in [(420,.84,"figs",3,.93),(480,.84,"figs",-2,.93),(160,.74,"fig",0,.94),
                  (420,.60,"figs",-3,.95),(480,.60,"figs",2,.95),(360,.55,"fig",4,.95),
                  (300,.50,"fig",-5,.96),(145,.26,"figs",2,.98),(205,.26,"figs",-3,.98),
                  (250,.15,"fig",4,.99)]:
    person(u,v,F1,k,r,s)
w('          </g>')
w('  </g>')

# ---------- 2F ワークショップ ----------
import math
w('  <!-- 2F ワークショップ -->')
w('  <g>')
slab(F2); walls(F2, F3)
easel(110,0.62,F2,0)
w('          <g class="fac-people">')
person(470,.80,F2,"fig",3,.93)
for ang in (90,150,30,210,330,270):
    u=330+115*math.cos(math.radians(ang)); v=0.52+0.22*math.sin(math.radians(ang))
    person(u,v,F2,"figs",(4 if ang%180 else -4),0.95)
person(170,.16,F2,"fig",-3,.99); person(206,.16,F2,"fig",3,.99)
w('          </g>')
w('  </g>')

# ---------- 3F インキュベーション ----------
w('  <!-- 3F インキュベーション -->')
w('  <g>')
slab(F3); walls(F3, F4)
for cu in (280,410):
    a=P(cu,0.30,F3); b=P(cu,0.95,F3)
    w(f'          <polygon points="{pts(a,b,(b[0],b[1]-46),(a[0],a[1]-46))}" fill="var(--wall-left)" stroke="var(--rule)" stroke-width="1"/>')
for u0,u1 in ((170,250),(300,380),(430,505)):
    box(u0,u1,0.60,0.75,F3,24)
w('          <g class="fac-people">')
for u in (185,230,315,360,445,490):
    person(u,0.68,F3,"figs",(3 if (u//45)%2 else -3),0.95)
person(200,0.35,F3,"fig",4,0.98)
w('          </g>')
w('  </g>')

# ---------- 4F 会員ラウンジ ----------
w('  <!-- 4F 会員ラウンジ -->')
w('  <g>')
slab(F4); walls(F4, RF)
box(110,215,0.52,0.66,F4,28)      # カウンター
table(290,0.35,F4,h=18,rx=26,ry=9)
table(430,0.62,F4,h=18,rx=26,ry=9)
w('          <g class="fac-people">')
for u,v,k,r,s in [(445,.86,"fig",-4,.93),(500,.86,"fig",5,.93),
                  (165,.76,"fig",0,.94),
                  (395,.62,"figs",-3,.95),(465,.62,"figs",3,.95),
                  (290,.52,"figs",4,.96),
                  (170,.42,"fig",-4,.97),
                  (255,.35,"figs",3,.98),(325,.35,"figs",-3,.98)]:
    person(u,v,F4,k,r,s)
w('          </g>')
w('  </g>')

# ---------- 屋根 ----------
w('  <!-- 屋根 -->')
w('  <g>')
slab(RF)
w(f'          <polygon points="{pts((BL,RF+DY),(BR,RF+DY),(BR,RF+DY-18),(BL,RF+DY-18))}" fill="var(--wall-back)"/>')
w(f'          <polygon points="{pts((X0,RF),(BL,RF+DY),(BL,RF+DY-18),(X0,RF-18))}" fill="var(--wall-left)"/>')
w(f'          <polygon points="{pts((CUT,RF),(BR,RF+DY),(BR,RF+DY-18),(CUT,RF-18))}" fill="var(--wall-left)"/>')
w('  </g>')

# ---------- 外形線 ----------
w('  <g fill="none">')
w(f'          <line x1="{X0}" y1="{RF-18}" x2="{X0}" y2="{B3+12}" stroke="var(--line)" stroke-width="1.4"/>')
w(f'          <line x1="{BR}" y1="{RF+DY-18}" x2="{BR}" y2="{B3+DY+12}" stroke="var(--line)" stroke-width="1.4"/>')
w(f'          <line x1="{BL}" y1="{RF+DY-18}" x2="{BL}" y2="{B3+DY+12}" stroke="var(--rule)" stroke-width="1"/>')
w('  </g>')

# ---------- 街の人 ----------
w('  <g class="fac-people">')
for x in (100,146,192): w(f'          <g transform="translate({x},{GROUND})"><use href="#fac-fig"/></g>')
w('  </g>')

# ---------- ラベル ----------
LAB=[("4F","ホールドする","会員ラウンジ",F4+DY),
     ("3F","成長する","インキュベーション",F3+DY),
     ("2F","葛藤を超える","ワークショップ",F2+DY),
     ("1F","開く","オフィス・アトリエ・カフェ",F1+DY),
     ("B1","行動しインパクトを出す","クラブ",B1+DY)]
w('  <g>')
w('          <g class="fac-lead">')
for _,_,_,y in LAB: w(f'            <line x1="{BR}" y1="{y}" x2="947" y2="{y}"/>')
w(f'            <path d="M947 {B1+DY} h10 v192 h-10"/>')
w('          </g>')
for tag,verb,name,y in LAB:
    w(f'          <text class="fac-tag"  x="955" y="{f(y-14)}">{tag}</text>')
    w(f'          <text class="fac-verb" x="955" y="{f(y+5)}">{verb}</text>')
    w(f'          <text class="fac-name" x="955" y="{f(y+24)}">{name}</text>')
ty=(B1+DY+B3+DY)/2
w(f'          <text class="fac-tag"  x="967" y="{f(ty-14)}">B2-B3</text>')
w(f'          <text class="fac-verb" x="967" y="{f(ty+5)}">恐れを捨てる</text>')
w(f'          <text class="fac-name" x="967" y="{f(ty+24)}">小劇場</text>')
w('  </g>')
w('')
w('</svg>')

open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "out.svg"), "w", encoding="utf-8").write("\n".join(out))
print("SVG 生成 OK 行数", len(out))
