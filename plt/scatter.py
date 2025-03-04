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
    
    
    s = 10
    c = 'b'
    alpha = 1
    #bit
    if("s" in data):
        s = data["s"]
    
    if("c" in data):
        c = data["c"]
    
    if("tra" in data):
        alpha = data["tra"]


    A = data["A"]
    B = data["B"]
    print(str(s)+ " " + str(alpha))
    ax.scatter(A, B, s = s, c = c, alpha = alpha)
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
        "A" : [1,2,3,4,5],
        "B" : [5,4,3,2,1]
        
    }
    scatter(data)

