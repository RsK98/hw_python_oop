from dataclasses import dataclass


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    def get_message(self):
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration:.3f} ч.; '
                f'Дистанция: {self.distance:.3f} км; '
                f'Ср. скорость: {self.speed:.3f} км/ч; '
                f'Потрачено ккал: {self.calories:.3f}.')


@dataclass
class Training:
    """Базовый класс тренировки."""
    M_IN_KM = 1000
    LEN_STEP = 0.65

    action: int
    duration: float
    weight: float

    def get_distance(self) -> float:
        """Получить дистанцию в км."""

        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""

        speed = self.get_distance() / self.duration
        return speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

        raise NotImplementedError()

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""

        message = InfoMessage(self.__class__.__name__,
                              self.duration,
                              self.get_distance(),
                              self.get_mean_speed(),
                              self.get_spent_calories())
        return message


@dataclass
class Running(Training):
    """Тренировка: бег."""
    CF_CALORIES_RUN_1 = 18
    CF_CALORIES_RUN_2 = 20
    CF_MIN = 60

    def get_spent_calories(self):
        calories = ((((self.CF_CALORIES_RUN_1 * self.get_mean_speed()
                    - self.CF_CALORIES_RUN_2) * self.weight / self.M_IN_KM))
                    * (self.CF_MIN * self.duration))
        return calories


@dataclass
class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    CF_CALORIES_WLK_3 = 0.035
    CF_CALORIES_WLK_4 = 0.029
    CF_MIN = 60

    height: float

    def get_spent_calories(self):
        calories = ((self.CF_CALORIES_WLK_3 * self.weight
                    + (self.get_mean_speed() ** 2 // self.height)
                    * self.CF_CALORIES_WLK_4 * self.weight)
                    * (self.CF_MIN * self.duration))
        return calories


@dataclass
class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP = 1.38

    length_pool: float
    count_pool: float

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""

        speed = (self.length_pool * self.count_pool
                 / self.M_IN_KM / self.duration)
        return speed

    def get_spent_calories(self):
        cf_calories_5 = 1.1
        calories = (self.get_mean_speed() + cf_calories_5) * 2 * self.weight
        return calories


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    dict = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    if workout_type in dict:
        call_class = dict[workout_type]
        if call_class == Swimming:
            return Swimming(data[0], data[1], data[2], data[3], data[4])
        elif call_class == Running:
            return Running(data[0], data[1], data[2])
        elif call_class == SportsWalking:
            return SportsWalking(data[0], data[1], data[2], data[3])


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
