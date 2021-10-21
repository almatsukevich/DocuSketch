import pandas as pd
import matplotlib.pyplot as plt
class DrawPlots:
    
    def draw_plots(self):
        df = pd.read_json('deviation.json')
        t=plt.plot(df['mean'], df['max'], df['min'])
        return print(t)

g = DrawPlots()
g.draw_plots()

