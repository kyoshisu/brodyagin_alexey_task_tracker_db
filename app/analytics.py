import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy.orm import Session
from app import models


def generate_status_chart(db: Session, user_id: int):
    # Загружаем данные пользователя из БД
    tasks = db.query(models.Task.status).filter(models.Task.owner_id == user_id).all()

    if not tasks:
        return {"message": "No tasks to analyze"}

    # Превращаем в DataFrame (Pandas)
    df = pd.DataFrame(tasks, columns=["status"])

    # Группировка (Аналитика)
    status_counts = df["status"].value_counts()

    # Визуализация (Seaborn)
    plt.figure(figsize=(8, 5))
    sns.barplot(x=status_counts.index, y=status_counts.values, palette="Set2")
    plt.title(f"Статистика задач по статусам (Пользователь {user_id})")
    plt.xlabel("Статус")
    plt.ylabel("Количество задач")

    # Сохраняем график
    filepath = "tasks_analytics.png"
    plt.savefig(filepath)
    plt.close()  # Очищаем память

    return {"message": "Analytics generated", "image_path": filepath, "data": status_counts.to_dict()}