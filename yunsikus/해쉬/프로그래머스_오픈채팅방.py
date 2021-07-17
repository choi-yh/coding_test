def solution(record):
    id_to_name_dict = {} # {"uid1234": "Muzi", "uid4567":"Ryan", ...}
    answer = []

    for line in record:
        line = line.split()
        if (line[0] == 'Enter') or (line[0] == 'Change'):
            id_to_name_dict[line[1]] = line[2]

    result = []
    for line in record:
        line = line.split()
        if line[0] == 'Enter':
            name = id_to_name_dict[line[1]]
            result.append('{}님이 들어왔습니다.'.format(name))
        if line[0] == 'Leave':
            name = id_to_name_dict[line[1]]
            result.append('{}님이 나갔습니다.'.format(name))
    return result
