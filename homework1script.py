##https://docs.spyder-ide.org/5/faq.html#using-packages-installer
import scipy
import plotnine as p9
import pandas as pd
data=pd.read_csv(".csv",index_col="Title"); data=data[['My Rating','Average Rating',"Number of Pages","Binding","Date Read"]]     
a=[];
data=data.dropna(subset=[ 'Binding' ])
for book in data.index:
    if (data.loc[book]["Binding"] in [ "Hardcover" ,"Kindle Edition" ,"Mass Market Paperback" ,"Paperback" ,"ebook" ])==True:
        a.append(book) ##364
data=data.loc [ a ]
p9.ggplot(data,p9.aes(x="Number of Pages",fill="My Rating"))+p9.geom_histogram()+p9.facet_grid('My Rating~.')