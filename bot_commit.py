import git
from datetime import datetime
import time
import random
import os

# Путь к локальному репозиторию
repo_path = r'C:\Users\llllllllk\Desktop\Bot-for-commits'

# Файл для обновления
file_path = os.path.join(repo_path, 'commits.log')

# Сообщения для коммитов
messages = [
    "Fix bug", "Update dependencies", "Improve performance",
    "Update README.md", "Clean code", "Add new feature"
]

# Открываем репозиторий
repo = git.Repo(repo_path)

# Получаем удалённый репозиторий и текущую ветку
origin = repo.remote(name='origin')
current_branch = repo.active_branch

print(f"🔧 Работаем в ветке: {current_branch}")

# Делаем 200 коммитов с пуши после каждого
for i in range(200):
    # Обновляем файл
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(f'Commit #{i+1} at {datetime.now()}\n')

    # Добавляем изменения
    repo.index.add(['commits.log'])

    # Делаем коммит
    commit_msg = f"🤖 {random.choice(messages)} — {i+1}"
    repo.index.commit(commit_msg)
    print(f"[{i+1}/200] Коммит создан: {commit_msg}")

    # Отправляем на GitHub
    try:
        origin.push(refspec=f"{current_branch}:{current_branch}")
        print(f"[{i+1}/200] Коммит отправлен на GitHub ✅")
    except Exception as e:
        print(f"❌ Ошибка при пуше {i+1}: {e}")
        break

    # Пауза между коммитами (50–70 секунд)
    wait_time = random.randint(50, 70)
    print(f"[{i+1}/200] Жду {wait_time} секунд перед следующим коммитом...")
    time.sleep(wait_time)

print("🎉 Все коммиты успешно обработаны!")