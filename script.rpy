default player_name = ""
default stability = 0
default sanity = 5   # range 0–10
default inventory = []
default item_number = 0
default events = []
default oxygen = 100

define config.main_menu_music = "menu_music.mp3"
define l = Character("Lucas")
define v = Character("Voice", what_italic=True)
define n = Character(name=None)

image Lucas = im.Scale('Lucas.png', 1000, 1000)
image Lucas_pointing = im.Scale('Lucas_pointing.png', 1000, 1000)
image Lucas_speaking = im.Scale('Lucas_speaking.png', 1000, 1000)
image bg generator room = im.Scale('bg generator room.jpeg', 1920, 1080)
image bg storage_crowbar = im.Scale('bg storage_crowbar.jpeg', 1920, 1080)
image bg storage_witems = im.Scale('bg storage_witems.jpeg', 1920, 1080)
image bg storage_wrench = im.Scale('bg storage_wrench.jpeg', 1920, 1080)
image bg storagenoitems = im.Scale('bg storagenoitems.jpeg', 1920, 1080)
image bg mine enterance = im.Scale('bg mine enterance.jpeg', 1920, 1080)
image bg road section = im.Scale('bg road section.jpeg', 1920, 1080)
image bg leftside = im.Scale('bg leftside.jpeg', 1920, 1080)
image bg leftside2 = im.Scale('bg leftside2.jpeg', 1920, 1080)
image bg johnshand = im.Scale('bg johnshand.jpeg', 1920, 1080)
image bg johnshand2 = im.Scale('bg johnshand2.jpeg', 1920, 1080)
image bg rightside = im.Scale('bg rightside.jpeg', 1920, 1080)
image bg deep = im.Scale('bg deep.jpeg', 1920, 1080)
image bg exit = im.Scale('bg exit.jpeg', 1920, 1080)


label start:
    stop music fadeout 2.0
    scene black
    with fade

    play music "occult-chant-ambience.mp3" fadein 1.0

    $ player_name = renpy.input("What is your name?").strip()

    if not player_name:
        $ player_name = "Elias"

    n "Are you sure [player_name]? Is this your name?"

    menu:
        "Yes":
            $ p = Character(player_name)
            jump intro_scene
            
        "No":
            jump then_what_is_it

label then_what_is_it:
    scene black
    with fade

    $ player_name = renpy.input("Then what is your name?").strip()

    if not player_name:
        $ player_name = "Elias"

    n "Are you sure [player_name]? Is this your name?"

    menu:
        "Yes":
            # Charakter mit dem eingegebenen Namen erstellen
            $ p = Character(player_name)
            jump intro_scene
            
        "No":
            jump then_what_is_it

label intro_scene:

    scene bg tunnel
    with fade

    show Lucas
    with dissolve

    play music "mine_ambient.ogg" fadein 2.0

    show Lucas_speaking

    l "Did you feel that?"

    p "Feel what?"

    show Lucas_pointing

    l "The vibration. It's different today."

    p "You're imagining it. We've always worked under these circumstances."

    show Lucas_speaking

    l "I'm not imagining it. Im not delusional."

    "A small shower of dust falls from the ceiling."

    show Lucas_pointing

    l "There. That."

    scene bg tunnel

    show Lucas at left
    with move

    menu:
        "Take his concern seriously.":
            $ sanity += 1
            p "Alright. Show me the cracks."

            "You walk toward the support beams."

            "There are hairline fractures running across the rock."

            l "That wasn't here yesterday."

            scene bg tunnel

            show Lucas_speaking
            with move

            p "We should report it after the shift."

        "Brush it off":
            $ sanity -= 1
            p "We've seen worse."

            scene bg tunnel

            show Lucas
            with move

            l "You're pushing too hard."

            show Lucas_speaking

            p "We're behind schedule."

            show Lucas_speaking

    l "Why are you like this lately? Should we not report this immediately?"

    menu:
        "No, because we need the money.":
            $ sanity -= 1
            p "Overtime keeps this place running."

        "No, because I don't want another failure.":
            $ sanity += 1
            p "I can't mess this up again."


label exploration_1:

    scene bg collapse
    with fade

    play sound "blast-mining.mp3"

    p "Lucas?"
    p "Answer me!"

    play sound "radio_static.mp3"
    v "…ten more minutes…"

    menu:
        "It was just interference.":
            $ stability -= 1
            menu:
                "What can I do...":
                    p "I can't do this all by myself"
                    jump bad_ending

                "I need to get out of here":
                    jump road_section

        "Lucas?!":
            $ stability += 1
            p "I need to do something to get out of here"
            p "I really don't know what to do..."

            menu:
                "I am really stuck, desparate und alone... ":
                    p "I can't do this all by myself"
                    jump bad_ending

                "I need to get out of here":
                    jump road_section

label road_section:

    scene bg road section
    with fade

    n "You have two option."
    n "You can go either left or right."
    n "From the passage on the left you hear voices."
    n "Maybe..."
    n "They are other friends of yours, who also could've survived the collapse of the cave."
    n "However the right side seems like a better option."
    n "It is likely for you to get to the generator."
    n "What are you going to do?"

    menu:
        "Go to the left.":
            jump left_side
        
        "Go to the right.":
            jump right_side

label road_section2:

    scene bg road section
    with fade

    n "You have two option."
    n "You can go either left or right."
    n "What are you going to do?"

    menu:
        "Go to the left.":
            if "John's pickaxe" not in inventory:
                jump left_side1
            else:
                jump left_side2
        
        "Go to the right.":
            jump right_side

label road_section3:

    scene bg road section
    with fade

    n "You have two option."
    n "You can go either left or right."
    n "What are you going to do?"

    menu:
        "Go to the left.":
            jump left_side2
        
        "Go to the right.":
            jump right_side2

label road_section4:

    scene bg road section
    with fade

    n "You have two option."
    n "You can go either left or right."
    n "What are you going to do?"

    menu:
        "Go to the left.":
            if "Wrench" in inventory:
                jump left_side2
            else:
                jump left_side1
        
        "Go to the right.":
            jump right_side2


label left_side:

    n "You choose to go left.."

    scene bg leftside
    
    p "Is anyone here?!"
    n "It seems nobody is here.."
    n "You only see the broken cave shaft and a couple bats flying around in this undergound prison"
    n "You look closely and see the dead body of one of your coworker"
    p "John... Please answer me..."
    n "You begin sobbing beneath John's dead body, you see the pickaxe in his hand"
    n "You had lost yours during the collapse"
    n "It may be useful."

    n "Are you going to take the pickaxe?"

    menu:
        "Take John's pickaxe":
            scene bg johnshand
            $ inventory.append("John's pickaxe")
            n "You took John's pickaxe."
            jump road_section2

        "Don't take the pickaxe":
            n "You looked at John's cold body for the last time.."
            jump road_section2

label left_side1:

    n "You choose to go left.."

    scene bg leftside
    
    n "You begin sobbing beneath John's dead body, you see the pickaxe in his hand"
    n "You had lost yours during the collapse"
    n "It may be useful."

    n "Are you going to take the pickaxe?"

    menu:
        "Take John's pickaxe":
            scene bg johnshand
            $ inventory.append("John's pickaxe")
            n "You took John's pickaxe."
            jump road_section2

        "Don't take the pickaxe":
            n "You looked at John's cold body for the last time.."
            jump road_section2


label left_side2:

    n "You choose to go left.."

    scene bg leftside
    
    n "You only see the broken cave shaft and a couple bats flying around in this undergound prison"
    n "You look to the dead body of one of your coworker"
    n "You begin sobbing beneath John's dead body, his had is empty"
    n "You go away..."

    jump road_section2


label right_side:
    
    n "You choose to go right.."
    
    scene bg rightside

    n "You got down in the mine, it is hard to breath but you are sure that thats the way you want to go"
    n "Eventually, you reach the Section A"
    p "It is hard to breathe here. I suppose there is a gas leakage here"
    p "I really need to be fast, or else I will pass out in here"

    jump hallucination_1

label right_side2:
    
    n "You choose to go right.."
    
    scene bg rightside

    n "You got down in the mine, it is hard to breathe but you are sure that thats the way you want to go"
    n "Eventually, you reach the Section A"
    p "It is hard to breathe here. I suppose there is a gas leakage here"
    p "I really need to be fast, or else I will pass out in here"
    jump exploration_hub

label hallucination_1:

    scene bg deep
    with fade

    v "You knew."

    menu:
        "I didn’t know.":
            $ stability += 1
        "It wasn’t my fault.":
            $ stability -= 1

    jump exploration_hub

label exploration_hub:

    scene bg collapse
    with fade

    "Oxygen: [oxygen]"
    "Sanity: [sanity]"

    if oxygen <= 0:
        jump suffocation_ending

    menu:
        "Investigate Storage Tunnel":
            $ oxygen -= 10
            jump storage_tunnel

        "Check Generator Room":
            $ oxygen -= 15
            jump generator_room
        
        "Go to the closed mine enterance":
            jump mine_enterance

        "Go back to the road section":
            jump road_section4

label mine_enterance:
    scene bg mine enterance
    if "Generator working" in events:
        n "Breather Valves have released the toxic gas it is safe to approach to the enterance"
        if "John's pickaxe" not in inventory:
            n "You have nothing to break those tuff stone pieces"
            p "I should've have gotten his pickaxe"
            jump exploration_hub
        else:
            n "You have John's pickaxe"
            n "You can try to break those rocks and find your way to the surface"
            menu:
                "Try to break the rocks?":
                    play sound "rock_slide.mp3"
                    n "You break those huge rocks with determination"
                    n "Between the rocks the sunlight can be seen"
                    play sound "outside voices.mp3"
                    n "Finally you manage to find your way to the surface"
                    jump good_ending
                "Do nothing":
                    v "Are you really so desparate?"
                    v "Staying here?"
    else:
        n "The toxic gas concentration is too high"
        n "It is extremely dangerous to go to that section of the mine"
        menu:
            "Do you still want to go to there?"
            "Yes":
                jump suffocation_ending
            "No":
                "First I need to get the breather valves working"
                jump exploration_hub

label storage_tunnel:

    # İkisi de envanterde yoksa
    if "Wrench" not in inventory and "Crowbar" not in inventory:
        scene bg storage_witems
        with fade
        n "You came to the storage room"
        n "Here you can find the necessary equipment to survive"
        n "On the table there are 2 objects laying"
        n "A crowbar and a wrench"
        n "Which one are you taking?"
    # Sadece Wrench varsa → Crowbar kaldı
    elif "Wrench" in inventory and "Crowbar" not in inventory:
        scene bg storage_crowbar
        with fade
        n "You came to the storage room"
        n "On the table there is 1 object laying"
        n "Only a crowbar"
    # Sadece Crowbar varsa → Wrench kaldı
    elif "Crowbar" in inventory and "Wrench" not in inventory:
        scene bg storage_wrench
        with fade
        n "You came to the storage room"
        n "On the table there is 1 object laying"
        n "Only a wrench"
    # İkisi de varsa → boş
    else:
        scene bg storagenoitems
        with fade
        n "You came to the storage room"
        n "On the table there is nothing"
        jump exploration_hub

    menu:
            "Crowbar":
                if "Crowbar" in inventory:
                    "You have crowbar in your inventory"
                else:
                    if len(inventory) <= 3:
                        $ inventory.append("Crowbar")
                        scene bg storage_wrench
                        n "You took the Crowbar"
                    else:
                        menu:
                            "Take it?":
                                p "The things are becoming heavy"
                                if len(inventory) >= 3:
                                    "You can't carry too many items at once"
                                    "Which items do you want to drop?"
                                    menu:
                                        "[inventory[0]]":
                                            $ inventory.remove(inventory[0])
                                        "[inventory[1]]":
                                            $ inventory.remove(inventory[0])
                                        "[inventory[2]]":
                                            $ inventory.remove(inventory[0])

                                if "Wrench" in inventory:
                                    scene bg storagenoitems
                                    "You got crowbar"
                                elif "Wrench" not in inventory:
                                    scene bg storage_wrench
                                    "You got crowbar"
                            "Leave it":
                                pass
            "Wrench":
                if "Wrench" in inventory:
                    "You have wrench in your inventory"
                else:
                    if len(inventory) <= 3:
                        $ inventory.append("Wrench")
                        scene bg storage_crowbar
                        n "You took the wrench"
                    else:
                        menu:
                            "Take it?":
                                p "The things are becoming heavy"
                                if len(inventory) >= 3:
                                    "You can't carry too many items at once"
                                    "Which items do you want to drop?"
                                    menu:
                                        "[inventory[0]]":
                                            $ inventory.remove(inventory[0])
                                        "[inventory[1]]":
                                            $ inventory.remove(inventory[0])
                                        "[inventory[2]]":
                                            $ inventory.remove(inventory[0])

                                elif "Crowbar" in inventory:
                                    scene bg storagenoitems
                                    "You got wrench"
                                if "Crowbar" not in inventory:
                                    scene bg storage_crowbar
                                    "You got wrench"
                            "Leave it":
                                pass

    if sanity <= 3:
        "The shadows seem closer."
        v "[player_name]..."
    
    jump exploration_hub

label generator_room:

    scene bg generator room
    with fade

    n "You see a big panel"
    n "It is loose."

    if "Wrench" in inventory:

        menu:
            "Use Wrench to open panel":
                $ inventory.append("Generator Fuse")
                $ item_number += 1
                "You found a Generator Fuse."
                if "Generator Fuse" in inventory:
                    menu:
                        "You can start the emergency generator with this fuse"
                        "Use generator fuse":
                            $ events.append("Generator working")
                            $ inventory.remove("Generator Fuse")
                            "You used the generator fuse"
                            "Generator is now working"
                            "Breather Valves are now opened"
                        
            "Leave":
                pass
    else:
        "You need something to pry this open."

    jump exploration_hub

label suffocation_ending:

    scene black
    n "Your body's oxygen level is critical"
    "Your breathing slows."
    "Darkness consumes everything.."
    "You existence perishes out of the world"
    v "Staying here for the eternity to come"

    return

label generator_puzzle:

    p "The generator powers the emergency shaft."

    menu:
        "Restore power to Exit Shaft":
            jump deep_chamber
        "Restore power to Storage Tunnel":
            $ stability -= 1
            v "Wrong way."
            jump deep_chamber

label deep_chamber:

    scene bg deep
    with fade

    if stability >= 1:
        v "You could have stopped it."
    else:
        v "You've buried us."

label final_choice:

    menu:
        "I should have stopped the shift.":
            $ stability += 2
        "It wasn’t my fault.":
            $ stability -= 2

    if stability >= 2:
        jump good_ending
    else:
        jump bad_ending

label good_ending:

    scene bg exit
    with fade

    p "I'm sorry.."

    "Light breaks through the darkness."

    p "Some things belong beneath the surface… but not the truth."

    n "Light and the fresh air filled out your body"

    n "Although you are not below the surface anymore..."

    v "...the Echoes Beneath always linger in the hollow spaces of your mind"

    return

label bad_ending:

    scene bg deep
    with fade

    n "The desperation and the true REGRET claw reminder that even HOPE has abandoned YOU "

    n "You gave up..."

    v "[player_name]..."

    scene black
    pause 2

    "... was never found."

    return