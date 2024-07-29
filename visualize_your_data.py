import pandas as pd
from matplotlib import pyplot as plt
def display_graph(csv_file_name,graph_type,column_x,column_y):
    df = pd.read_csv(csv_file_name)
    df[column_y] = pd.to_numeric(df[column_y], errors='coerce')

    # Plot based on graph_type
    if graph_type == '1':
        plt.plot(df[column_x], df[column_y], marker='o', linestyle='-')
        plt.title('Line Plot')
        plt.xlabel(column_x)
        plt.ylabel(column_y)
    elif graph_type == '2':
        plt.scatter(df[column_x], df[column_y], marker='o')
        plt.title('Scatter Plot')
        plt.xlabel(column_x)
        plt.ylabel(column_y)
    elif graph_type == '3':
        plt.hist(df[column_y].dropna(), bins=20)
        plt.title('Histogram')
        plt.xlabel(column_y)
        plt.ylabel('Frequency')
    elif graph_type == '4':
        if len(df[column_y]) == len(df[column_x]):
            plt.pie(df[column_y], labels=df[column_x], autopct='%1.1f%%')
            plt.title('Pie Chart')
        else:
            print("For pie chart, column_y should be numeric data and column_x should be categorical data.")
    else:
        print("Invalid graph type selected.")

    plt.show()



if __name__ == '__main__':
    csv_file_name=input("Enter your csv file name, please add .csv extension in the end: ")
    column_x=input("Enter x column: ")
    column_y=input("Enter y column: ")
    graph_type=input("Select 1-Line Plot 2-Scatter Plot 3- Hist 4-Pie Chart: ")
    display_graph(csv_file_name,graph_type,column_x,column_y)


