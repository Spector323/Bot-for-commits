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

# Делаем 200 коммитов
for i in range(200):
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(f'Commit #{i+1} at {datetime.now()}\n')
    
    repo.index.add(['commits.log'])
    repo.index.commit(f"🤖 {random.choice(messages)} — {i+1}")
    
    wait_time = random.randint(50, 70)
    print(f"[{i+1}/200] Commit done. Waiting {wait_time} sec...")
    time.sleep(wait_time)

# Пушим все коммиты
repo.git.push()
print("✅ Все 200 коммитов отправлены!")