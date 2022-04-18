import sys
from random import randrange, choice

COMPASS = ['n', 'w', 's', 'e']


def update_compass(go_to, current_position):
    result_position = ''
    if go_to:
        direction = (COMPASS.index(current_position) + 1) % 4 if go_to == 'l' else \
            (COMPASS.index(current_position) - 1) % 4
        result_position = COMPASS[direction]
        print(f'turning to: {result_position}')
    return result_position if result_position else current_position


def move_probes(m_size, positions, instructions):
    print('_' * 50)
    for instruction, position in zip(instructions, positions):
        index = 0
        if (position[0] <= m_size[0] and position[1] <= m_size[1]) and position[0] >= 0 and position[1] >= 0:
            print(f"Deploying probe {positions.index(position)+1} at: {position}")
            while index < len(instruction):
                i = instruction[index]

                go_to = i if i in 'lr' else ''

                position[-1] = update_compass(go_to, position[-1])
                if i == 'm':
                    if position[-1] == 'n':
                        position[1] += 1
                        print(f'going north: {position[0], position[1]}')
                    if position[-1] == 'e':
                        position[0] += 1
                        print(f'going east: {position[0], position[1]}')
                    if position[-1] == 'w':
                        position[0] -= 1
                        print(f'going west: {position[0], position[1]}')
                    if position[-1] == 's':
                        position[1] -= 1
                        print(f'going south: {position[0], position[1]}')

                index += 1
            print('_'*50)
            positions[instructions.index(instruction)] = position
        else:
            print(f"Trying to land probe {positions.index(position)+1} at: {position}")
            print(f"Probe {positions.index(position)+1} was destroyed")
            print(f"Cause: Landed outside of the landing area")

    print(positions)


def get_entry():
    with open('input.txt', 'r') as entry:
        entry = [e.replace('\n', '') for e in entry.readlines()]
        m_size_str = entry[0].split()
        m_size = (int(m_size_str[0]), int(m_size_str[1]))

    positions = []
    instructions = []
    entry_length = len(entry[1:])
    for line_index in range(1, entry_length, 2):
        current_probe_position = entry[line_index].split()
        current_probe_instructions = entry[line_index+1]

        positions.append([int(current_probe_position[0]),
                          int(current_probe_position[1]),
                          current_probe_position[2].lower()])
        instructions.append(current_probe_instructions.lower())

    return m_size, positions, instructions


def get_random_entry(random_qnt):
    directions = ['l', 'r', 'a', 'c', 'd']
    m_size = (randrange(1, 10), randrange(1, 10))
    positions = [[randrange(-5, 10), randrange(-5, 10), choice(COMPASS)] for _ in range(random_qnt)]
    instructions = [''.join([choice(directions) for _ in range(randrange(1, 10))]) for _ in range(random_qnt)]
    return m_size, positions, instructions


if __name__ == '__main__':
    random = None
    print(sys.argv)
    if len(sys.argv) >= 2:
        random = int(sys.argv[1])

    board_size, probe_positions, probe_instructions = get_random_entry(random) if random else get_entry()
    move_probes(board_size, probe_positions, probe_instructions)
