label bad_ending:
    # Falling action: Their partner establishes that nothing is wrong. They hold an ominous presence and the MC is not given answers. The MC accepts that this is all to their life.
    
    "This assortment of items details a life, her life. Though strange and unfamiliar she starts to paint a picture of who lives here, of how she lives."

    stop music 

    play sound "audio/knock.ogg"

    "Suddenly, she hears knocking at the door."

    scene bg door at half_size
    with slow_dissolve

    play music "audio/White Noise.mp3" fadein 1.5 fadeout 0.5 volume 0.1

    "She felt irritated, being disturbed by the abrupt sound."
    
    "Turning around, her hands hover over the doorknob, but an invisible barrier, her hesitation, prevents her from turning it for a moment."
    
    play sound "audio/knock.ogg"

    "She stands still without opening it until her thoughts are interrupted by the knock again." 
    
    "She was curious about who lies on the other side, but then she figures that they would've had to harmed her.{w} There must be a reason why she is here." 
    
    play sound "audio/keys jingle.wav"
    queue sound "audio/doorcreak.wav"

    "Before she can open the door, she hears the jangle of keys and the door creaks open."

    stop music 

    scene bg apartment
    with vpunch

    show lili happy

    B "{cps=50}Hey honey! I'm hoooome!!{/cps}"

    play music "audio/In Game Song - Final.mp3" fadein 1.0

    "She stands uncomfortably, confused as to who this person is and what they are doing here." 

    "The person has an apron, full of colored stains and wrinkles draped around them. They give off a sort of weird awkwardness in their stance, perhaps an act a perpretrator to appear innocent." 
    
    "They smell like coffee and syrup, a sickenly sweet odor that could give her a noise-induced migraine again." 
    
    "This stranger stares back at her with a sort of happy look a puppy would give seeing their owner come home." 
    
    show lili concerned
    with sprite_dissolve

    "Their face then flips to a concerned gape when that affection isn't reciprocated."

    A "What are you doing here?"

    "She was met with a deafening silence. Every confusion, memory, and her life since she supposedly came here was always met with silence."

    B suspicious "...."

    "The person in front of her nervously smiled at that. Clearly an expression admitting guilt, she thought to herself."

    B scared "Heh is this a joke?"

    A "Do you know where I am?"

    B "..."

    "Silence again. Every nonresponse just tells her that the stranger knows something she doesn't."

    "They tilt their head and put their hand on her shoulder."

    B concerned "Are you okay?..."

    A "Do you know where we are?"

    B "Oh goodness! Are you feeling sick? Where does it hurt?"

    "The way this stranger ignores her questions frustrates her, but her calmness marks her as someone safe."

    B "How long have you been up?"

    A "I don't know..."

    B suspicious "You're acting strange... Do you remember falling or injuring yourself at all?"

    "She puts her palm to her head and says truthfully."

    A "I don't remember, anything..."

    B scared "..."

    B concerned "I think we must see a doctor... {w}How can you not remember anything?"

    stop music fadeout 0.5

    scene black
    with fade

    hide lili

    "Her head rings, a throbbing ache, that noise again, that daze. She wobbles, struggling to stand up."

    "They pull her arm to their shoulders and helped her walk to the car."

    "The two head to an ER. Once confronted with a doctor, they are unable to determine what has happened to her. They say she may have a severe concussion. She is instructed to rest and to come back another day for a scanning."

    "Slowly she begins to remember certain things both in time and her so-called partner's explanations. _____s her name. _____ is her partner."

    "They live what seems to be a boring life in the city. Working and making ends meet." 
    
    "She works in an office of ______, a desk job, and she put in a sick week request to ensure she had time to rest." 
    
    "Slowly she remember, how they met, how she got her job, her education, her hobbies. But throughout all of them something was still not quite right."

    # Resolution: The MC is denied the truth and remains in their state. Forgetting who they are and reaching normalcy.

    play music "audio/Bad Ending - Final.mp3" fadein 1.5

    scene cg bad end
    with dissolve 

    $ renpy.pause(3.0, hard=True)
    pause

    "As time moved forward, the two both moved on. --___ began to be herself again, from what she remembered 'herself' to be."
    
    "She thought it odd to have a partner, but she accepted this reality as normal. The doctors suggested therapy, to which she decided to skip."
    
    "She went on with her life, as it was given to her."

    "Once able to work again, she fell into routine. She would work, come home, cook, talk to her partner sometimes, and repeat."
    
    "Her job was not difficult, she found it strange to work after having little recollection of it. But eventually, she knew how to continue her life."

    "She accepted this as her life. Dull, drab-like. She knows comfort in her stillness."
    
    "But something still stuck in the back of her mind.{w} That noise. {w}That aching noise. {w}It would come back in forms of waves, headaches, and restlessness." 
    
    "As much as she tried to stray away from it, those migraines were something she could never rid of."

    "But still, she lived her day to day life. This was how things are now." 
    
    "She convinced herself that the buzzing feeling would not bother her. If that feeling was there from the beginning, then it may as well be apart of her life forever."

    call credits 
    
    return