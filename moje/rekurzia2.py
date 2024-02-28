from typing import List

def seat_permutations(friends: List[str]) -> List[List[str]]:
    if len(friends) == 0:
        return [[]]
    elif len(friends) == 1:
        return [friends]

    all_permutations = []

    for i in range(len(friends)):
        current_friend = friends[i]
        remaining_friends = friends[:i] + friends[i+1:]
        remaining_permutations = seat_permutations(remaining_friends)

        for perm in remaining_permutations:
            all_permutations.append([current_friend] + perm)

    return all_permutations

# Testy:
print(seat_permutations(["Karlik","Karlos"]))  # [['Karlik', 'Karlos'], ['Karlos', 'Karlik']]
print(seat_permutations(["Karlik","Karlos", "Aida"]))  # [['Karlik', 'Karlos', 'Aida'], ['Karlik', 'Aida', 'Karlos'], ['Karlos', 'Karlik', 'Aida'], ['Karlos', 'Aida', 'Karlik'], ['Aida', 'Karlik', 'Karlos'], ['Aida', 'Karlos', 'Karlik']]
print(seat_permutations(["Karlik"]))  # [['Karlik']]
print(seat_permutations([]))  # [[]]
