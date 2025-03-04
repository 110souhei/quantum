import numpy as np
import matplotlib.pyplot as plt


def scatter(data : dict):
    
    #get_figsize
    if("figsize_x" in data and "figsize_y" in data):
        fig = plt.figure(figsize = (data["figsize_x"],data["figsize_y"]))#画像サイズの調節
    else:
        fig = plt.figure()

    ax = fig.add_subplot(111)
    
    #label
    if("title" in data):
        ax.set_title(data["title"])
    if("xlabel" in data):
        ax.set_xlabel(data["xlabel"])
    if("ylabel" in data):
        ax.set_ylabel(data["ylabel"])
    
    ax.bar(data["A"],data["B"])
    plt.show()
    




if __name__ == "__main__":
    
    data = {
        #"figsize_x" : 12,
        #"figsize_y" : 8, #サイズの調節
        "title" : "titttttttttttle",
        "xlabel" : "xxxxxxxxxxxxxxxx",
        "ylabel" : "yyyyyyyyyyyyyyyy",
        "s" : 100,
        "c" : "r",
        "tra" : 0.5,
        "A" : ["AAAA","BBB","CCC","BB","RERE"],
        "B" : [5,4,3,2,1]
        
    }
    scatter(data)
