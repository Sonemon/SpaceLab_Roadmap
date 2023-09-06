import logging

#logging.basicConfig(level=logging.ERROR, encoding='utf-8')

def isPlantsWin(plants: list, zombies: list):
    '''Проверяем выйграют ли растения против зомби'''
    def whoWinBattle(plant, zombie):
        '''Проверка кто победит на своих индексах'''
        if plant == zombie: return 0,0
        elif plant>zombie: return plant,0
        else: return 0,zombie
    
    try:
        for i in range(min(len(plants), len(zombies))):
            plants[i],zombies[i] = whoWinBattle(plants[i], zombies[i])
        if len(zombies) > len(plants): return False
        if sum(plants) >= sum(zombies): return True
        else: return False
        
    except Exception as e :
        logging.error(f"Error: {e}")
        return False

print(isPlantsWin([2,4,6,8],[1,3,5,7]))
print(isPlantsWin([2,4],[1,3,5,7]))
print(isPlantsWin([2,4,0,8],[1,3,5,7]))
print(isPlantsWin([1,2,1,1],[2,1,1,1]))