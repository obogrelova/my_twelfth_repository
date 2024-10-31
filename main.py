# План проекта по этапам:
# 1. Создание базового класса 'Hero'.
#    Определим атрибуты героя: 'name', 'health', 'attack_power'.
#    Добавим метод 'attack(other)', который уменьшает здоровье противника на величину атаки.
#    Реализуем метод 'is_alive()', проверяющий, жив ли герой (здоровье больше 0).
#
# 2. Создание класса 'Game'.
#    Добавим атрибуты 'player' и 'computer', которые будут экземплярами класса 'Hero'.
#    Реализуем метод 'start', который будет проводить игру, чередуя ходы игрока и компьютера до тех пор, пока
#    один из героев не потеряет всё здоровье.
#    Добавим вывод информации о каждом ходе и итог игры (победителя).
#
# 3. Реализация игровой логики.
#    Добавим случайный выбор кто начнет игру (игрок или компьютер).
#    Обеспечим чередование ходов и проверку состояния здоровья после каждой атаки.
#
# 4. Вывод результатов и интерфейс пользователя.
#    Сделаем интерфейс игры в консоли, с выводом информации о здоровье и атаке героев после каждого раунда.
#    Выведем финальный результат игры с информацией о победителе.



import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        """Наносит урон противнику."""
        damage = self.attack_power
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона!")

    def is_alive(self):
        """Проверяет, жив ли герой."""
        return self.health > 0


class Game:
    def __init__(self, player_name, computer_name="Компьютер"):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        """Начинает игру, чередует ходы до победы одного из героев."""
        print("Игра начинается!")
        print(f"{self.player.name} против {self.computer.name}!")

        turn = random.choice(["player", "computer"])

        while self.player.is_alive() and self.computer.is_alive():
            if turn == "player":
                self.player.attack(self.computer)
                if not self.computer.is_alive():
                    print(f"{self.computer.name} повержен! {self.player.name} выиграл!")
                    break
                turn = "computer"
            else:
                self.computer.attack(self.player)
                if not self.player.is_alive():
                    print(f"{self.player.name} повержен! {self.computer.name} выиграл!")
                    break
                turn = "player"

            print(f"{self.player.name} здоровье: {self.player.health}")
            print(f"{self.computer.name} здоровье: {self.computer.health}")
            print("-" * 20)

if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()