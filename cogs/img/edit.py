from PIL import Image, ImageFont, ImageDraw
import numpy as np
import requests
import urllib.request
import os

WHITE = (255,255,255)
BLACK = (0,0,0)
 

def fill_img(profile):
    my_image = Image.open('template.png')
    font_str = 'font.ttf'
    urllib.request.urlretrieve(profile['clan']['badgeUrls']['large'], profile['clan']['badgeUrls']['large'][47:])
    urllib.request.urlretrieve(profile['league']['iconUrls']['medium'], profile['league']['iconUrls']['medium'][48:])
    clan_badge_img = Image.open(profile['clan']['badgeUrls']['large'][47:])
    clan_badge_img = clan_badge_img.resize((int(clan_badge_img.size[0] * 0.5),int(clan_badge_img.size[1] * 0.5)), 0)
    league_badge_img = Image.open(profile['league']['iconUrls']['medium'][48:])
    league_badge_img = league_badge_img.resize((int(league_badge_img.size[0] * 0.64),int(league_badge_img.size[1] * 0.64)), 0)
    image_editable = ImageDraw.Draw(my_image)
    color=(255,255,255)
    clash_font = ImageFont.truetype(font_str, 25)


    #name
    image_editable.text((104,21), profile['name'], color, font=clash_font, stroke_width=2, stroke_fill=BLACK)
    #tag
    clash_font = ImageFont.truetype(font_str, 17)   
    image_editable.text((104, 60), profile['tag'], color, font=clash_font, stroke_width=2, stroke_fill=BLACK)
    #lvl
    clash_font = ImageFont.truetype(font_str, 25)
    image_editable.text((34, 51), str(profile['expLevel']), color, font=clash_font, stroke_width=2, stroke_fill=BLACK)
    #role
    clash_font = ImageFont.truetype(font_str, 15)
    image_editable.text((104, 91), profile['role'].capitalize(), color, font=clash_font, stroke_width=2, stroke_fill=BLACK)
    #clan
    clash_font = ImageFont.truetype(font_str, 20)
    image_editable.text((550, 25), profile['clan']['name'], color, font=clash_font, stroke_width=2, stroke_fill=BLACK)
    #trophies
    clash_font = ImageFont.truetype(font_str, 31)
    image_editable.text((1076, 111), str(profile['trophies']), color, font=clash_font, stroke_width=2, stroke_fill=BLACK)
    #max trophies
    clash_font = ImageFont.truetype(font_str, 25)
    image_editable.text((1051, 232), str(profile['bestTrophies']), color, font=clash_font, stroke_width=2, stroke_fill=BLACK)
    #war stars
    image_editable.text((1048, 335), str(profile['warStars']), color, font=clash_font, stroke_width=2, stroke_fill=BLACK)
    #donated
    clash_font = ImageFont.truetype(font_str, 15)
    image_editable.text((239, 433), str(profile['donations']), color, font=clash_font, stroke_width=2, stroke_fill=BLACK)
    #received
    image_editable.text((547, 433), str(profile['donationsReceived']), color, font=clash_font, stroke_width=2, stroke_fill=BLACK)
    #attack wins
    image_editable.text((847, 433), str(profile['attackWins']), color, font=clash_font, stroke_width=2, stroke_fill=BLACK)
    #defense wins
    image_editable.text((1202, 433), str(profile['attackWins']), color, font=clash_font, stroke_width=2, stroke_fill=BLACK)
    #league
    clash_font = ImageFont.truetype(font_str, 20)
    image_editable.text((1000, 65), profile['league']['name'], color, font=clash_font, stroke_width=2, stroke_fill=BLACK)
    #clan badge
    my_image.paste(clan_badge_img, (551, 82), clan_badge_img)
    #league badge
    my_image.paste(league_badge_img, (823, 16), league_badge_img)

    tag = profile['tag']
    my_image.save(f'{tag}.png')


