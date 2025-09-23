label objects_menu:

    # object flags
    default Clock = False
    default Picture = False
    default Hobby = False
    default Clothes = False
    default Mirror = False

    A "Use the buttons :3"

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

label decide:
    e "You did it!"
    return

label clock:
    $ Clock = True
    jump objects_menu

label picture:
    $ Picture = True
    jump objects_menu

label hobby:
    $ Hobby = True
    jump objects_menu

label clothes:
    $ Clothes = True
    jump objects_menu

label mirror:
    $ Mirror = True
    jump objects_menu