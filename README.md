# Password Manager

Проект Password Manager представляет собой простое консольное приложение для управления паролями. Приложение использует шифрование для безопасного хранения паролей.

## Установка

1. Убедитесь, что у вас установлен Python версии 3 и выше.
2. Установите библиотеку cryptography, используя pip:

3. ## Использование

1. Запустите файл `password_manager.py`.
2. Выберите один из двух режимов: добавление нового пароля (`add`) или просмотр существующих паролей (`view`).
3. Для добавления нового пароля введите логин и пароль. Пароль будет зашифрован и сохранен в файле `passwords.txt`.
4. Для просмотра существующих паролей введите `view`. Все пароли будут дешифрованы и выведены на экран.

Примечание: При первом запуске программа создаст файл `key.key`, в котором будет храниться ключ шифрования. Не удаляйте или не изменяйте этот файл, иначе вы потеряете доступ к зашифрованным паролям.
