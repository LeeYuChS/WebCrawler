import matplotlib.pyplot as plt
import pandas as pd

def plot_country(df_life, df_gdp, country_name, gdp_col):
    df_country = pd.concat([df_life, df_gdp], axis=1)
    df_country = df_country.dropna()
    ax = df_country.set_index(gdp_col).plot(title=f"{country_name} GDP vs Life Expectancy")
    ax.grid(True)
    plt.show()

def plot_multi_life(df_life):
    ax = df_life.plot(title="Life Expectancy Comparison", marker='o')
    ax.grid(True)
    plt.show()
