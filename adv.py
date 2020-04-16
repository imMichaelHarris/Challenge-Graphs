from room import Room
from player import Player
from world import World
from graph import Queue, Stack, Graph
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

graph = Graph()
# Create graph
# Populate graph by moving in direction and updating the adjacency list values
queue = Queue()
queue.enqueue([player.current_room])
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)
count = 0
# while queue.size() > 0:
while count < 5:
    room = world.starting_room
    graph.add_vertex(room.id)
    for direction in room.get_exits():
        print("Hi", direction)
        print(room.get_room_in_direction(direction).id)
        room.connect_rooms(direction, room.get_room_in_direction(direction))
        room_id = room.get_room_in_direction(direction).id
        if room_id not in graph.vertices:
            print("Here")
            graph.add_vertex(room_id)
    print(graph.vertices)
    count+= 1


for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
