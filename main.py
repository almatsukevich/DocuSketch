import pandas as pd
import matplotlib.pyplot as plt
class DrawPlots:
    
    def draw_plots(self):
        df = pd.read_json('deviation.json') #reading file
        dfs = df.sort_values('mean', ascending=False) #sort DataFrame by value "mean"
        dfs.plot(x="name", y=["mean", "max", "min"])
        plt.savefig('plots/plot_mean.png')
        dfs = df.sort_values('floor_mean', ascending=False) #sort DataFrame by value "mean"
        dfs.plot(x="name", y=["floor_mean", "floor_max", "floor_min"])
        plt.savefig('plots/plot_floor.png')
        dfs = df.sort_values('ceiling_mean', ascending=False) #sort DataFrame by value "mean"
        dfs.plot(x="name", y=["ceiling_mean", "ceiling_max", "ceiling_min"])
        plt.savefig('plots/plot_ceiling.png')
        return plt.show()

g = DrawPlots()
g.draw_plots()

