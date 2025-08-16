import matplotlib.pyplot as plt
import pandas as pd
import os

save_path = "./plot_result"
os.makedirs(save_path, exist_ok=True)

def plot_country(df_life, df_gdp, country_name, gdp_col):
    df_country = pd.concat([df_life, df_gdp], axis=1)
    df_country = df_country.dropna()
    ax = df_country.set_index(gdp_col).plot(title=f"{country_name} GDP vs Life Expectancy")
    ax.grid(True)
    plt.savefig(os.path.join(save_path, f"{country_name}.png"))
    plt.show()

def plot_multi_life(df_life):
    ax = df_life.plot(title="Life Expectancy Comparison", marker='o')
    ax.grid(True)
    plt.savefig(os.path.join(save_path, "Life Expectancy Comparison.png"))
    plt.show()

def plot_multi_gdp(df_gdp):
    ax = df_gdp.plot(title="GDP Comparison", marker='o')
    ax.grid(True)
    plt.savefig(os.path.join(save_path, "GDP Comparison.png"))
    plt.show()