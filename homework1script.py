"""The following creates a graph using data from the books
 Professor Nussbaum has read and tracked using goodreads.com"""
import plotnine as p9
import pandas as pd

data=pd.read_csv("nussbaum_goodreads_library_export.csv",
                 index_col="Title")

data=data[['My Rating',
           'Average Rating',
           "Number of Pages",
           "Binding",
           "Date Read"]]

a=[]
data=data.dropna(subset=['Binding'])

for book in data.index:
    if (data.loc[book]["Binding"] in ["Hardcover",
                                      "Kindle Edition",
                                      "Mass Market Paperback",
                                      "Paperback","ebook"]) is True:
        a.append(book)

data=data.loc[a]

plot = p9.ggplot(data,
                 p9.aes(x="Number of Pages",
                        fill="My Rating"))+p9.geom_histogram()+p9.facet_grid('My Rating~.')
