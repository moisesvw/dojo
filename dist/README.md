# MapReduce

The motivation of this folder is to learn about how map reduce works, the basic concept of how to hadoop works with this technique.
It have results from a Udacity
course I took in 2014 with [Cloudera](https://classroom.udacity.com/courses/ud617)

The command below calculates the sales per store from a text file. This is how MapReduce works. Map -> (key, values) | sort | Reduce from -> (key, value). This example keys are store names, values are sales per day

```sh
$ cat data/purchases.txt | mapreduce/mapper_sales.py | sort | mapreduce/reducer_sales.py
```

The result should be something like this 

```
Anchorage	354.34
Arlington	791.01
Atlanta	        471.85
Aurora	        7.39
Austin	        806.77
Baltimore	315.09
Baton Rouge	84.45
Boston  	1015.76
Chandler	366.83
Charlotte	565.63
```