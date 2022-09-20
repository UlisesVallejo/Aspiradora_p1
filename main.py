import random

class Agent:
    def __init__(self):
        self.__state = random.choice([0, 1])
        self.__environment = [random.choice([True, False]), random.choice([True, False])]
        self.__cost = 0
        self.__solution = []

    def on(self):
        print("Estado inicial")
        print("Aspiradora en lado:", "izquierdo" if self.__state == 0 else "derecho")
        print("Lado izquierdo:", "sucio" if self.__environment[0] else "limpio")
        print("Lado derecho:", "sucio" if self.__environment[1] else "limpio")
        print("--------------------------------")

        while self.__environment[0] or self.__environment[1]:
            if self.__environment[self.__state]: # limpiar
                self.__environment[self.__state] = False
                self.__cost += 1
                action = "Aspirar"

            else: # mover
                if self.__state == 0:
                    self.__state = 1
                    action = "Derecha"

                else:
                    self.__state = 0
                    action = "Izquierda"

                self.__cost += 1

            self.__solution.append(action)

            print("Acción:", action)
            print("Aspiradora en lado:", "izquierdo" if self.__state == 0 else "derecho")
            print("Lado izquierdo:", "sucio" if self.__environment[0] else "limpio")
            print("Lado derecho:", "sucio" if self.__environment[1] else "limpio")
            print("Costo acumulado:", self.__cost)
            print("--------------------------------")

        print("Acción: NoOp")
        print("Aspiradora en lado:", "izquierdo" if self.__state == 0 else "derecho")
        print("Lado izquierdo:", "sucio" if self.__environment[0] else "limpio")
        print("Lado derecho:", "sucio" if self.__environment[1] else "limpio")
        print("Costo acumulado:", self.__cost)

        print("\nSolución:", self.__solution)


if __name__ == "__main__":
    aspiradora = Agent()
    aspiradora.on()