# Life Expectancy vs. GDP Crawler & Plotter

This project uses Python with `BeautifulSoup` to crawl the life expectancy and GDP per capita data for five regions: Taiwan, China, Japan, South Korea, and Singapore. It then utilizes `Matplotlib` to generate a comparative chart, visualizing the relationship between these two key metrics.

---

## Requirements

* Python 3.12+

---

## Installation

1.  **Clone the repository and navigate to the project directory:**
    ```bash
    git clone <your-repository-url>
    cd <project-directory>
    ```

2.  **Create and activate a virtual environment:**
    * On Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    * On macOS/Linux:
        ```bash
        python -m venv venv
        source venv/bin/activate
        ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: A `requirements.txt` file is recommended. If you don't have one, create it and add the following lines)*
    ```
    beautifulsoup4
    matplotlib
    pandas
    requests
    ```

---

## Project Structure
```
project/
├── fetch_data.py       # Fetches data and returns a pandas DataFrame.
├── plot.py             # Contains the plotting logic.
├── main.py             # Main script to execute the crawl and plot.
└── README.md           # This file.
```

---

## Usage

Simply run the `main.py` script from your terminal:
```bash
python main.py
```
This will execute the web crawling process, process the data, and generate a chart named `life_expectancy_vs_gdp.png` in the project's root directory.

