# Walk
Repository for NAO V6 walking code

## Правила работы с GitHub

### Порядок действий

1) На гитхабе в разделе Issues создаем new issue с осмысленным названием. Также можно создать ветку у себя в локальном репозитории.
2) Работа ведется у себя на ветке.
3) Комит пишется в соответствии со следующей структурой: "*Изменения, сделанные в коммите*" (коммиты пишем на удобном вам языке).
4) Пушим ветку на удаленный репозиторий.

### Ветки в GitHub
Создание ветки
```
git branch branch_name
```
Переключиться на нужную ветку
```
git checkout branch_name
```

Основная ветка имеет название "main". В ней работать нельзя.

## Работа на своей ветке

### Как работать с локальным репозиторием

Откройте командную строку и переключитесь на нужную вам папку. Далее пишите в комнадной строке:

```
git pull github_repo_link
```

Здесь вместо github_repo_link" ссылка на нужный вам репозиторий. Потом переключитесь на нужную вам ветку:

```
git checkout branch_name
```

branch_name - это имя ветки. После того, как вы поработали с кодом и решили запушить изменения на удаленный репозиторий пишете:

```
git add file_name
git commit
```

Здесь file_name это имя файла или нескольких файлов, в которых произошли изменения.

### Пару полезных советов

На своей ветке можно (и даже нужно) поменять файл с описанием (README.md) на тот, который нужен вам. В этом файле должно быть описание того, как должна происходить сборка и запуск ноды для симулятора webots.

При работе не переключайтесь на чужие ветки, чтобы избежать конфликты. Если все же вы вдвоем работаете над одной веткой и конфликты неизбежны, заранее решите, как вы будете решать данную проблему (можно делить код на два и более файлов, чтобы было удобнее пользоваться git merge).

Не стоит пушить на github нерабочий и тем более не собирающийся код. Старайтесь, чтобы на удаленном репозитории находились последние рабочие версии (они могут включать в себя какие-либо некритические ошибки и баги, которые стоит отмечать в тексте коммита). Версии с незапускающимся, несобиращимся и включающем в себя критические ошибки (например segmentation fault) кодом на удаленный репозиторий пушить не стоит, дабы не смутить других людей, которые будут использовать ваш код.
