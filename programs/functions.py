import devices # NEEDED

bus = devices.bus() # NEEDED

############
# BUILT-IN #
############
modredstone = bus.find("redstone")
modmonitor = bus.find("oc2:monitor")
modcomputer = bus.find("oc2:computer")
modflash_memory_flasher = bus.find("oc2:flash_memory_flasher")
modprojector = bus.find("oc2:projector")
moddiskdrive = bus.find("oc2:disk_drive")

########
# MODS #
########

# Just Stargate Mod
jsgstargatefunctions = bus.find("stargate")
jsgdhdfunctions = bus.find("jsg:dhd_milkyway")

# Valkyrien Skies
vsfunctions = bus.find("ship")

f = open('output-functions.txt', 'w')
f.write('FUNCTIONS LIST\n')
f.write('\n')
f.write('\n')
f.write('BUILT-IN FUNCTIONS\n')
f.write('\n')
f.write('REDSTONE\n')
f.write(str(modredstone))
f.write('\n')
f.write('MONITOR\n')
f.write(str(modmonitor))
f.write('\n')
f.write('COMPUTER\n')
f.write(str(modcomputer))
f.write('\n')
f.write('FLASH MEMORY FLASHER\n')
f.write(str(modflash_memory_flasher))
f.write('\n')
f.write('PROJECTOR\n')
f.write(str(modprojector))
f.write('\n')
f.write('DISK DRIVE\n')
f.write(str(moddiskdrive))
f.write('\n')
f.write('\n')
f.write('ADDED BY MODS\n')
f.write('\n')
f.write('JUST STARGATE MOD FUNCTIONS\n')
f.write('\n')
f.write('STARGATE\n')
f.write(str(Jsgstargatefunctions))
f.write('\n')
f.write('DIAL HOME DEVICE\n')
f.write(str(jsgdhdfunctions))
f.write('\n')
f.write('\n')
f.write('VALKYRIEN SKIES FUNCTIONS\n')
f.write('\n')
f.write(str(vsfunctions))
f.write('\n')
f.close()