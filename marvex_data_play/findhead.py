import pandas as pd
pd.set_option('display.max_columns',500)

align = pd.read_csv("C:\\Users\\vd.gokkulkumar\\Desktop\\projects\\rnr\\alignment.csv")

dfd = dict(zip(align.agentemail, align.supervisor))

DF_list= list()

for i in range(0, len(dfd)):
    emp = list(dfd.keys())[i]
    a_dataframe = pd.DataFrame()
    name = []
    counter = 1

    a_dataframe.insert(0, 0, [emp])

    def get_head(keyf):
        global counter

        for key, value in dfd.items():
            if keyf == key:
                if value != '-':
                    print(value)
                    val = value
                    name.append(val)
                    a_dataframe.insert(counter, counter, [val])
                    counter = counter + 1
                    get_head(val)
                else:
                    DF_list.append(a_dataframe)
                    head = keyf
                    print(head + ' is the head' )
                # return value

    get_head(emp)

ready_df = pd.concat(DF_list)
ready_df.columns = ['agentemail','l1','l2','l3','l4','l5','l6']

