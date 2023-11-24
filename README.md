1) Получение списка всех комнат GET 'api/room_list/'

2) Фильтрация по цене и количеству мест GET api/room/?price=100&seat_number=2 апи для фильтрации

3) Сортировка GET api/room/?ordering=price, api/room/?ordering=-price или api/room/?ordering=-seat_number. Знак - сортирует значения в обратном порядке.

4)Фильтрация по времени GET /rooms?start_date=<start_date>&end_date=<end_date>

Пример ввода времени /api/room/?start_date=2022-09-21 12:00:00&end_date=2022-09-22 12:00:00

5)Бронирование POST /bookings

содержимое запроса:

{
    "room": <room_id>,
    "start_date": "<start_date>",
    "end_date": "<end_date>"
}

6) Отмена бронирования DELETE /bookings/<booking_id>

7) Просмотр записей конкретного юзера GET /users/<user_id>/

8) Регистрация пользователя POST /register
   содержимое
{
    "username": "new_username",
    "password": "new_password"
}
