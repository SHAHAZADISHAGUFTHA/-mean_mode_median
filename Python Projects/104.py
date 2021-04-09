import csv
import statistics as st

with open("SOCR-HeightWeight.csv",newline="")as f:
    reader=csv.reader(f)
    data=list(reader)

data.pop(0)
given_data=[]

for i in range (len(data)):
    n_num=data[i][1]
    given_data.append(float(n_num))

total_numbers = len(given_data)
sum_of_all_weights = 0

for i in given_data:
    sum_of_all_weights+=i

mean1=sum_of_all_weights/total_numbers

Mean_of_weights = st.mean(given_data)
print("Mean of all weights(average) =  ",Mean_of_weights)

Mode_of_weights = st.mode(given_data)
print("Mode of all weights =  ",Mode_of_weights)

Median_of_weights = st.median(given_data)
print("Median of all weights =  ",Median_of_weights)
