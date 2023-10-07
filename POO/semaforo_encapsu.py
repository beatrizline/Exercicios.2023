import time

class Semaforo:
    def __init__(self, t_verde=0, t_vermelho=0, t_amarelo=0, principal=True, sem_sec=None):
        self.__t_verde = t_verde
        self.__t_vermelho = t_vermelho
        self.__t_amarelo = t_amarelo
        self.__principal = principal
        self.__sem_sec = sem_sec

    def __str__(self):
        return f"Semaforo: principal={self.__principal}, t_verde={self.__t_verde}, t_vermelho={self.__t_vermelho}, t_amarelo={self.__t_amarelo}, principal={self.__principal}, sem_sec={self.__sem_sec}"

    def ligar_semaforo(self):
        if self.__principal and self.__sem_sec is not None:
            raise ValueError("Não é permitido ligar um semáforo principal a um semáforo secundário.")

        while True:
            print(self)
            print('Verde')
            time.sleep(self.__t_verde)
            print('Vermelho')
            time.sleep(self.__t_vermelho)
            print("Amarelo")
            time.sleep(self.__t_amarelo)

if __name__ == '__main__':
    s1 = Semaforo(5,3,1,True)
    s2 = Semaforo(10,8,2, s1)

    try:
        s3 = Semaforo(10,8,2,True, s2)
    except ValueError as a:
        print(a)

    s1.ligar_semaforo()