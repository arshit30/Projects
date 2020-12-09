import matplotlib.pyplot as plt

def plot_bar(data,col1,col2):
    plt.bar(data[col1],data[col2])
    plt.title('Bar plot')
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.show()
    
def plot_scatter(data,col1,col2):
    plt.scatter(data[col1],data[col2])
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.show()
    
def plot_hist(data,col):
    plt.hist(data[col])
    plt.legend(col)
    plt.ylabel(col)
    plt.show()
    
def plot_box(data,col):
    plt.boxplot(data[col])
    plt.ylabel(col)
    plt.legend(col)
    plt.show()
    
def plot_pie(data,col):
    vals=data[col].value_counts()
    values=list(vals.values)
    categories=list(vals.keys().values)
    plt.pie(values,labels=categories,autopct='%1.1f%%')
    plt.legend(categories)
    plt.show()