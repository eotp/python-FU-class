for borough in (airbnb_NY['Boroughs'].unique()):

    print(borough)

    airbnb_NY_borough = airbnb_NY.loc[airbnb_NY['Boroughs']==borough]

    x = airbnb_NY_borough['Latitude']
    
    y = airbnb_NY_borough['Longitude']
    
    plt.scatter(x,y, s=2, alpha=0.25)