# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# Names can be changed later in the story. Possibly in the ending, change the character's name through a 
# different define function. Like for example, define E = Character("Real Name")

define A = Character("???", color = "#ffffff", ctc = "ctc", ctc_pause = "ctc", ctc_position = "nestled")
define B = Character("???", image = "lili", color = "#cc0000", ctc = "ctc", ctc_pause = "ctc", ctc_position = "nestled")
define U = Character("Memory", color = "#ffffff", ctc = "ctc", ctc_pause = "ctc", ctc_position = "nestled")
define L = Character("Her Lover", image = "lili", color = "#cc0000", ctc = "ctc", ctc_pause = "ctc", ctc_position = "nestled")
define narrator = Character(name=None, ctc = "ctc", ctc_pause = "ctc", ctc_position = "nestled")

# The game starts here.

# Define wave rendered images
image color_effect = TranslateImage(Transform(WaveImage("images/color texture.png", speed = 30, amp=20, freq=65, horizontal=True, melt="wrap", sin_extreme=True),xzoom=1.5,yzoom = 1.2, nearest=True), True, False)

# Default settings
define slow_dissolve = Dissolve(1.0)
define sprite_dissolve = Dissolve(0.3)
define slow_fade = Fade(2.0, 0.0, 3.0, color='#fff')
default preferences.text_cps = 40
default preferences.fullscreen = False
default preferences.skip_unseen = False
define config.say_attribute_transition = sprite_dissolve

# half size image
transform half_size: 
    zoom 0.5 

# white screen
image white = "#fff"

# click to continue button
image ctc:
    "gui/ctc_button.png"
    linear 0.75 alpha 1.0
    linear 0.75 alpha 0.0
    repeat

label splashscreen:
    scene white
    with Pause(1)

    play music "audio/White Noise.mp3" fadein 1.5 fadeout 0.5 volume 0.1

    show text "{color=#000000}Made for the SGDA Fall '25 Game Jam.{/color}"
    with dissolve
    $ renpy.pause()
    hide text with dissolve
    with Pause(1)

    stop music fadeout 1.0
    
    return

label start:

    # scene black shows a black screen 

    scene black

    # {w} for dramatic text effect. You have to click to go through more dialogue in the same text box.

    "Buzzing. {w}Sparkling pain of noise. {w}Suffocating sound. {w}A dissonance ringing in her ear that she cannot get rid of."

    "Prickling in her mind, she lets it linger. But that has left the kaleidoscope to surround her, busying her entire body with a cacophony in the void."

    # vpunch is there to make the screen shake. It's there for a dramatic effect for when the MC wakes up.

    scene bg apartment
    with vpunch

    play music "audio/In Game Song - Final.mp3" fadein 1.0 fadeout 0.5

    "Her eyes jolt open. {w}Stabilizing herself against a wall behind her with an arm, she observes her surroundings and marks them as unfamiliar to her." 
    
    "The pandemonium once full in her mind slowly dissipates. She decides to tread through the dim lit room in front of her."

    "Scanning the space, she is muddled with a disarray feelings that move like raging waves within her."
    
    # Mazie notes: ( I wanted to say that as she scans the area she is confronted with a confusing feeling of familiarity and strangeness. This place is wrong.)"
    # After the text "scanning the space," add a show character expression sprite here.

    A "Where am I?"

    "She picks herself up from the hard mattress and stands on the floor."

    "In her confusion, she continues to wander aimlessly around the awfully tidied bedroom." 

    "She notices at first that the smell of cleaning chemicals fill her lungs. Pictures hanging around her room were aligned on the wall like a grid." 

    "She touches the bedside table and feels the unusual slipperiness of it, supposing all the friction has been forcibly wiped away." 

    "Everything in the room is placed perfectly, as if nobody lived here. For a moment, she tries to remember how she got here but her efforts are futile."

    "She even tries to search within her own memories of her own name, and yet she can't come up with a single letter of it."

    A "This must be a dream..."

    "As her eyes bounce around the space, she takes a moment to observe the room in front of her."
     
    jump objects_menu
