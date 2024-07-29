import pandas as pd
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
# global variable
data=[]
def perform_aggregation():
    new_df=pd.read_csv('book_data.csv')
    grouped_category=new_df.groupby('category')
    aggregate_price=grouped_category['book_price'].sum().reset_index()
    aggregate_price.columns=['Category','Price']

    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))
    # plot category vs price graph

    ax1.plot(aggregate_price['Category'],aggregate_price['Price'], marker='*', ls=':', color='r')
    ax1.set_title('C vs P')
    ax1.set_xlabel('Category')
    ax1.set_ylabel('Price')
    ticks=aggregate_price['Category'][::8]
    ax1.set_xticks(ticks=ticks)




    aggregate_rating=grouped_category['star_rating'].mean().reset_index()
    aggregate_rating.columns=['Category','Rating']

    ax2.scatter(aggregate_rating['Category'],aggregate_rating['Rating'], marker='o', ls='-', color='b')
    ax2.set_title("C vs R")
    ax2.set_xlabel('Category')
    ax2.set_ylabel('Rating')
    ticks = aggregate_rating['Category'][::8]
    ax2.set_xticks(ticks =ticks)

    plt.show()

def rating(rating_class):
    # print(rating_class)
    if(rating_class[1]=='One'):
        return 1
    elif(rating_class[1]=='Two'):
        return 2
    elif (rating_class[1] == 'Three'):
        return 3
    elif (rating_class[1] == 'Four'):
        return 4
    else:
        return 5

def extract_book_details(category_page_url,session):
    print('entered in extract_book_details')
    response=session.get(category_page_url)
    soup=BeautifulSoup(response.content,'html.parser')
    book_list=soup.findAll('li',class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
    for book in book_list:
        book_dict={
            'category':soup.find('div',class_='page-header action').find('h1').text,
            'book_name':book.find('h3').find('a').get('title'),
            'book_price':float(book.find('p',class_='price_color').text[1:]),
            'star_rating':rating(book.find('article',class_='product_pod').find('p').get('class'))
        }
        data.append(book_dict)
    df=pd.DataFrame(data)
    df.to_csv('book_data.csv',index=False)

def category_url(url,session):
    print('entered in category_url function')
    response=session.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    navigation_list=soup.find('ul',class_="nav nav-list").findAll('li')
    for nav_item in navigation_list:
        category_page_url=url+nav_item.find('a').get('href')
        extract_book_details(category_page_url,session)

if __name__ == '__main__':
    # session=requests.session()
    # home_url="https://books.toscrape.com/"
    # category_url(home_url,session)
    perform_aggregation()

