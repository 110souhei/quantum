import json
import random
import numpy as np




f = open('info.json','r')
random.seed = 2

json_dict = json.load(f)

print(json_dict)

print(json_dict["gen"])

print(len(json_dict["gen"]["norm1"]))


#make input
for key,val in json_dict["gen"].items():
    print(val)
    test_case = val['tests']
    num_test_type = 1
    test_sum_array = np.zeros(len(val))
    count = 0
    for t,i in val.items():
        if(t == 'tests'):
            continue
        num_test_type = num_test_type * len(i)
        test_sum_array[count] = len(i)
        count += 1

    inv_array = np.ones(len(val))
    for i in range(count-1):
        inv_array[count-2-i] = inv_array[count-1-i]*test_sum_array[count-1-i]

    for i in range(num_test_type):
        k = i
        testname = key + "/"
        count = 0
        testcase_parameter = {}
        for type_name , number_type in val.items():
            if(type_name == 'tests'):
                continue
            testcase_parameter[type_name] = (number_type[int(k/inv_array[count])]) 
            testname += type_name + '_' + str(number_type[int(k/inv_array[count])]) + '/'
            k%=inv_array[count]
            count+=1
        print(testname)
        print(testcase_parameter)
    print(num_test_type)




