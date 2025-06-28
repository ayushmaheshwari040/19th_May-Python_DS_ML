
def login(acc_no, password): 
    with open("bank_data.csv","r") as f: 
        data=f.readlines()

    data=data[1:]

    data1=[]
    for i in range(len(data)): 
        a=data[i].strip().split(',')
        v=[a[0],int(a[1]),int(a[2]),int(a[3]),a[4]]
        data1.append(v)

    final_data_ls=[]
    for i in range(len(data1)): 
        final_data_dict={}
        final_data_dict['Name']=data1[i][0]
        final_data_dict['Balance']=data1[i][1]
        final_data_dict['Account Number']=data1[i][2]
        final_data_dict['Aadhar Number']=data1[i][3]
        final_data_dict['password']=data1[i][4]
        final_data_ls.append(final_data_dict)

    for user in final_data_ls:
        if user['Account Number'] == acc_no:
            if user['password'] == password:
                print(f"Welcome Back User! {user['Name']}")
                return True
            else:
                print("Invalid password.")
                return False
    else:            
        print("User does not exist.")


def signup(username, balance, password, aadhar): 
    import random
    acc_no=random.randint(1000,9999)

    row=f"{username},{balance},{acc_no},{aadhar},{password}\n"
    with open('bank_data.csv','a') as f: 
        f.write(row)

    print(f"Your data has be recorded and your account no. is: {acc_no}")
