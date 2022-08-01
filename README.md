# Walk_back

## Описание

Это ветка репозитория **Walk** направленная на создание ходьбы назад для Nao V6.

## Запуск

```
git clone https://github.com/Starkit-SPL/Walk/tree/main
git checkout Walk_back
```

Запускаем webots, открываем файл nao_robocup.wbt

Открываем еще одно окно терминала и пишем:

```
source /opt/ros/galactic/setup.bash
ros2 run nao_lola nao_lola
```

Возвращаемся в терминал с репозиторием ходьбы и пишем такой код:

```
colcon build --packages_select walk_back
source /opt/ros/galactic/setup.bash
. install.setup.bash
ros2 run walk_back walk_back
```

## TO DO

- [x] Подключение к роботу и управление сервомоторами
- [ ] Файлы с фреймами при помощи pose_design
- [ ] Тесты для проверки корректной передачи фреймов на сервомоторы
- [x] Сама ходьба при помощи переключения фреймов
- [ ] Методы для запуска и остановки ходьбы через командную строку

