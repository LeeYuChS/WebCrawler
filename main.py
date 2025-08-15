from fetch_data import fetch_data
from plot import plot_country, plot_multi_life
import pandas as pd

website_life = {
    'Taiwan': 'https://www.indexmundi.com/g/g.aspx?c=tw&v=30',
    'China': 'https://www.indexmundi.com/g/g.aspx?v=30&c=ch&l=en',
    'Japan': 'https://www.indexmundi.com/g/g.aspx?v=30&c=ja&l=en',
    'KoreaS': 'https://www.indexmundi.com/g/g.aspx?v=30&c=ks&l=en',
    'Singapore': 'https://www.indexmundi.com/g/g.aspx?v=30&c=sn&l=en'
}
website_GDP = {
    'Taiwan': 'https://www.indexmundi.com/g/g.aspx?v=67&c=tw&l=en',
    'China': 'https://www.indexmundi.com/g/g.aspx?v=67&c=ch&l=en',
    'Japan': 'https://www.indexmundi.com/g/g.aspx?v=67&c=ja&l=en',
    'KoreaS': 'https://www.indexmundi.com/g/g.aspx?v=67&c=ks&l=en',
    'Singapore': 'https://www.indexmundi.com/g/g.aspx?v=67&c=sn&l=en'
}
    
def main():
    # 抓資料
    df_Taiwan = fetch_data(website_life['Taiwan'], 'Taiwan')
    df_China = fetch_data(website_life['China'], 'China')
    df_Japan = fetch_data(website_life['Japan'], 'Japan')
    df_KoreaS = fetch_data(website_life['KoreaS'], 'KoreaS')
    df_Singapore = fetch_data(website_life['Singapore'], 'Singapore')

    df_Taiwan_GDP = fetch_data(website_GDP['Taiwan'], 'Taiwan_GDP')
    df_China_GDP = fetch_data(website_GDP['China'], 'China_GDP')
    df_Japan_GDP = fetch_data(website_GDP['Japan'], 'Japan_GDP')
    df_KoreaS_GDP = fetch_data(website_GDP['KoreaS'], 'KoreaS_GDP')
    df_Singapore_GDP = fetch_data(website_GDP['Singapore'], 'Singapore_GDP')
    
    # print(df_Taiwan.head())
    # print(df_Taiwan.dtypes)
    # print(df_Taiwan_GDP.head())
    # print(df_Taiwan_GDP.dtypes)

    df_life = pd.concat([df_Taiwan, df_China, df_Japan, df_KoreaS, df_Singapore], axis=1)
    df_life = df_life.drop(index=['2001', '2014', '2016', '2018', '2019', '2020'], errors='ignore')

    df_gdp = pd.concat([df_Taiwan_GDP, df_China_GDP, df_Japan_GDP, df_KoreaS_GDP, df_Singapore_GDP], axis=1)
    df_gdp = df_gdp.drop(index=['1999', '2001', '2016', '2018'], errors='ignore')

    # 畫圖
    plot_country(df_Taiwan, df_Taiwan_GDP, "Taiwan", "Taiwan_GDP")
    plot_country(df_China, df_China_GDP, "China", "China_GDP")
    plot_country(df_Japan, df_Japan_GDP, "Japan", "Japan_GDP")
    plot_country(df_KoreaS, df_KoreaS_GDP, "KoreaS", "KoreaS_GDP")
    plot_country(df_Singapore, df_Singapore_GDP, "Singapore", "Singapore_GDP")
    
    plot_multi_life(df_life)

if __name__ == "__main__":
    main()