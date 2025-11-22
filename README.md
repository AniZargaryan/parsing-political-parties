# parsing-political-parties

A tool for parsing data from the HTML page of the Russian Ministry of Justice website. The goal is to extract the names of parties and links to their documents from the page, convert the links to the correct absolute form, and save the result in a convenient data structure.

## How does the program work?
The program:
1. Opens the local file page.html containing the HTML code of the page
2. Finds the section with the list of political parties on the page
3. Extracts:
- the name of each party
- a link to the corresponding document (if there is one; if not, returns None)
- corrects links (relative -> absolute, http -> https, without query parameters)
3. Outputs the found data to the console
4. Saves the result to the parties.json file

## Data

**Where does HTML come from and how do you prepare it?**

Landing page: https://minjust.gov.ru/ru/pages/politicheskie-partii/

Since a direct request via requests can lead to errors, a **local HTML file** is used. 
It is saved manually:
1. Open the page in a browser.
2. Right-click -> **Сохранить страницу как...** (***Ctrl + S***)
3. Format: **Веб-страница, только HTML (*.html; *.htm)**
4. File name: **page.html**
5. Place this file in the root of the project next to **parse_parties.py** (*C:\Users\User\parsing-political-parties*)

This is the file that will be processed by the program.

## Project structure
```bash
parsing-political-parties
├─ .gitignore        # excludes venv/, __pycache__/, *.pyc, and other temporary files for Python
├─ page.html         # locally saved HTML page of the Russian Ministry of Justice website
├─ parse_parties.py  # main parser script
├─ parties.json      # example of saved results in the form of a list of dictionaries
├─ README.md         # documentation: description, configuration, launch
└─ requirements.txt  # list of libraries used (beautifulsoup4)
```

## Requirements / Dependencies

- **Python 3.10+**
- External library: **BeautifulSoup4**
- Standard library: **json**
- Dependencies are listed in the file: [`requirements.txt`](./requirements.txt)
```bash
beautifulsoup4
```

## Installation

```bash
# 1) Clone the repository
git clone https://github.com/AniZargaryan/parsing-political-parties.git
cd parsing-political-parties

# 2) Create and activate a virtual environment
python -m venv venv
## On Windows:
venv\Scripts\activate
## On macOS/Linux:
source venv/bin/activate

# 3) Install dependencies
python -m pip install -r requirements.txt
```

## Run the program

```bash
python parse_parties.py
```

## Results

After launching, you will see a list of parties in the *console/terminal*, and the result will be saved in the **parties.json** file.

### Example of final entry:

**Console / Terminal:**
```bash
Парсинг политических партий из локального HTML-файла 'page.html'...
Найдено партий: 21
1. Всероссийская политическая партия «ЕДИНАЯ РОССИЯ»: https://minjust.gov.ru/ru/documents/7767/
2. КПРФ - политическая партия КОММУНИСТИЧЕСКАЯ ПАРТИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ: https://minjust.gov.ru/ru/documents/7768/
3. Политическая партия ЛДПР – Либерально-демократическая партия России: https://minjust.gov.ru/ru/documents/7769/
4. Всероссийская политическая партия «ПАРТИЯ РОСТА»: https://minjust.gov.ru/ru/documents/7773/
5. Социалистическая политическая партия «СПРАВЕДЛИВАЯ РОССИЯ - ПАТРИОТЫ - ЗА ПРАВДУ»: https://minjust.gov.ru/ru/documents/7772/
6. Политическая партия «Российская объединенная демократическая партия «ЯБЛОКО»: https://minjust.gov.ru/ru/documents/7771/
7. Политическая партия «Демократическая партия России»: https://minjust.gov.ru/ru/documents/7775/
8. Политическая партия «Российская экологическая партия «ЗЕЛЁНЫЕ»: https://minjust.gov.ru/ru/documents/7784/
9. Политическая партия КОММУНИСТИЧЕСКАЯ ПАРТИЯ КОММУНИСТЫ РОССИИ: https://minjust.gov.ru/ru/documents/7785/
10. Всероссийская политическая партия ПАРТИЯ ЗА СПРАВЕДЛИВОСТЬ!: https://minjust.gov.ru/ru/documents/7787/
11. Политическая партия «ПАРТИЯ ПРОГРЕССА»: https://minjust.gov.ru/ru/documents/7776/
12. Политическая партия РОССИЙСКАЯ ПАРТИЯ СВОБОДЫ И СПРАВЕДЛИВОСТИ: https://minjust.gov.ru/ru/documents/7782/
13. Политическая партия СОЦИАЛЬНОЙ ЗАЩИТЫ: https://minjust.gov.ru/ru/documents/7788/
14. Политическая партия «РОССИЙСКАЯ ПАРТИЯ ПЕНСИОНЕРОВ ЗА СОЦИАЛЬНУЮ СПРАВЕДЛИВОСТЬ»: https://minjust.gov.ru/ru/documents/7790/
15. Политическая партия «Гражданская Платформа»: https://minjust.gov.ru/ru/documents/7791/
16. ВСЕРОССИЙСКАЯ ПОЛИТИЧЕСКАЯ ПАРТИЯ «РОДИНА»: https://minjust.gov.ru/ru/documents/7794/
17. Политическая партия «Казачья партия Российской Федерации»: https://minjust.gov.ru/ru/documents/7797/  
18. Политическая партия «Партия Возрождения России»: https://minjust.gov.ru/ru/documents/7803/
19. Политическая партия ЗЕЛЕНАЯ АЛЬТЕРНАТИВА: https://minjust.gov.ru/ru/documents/7818/
20. Политическая партия «Партия прямой демократии»: https://minjust.gov.ru/ru/documents/7819/
21. Политическая партия «НОВЫЕ ЛЮДИ»: https://minjust.gov.ru/ru/documents/7816/
Данные сохранены в parties.json
```

**Файл "parties.json":**
```bash
[
  {
    "name": "Всероссийская политическая партия «ЕДИНАЯ РОССИЯ»",
    "doc_url": "https://minjust.gov.ru/ru/documents/7767/"
  },
  {
    "name": "КПРФ - политическая партия КОММУНИСТИЧЕСКАЯ ПАРТИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ",
    "doc_url": "https://minjust.gov.ru/ru/documents/7768/"
  },
  {
    "name": "Политическая партия ЛДПР – Либерально-демократическая партия России",
    "doc_url": "https://minjust.gov.ru/ru/documents/7769/"
  },
  {
    "name": "Всероссийская политическая партия «ПАРТИЯ РОСТА»",
    "doc_url": "https://minjust.gov.ru/ru/documents/7773/"
  },
  {
    "name": "Социалистическая политическая партия «СПРАВЕДЛИВАЯ РОССИЯ - ПАТРИОТЫ - ЗА ПРАВДУ»",
    "doc_url": "https://minjust.gov.ru/ru/documents/7772/"
  },
  {
    "name": "Политическая партия «Российская объединенная демократическая партия «ЯБЛОКО»",
    "doc_url": "https://minjust.gov.ru/ru/documents/7771/"
  },
  {
    "name": "Политическая партия «Демократическая партия России»",
    "doc_url": "https://minjust.gov.ru/ru/documents/7775/"
  },
  {
    "name": "Политическая партия «Российская экологическая партия «ЗЕЛЁНЫЕ»",
    "doc_url": "https://minjust.gov.ru/ru/documents/7784/"
  },
  {
    "name": "Политическая партия КОММУНИСТИЧЕСКАЯ ПАРТИЯ КОММУНИСТЫ РОССИИ",
    "doc_url": "https://minjust.gov.ru/ru/documents/7785/"
  },
  {
    "name": "Всероссийская политическая партия ПАРТИЯ ЗА СПРАВЕДЛИВОСТЬ!",
    "doc_url": "https://minjust.gov.ru/ru/documents/7787/"
  },
  {
    "name": "Политическая партия «ПАРТИЯ ПРОГРЕССА»",
    "doc_url": "https://minjust.gov.ru/ru/documents/7776/"
  },
  {
    "name": "Политическая партия РОССИЙСКАЯ ПАРТИЯ СВОБОДЫ И СПРАВЕДЛИВОСТИ",
    "doc_url": "https://minjust.gov.ru/ru/documents/7782/"
  },
  {
    "name": "Политическая партия СОЦИАЛЬНОЙ ЗАЩИТЫ",
    "doc_url": "https://minjust.gov.ru/ru/documents/7788/"
  },
  {
    "name": "Политическая партия «РОССИЙСКАЯ ПАРТИЯ ПЕНСИОНЕРОВ ЗА СОЦИАЛЬНУЮ СПРАВЕДЛИВОСТЬ»",
    "doc_url": "https://minjust.gov.ru/ru/documents/7790/"
  },
  {
    "name": "Политическая партия «Гражданская Платформа»",
    "doc_url": "https://minjust.gov.ru/ru/documents/7791/"
  },
  {
    "name": "ВСЕРОССИЙСКАЯ ПОЛИТИЧЕСКАЯ ПАРТИЯ «РОДИНА»",
    "doc_url": "https://minjust.gov.ru/ru/documents/7794/"
  },
  {
    "name": "Политическая партия «Казачья партия Российской Федерации»",
    "doc_url": "https://minjust.gov.ru/ru/documents/7797/"
  },
  {
    "name": "Политическая партия «Партия Возрождения России»",
    "doc_url": "https://minjust.gov.ru/ru/documents/7803/"
  },
  {
    "name": "Политическая партия ЗЕЛЕНАЯ АЛЬТЕРНАТИВА",
    "doc_url": "https://minjust.gov.ru/ru/documents/7818/"
  },
  {
    "name": "Политическая партия «Партия прямой демократии»",
    "doc_url": "https://minjust.gov.ru/ru/documents/7819/"
  },
  {
    "name": "Политическая партия «НОВЫЕ ЛЮДИ»",
    "doc_url": "https://minjust.gov.ru/ru/documents/7816/"
  }
]
```

# Enjoy using the program! 
