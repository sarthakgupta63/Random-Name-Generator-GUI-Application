"""
Generates Random Wierd Names into a Basic GUI Application.
"""

import tkinter
from tkinter import *
import random

window = Tk()
window.geometry('1000x500')
window.title("What's your Super Name!")
label_1 = Label(window, text="Welcome!", fg='white', bg='black')
label_2 = Label(window, text="Let's find Your Super Name", fg='white', bg='black')
label_1.config(font=("Courier", 44))
label_2.config(font=("Courier", 44))
label_1.pack(fill='x')
label_2.pack(fill='x')

def random_name():
    """
    Directly returns the name into the GUI window.
    """

    fnames = ['Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie­Weenie'", "Bob 'Stinkbug'",
    'Bowel Noises', 'Boxelder', "Bud 'Lite' ", 'Butterbean', 'Buttermilk', 'Buttocks', 'Chad',
    'Chesterfield', 'Chewy', 'Chigger", "Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat', 'Crapps',
    'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso', 'Fancypants', 'Figgs', 'Foncy',
    'Gootsy', 'Greasy Jim', 'Huckleberry', 'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'",
    'Johnny', 'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"', 'Mergatroid', '"Mr Peabody"',
    'Oil­Can', 'Oinks', 'Old Scratch', 'Ovaltine', 'Pennywhistle', 'Pitchfork Ben', 'Potato Bug',
    'Pushmeet','Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut', "Sid 'The Squirts'", 'Skidmark',
    'Slaps', 'Snakes', 'Snoobs', 'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky', 'Storyboard',
    'Sweet Tea', 'TeeTee', 'Wheezy Joe', "Winston 'Jazz Hands'", 'Worms']

    lnames = ['Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom', 'Breedslovetrout', 'Butterbaugh',
    'Clovenhoof', 'Clutterbuck', 'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
    'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater', 'Hootkins', 'Jefferson', 'Jenkins',
    'Jingley­Schmidt', 'Johnson', 'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
    'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf', 'Oxhandler', 'Pealike', 'Pennywhistle',
    'Peterson', 'Pieplow', 'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater', 'Rosenthal', 'Rubbins',
    'Sackrider', 'Snuggleshine', 'Splern', 'Stevens', 'Stroganoff', 'Sugar­Gold', 'Swackhamer', 'Tippins',
    'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax', 'Weiners', 'Whipkey', 'Wigglesworth',
    'Wimplesnatch', 'Winterkorn', 'Woolysocks']

    colors = ['Red', 'Yellow', 'Blue', 'Orange', 'Green', 'Violet']

    first = random.choice(fnames)
    last = random.choice(lnames)
    full_name = first + " " + last

    bg_color = random.choice(colors)

    label_3 = Label(window, text=full_name, bg=bg_color)
    label_3.config(font=("Verdana", 25))
    label_3.pack()


Button(window, text="Know Your Name", command=random_name).pack()
window.mainloop()
