## CI/CD для статического сайта в SourceCraft

## Цель работы

Освоить процесс переноса Git-репозитория с платформы GitHub на платформу Yandex SourceCraft с использованием SSH-аутентификации, а также научиться настраивать локальный репозиторий для работы с несколькими удалёнными репозиториями одновременно.

---

## Задание

1. Реализовать сценарий автоматического развертывания статического сайта, построенного на движке mkdocs с использованием платформы SourceCraft ([документация](https://sourcecraft.dev/portal/docs/ru/sourcecraft/tutorials/sites)).
2. Реализовать сценарий автоматического развертывания этого же статического сайта с помощью GitHub Actions. В рамках одного локального репозитория добавить 2 удаленных репозитория (сурскрафт и origin / гитхаб). Команда для добавления репозитория показана ниже.
3. Продемонстрировать результаты выполнения. В качестве ответа оставить 4 ссылки. 
4. Для задачи 2 деплой реализовать с помощью Actions (например, [этого](https://github.com/marketplace/actions/github-pages-action) или [этого](https://github.com/marketplace/actions/deploy-mkdocs)).
Начальная последовательность шагов для выполнения задачи 1 и 2 
- Авторизуйтесь с использованием своего аккаунта в Яндекс на сайте sourcecraft.dev.
- Создайте публичную организацию.
- Создайте пустой репозиторий.
- Создайте токен для работы по HTTPS: https://sourcecraft.dev/portal/docs/ru/sourcecraft/security/pat (рекомендуется) или [SSH](https://sourcecraft.dev/portal/docs/ru/) Токен необходимо записать куда-то, чтобы не забыть, поскольку посмотреть второй раз его не получится. Токен должен быть с правами Maintainer. Лучше создавать токен по длительности на пол года / год.
- Откройте свой локальный репозиторий в IDE и добавьте дополнительный удаленный репозиторий с помощью команды `git remote add sourcecraft https://<имя_аккаунта>:<персональный_токен>@git.sourcecraft.dev/<имя_аккаунта>/<имя_репозитория>.git`
- Проверьте, что удаленный репозиторий, доступный по имени sourcecraft, был добавлен в список удаленных репозиториев `git remote -v`. У вас должен отображаться второй удаленный (remote) репозиторий sourcecraft. 
- После этого возможно выполнение команды `git push origin main`, `git push sourcecraft main`.

---

## Код и команды 

1. Организация структуры проекта

Файлы распределены согласно стандарту MkDocs:
- `mkdocs.yml` - в корне репозитория
- `docs/` - исходные Markdown-файлы
- `site/` - папка для сборки (добавлена в `.gitignore`)

Были добавлены: 
- `.github/workflows/deploy-mkdocs.yml` с описанием пайплайна сборки и публикации
- `sourcecraft/ci.yaml` - пайплайн сборки и публикации в ветку release
- `sourcecraft/sites.yaml` - указание источника для хостинга
- `requirements.txt`- упрощает установку зависимостей как локально, так и на CI-серверах.

2. Генерация SSH-ключа
```
ssh-keygen -t ed25519 -C "моя почта"
```
Использован алгоритм `ed25519` как современный и безопасный стандарт.
Ключ сохранён по умолчанию в `~/.ssh/id_ed25519`(приватный) и `~/.ssh/id_ed25519.pub` (публичный).

Публичный ключ был получен командой:
```
cat ~/.ssh/id_ed25519.pub
```
Далее он был добавлен в настройки аккаунтов GitHub и SourceCraft.
- В настройках аккаунта GitHub: `Settings → SSH and GPG keys → New SSH key`
- В настройках аккаунта SourceCraft: `Профиль → SSH Keys → Add new key`

Полезная команда для запоминания пароля в течение сессии:
```
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```
3. Перенос репозитория на SourceCraft

На платформе SourceCraft был создан новый репозиторий с именем "obabkisan-portfolio": `"Ваша мастерская" -> "Репозитории" -> "Новый репозиторий" -> "Пустой репозиторий"`. Репозиторий был создан без инициализации `README` и `.gitignore`, чтобы избежать конфликтов с уже существующей историей коммитов из GitHub

Переходим в существующий локальный репозиторий, добавляем SourceCraft как новый удалённый репозиторий:

```
cd obabkisan.github.io.git
git remote add sourcecraft ssh://ssh.sourcecraft.dev/obabkisan/obabkisan-portfolio.git
```
Проверяем, что добавилось:
```
git remote -v
```
Ожидаемый вывод:
```
origin  git@github.com:obabkisan/obabkisan.github.io.git (fetch)
origin  git@github.com:obabkisan/obabkisan.github.io.git (push)
sourcecraft  ssh://ssh.sourcecraft.dev/obabkisan/obabkisan-portfolio.git (fetch)
sourcecraft  ssh://ssh.sourcecraft.dev/obabkisan/obabkisan-portfolio.git (push)
```
5. Отправка конфигураций на платформы 
```
git add .
git commit -m "add auto-deploy configs for SourceCraft and GitHub Pages"
git push origin main # отправка на GitHub
git push sourcecraft main # тправка на SourceCraft
```
После пуша автоматически запустились пайплайны, сайты опубликованы и доступны по ссылкам:
- [статический сайт на SourceCraft](https://obabkisan.sourcecraft.site/obabkisan-portfolio/)
- [статический сайт на GitHub Pages](https://obabkisan.github.io/)
---
## Вывод

В ходе выполнения работы были освоены настройка SSH-аутентификации для работы с несколькими Git-хостингами, конфигурирование CI/CD-пайплайнов для автоматического развёртывания статического сайта на MkDocs и управление структурой репозитория. Настроена публикация сайта на GitHub Pages и SourceCraft через GitHub Actions и SourceCraft CI/CD. Полученные навыки позволяют автоматизировать обновление сайтов, управлять кодом на нескольких платформах одновременно и обеспечивать резервное копирование репозиториев с минимальными затратами времени.