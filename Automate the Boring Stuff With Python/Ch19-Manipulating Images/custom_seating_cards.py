# Custom Seating Cards

# https://stackoverflow.com/questions/1970807/center-middle-align-text-with-pil
from PIL import Image, ImageDraw, ImageFont

guests = []

# Open guest list
with open('guests.txt', 'r') as fh:
    for line in fh.readlines():
        guests.append(line.rstrip())

charlinda_font = ImageFont.truetype(font='charlinda.otf', size=36)
# Create a card for each guest
for guest in guests:
    seating_card = Image.new('RGBA', (288, 360), 'white')
    width, height = seating_card.size
    # Put the flowery background
    background = Image.open('flower.jpg')
    seating_card.paste(background, (0, 0))
    # Put the text
    draw = ImageDraw.Draw(seating_card)
    card_body = f'{guest}'
    text_width, text_height = draw.textsize(card_body, font=charlinda_font)
    draw.text(((width-text_width)/2, (height-text_height)/2),
              f'{guest}', fill='black', font=charlinda_font)
    draw.rectangle([(0, 0), (287, 359)], outline='black', width=2)
    # Save the image
    seating_card.save(f'{guest}.png')
