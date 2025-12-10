#!/bin/bash

echo "=== CI Script Started ==="

PROJECT_DIR=$(pwd)
DIST_DIR="$PROJECT_DIR/dist"
INSTALL_DIR="$PROJECT_DIR/install"

echo "[CI] Рабочая директория: $PROJECT_DIR"

# 1. Проверка файлов
echo "[CI] Проверка файлов проекта..."

REQUIRED_FILES=("main.py" "calc.py" "memory.py")

for file in "${REQUIRED_FILES[@]}"; do
    if [[ ! -f "$file" ]]; then
        echo "[CI] Файл отсутствует: $file"
        exit 1
    fi
done

echo "[CI] Все требуемые файлы на месте"

# 2. Тесты
echo "[CI] Запуск тестов..."
python -m unittest discover -s . -p "test*.py"

if [[ $? -ne 0 ]]; then
    echo "[CI] Тесты не пройдены"
    exit 1
fi

echo "[CI] Все тесты успешно пройдены"

# 3. Архив
mkdir -p "$DIST_DIR"

APP_NAME="Calculator"
VERSION=$(date +"%Y.%m.%d-%H%M")
ARCHIVE="${APP_NAME}_${VERSION}.tar.gz"

echo "[CI] Создание архива: $ARCHIVE"

tar -czf "$DIST_DIR/$ARCHIVE" \
    --exclude='*.pyc' \
    --exclude='__pycache__' \
    .

echo "[CI] Архив создан: $DIST_DIR/$ARCHIVE"

# 4. Распаковка в ./install
echo "[CI] Установка в папку '$INSTALL_DIR'..."

rm -rf "$INSTALL_DIR"
mkdir -p "$INSTALL_DIR"
tar -xzf "$DIST_DIR/$ARCHIVE" -C "$INSTALL_DIR"

echo "[CI] Установка завершена!"
echo "=== CI Script Finished Successfully ==="
