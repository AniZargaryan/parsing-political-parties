import json
from bs4 import BeautifulSoup

# Целевая страница
URL = "https://minjust.gov.ru/ru/pages/politicheskie-partii/"
BASE_URL = "https://minjust.gov.ru" # базовый домен для относительных ссылок

# Локальный файл со скачанным HTML и файл для сохранения результата
INPUT_FILE = "page.html"
OUTPUT_FILE = "parties.json"


def load_local_html(file_path):
    """
    Читает локальный HTML-файл (file_path) и возвращает его содержимое как строку.
    Возвращает None в случае ошибки.
    """
    try:
        with open(file_path, "r", encoding = "utf-8") as f:
            return f.read()
    except OSError as e:
        print(f"Ошибка при чтении файла {file_path}: {e}")
        return None


def normalize_url(href):
    """
    Приводит ссылку href к абсолютному виду URL с https и без query-параметров.

    1) Если ссылка относительная (начинается с "/") -> добавляет базовый домен.
    2) Если ссылка начинается с "//" -> добавляет протокол "https:".
    3) Если ссылка начинается с "http://" -> заменяет на протокол "https://".
    4) Убирает query-параметры (включая "?" и всё после него).

    Если ссылки нет (href пустой или None), возвращает None.
    """

    if not href:
        return None

    href = href.strip()

    # Относительный путь -> добавляем базовый домен
    if href.startswith("/"):
        href = BASE_URL + href

    # Ссылка вида //minjust.gov.ru/... -> добавляем "https:" 
    if href.startswith("//"):
        href = "https:" + href

    # "http" -> "https"
    if href.startswith("http://"):
        href = "https://" + href[len("http://"):]

    # query-параметры (?something=...) -> убираем их
    if "?" in href:
        href = href.split("?", 1)[0]

    return href


def parse_parties(html_content):
    """
    Извлекает список политических партий и ссылки на их документы
    из HTML-страницы Минюста.

    Пример: на странице блок со списком партий выглядит так:
    ------------------------------------------------------
    <div class="page-block" id="section-765">
        <h3>Cписок зарегистрированных политических партий</h3>
        <div class="page-block-text">
            <ol>
                <li><a href="/ru/documents/7767/">Всероссийская политическая партия ...</a></li>
                <li><a href="https://minjust.gov.ru/ru/documents/7768/">КПРФ - политическая партия...</a></li>
                ...
            </ol>
        </div>
    </div>
    ------------------------------------------------------
    
    1) Находим <div> с id = "section-765" - блок со списком зарегистрированных партий
    2) Внутри находим <div class="page-block-text"> (текстовый блок) и внутри него <ol> (маркированный список)
    3) Внутри каждая партия представлена как <li> (элемент списка), внутри <li> есть <a> с текстом и ссылкой (гиперссылка на документ партии)

    Возвращает список словарей вида:
    [
        {
            "name": <название партии>,
            "doc_url": <абсолютная ссылка на документ или None>
        },
        ...
    ]
    """
    
    soup = BeautifulSoup(html_content, "html.parser")
    parties = []

    # 1) Находим <div class="page-block" id="section-765"> ... </div>
    block = soup.find("div", id = "section-765")
    if block is None:
        raise RuntimeError('Не найден блок с id="section-765" со списком партий') # ошибка в данных

    # 2) Внутри находим <div class="page-block-text">...<ol>...</ol>...</div>
    text_block = block.find("div", class_ = "page-block-text")
    if text_block is None:
        raise RuntimeError("Не найден блок с классом 'page-block-text' внутри section-765")

    ol = text_block.find("ol")
    if ol is None:
        raise RuntimeError("Не найден список <ol> с партиями внутри section-765")

    # 3) Перебираем каждую парти (<li> внутри <ol>), внутри <li> есть <a> (гиперссылка)
    for li in ol.find_all("li"):

        a_tag = li.find("a")
        
        if a_tag:
            # Текст ссылки = название партии
            name = a_tag.get_text().strip()
            raw_href = a_tag.get("href")
            doc_url = normalize_url(raw_href)
        else:
            # Если нет <a> -> берём текст всего <li>, а ссылка = None
            name = li.get_text().strip()
            doc_url = None

        # Если пустой элемент -> пропускаем его
        if not name:
            continue
        
        parties.append({
            "name": name,
            "doc_url": doc_url
        })

    return parties


def save_to_json(data, filename):
    """
    Принимает данные (data) и сохраняет их в JSON-файл (filename).
    """
    # data - список словарей
    # filename = "parties.json" - имя файла для сохранения
    try:
        with open(filename, "w", encoding = "utf-8") as f:
            json.dump(data, f, ensure_ascii = False, indent = 2)
        print(f"Данные сохранены в {filename}")
    except OSError as e:
        print(f"Ошибка при сохранении файла {filename}: {e}")


def main():
    
    print(f"Парсинг политических партий из локального HTML-файла '{INPUT_FILE}'...")
    
    html = load_local_html(INPUT_FILE)
    if not html:
        return # остановка работы функции main() (парсинг) при ошибке чтения файла

    parties = parse_parties(html)

    print(f"Найдено партий: {len(parties)}")
    i = 1
    for party in parties:
        print(f"{i}. {party['name']}: {party['doc_url']}")
        i += 1
    save_to_json(parties, OUTPUT_FILE)


if __name__ == "__main__":
    main()