# Лабораторна робота №2. Створення та використання функцій, реалізація рекурсії
# Варіант: __ (9)
# ПІБ: __ (Ровний Максим)

# Тут має бути Ваш код

import time

racers_data = [
    {"name": "Микс", "car": "Японская девятка", "speed": 420, "drift_score": 1000000},
    {"name": "Артём", "car": "паса", "speed": 70, "drift_score": 1},
    {"name": "Макс Фесюк дединсайд тру канеки ss-rang гуль", "car": "нисан", "speed": 255, "drift_score": 8800},
    {"name": "Дима бульба", "car": "иж ода", "speed": 270, "drift_score": 6000},
    {"name": "Диана", "car": "мерседес", "speed": 220, "drift_score": 5000},
    {"name": "Юзков", "car": "геншин", "speed": 20, "drift_score": 7},
    {"name": "Кент", "car": "Nissan Silvia S14", "speed": 230, "drift_score": 6800},
    {"name": "тренер", "car": "Subaru Impreza WRX", "speed": 280, "drift_score": 10000},
    {"name": "Диана бим бим бам бам", "car": "Mitsu Lancer Evo IV BIM BAM BUM", "speed": 250, "drift_score": 6200},
    {"name": "Поплавский", "car": "Mitsu Lancer Evo III", "speed": 265, "drift_score": 7100},
    {"name": "Лёша", "car": "китайское говно", "speed": 2, "drift_score": 8},
    {"name": "Кай", "car": "Toyota MR2", "speed": 235, "drift_score": 7800},
    {"name": "Хідео", "car": "Toyota Supra RZ", "speed": 290, "drift_score": 5500},
    {"name": "Кодзо", "car": "Nissan Skyline R34", "speed": 300, "drift_score": 6500},
    {"name": "Томоякі", "car": "Honda S2000", "speed": 255, "drift_score": 8500},
    {"name": "Смайлі", "car": "Honda Integra Type R", "speed": 245, "drift_score": 7200},
    {"name": "Дайкі", "car": "Honda Civic Type R", "speed": 235, "drift_score": 7000},
    {"name": "Нобухіко", "car": "Toyota Altezza", "speed": 225, "drift_score": 6900},
    {"name": "Кьоко", "car": "Mazda RX-7 FD (Black)", "speed": 258, "drift_score": 7700},
    {"name": "Акіяма", "car": "Suzuki Cappuccino", "speed": 190, "drift_score": 8900},
]



def calculate_race_time(distance_km: float, avg_speed_kmh: float) -> float:
    """Розраховує час проходження траси у хвилинах."""
    if avg_speed_kmh <= 0:
        return 0.0
    return (distance_km / avg_speed_kmh) * 60

def calculate_drift_points(angle: float, speed: float) -> int:
    """Розраховує зароблені бали за один дрифт-кут."""
    return int((angle * 10) + (speed * 2))

def tuning_cost(base_part_price: float, install_nitro: bool = False, carbon_hood: bool = False) -> float:
    """Розраховує загальну вартість апгрейду авто (в гривнах)."""
    total = base_part_price
    if install_nitro:
        total += 150000  
    if carbon_hood:
        total += 85000   
    return total

def team_total_drift_score(*scores: int) -> int:
    """Обчислює сумарний рахунок команди гонщиків за заїзд."""
    return sum(scores)

hp_to_kw = lambda hp: round(hp * 0.7457, 2)

kmh_to_mph = lambda kmh: round(kmh * 0.621371, 2)


def find_max_speed_recursive(data: list, n: int) -> int:
    """Рекурсивно знаходить максимальну швидкість серед усіх автомобілів у базі."""
    
    if n == 1:
        return data[0]['speed']
    
    max_in_rest = find_max_speed_recursive(data, n - 1)
    current_speed = data[n - 1]['speed']
    
    return current_speed if current_speed > max_in_rest else max_in_rest

def upgrade_fleet_speed(data: list, upgrade_func: callable) -> list:
    """
    Функція вищого порядку. 
    Приймає список гонщиків та функцію тюнінгу, що змінює їхню швидкість.
    """
    upgraded_fleet = []
    for racer in data:
        new_racer = racer.copy()
        new_racer['speed'] = upgrade_func(racer['speed'])
        upgraded_fleet.append(new_racer)
    return upgraded_fleet


def main():
    print("="*50)
    print(" 🎌 KNUBA DRIFT: СИСТЕМА УПРАВЛІННЯ ПЕРЕГОНАМИ 🎌")
    print("="*50)

    turbo_upgrade = lambda speed: speed + 35 

    while True:
        print("\n🏁 ГОЛОВНЕ МЕНЮ:")
        print("1. Показати всіх гонщиків бази")
        print("2. Знайти еліту (швидкість > 250 км/год) [filter]")
        print("3. Встановити турбіни на всі авто (+35 км/год) [Функція вищого порядку]")
        print("4. Знайти максимальну швидкість (Рекурсія)")
        print("5. Розрахувати час проходження траси Ванган")
        print("6. Розрахувати вартість тюнінгу в майстерні")
        print("7. Дізнатися рахунок команди 'Akagi RedSuns' (*args)")
        print("0. Вийти з гаража")

        try:
            choice = int(input("\nОберіть опцію (0-7): "))

            if choice == 1:
                print("\nСписок гонщиків:")
                for r in racers_data:
                    print(f"Водій: {r['name']:<10} | Авто: {r['car']:<20} | Швидкість: {r['speed']} км/год | Дрифт: {r['drift_score']}")
            
            elif choice == 2:

                elite = list(filter(lambda r: r['speed'] > 250, racers_data))
                print("\nЕлітні гонщики (Швидкість > 250 км/год):")
                for r in elite:
                    print(f"{r['name']} на {r['car']} ({r['speed']} км/год)")
            
            elif choice == 3:
                upgraded = upgrade_fleet_speed(racers_data, turbo_upgrade)
                print("\nТюнінг успішно завершено! Нові показники (перші 5 авто):")
                for r in upgraded[:5]:
                    print(f"{r['car']}: {r['speed']} км/год")
            
            elif choice == 4:
                max_spd = find_max_speed_recursive(racers_data, len(racers_data))
                print(f"\nАбсолютний рекорд швидкості в базі: {max_spd} км/год!")
            
            elif choice == 5:
                dist = float(input("Введіть довжину траси (км): "))
                spd = float(input("Введіть середню швидкість авто (км/год): "))
                time_mins = calculate_race_time(dist, spd)
                print(f"\nЧас заїзду складе: {time_mins:.2f} хвилин.")
            
            elif choice == 6:
                base = float(input("Введіть базову вартість деталей (ієни): "))
                nitro_ans = input("Ставимо закис азоту (Так/Ні)? ").strip().lower()
                carbon_ans = input("Ставимо карбоновий капот (Так/Ні)? ").strip().lower()
                
                nitro = True if nitro_ans in ['так', 'yes', 'y', 'т'] else False
                carbon = True if carbon_ans in ['так', 'yes', 'y', 'т'] else False
                
                cost = tuning_cost(base, install_nitro=nitro, carbon_hood=carbon)
                print(f"\nЗагальний чек за тюнінг: {cost:,.0f} ієн.")
            
            elif choice == 7:

                score = team_total_drift_score(racers_data[1]['drift_score'], racers_data[2]['drift_score'], 7500)
                print(f"\nСумарний командний рахунок: {score} балів!")
            
            elif choice == 0:
                print("\nГлушимо мотор. До зустрічі на перевалі! 🏎️💨")
                time.sleep(1)
                break
            
            else:
                print("❌ Помилка: Такої передачі не існує! Оберіть від 0 до 7.")

        except ValueError:
            print("❌ Помилка вводу: Будь ласка, вводьте лише числа!")

if __name__ == "__main__":
    main()