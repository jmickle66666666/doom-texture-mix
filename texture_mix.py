import omg
import omg.mapedit
import sys
from random import shuffle

if (len(sys.argv) != 3):
    print("Usage: texture_mix.py wad_path map_name")
    sys.exit()

wad = omg.WAD(sys.argv[1])
output = omg.WAD()

def randomize_textures(twad,tmap):

    map = omg.mapedit.MapEditor(twad.maps[tmap])

    texturelist = []

    for s in map.sidedefs:
        if (s.tx_up != "-"): 
            if (s.tx_up not in texturelist):
                texturelist.append(s.tx_up)
        if (s.tx_mid != "-"): 
            if (s.tx_mid not in texturelist):
                texturelist.append(s.tx_mid)
        if (s.tx_low != "-"): 
            if (s.tx_low not in texturelist):
                texturelist.append(s.tx_low)
                
    mixed_list = texturelist[:]
    shuffle(mixed_list)

    for s in map.sidedefs:
        if (s.tx_up != "-"):
            s.tx_up = mixed_list[texturelist.index(s.tx_up)]
        if (s.tx_mid != "-"):
            s.tx_mid = mixed_list[texturelist.index(s.tx_mid)]
        if (s.tx_low != "-"):
            s.tx_low = mixed_list[texturelist.index(s.tx_low)]
        
    

    output.maps[tmap] = map.to_lumps()
    

for m in wad.maps:
    randomize_textures(wad,m)
    
output.to_file("output.wad")