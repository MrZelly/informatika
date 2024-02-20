from typing import List

# Tuto funkci implementuj.
def seat_permutations(friends: List[str]) -> List[List[str]]:
    vsetky_moznosti = []
    if len(friends) == 0:
        return([])
    elif len(friends) == 1:
        return[friends]
    
    for i in range(len(friends)):
        aktualny = friends[i]
        zvysok = friends[:i] + friends[i+1:]
        ostatne_moznosti = seat_permutations(zvysok)

        for moznost in ostatne_moznosti:
            vsetky_moznosti.append([aktualny] + moznost)
    
    return(vsetky_moznosti)
        

# Testy:
print(seat_permutations(["Karlik","Karlos"]))  # [['Karlik', 'Karlos'], ['Karlos', 'Karlik']]
print(seat_permutations(["Karlik","Karlos", "Aida", "Test", "B"]))  # [['Karlik', 'Karlos', 'Aida'], ['Karlik', 'Aida', 'Karlos'], ['Karlos', 'Karlik', 'Aida'], ['Karlos', 'Aida', 'Karlik'], ['Aida', 'Karlik', 'Karlos'], ['Aida', 'Karlos', 'Karlik']]
print(len(seat_permutations(["Karlik","Karlos", "Aida", "Test", "B"])))
print(seat_permutations(["Karlik"]))  # [['Karlik']]
print(seat_permutations([]))  # [[]]

