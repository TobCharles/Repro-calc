
print("=============== REPROCESSING CALCULATOR ===============\n")

# this is supposed to work, but get_sec_type() always gets skipped regardless of rig_mod's values, why?
def get_rig_type() -> int:
    global rig_type, rig_mod

    print("""Step 1: Select Rig type:\n
    1. Tech I Structure rig
    2. Tech II Structure rig
    9. Unsure (calculation assumes un-rigged)
    0. No Structure rig
    """)

    rig_type = input("Rig type:")
    while rig_type not in ['1','2','9','0']:
        print("Invalid, please pick options 1,2,9 or 0:")
        rig_type = input("Rig type:")
    if rig_type == 1:
        rig_mod = 1
    elif rig_type == 2:
        rig_mod = 3
    else:
        rig_mod = 0
    
    return rig_mod

def get_sec_type(rig_mod: int) -> float:
    global sec_type, sec_mod

    if rig_mod == 0:
        sec_mod = 0.0
        print("\nNOTICE: Structure is unrigged, skipping security modifier...\n")
    else:
        print("""Step 2: Select Security Modifier:\n
        1. High-Security
        2. Low-Security
        3. Null-Security/W-Space
        """)
        while sec_type not in ['1','2','3']:
            print("Invalid, please pick options 1-3:")
            sec_type = input("Security value:")
        if sec_type == 2:
            sec_mod = 0.06
        elif sec_type == 3:
            sec_mod = 0.12
        else:
            sec_mod = 0
        
        return sec_mod

def get_strc_type() -> float:
    global strc_type, strc_mod

    print("""Step 3: Select structure type:\n
    1. Athanor structure
    2. Tatara structure
    9. Other structure types
    """)

    strc_type = input("Structure type:")
    while strc_type not in ['1','2','9']:
        print("Invalid, please pick options 1,2 or 9:")
        strc_type = input("Structure type:")
    if strc_type == 1:
        strc_mod = 0.02
    elif strc_type == 2:
        strc_mod = 0.055
    else:
        strc_mod = 0.0

    return strc_mod

def get_rep_skill() -> int:
    global rep_skill, rep_mod

    print("""Step 4: Select reprocessing skill level:
    1. Reprocessing I
    2. Reprocessing II
    3. Reprocessing III
    4. Reprocessing IV
    5. Reprocessing V
    0. No Reprocessing skill
    """)

    rep_skill = input("Reprocessing Skill:")
    while rep_skill not in range(0,6):
        print("Invalid, please pick options 1-5 or 0:")
        rep_skill = input("Reprocessing Skill:")
    else:
        rep_mod = rep_skill

    return rep_mod

def get_eff_skill() -> int:
    global eff_skill, eff_mod

    print("""Step 5: Select reprocessing efficiency skill level:
    1. Reprocessing Efficiency I
    2. Reprocessing Efficiency II
    3. Reprocessing Efficiency III
    4. Reprocessing Efficiency IV
    5. Reprocessing Efficiency V
    0. No Reprocessing Efficiency skill
    """)

    eff_skill = input("Reprocessing Skill:")
    while eff_skill not in range(0,6):
        print("Invalid, please pick options 1-5 or 0:")
        eff_skill = input("Reprocessing Skill:")
    else:
        eff_mod = rep_skill

    return eff_mod

def get_ore_skill() -> int:
    global ore_skill, ore_mod

    print("""Step 6: Select specific ore skill level:
    1. <Ore> Reprocessing I
    2. <Ore> Reprocessing II
    3. <Ore> Reprocessing III
    4. <Ore> Reprocessing IV
    5. <Ore> Reprocessing V
    0. No <Ore> Reprocessing skill
    """)

    ore_skill = input("Specific Ore Skill:")
    while ore_skill not in range(0,6):
        print("Invalid, please pick options 1-5 or 0:")
        ore_skill = input("Specific Ore Skill:")
    else:
        ore_mod = ore_skill

    return ore_mod

def get_imp_type() -> float:
    global imp_type, imp_mod

    print("""Step 7: Select Implants:
    1. RX-801 Implant
    2. RX-802 Implant
    3. RX-804 Implant
    0. No Implants
    """)

    imp_type = input("Implant Type:")
    while imp_type not in range(0,4[1]):
        print("Invalid, please pick options 1-3 or 0:")
        imp_type = input("Implant Type:")
    if imp_type == 1:
        imp_mod = 0.01
    elif imp_type == 2:
        imp_mod = 0.02
    elif imp_type == 3:
        imp_mod = 0.04
    else:
        imp_mod = 0.0

    return imp_mod

get_rig_type()
get_sec_type(rig_mod)
get_strc_type()

print(
    "You have selected options:\nRig Type:",
    rig_mod,
    "\n" "Security Type:",
    sec_mod,
    "\n" "Structure Type:",
    strc_mod,
    "\n" "Reprocessing Skill:",
    rep_mod,
    "\n" "Efficiency Skill:",
    eff_mod,
    "\n" "Specific Skill:",
    ore_mod,
    "\n" "Implant Type:",
    imp_mod
)


