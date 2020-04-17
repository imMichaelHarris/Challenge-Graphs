from room import Room
from player import Player
from world import World
from graph import Queue, Stack, Graph

import random
from ast import literal_eval




# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []







# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

visited = {}
traversal_graph = Graph()
current = player.current_room
stack = Stack()
queue = Queue()

print(room_graph)

# while len(visited_rooms) < len(room_graph):
#     current_room = player.current_room.id
#     room_exits = player.current_room.get_exits()
#     stack.push(room_exits)

#     #Check
#     if player.current_room.id not in visited_rooms:
#         # ?
#         # visited_rooms[player.current_room.id] = player.current_room.get_exits()
#         visited[player.current_room.id] = player.current_room.get_exits()
#         # for e in player.current_room.get_exits()

#     # print(f"While {room_exits}")
#     # push to stack then move 
#     while len(stack.stack) < 1:
#         print(stack.pop())

opposite_directions = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}


            
def mapTraversal(room, visited=[]):
    # stack = Stack()
    path = []
    # stack.push([room])
    # visited = [room]
    # print("Here", player)

    # while stack.size() > 0:
    #     room = stack.pop()[-1]
    #     for direction in player.current_room.get_exits():
    #         player.travel(direction)

    #         if player.current_room.id in visited:
    #             player.travel(opposite_directions[direction])
    #         else:
    #             visited.append(player.current_room.id)
    #             path.append(direction)
    #             path = path + player.current_room.id
    #             stack.push(path)
    #             player.travel(opposite_directions[direction])
    #             path.append(opposite_directions[direction])
    for direction in player.current_room.get_exits():
        player.travel(direction)

        if player.current_room.id in visited:
            # Go back and look and other exits for a bft
            player.travel(opposite_directions[direction])
        else:
            # Or add room in visited and add direction  to path
            # Repeat until all rooms are explored
            visited.append(player.current_room.id)
            path.append(direction)
            path = path + mapTraversal(player.current_room.id, visited)
            player.travel(opposite_directions[direction])
            path.append(opposite_directions[direction])

    return path
# def populate_graph():
#     # while True:
#     # for room_exit in player.current_room.get_exits():
#     traversal_graph.add_room_to_graph(current.id, current.get_exits())
#     stack.push(traversal_graph.rooms[current.id])
#     while stack.size() > 0:
#         e = stack.pop()
#         print(f"Pop {e}")
#         for room_exit in e:
#             print(f"loop {room_exit}")
#             print(f"visited {visited}")
#             # Room hasn't been traveled to 
#             if traversal_graph.rooms[current.id][room_exit] != "?":
#                 player.travel(room_exit)
#             player.travel(room_exit)
#             traversal_graph.add_room_to_graph(player.current_room.id, current.get_exits())
#             traversal_graph.update_rooms(current.id, room_exit, player.current_room.id)

    # if traversal_graph[current.id] not in visited:
    #     for room_exit in player.current_room.id:
    #         print(f"Exits {room_exit}")
    #         player.travel(room_exit)
    #         traversal_graph.add_room_to_graph(player.current_room.id, player.current_room.get_exits())
    #         print(f"Player {player.current_room.id}")
    #         print(f"Current {current.id}")
    #         traversal_graph.update_rooms(current.id, room_exit, player.current_room.id)
    #         # stack.push(room_exits.pop())
    #         print(f"Stack - {stack.pop()}")

# def get_unexplored()

# traversal_graph.add_room_to_graph(player.current_room.id, player.current_room.get_exits())
# traversal_graph.add_room_to_graph(3)
# traversal_graph.update_rooms(3, "n", 0)
print(f"My Path {traversal_path}")
# populate_graph()
# my_queue = []
traversal_path = mapTraversal(player)

# player.current_room.get_exits()

print(player.current_room.id)
for move in traversal_path:
    player.travel(move)
    print(player.current_room.id)
    visited_rooms.add(player.current_room)

print(f"Visited rooms {visited_rooms}, Graph length {room_graph}")


if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms {len(traversal_path)}")




#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     print(f"Current room - {player.current_room.id}")
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
