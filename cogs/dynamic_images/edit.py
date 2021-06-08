from PIL import Image, ImageFont, ImageDraw
import numpy as np
import urllib.request

WHITE = (255,255,255)
BLACK = (0,0,0)
 

def fill_text(color=(255,255,255), font_str='font.ttf', name='', lvl=1, tag='#', role='', clan='', league='', war_stars=0, trophies=0, max_trophies=0, troops_donated=0, troops_received=0, attacks_won=0, defenses_won=0, clan_badge='', league_badge=''):
    my_image = Image.open('template.png')
    urllib.request.urlretrieve(clan_badge, clan_badge[47:])
    urllib.request.urlretrieve(league_badge, league_badge[48:])
    clan_badge_img = Image.open(clan_badge[47:])
    clan_badge_img = clan_badge_img.resize((int(clan_badge_img.size[0] * 0.5),int(clan_badge_img.size[1] * 0.5)), 0)
    league_badge_img = Image.open(league_badge[48:])
    league_badge_img = league_badge_img.resize((int(league_badge_img.size[0] * 0.64),int(league_badge_img.size[1] * 0.64)), 0)
    image_editable = ImageDraw.Draw(my_image)

    clash_font = ImageFont.truetype(font_str, 25)
    name = name
    tag = '#'+tag

    #name
    image_editable.text((104,21), name, color, font=clash_font, stroke_width=2, stroke_fill=BLACK)
    #tag
    clash_font = ImageFont.truetype(font_str, 17)   
    image_editable.text((104, 60), tag, color, font=clash_font, stroke_width=2, stroke_fill=BLACK)
    #lvl
    clash_font = ImageFont.truetype(font_str, 25)
    image_editable.text((34, 51), str(lvl), color, font=clash_font, stroke_width=2, stroke_fill=BLACK)
    #role
    clash_font = ImageFont.truetype(font_str, 15)
    image_editable.text((104, 91), role, color, font=clash_font, stroke_width=2, stroke_fill=BLACK)
    #clan
    clash_font = ImageFont.truetype(font_str, 20)
    image_editable.text((550, 25), clan, color, font=clash_font, stroke_width=2, stroke_fill=BLACK)
    #trophies
    clash_font = ImageFont.truetype(font_str, 31)
    image_editable.text((1076, 111), str(trophies), color, font=clash_font, stroke_width=2, stroke_fill=BLACK)
    #max trophies
    clash_font = ImageFont.truetype(font_str, 25)
    image_editable.text((1051, 232), str(max_trophies), color, font=clash_font, stroke_width=2, stroke_fill=BLACK)
    #war stars
    image_editable.text((1048, 335), str(war_stars), color, font=clash_font, stroke_width=2, stroke_fill=BLACK)
    #donated
    clash_font = ImageFont.truetype(font_str, 15)
    image_editable.text((239, 433), str(troops_donated), color, font=clash_font, stroke_width=2, stroke_fill=BLACK)
    #received
    image_editable.text((547, 433), str(troops_received), color, font=clash_font, stroke_width=2, stroke_fill=BLACK)
    #attack wins
    image_editable.text((847, 433), str(attacks_won), color, font=clash_font, stroke_width=2, stroke_fill=BLACK)
    #defense wins
    image_editable.text((1202, 433), str(defenses_won), color, font=clash_font, stroke_width=2, stroke_fill=BLACK)
    #league
    clash_font = ImageFont.truetype(font_str, 20)
    image_editable.text((1000, 65), league, color, font=clash_font, stroke_width=2, stroke_fill=BLACK)
    #clan badge
    my_image.paste(clan_badge_img, (551, 82), clan_badge_img)
    #league badge
    my_image.paste(league_badge_img, (833, 16), league_badge_img)

    my_image.save(f'img/{tag}.png')


