import omg
import omg.mapedit
import sys
from random import shuffle

if (len(sys.argv) != 2):
    print("Usage: texture_mix.py wad_path")
    sys.exit()

wad = omg.WAD(sys.argv[1])
output = omg.WAD()

def randomize_textures(twad,tmap):

    map = omg.mapedit.MapEditor(twad.maps[tmap])

    texturelist = []
    floorlist = []
    ceillist = []
    
    for f in map.sectors:
        if (f.tx_floor != "F_SKY1"): floorlist.append(f.tx_floor)
        if (f.tx_ceil != "F_SKY1"): ceillist.append(f.tx_ceil)
    
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
    mixed_flist = floorlist[:]
    mixed_clist = ceillist[:]
    shuffle(mixed_list)
    shuffle(mixed_flist)
    shuffle(mixed_clist)
    
    for f in map.sectors:
        if (f.tx_floor != "F_SKY1"): f.tx_floor = mixed_flist[floorlist.index(f.tx_floor)]
        if (f.tx_ceil != "F_SKY1"): f.tx_ceil = mixed_clist[ceillist.index(f.tx_ceil)]

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