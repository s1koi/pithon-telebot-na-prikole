from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.hp = self.get_hp()
        self.atk = self.get_atk()
        self.deff = self.get_deff()
        self.rare = self.rare()

        Pokemon.pokemons[pokemon_trainer] = self
    def rare(self):
        if self.pokemon_number >= 1 and self.pokemon_number < 500:
            rare = "редкий"
        elif self.pokemon_number > 500 and self.pokemon_number < 600 :
            rare = "супер редкий"
        elif self.pokemon_number > 600 and self.pokemon_number < 700 :
            rare = "ультра редкий"
        elif self.pokemon_number > 700 and self.pokemon_number < 800 :
            rare = "эпический"
        elif self.pokemon_number > 800 and self.pokemon_number < 950 :
            rare = "мифический"
        elif self.pokemon_number > 950 and self.pokemon_number < 1000 :
            rare = "легендарный"
        return (rare)
    # Метод для получения картинки покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
    
    # Метод для получения имени покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['front_default'])
        else:
            return "Ne povezlo ne fortanulo"
    
    def get_hp(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['stats'][0]['base_stat'])
        else:
            return "Ne povezlo ne fortanulo"
    
    def get_atk(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['stats'][1]['base_stat'])
        else:
            return "Ne povezlo ne fortanulo"
        
    def get_deff(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['stats'][2]['base_stat'])
        else:
            return "Ne povezlo ne fortanulo"
    
    def attack(self, enemy):
        if isinstance(enemy, Wizard): # Проверка на то, что enemy является типом данных Wizard (является экземпляром класса Волшебник)
            шанс = randint(1,5)
            if шанс == 1:
                return "Покемон-волшебник применил щит в сражении"
        if enemy.hp > self.atk:
            enemy.hp -= self.atk
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"

        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "


    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}\n\nHP покемона: {self.hp}\n\nATK покемона: {self.atk}\n\nзащита покемона: {self.deff}\n\nРедкость: {self.rare}\n\n{self.img}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    def show_hp(self):
        return self.hp


class Wizard(Pokemon):
    def attack(self, enemy):
        if isinstance(enemy, Wizard): # Проверка на то, что enemy является типом данных Wizard (является экземпляром класса Волшебник)
            шанс = randint(1,5)
            if шанс == 1:
                return "Покемон-волшебник применил щит в сражении"

class Fighter(Pokemon):
    def attack(self, enemy):
        супер_сила = randint(5,15)
        self.сила += супер_сила
        результат = super().attack(enemy)
        self.сила -= супер_сила
        return результат + f"\nБоец применил супер-атаку силой:{супер_сила} "





