class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float,
                 ):
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        print (f"Тип тренировки: {self.training_type}; Длительность: {self.duration} ч.; "
              f"Дистанция: {self.distance} км;  Ср. скорость: {self.speed} км/ч; "
              f"Потрачено ккал: {self.calories}.")



class Training:
    """Базовый класс тренировки."""
    M_IN_KM = 1000
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight


    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        dist_in_km = self.action * Running.LEN_STEP / Training.M_IN_KM
        return dist_in_km


    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        if TYPE == 'Running':
            average_speed = Running.DISTANCE / self.duration
            return average_speed
        elif TYPE == 'SportsWalking':
            average_speed = SportsWalking.DISTANCE / self.duration
            return average_speed
        elif TYPE == 'Swimming':
            average_speed = Swimming.DISTANCE / self.duration
            return average_speed


    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        if TYPE == 'Running':
            result_cal = Running.CALORIES_RUN
            return round(result_cal, 3)
        elif TYPE == 'SportWalking':
            result_cal = SportsWalking.CALORIES_WALK
            return round(result_cal, 3)
        elif TYPE == 'Swimming':
            result_cal = Swimming.CALORIES_SWIM
            return round(result_cal, 3)
        # if TYPE == 'Running':
        #     calories_burned = ((Running.coeff_calorie_1 * Training.get_mean_speed(self) - Running.coeff_calorie_2) *
        #                        self.weight / Training.M_IN_KM * self.duration * 60)
        #     return round(calories_burned, 3)
        #
        # elif TYPE == 'SportsWalking':
        #     calories_burned = (((SportsWalking.coeff_calorie_1 * self.weight) + (Training.get_mean_speed(self)**2 //
        #                                                                          SportsWalking(self.hight)) *
        #                         SportsWalking.coeff_calorie_2 * self.weight) * self.duration * 60)
        #     return round(calories_burned, 3)
        #
        # elif TYPE == 'Swimming':
        #     calories_burned = ((Training.get_mean_speed(self) + Swimming.coeff_calorie_1) * Swimming.coeff_calorie_2 *
        #                        self.weight)
        #     return round(calories_burned, 3)
        pass


    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        pass



class Running(Training):
    """Тренировка: бег."""
    LEN_STEP = 0.65
    DISTANCE = ()
    SPEED = ()
    CALORIES = ()
    CALORIES_RUN = ()
    coeff_calorie_1 = 18
    coeff_calorie_2 = 20

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ):
        super().__init__(action, duration, weight)
        dist_run = Training.get_distance(self)
        Running.DISTANCE = dist_run
        speed_run = Training.get_mean_speed(self)
        Running.SPEED = speed_run
        Running.CALORIES_RUN = ((Running.coeff_calorie_1 * Training.get_mean_speed(self) - Running.coeff_calorie_2) *
                               self.weight / Training.M_IN_KM * self.duration * 60)
        calories_run = Training.get_spent_calories(self)
        Running.CALORIES = calories_run
        message = InfoMessage('RUN', self.duration, Running.DISTANCE, Running.SPEED,
                                                      Running.CALORIES)
        message.get_message()



class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    LEN_STEP = 0.65
    DISTANCE = ()
    SPEED = ()
    CALORIES = ()
    CALORIES_WALK = ()
    coeff_calorie_1 = 0.035
    coeff_calorie_2 = 0.029

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 hight: float,
                 ):
        super().__init__(action, duration, weight)
        self.hight = hight
        dist_walk = Training.get_distance(self)
        SportsWalking.DISTANCE = dist_walk
        speed_walk = Training.get_mean_speed(self)
        SportsWalking.SPEED = speed_walk
        SportsWalking.CALORIES_WALK = (SportsWalking.coeff_calorie_1 * self.weight +
                                       (SportsWalking.SPEED ** 2 // self.hight) *
                                       SportsWalking.coeff_calorie_2 * self.weight) * (self.duration * 60)
        calories_walk = Training.get_spent_calories(self)
        SportsWalking.CALORIES = calories_walk

        message = InfoMessage('WLK', self.duration, SportsWalking.DISTANCE, SportsWalking.SPEED,
                                              SportsWalking.CALORIES)
        message.get_message()



class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP = 1.38
    DISTANCE = ()
    SPEED = ()
    CALORIES = ()
    CALORIES_SWIM = ()
    coeff_calorie_1 = 1.1
    coeff_calorie_2 = 2

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length: float,
                 quantity: int,
                 ):
        super().__init__(action, duration, weight)
        self.lenght = length
        self.quantity = quantity
        dist_swim = Training.get_distance(self)
        Swimming.DISTANCE = dist_swim
        speed_swim = Training.get_mean_speed(self)
        Swimming.SPEED = speed_swim
        Swimming.CALORIES_SWIM= ((Training.get_mean_speed(self) + Swimming.coeff_calorie_1) * Swimming.coeff_calorie_2 *
                               self.weight)
        calories_swim = Training.get_spent_calories(self)
        Swimming.CALORIES = calories_swim

        message = InfoMessage( 'SWM', self.duration, Swimming.DISTANCE, Swimming.SPEED,
                                              Swimming.CALORIES)
        message.get_message()




def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    global TYPE
    if workout_type == 'SWM':
        TYPE = 'Swimming'
        Training = Swimming(data[0], data[1], data[2], data[3], data[4])
        return Training
    elif workout_type == 'RUN':
        TYPE = 'Running'
        Training = Running(data[0], data[1], data[2])
        return Training
    elif workout_type == 'WLK':
        TYPE = 'SportWalking'
        Training = SportsWalking(data[0], data[1], data[2], data[3])
        return Training
    else:
        print(f'Неверное значение названия тренеровки')

def main(training: Training) -> None:
    """Главная функция."""
    info = Training.show_training_info
    return info

if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

