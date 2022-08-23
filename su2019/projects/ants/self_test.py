# import ants, importlib
# importlib.reload(ants)
# hive = ants.Hive(ants.AssaultPlan())
# dimensions = (2, 9)
# colony = ants.AntColony(None, hive, ants.ant_types(),
# 	ants.dry_layout, dimensions)
# queen_tunnel, side_tunnel = [[colony.places['tunnel_{0}_{1}'.format(i, j)] for j in range(9)] for i in range(2)]
# queen = ants.QueenAnt()
# queen_tunnel[7].add_insect(queen)

# thrower = ants.ThrowerAnt()
# fire = ants.FireAnt()
# ninja = ants.NinjaAnt()
# side = ants.ThrowerAnt()
# front = ants.NinjaAnt()

# queen_tunnel[0].add_insect(thrower)
# queen_tunnel[1].add_insect(fire)
# queen_tunnel[2].add_insect(ninja)
# queen_tunnel[8].add_insect(front)
# side_tunnel[0].add_insect(side)

# buffed_ants = [thrower, fire, ninja]
# print(buffed_ants)
# old_dmgs = [ant.damage for ant in buffed_ants]
# print(old_dmgs)
# queen.action(colony)
# for ant, dmg in zip(buffed_ants, old_dmgs):
# 	assert ant.damage == dmg * 2,\
# 	"{0}'s damage is {1}, but should be {2}".format(ant, ant.damage, dmg * 2)
# for ant in [side, front]:
# 	assert ant.damage == dmg,\
# 	"{0}'s damage is {1}, but should be {2}".format(ant, ant.damage, dmg)
# assert queen.damage == 1,\
# 'QueenAnt damage was modified to {0}'.format(ant.damage)
# tank = ants.TankAnt()
# guard = ants.BodyguardAnt()
# queen_tank = ants.TankAnt()
# queen_tunnel[6].add_insect(tank)
# queen_tunnel[1].add_insect(guard)
# queen_tunnel[7].add_insect(queen_tank)
# buffed_ants.extend([tank, guard])
# print(buffed_ants)
# old_dmgs.extend([ant.damage for ant in [tank, guard, queen_tank]])
# print(old_dmgs)
# queen.action(colony)
# for ant, dmg in zip(buffed_ants, old_dmgs):
# 	print(ant, ant.damage, dmg)
# 	assert ant.damage == dmg * 2,\
# 	"{0}'s damage is {1}, but should be {2}".format(ant, ant.damage, dmg * 2)


# import ants, importlib
# importlib.reload(ants)
# hive = ants.Hive(ants.AssaultPlan())
# dimensions = (2, 9)
# colony = ants.AntColony(None, hive, ants.ant_types(),
#          ants.dry_layout, dimensions)
# queen = ants.QueenAnt()
# impostor = ants.QueenAnt()
# container = ants.TankAnt()
# colony.places['tunnel_0_3'].add_insect(container)
# colony.places['tunnel_0_3'].add_insect(impostor)
# impostor.action(colony)
# colony.places['tunnel_0_3'].ant is container
# print(colony.places['tunnel_0_3'].ant)

# import ants, importlib
# importlib.reload(ants)
# hive = ants.Hive(ants.AssaultPlan())
# dimensions = (2, 9)
# colony = ants.AntColony(None, hive, ants.ant_types(),
#          ants.dry_layout, dimensions)
# ants.bees_win = lambda: None
# # QueenAnt Placement
# queen = ants.QueenAnt()
# impostor = ants.QueenAnt()
# front_ant, back_ant = ants.ThrowerAnt(), ants.ThrowerAnt()
# tunnel = [colony.places['tunnel_0_{0}'.format(i)]
#          for i in range(9)]
# tunnel[1].add_insect(back_ant)
# tunnel[7].add_insect(front_ant)
# tunnel[4].add_insect(impostor)
# print(impostor.place)
# impostor.action(colony)

# from ants import *
# hive, layout = Hive(AssaultPlan()), dry_layout
# dimensions = (1, 9)
# colony = AntColony(None, hive, ant_types(), layout, dimensions)
# # Testing Slow
# slow = SlowThrower()
# bee = Bee(3)
# colony.places["tunnel_0_0"].add_insect(slow)
# colony.places["tunnel_0_4"].add_insect(bee)
# slow.action(colony)
# colony.time = 1
# bee.action(colony)
# bee.place.name # SlowThrower should cause slowness on odd turns
# print(bee.place.name)
# colony.time += 1
# bee.action(colony)
# bee.place.name
# print(bee.place.name)
# for _ in range(3):
#     colony.time += 1
#     bee.action(colony)
# bee.place.name
# print(bee.place.name)

# from ants import *
# hive, layout = Hive(AssaultPlan()), dry_layout
# dimensions = (1, 9)
# colony = AntColony(None, hive, ant_types(), layout, dimensions)
# # Testing Scare
# error_msg = "ScaryThrower doesn't scare for exactly two turns."
# scary = ScaryThrower()
# bee = Bee(3)
# colony.places["tunnel_0_0"].add_insect(scary)
# colony.places["tunnel_0_4"].add_insect(bee)
# scary.action(colony)
# bee.action(colony)
# bee.place.name # ScaryThrower should scare for two turns

# from ants import *
# hive, layout = Hive(AssaultPlan()), dry_layout
# dimensions = (1, 9)
# colony = AntColony(None, hive, ant_types(), layout, dimensions)
# # Testing if effects stack
# slow = SlowThrower()
# bee = Bee(3)
# slow_place = colony.places["tunnel_0_0"]
# bee_place = colony.places["tunnel_0_4"]
# slow_place.add_insect(slow)
# bee_place.add_insect(bee)
# for _ in range(2):    # slow bee two times
#    slow.action(colony)
# colony.time = 1
# for _ in range(5):        # bee should only move on odd times
#    bee.action(colony)
#    colony.time += 1
# bee.place.name

# from ants import *
# hive, layout = Hive(AssaultPlan()), dry_layout
# dimensions = (1, 9)
# colony = AntColony(None, hive, ant_types(), layout, dimensions)
# # Testing if effects stack
# slow = SlowThrower()
# bee = Bee(3)
# slow_place = colony.places["tunnel_0_0"]
# bee_place = colony.places["tunnel_0_4"]
# slow_place.add_insect(slow)
# bee_place.add_insect(bee)
# for _ in range(2):    # slow bee two times
#    slow.action(colony)
# colony.time = 1
# for _ in range(5):        # bee should only move on odd times
#    bee.action(colony)
#    colony.time += 1
# bee.place.name
# colony.time += 1      # slow effects have worn off
# print(colony.time, bee.duration)
# bee.action(colony)
# bee.place.name
# print(bee.place.name)


from ants import *
hive, layout = Hive(AssaultPlan()), dry_layout
dimensions = (1, 9)
colony = AntColony(None, hive, ant_types(), layout, dimensions)
# Testing Scare
error_msg = "ScaryThrower doesn't scare for exactly two turns."
scary = ScaryThrower()
bee = Bee(3)
colony.places["tunnel_0_0"].add_insect(scary)
colony.places["tunnel_0_4"].add_insect(bee)
scary.action(colony)
bee.action(colony)
bee.place.name # ScaryThrower should scare for two turns
bee.action(colony)
bee.place.name # ScaryThrower should scare for two turns
bee.action(colony)
bee.place.name



