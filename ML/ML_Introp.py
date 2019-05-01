# -*- coding: utf-8 -*-
######################################
# setup variable for the application  
v_print_ver = 1
v_print_conf = 1
v_print_debug_msg = 1 
v_print_data_analysis = 1
# End setup variable for the application 
#########################################

#########################################
# Print config 
if v_print_conf == 1:
        print("\nVariable configuration parameters ")
        print('v_print_ver: {}' .format(v_print_ver))
        print('v_print_conf: {}' .format(v_print_conf))
        print('v_print_debug_msg: {}' .format(v_print_debug_msg))
        print('v_print_data_analysis : {}' .format(v_print_data_analysis))
        
#END Print config 
######################################
        
        
#########################################
#Print versions
if v_print_ver == 1 :
    print("\nVersions of all librries used in this application ")
     
    import sys
    print('Python: {}'.format(sys.version))
    
    import scipy
    print('scipy: {}' .format(scipy.__version__))
    
    import numpy
    print('numpy: {}' .format(numpy.__version__))
    
    import matplotlib
    print('matplotlib: {}'.format(matplotlib.__version__))
    # pandas
    import pandas
    print('pandas: {}'.format(pandas.__version__))
    # scikit-learn
    import sklearn
    print('sklearn: {}'.format(sklearn.__version__))
    
#end print versions
#########################################


#########################################
# import Libraries


# Load libraries
try:
    if v_print_debug_msg == 1 :
        print('Msg: Import libraries')
        
    import pandas
    from pandas.plotting import scatter_matrix
    import matplotlib.pyplot as plt
    from sklearn import model_selection
    from sklearn.metrics import classification_report
    from sklearn.metrics import confusion_matrix
    from sklearn.metrics import accuracy_score
    from sklearn.linear_model import LogisticRegression
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    from sklearn.naive_bayes import GaussianNB
    from sklearn.svm import SVC
except ImportError:
    print('Error: Failed to load mudules')

# end import libraries 
#########################################


#########################################
#Load dataset
try:
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
    names = ['sepal-length' , 'sepal-width' , 'petal-length' , 'petal-width' , 'class' ]
    dataset = pandas.read_csv(url ,names=names)
    if v_print_debug_msg == 1 :
        print('Msg : Loaded data successfully')
    
except:
    print ('Error: Failed to load data set ')

# End Load dataset
#########################################
    
#########################################
# Analyse dataset 
if v_print_data_analysis == 1 :
    try:
        if v_print_debug_msg == 1 :
            print('Msg: Data analysis graphs')
        
        #shape of dataset
        print(dataset.shape)
        
        # Head first 20 rows
        print(dataset.head(20) )
        
        # desription
        print(dataset.describe())
        
        #class distribution
        print(dataset.groupby('class').size())
        
        #########################################
        #Display some graphs
                
        #boxplots
        dataset.plot(kind='box' , subplots=True , layout=(2,2) ,sharex=False , sharey=False)
        plt.show
        
        #histograms
        dataset.hist()
        plt.show    
        
        #print interactions between variables
        # scatter plots
        scatter_matrix(dataset)
        plt.show
        
    except:
        print('Error : data analysis')
        
        
#END Analyse dataset 
#########################################

#----------------------------------------
# test some smple code on Arrays  
#can delete this section of code 

from numpy import array
data = [11,22,33,44,55,66] # this is a list 

data = array(data) #convert list to an array
print(data)
print(type(data))

      


# End array test
#----------------------------------------
        
        
#########################################       
#split dataset array into 80/20% chunks
       
 # Split-out validation dataset
array = dataset.values
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

# end split dataset array into 80/20% chunks
#########################################





