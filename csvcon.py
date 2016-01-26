import openpyxl
import pandas as pd

path = 'C:\Users\Felipe\Python\tiago'

wb = openpyxl.load_workbook(path + 'Loterias Caixa - In Loco Media.xlsx')
sheets = wb.get_sheet_names()

CSVList = []

for sheet in sheets:

    #get the current active sheet
    active_sheet = wb.get_sheet_by_name(sheet)

    #count numbers of rows
    row_count = active_sheet.get_highest_row() - 1
    #count number of columns
    column_count = active_sheet.get_highest_column()

    count = 0
    values = []


    #write each row to a list, stop when reached max rows (REVIEW THIS - would have thought there was a better way than using a counter)
    while count <= row_count:               
        for i in active_sheet.rows[count]:
            values.append(i.value)      
        count = count + 1

    #split values list into tuples based on number of columns 
    split_rows = zip(*[iter(values)]*column_count)

    #convert list of tuples to list of lists  (REVIEW THIS - creating a tuple and then converting to list seems like extra work?!?)
    rows = [list(elem) for elem in split_rows]

    #get elements of file and store (REVIEW THIS - looks messy?)
    title = rows.pop(0)[0]
    headers = rows.pop(0)
    headers[1] = 'Last Year'
    rows.pop(0) 

    #create pandas dataframe
    df = pd.DataFrame(rows, columns=headers)

    #take header_id and remove to normalise the data
    header_id = headers.pop(2)


    normalise_data = pd.melt(df, id_vars=header_id, value_vars=headers, var_name='Measure', value_name='Value') 
    normalise_data.insert(0, 'Subject', title)  
    CSVList.append(normalise_data)


frame = pd.concat(CSVList)
frame.to_csv(path + 'CSV Outputs/' + 'final.csv', sep=',', index=False)