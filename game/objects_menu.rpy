label objects_menu:

    # object flags
    default Clock = False
    default Picture = False
    default Hobby = False
    default Clothes = False
    default Mirror = False

    # ending values
    default acceptance = 0
    default repression = 0

    if Clock and Picture and Hobby and Clothes and Mirror:
        jump decide
    else:
        call screen object_selection

    # TODO: change the xpos & ypos on each button to match the background!
    # also, button images are placeholders, so change them :)

    screen object_selection:
        if not Clock:
            imagebutton:
                xpos 0.5
                ypos 0.2
                xanchor 0.5
                yanchor 0.5
                idle "button_idle.png"
                hover "button_hover.png"
                action Jump("clock")
        if not Picture:
            imagebutton:
                xpos 0.5
                ypos 0.3
                xanchor 0.5
                yanchor 0.5
                idle "button_idle.png"
                hover "button_hover.png"
                action Jump("picture")
        if not Hobby:
            imagebutton:
                xpos 0.5
                ypos 0.4
                xanchor 0.5
                yanchor 0.5
                idle "button_idle.png"
                hover "button_hover.png"
                action Jump("hobby")
        if not Clothes:
            imagebutton:
                xpos 0.5
                ypos 0.5
                xanchor 0.5
                yanchor 0.5
                idle "button_idle.png"
                hover "button_hover.png"
                action Jump("clothes")
        if not Mirror:
            imagebutton:
                xpos 0.5
                ypos 0.6
                xanchor 0.5
                yanchor 0.5
                idle "button_idle.png"
                hover "button_hover.png"
                action Jump("mirror")        

# evaluate points for good vs bad ending
label decide:
    if acceptance > repression:
        jump good_ending
    else:
        jump bad_ending

label clock:
    $ Clock = True
    "The clocks hands move robotically and rhythmically, reminding her of the passage of time. There is nothing unusual about its presence."
    "For every second that ticks, she wonders to herself, how long has she been here? As the parent hand tocked, her questions stumble further."
    "The length of her stay concerns her, as she is unable to pick apart the answer from her head."
    "Furthermore, she worries if anyone is waiting for her, but deep down, she feels like nobody is coming here."
    menu:
        "Peculiar":
            $ acceptance += 1
            "It has a peculiar shape compared to the minimalism of other items in this room. The glass in front of the time reflected her image."
            "She remembers placing the clock there, so this must be her home. But for some reason, her mind couldn't fathom that this was the place that she lived in."
            "There was none of the soothing familiarity that she hoped that she would pick up from this memory."
            "'Home' shouldn't be as strange as this."
        "Constraining":
            $ repression += 1
            "She remembers breaking a previous clock. This clock was not the first to be here. Not the first to stay steady on the wall."
            "Clumsy her hands are, she remembers something, and something she wishes she has not."
            "She thinks about how much she despises this clock. {w} Every clock in her sight. {w} Every single clock in existence. {w} All time does is constraint, rule, and burden."
            "She grows frustrated at its looming presence, but nothing happens."
    jump objects_menu

label picture:
    $ Picture = True
    "Her eyes move to an assortment of paintings and pictures. Displayed in unison are a collage of paintings and pictures."
    "Inspecting further she notes them to be photographs of scenery. Airy hills and mountains, oceans and scenic views."
    "Mixed in with the photographs lie sketches and messy paintings, amatureish at best, but for some reason still in line with the beautiful sceneries."
    menu:
        "Awestruck":
            $ acceptance += 1
            "She finds them pleasing to the eye, calming and quiet. For a moment, her eyes dance and she imagines breathing in the nature displayed on these pictures."
            "The forest fluff of the oak trees rustling in the harsh wind."
            "The sand kicking up at her feet as the waves wash up at the shoreline."
            "Raising her hands towards the sky and picturing herself grasping at the clouds."
            "She wonders who or when these pictures were made. If they are hers or if they were given to her. For such poor work to be hung, they must be cherished by someone kind."
        "Dull":
            $ repression += 1
            "Staring deeply, she finds herself devoid of emotion in these pieces.{w} Drab. {w}Dull. {w}Nothing."
            "Her eyes wearied at the array of places. She wonder why she is even looking when there is nothing to be found here."
            "The artist behind this chaotic display ought to find other hobbies, she thinks to herself."
    jump objects_menu

label hobby:
    $ Hobby = True
    "She focuses on a stack of neatly placed box of puzzles on the center table of the room. Pictures of forests, oceans and ponies. Quite an odd collection."
    menu:
        "Curious":
            $ acceptance += 1
            "Looking closer, she notices that the puzzles have not be open yet. She wonders to herself if they were new or a present to her."
            "She opens a box that had an ocean scenery on the front. Bits and pieces of a whipped blue to be connected."
            "The faint light creeping from the window shines on the puzzles with the iridescent sapphire hues on the front."
            "She closes the box."
        "Chaotic":
            $ repression += 1
            "She wonders why anyone could ever enjoy an activity such as this. Putting pieces together to create a picture meaning nothing."
            "Such a useless experience.{w} A waste of time.{w} There are better things to do, she's sure of it, though she cannot remember anything productive that she would do if she could."
            "A cold reminder of her forgetting."
    jump objects_menu

label clothes:
    $ Clothes = True
    "A rack of clothing stands awkwardly aside a wall. Every article of attire hangs neatly, and organized."
    menu:
        "Organized":
            $ acceptance += 1
            "In her inspection of the rack, she accepts these items as her own, though she does not remember her hands putting the clothes here."
            "The rack is orderly, each piece of clothing carefully dangling like stairs on a staircase. The shoes aside them are clean as well, not an inch of dirt can be found on the outsoles."
            "It's a satisfying image. She remembers feeling proud of their assortment, but nothing further."
        "Restricted":
            $ repression += 1
            "Uniform. If this is her clothes, then it must be from a place that does not allow casual attire. Even worse, she wonders if she has picked these outfits herself, which she likely has."
            "She cannot remember where she works, but announces in her mind that only a stuck up person would wear such clothes. She grows frustrated in believing this is her home."
            "Her irritation pricks deeply into her skin as she stares more at the clothes."
    jump objects_menu

label mirror:
    $ Mirror = True
    "This mirror is strikingly dirty compared to everything else that has been polished in this room. She wonder what would allow herself to let it get this dusty." 
    menu:
        "Clean":
            $ acceptance += 1
            "This mirror is strikingly dirty compared to everything else that has been polished in this room. She wonder what would allow herself to let it get this dusty."
            "She decides to wipe her palm against the dust to look clearly at herself. Inspecting the reflection, she is reminded of her situation, and is concerned once again."
            "She brushes off the dusty hand with her other hand and thinks on cleaning the mirror later."
        "Avoid":
            $ repression += 1
            "She does not want to look at it. A subconscious tells her not to, something deep inside of her, where that buzzing feeling lies in a caged locked up for a greater good."
            "Her image was forbidden from her eyes. Growing fearful of the mirror, she quickly turned away."
    jump objects_menu