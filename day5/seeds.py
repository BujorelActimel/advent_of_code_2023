def main():
    maps = read_file("input.txt")[len("seeds: "):]
    seeds, maps = get_seeds(maps)
    seed_to_soil, maps = get_map(maps, "seed-to-soil map:\n", "soil-to")
    soil_to_fertilizer, maps = get_map(maps, "soil-to-fertilizer map:\n", "fertilizer-to")
    fertilizer_to_water, maps = get_map(maps, "fertilizer-to-water map:\n", "water-to")
    water_to_light, maps = get_map(maps, "water-to-light map:\n", "light-to")
    light_to_temperature, maps = get_map(maps, "light-to-temperature map:\n", "temperature-to")
    temperature_to_humidity, maps = get_map(maps, "temperature-to-humidity map:\n", "humidity-to")
    humidity_to_location, maps = get_map(maps, "humidity-to-location map:\n", eof=True)

    curr_location = float('inf')
    for _, seed in enumerate(seeds):
        soil = get_value(seed_to_soil, seed)
        fertilizer = get_value(soil_to_fertilizer, soil)
        water = get_value(fertilizer_to_water, fertilizer)
        light = get_value(water_to_light, water)
        temperature = get_value(light_to_temperature, light)
        humidity = get_value(temperature_to_humidity, temperature)
        location = get_value(humidity_to_location, humidity)
        if location < curr_location:
            curr_location = location

    print(curr_location)


def get_seeds(maps: str):
    next_i = maps.index("seed-to-soil map:\n")
    for i, c in enumerate(maps):
        if c == '\n':
            seeds_str = maps[0:i]
            seeds = map(int, seeds_str.split(" "))
            return list(seeds), maps[next_i:]


def get_map(maps: str, header: str, next_header: str = "", eof: bool = False):
    next_i = maps.index(next_header) if not eof else len(maps)
    soil_fertilizer_maps = maps[len(header):next_i]
    result = extract_map(soil_fertilizer_maps.splitlines())
    return result, maps[next_i:]


def extract_map(lines: list[str]) -> dict:
    result = []
    for entry in lines:
        if len(entry) > 0:
                           # (dst, src, r)
            result.append( tuple(map(int, entry.split(" "))) )

    return result


def get_value(map, key):
    dst, src, r = 0, 1, 2

    for m in map:
        if key >= m[src] and key < m[src]+m[r]:
            return m[dst] + (key - m[src])

    return key


def read_file(path: str) -> str:
    with open(path, 'r') as f:
        return f.read()


if __name__ == '__main__':
    main()


# def main():
#     all_matrixes = []
#     with open("test_input.txt") as f:
#         lines = f.readlines()
#         seeds = list(map(int, lines[0].split(": ")[1].strip().split()))

#         for i in range(2, 33):
#             if "map" in lines[i]:
#                 curr_matrix = []
#             elif lines[i].strip() == "":
#                 all_matrixes.append(curr_matrix)
#             else:
#                 curr_matrix.append(list(map(int, lines[i].strip().split())))
#         all_matrixes.append(curr_matrix)
    
#     for matrix in all_matrixes:
#         transform(seeds, matrix)

#     print(min(seeds))
            

# def transform(seeds, matrix):
#     new_values = {}
#     for i in range(len(seeds)):
#         for line in matrix:
#             destination_start, source_start, length = line
#             if seeds[i] in range(source_start, source_start + length):
#                 new_values[i] = destination_start + seeds[i] - source_start
    
#     for i in range(len(seeds)):
#         if i in new_values:
#             seeds[i] = new_values[i]


# if __name__ == '__main__':
#     main()
