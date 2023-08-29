import logging

#logging.basicConfig(level=logging.ERROR, encoding='utf-8')

def isPifagorTriangle(vertices: list):
    try:
        if len(vertices) != 3:
            raise ValueError("В списке не 3 элемента")
        
        vertices.sort()
        return vertices[2]**2 == vertices[0]**2 + vertices[1]**2
    except Exception as e :
        logging.error(f"Упс, ошибка: {e}")
        return False

print(isPifagorTriangle([5,3,4]))
print(isPifagorTriangle([6,8,10]))
print(isPifagorTriangle([100,3,65]))