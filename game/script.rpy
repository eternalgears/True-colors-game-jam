# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# Names can be changed later in the story. Possibly in the ending, change the character's name through a 
# different define function. Like for example, define E = Character("Real Name")

define A = Character("???")

# The game starts here.

# Default settings
define slow_dissolve = Dissolve(1.0)
default preferences.text_cps = 40
default preferences.fullscreen = False
default preferences.skip_unseen = False

label start:

    # scene black shows a black screen 

    scene black

    # {w} for dramatic text effect. You have to click to go through more dialogue in the same text box.

    "Buzzing. {w}Sparkling pain of noise. {w}Suffocating sound. {w}A dissonance ringing in her ear that she cannot get rid of."

    "Prickling in her mind, she lets it linger. But that has left the kaleidoscope to surround her, busying her entire body with a cacophony in the void."

    # vpunch is there to make the screen shake. It's there for a dramatic effect for when the MC wakes up.

    scene bg bedroom
    with vpunch

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
