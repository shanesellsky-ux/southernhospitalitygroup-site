import json
from PIL import Image, ImageDraw, ImageFont, ImageOps
R='/home/claude/southernhospitalitygroup-site/'
OUT=R+'pins/'
import os; os.makedirs(OUT,exist_ok=True)
pins=json.load(open('/home/claude/pins/pins.json'))
TF='/usr/share/fonts/truetype/crosextra/Caladea-Bold.ttf'
SF='/usr/share/fonts/opentype/inter/Inter-SemiBold.otf'
def wrap(d,text,font,maxw):
    words=text.split(); lines=[]; cur=''
    for w in words:
        t=(cur+' '+w).strip()
        if d.textlength(t,font=font)<=maxw: cur=t
        else: lines.append(cur); cur=w
    lines.append(cur); return lines
for p in pins:
    im=Image.open(R+p['img']).convert('RGB')
    PH=1080
    ph=ImageOps.fit(im,(1000,PH),Image.LANCZOS,centering=(p.get('cx',0.5),p.get('cy',0.5)))
    c=Image.new('RGB',(1000,1500),'#1e2b24'); c.paste(ph,(0,0))
    d=ImageDraw.Draw(c)
    d.rectangle([0,PH,1000,PH+6],fill='#c9a45c')
    tag=ImageFont.truetype(SF,28)
    d.text((70,PH+48),p['kicker'].upper(),font=tag,fill='#c9a45c')
    size=64
    while True:
        f=ImageFont.truetype(TF,size); lines=wrap(d,p['headline'],f,860)
        if len(lines)<=3 or size<44: break
        size-=4
    y=PH+100
    for l in lines:
        d.text((70,y),l,font=f,fill='#f3ead8'); y+=int(size*1.15)
    foot=ImageFont.truetype(SF,26)
    d.text((70,1500-70),'Book direct and save  ·  southernhospitalitygroup.co',font=foot,fill='#cfc6b2')
    c.save(OUT+p['file'],quality=88)
print(len(pins))
