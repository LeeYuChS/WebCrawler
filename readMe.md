## Web Crawler
Using beautifulsoup try to crawl five country (Taiwan, China, Japan, South Korea, Singapore) data which people's life expectancy and GDP, and using matplotlib to plot a diagram.

## Installation & Requirements

Make sure you have Python 3.12+ installed. Then install the dependencies:

```bash
cd folder_path
python -m venv venvName

cd venvName/Scripts
activate

pip install bs4=0.0.2 matplotlib=3.10.5 pandas=2.3.1
# or
pip install -r requirements.txt
```
python 

```
project/
│
├─ fetch_data.py        # crawl data, then return DataFrame
├─ plot.py              # plot
├─ main.py              # main, including website dict
└─ README.md
```
