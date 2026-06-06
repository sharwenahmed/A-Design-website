from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, math, random
W,H=1600,1000
out='/mnt/data/sitework/assets'
os.makedirs(out,exist_ok=True)
try:
    font_big=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',70)
    font_med=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',34)
    font_small=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',24)
    font_tiny=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',18)
except:
    font_big=font_med=font_small=font_tiny=None

def grad(c1,c2):
    img=Image.new('RGB',(W,H),c1)
    p=img.load()
    for y in range(H):
        t=y/H
        for x in range(W):
            s=(x/W)*0.25+t*0.75
            p[x,y]=tuple(int(c1[i]*(1-s)+c2[i]*s) for i in range(3))
    return img.convert('RGBA')

def round_rect(d, xy, r, fill, outline=None, width=1):
    d.rounded_rectangle(xy, radius=r, fill=fill, outline=outline, width=width)

def browser(img, d, accent=(245,158,11), url='adesigns.demo/live-preview'):
    round_rect(d,(70,70,W-70,H-70),28,(14,18,28,255),(255,255,255,35),2)
    round_rect(d,(90,92,W-90,150),16,(26,32,45,255),(255,255,255,25),1)
    for i,c in enumerate([(255,95,87),(255,189,46),(39,201,63)]):
        d.ellipse((118+i*38,112,138+i*38,132), fill=c)
    round_rect(d,(260,106,W-130,136),12,(9,13,21,255),(255,255,255,18),1)
    d.text((285,111),url,fill=(180,190,205),font=font_tiny)

def btn(d,xy,text,fill,fg=(10,12,18)):
    x,y,w,h=xy
    round_rect(d,(x,y,x+w,y+h),h//2,fill)
    d.text((x+26,y+16),text,fill=fg,font=font_small)

def roof_shape(d, base_y, color=(120,45,30), accent=(245,158,11)):
    # house/roof illustration
    d.polygon([(850,base_y),(1180,base_y-190),(1510,base_y)], fill=color)
    d.polygon([(918,base_y),(1180,base_y-145),(1442,base_y)], fill=(55,68,86))
    for i in range(9):
        y=base_y-12-i*18
        d.line((910+i*12,y,1450-i*12,y),fill=(255,255,255,55),width=3)
    d.rectangle((940,base_y,1450,850),fill=(235,238,242))
    for x in [990,1125,1280]:
        round_rect(d,(x,base_y+55,x+90,base_y+145),8,(31,41,55))
    d.rectangle((1110,base_y+190,1250,850),fill=(118,78,52))

def cleaning_room(d, luxury=False):
    d.rectangle((840,210,1490,830),fill=(238,246,250) if not luxury else (230,221,205))
    d.rectangle((840,620,1490,830),fill=(211,226,233) if not luxury else (190,171,145))
    # sofa/counter
    round_rect(d,(930,500,1370,650),28,(38,163,190) if not luxury else (88,68,54))
    for x in range(950,1330,95):
        d.line((x,515,x,640),fill=(255,255,255,70),width=2)
    d.rectangle((900,335,1010,470),fill=(255,255,255))
    d.rectangle((1130,300,1410,455),fill=(255,255,255))
    for i in range(16):
        x=random.randint(860,1470); y=random.randint(230,600)
        d.ellipse((x,y,x+random.randint(8,20),y+random.randint(8,20)),fill=(255,255,255,120))

def draw_real_roof1(name):
    img=grad((10,15,24),(30,42,62)); d=ImageDraw.Draw(img)
    browser(img,d,(245,158,11),'primeroofing.demo/free-estimate')
    # website canvas
    round_rect(d,(110,170,1490,850),20,(245,247,250,255))
    d.rectangle((110,170,1490,255),fill=(255,255,255))
    d.text((155,198),'PRIME ROOFING',fill=(22,29,42),font=font_med)
    for i,t in enumerate(['Services','Projects','Reviews','Contact']): d.text((850+i*125,205),t,fill=(65,72,86),font=font_tiny)
    btn(d,(1260,190,180,48),'Free Quote',(245,158,11))
    d.rectangle((110,255,1490,850),fill=(233,238,244))
    roof_shape(d,600,(153,72,52),(245,158,11))
    d.text((155,340),'Roofing that protects\nyour home and budget',fill=(11,18,32),font=font_big)
    d.text((160,510),'Premium roof replacement, storm repair, and inspections\nfor homeowners who want the job done right.',fill=(58,66,82),font=font_small)
    btn(d,(160,615,220,58),'Get Estimate',(245,158,11))
    btn(d,(400,615,210,58),'Call Now',(255,255,255),(12,18,30))
    for i,v in enumerate(['4.9★ Rated','24hr response','10yr warranty']):
        round_rect(d,(160+i*185,740,320+i*185,790),12,(255,255,255,230)); d.text((180+i*185,754),v,fill=(20,28,42),font=font_tiny)
    img.save(f'{out}/{name}.png')

def draw_real_roof2(name):
    img=grad((15,12,10),(55,42,32)); d=ImageDraw.Draw(img)
    browser(img,d,(196,139,79),'luxuryroofs.demo/portfolio')
    round_rect(d,(110,170,1490,850),20,(18,18,18,255),(255,255,255,35),1)
    d.rectangle((110,170,1490,850),fill=(18,18,18))
    d.text((160,205),'CROWNLINE ROOFING',fill=(230,207,169),font=font_med)
    d.text((160,345),'Architectural roofing\nfor premium homes',fill=(255,255,255),font=font_big)
    d.text((164,520),'Designer shingles • Metal accents • Executive project management',fill=(210,196,178),font=font_small)
    btn(d,(164,620,260,58),'View Luxury Work',(230,207,169),(20,16,12))
    # realistic luxury house card
    round_rect(d,(800,250,1435,760),22,(44,38,31), (230,207,169,95),2)
    d.rectangle((835,490,1400,760),fill=(218,212,198))
    d.polygon([(790,495),(1115,285),(1440,495)],fill=(55,52,48))
    d.polygon([(855,500),(1115,340),(1375,500)],fill=(88,84,78))
    for x in [900,1040,1210]: round_rect(d,(x,550,x+120,660),6,(22,26,32))
    img.save(f'{out}/{name}.png')

def draw_art_roof1(name):
    img=grad((21,13,42),(114,40,18)); d=ImageDraw.Draw(img)
    browser(img,d,(255,110,55),'stormshield.demo/art-concept')
    for i in range(28):
        x=random.randint(110,1490); y=random.randint(180,820); r=random.randint(20,90)
        d.ellipse((x-r,y-r,x+r,y+r),fill=(255,130,40,random.randint(18,55)))
    d.text((150,245),'STORM SHIELD',fill=(255,216,180),font=font_med)
    d.text((150,345),'Emergency roof\nrepair with impact',fill=(255,255,255),font=font_big)
    d.text((154,528),'Bold landing page concept built for urgent storm calls.',fill=(255,224,205),font=font_small)
    btn(d,(154,615,230,58),'Call 24/7',(255,114,64))
    # abstract roof shards
    for i in range(14):
        pts=[(850+random.randint(-40,420),300+random.randint(-50,260)),(1020+random.randint(-80,420),460+random.randint(-40,230)),(760+random.randint(-30,430),690+random.randint(-20,80))]
        d.polygon(pts,fill=random.choice([(255,130,60,160),(255,198,86,135),(48,69,100,180),(18,24,38,220)]))
    img=img.filter(ImageFilter.UnsharpMask(radius=1,percent=120))
    img.save(f'{out}/{name}.png')

def draw_art_roof2(name):
    img=grad((3,35,32),(4,83,77)); d=ImageDraw.Draw(img)
    browser(img,d,(52,211,153),'greenpeak.demo/sustainable')
    d.text((145,230),'GREENPEAK ROOFS',fill=(174,255,226),font=font_med)
    d.text((145,340),'Sustainable roofing\nfor modern homes',fill=(255,255,255),font=font_big)
    d.text((150,522),'Artistic eco concept with clean visuals, financing CTAs, and green energy messaging.',fill=(204,255,238),font=font_small)
    btn(d,(150,615,260,58),'Explore Options',(52,211,153),(2,24,20))
    # geometric eco roof
    center=(1090,510)
    for i in range(5):
        scale=1-i*.12
        pts=[(center[0]-360*scale,center[1]+130*scale),(center[0],center[1]-230*scale),(center[0]+360*scale,center[1]+130*scale)]
        d.polygon(pts,outline=(174,255,226,190-i*30),fill=(52,211,153,22+i*10))
    for i in range(35):
        x=random.randint(790,1430); y=random.randint(260,760)
        d.arc((x,y,x+60,y+40),180,360,fill=(174,255,226,80),width=2)
    img.save(f'{out}/{name}.png')

def draw_real_clean1(name):
    img=grad((7,21,31),(20,67,82)); d=ImageDraw.Draw(img)
    browser(img,d,(34,211,238),'cleanpro.demo/book-now')
    round_rect(d,(110,170,1490,850),20,(247,252,255,255))
    d.rectangle((110,170,1490,250),fill=(255,255,255))
    d.text((158,198),'CLEANPRO',fill=(9,42,55),font=font_med)
    btn(d,(1250,190,190,48),'Book Clean',(34,211,238),(6,26,36))
    d.text((155,330),'Spotless homes,\nwithout the stress',fill=(9,42,55),font=font_big)
    d.text((160,505),'Residential cleaning plans with transparent pricing,\nrecurring appointments, and trusted teams.',fill=(65,86,98),font=font_small)
    btn(d,(160,610,240,58),'Get My Quote',(34,211,238),(4,22,30))
    cleaning_room(d,False)
    for i,v in enumerate(['Weekly','Bi-weekly','Move-out']):
        round_rect(d,(160+i*155,730,290+i*155,780),14,(235,248,252)); d.text((187+i*155,744),v,fill=(9,42,55),font=font_tiny)
    img.save(f'{out}/{name}.png')

def draw_real_clean2(name):
    img=grad((15,16,24),(42,36,48)); d=ImageDraw.Draw(img)
    browser(img,d,(203,176,112),'eliteclean.demo/concierge')
    round_rect(d,(110,170,1490,850),20,(23,24,31,255),(255,255,255,35),1)
    d.text((155,205),'ELITE HOME CARE',fill=(224,205,164),font=font_med)
    d.text((155,340),'Concierge cleaning\nfor luxury homes',fill=(255,255,255),font=font_big)
    d.text((160,520),'A premium website concept for high-ticket cleaning and white-glove service.',fill=(218,210,196),font=font_small)
    btn(d,(160,620,280,58),'Request Concierge',(224,205,164),(18,15,10))
    cleaning_room(d,True)
    img.save(f'{out}/{name}.png')

def draw_art_clean1(name):
    img=grad((8,26,42),(20,104,125)); d=ImageDraw.Draw(img)
    browser(img,d,(103,232,249),'sparkclean.demo/bright')
    for i in range(55):
        x=random.randint(120,1480); y=random.randint(170,850); r=random.randint(8,45)
        d.ellipse((x-r,y-r,x+r,y+r),fill=(255,255,255,random.randint(20,90)))
    d.text((150,230),'SPARK CLEAN',fill=(183,244,255),font=font_med)
    d.text((150,338),'Fresh, bright,\nand easy to book',fill=(255,255,255),font=font_big)
    d.text((154,522),'Artistic booking-first design made to feel friendly, fast, and trustworthy.',fill=(212,248,255),font=font_small)
    btn(d,(154,615,230,58),'Book Online',(103,232,249),(6,24,34))
    # abstract phone/card UI
    round_rect(d,(920,250,1325,780),42,(255,255,255,230),(255,255,255,80),2)
    for y,c in [(330,(34,211,238)),(430,(255,255,255)),(530,(34,211,238)),(630,(255,255,255))]:
        round_rect(d,(970,y,1275,y+58),20,c if c!=(255,255,255) else (231,247,252),(7,70,89,35),1)
    img.save(f'{out}/{name}.png')

def draw_art_clean2(name):
    img=grad((38,13,55),(107,31,84)); d=ImageDraw.Draw(img)
    browser(img,d,(244,114,182),'officeglow.demo/contracts')
    d.text((150,230),'OFFICE GLOW',fill=(255,197,223),font=font_med)
    d.text((150,338),'Commercial cleaning\nthat feels premium',fill=(255,255,255),font=font_big)
    d.text((154,522),'Artistic B2B concept for office contracts, proposals, and recurring plans.',fill=(255,219,236),font=font_small)
    btn(d,(154,615,260,58),'Get Proposal',(244,114,182),(35,10,26))
    # geometric building/office abstract
    for i,x in enumerate([820,960,1100,1240]):
        h=random.randint(330,520)
        round_rect(d,(x,800-h,x+100,800),12,(255,255,255,40+i*15),(255,255,255,70),1)
        for yy in range(820-h+30,780,58):
            d.rectangle((x+22,yy,x+78,yy+22),fill=(244,114,182,80))
    for i in range(20):
        d.line((850+random.randint(0,520),260+random.randint(0,440),850+random.randint(0,520),260+random.randint(0,440)),fill=(255,255,255,45),width=2)
    img.save(f'{out}/{name}.png')

for func,name in [
    (draw_real_roof1,'roofing-realistic-estimate'),(draw_real_roof2,'roofing-realistic-luxury'),
    (draw_art_roof1,'roofing-artistic-storm'),(draw_art_roof2,'roofing-artistic-green'),
    (draw_real_clean1,'cleanpro-realistic-home'),(draw_real_clean2,'cleanpro-realistic-luxury'),
    (draw_art_clean1,'cleanpro-artistic-bright'),(draw_art_clean2,'cleanpro-artistic-office')]:
    func(name)
print('done')
