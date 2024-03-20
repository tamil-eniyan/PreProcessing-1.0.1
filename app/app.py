from customtkinter import *
import tkinter as tk
from tkinter import filedialog,messagebox,ttk
import pandas as pd
from sklearn import preprocessing
from tkinter.ttk import *
from tkinter import *

label_encoder = preprocessing.LabelEncoder()
level_encoder = preprocessing.OneHotEncoder() 


df = pd.DataFrame()
column_names = ["None"]
list_flag = False

app = CTk()

app.geometry("1510x880")
set_appearance_mode('light')
app.title('ML')
app.pack_propagate(False)
app.resizable(0,0)
#option menu choosing

clicked = StringVar() 
clicked.set( "Select an option" )

frame1 = tk.LabelFrame(app,text="DataFrame",height=300,width=400 )
command_frame = tk.LabelFrame(app,text="Commands")
preprocessing_frame = tk.LabelFrame(app,text="Pre Processing",height=400,width=200)
file_frame = tk.LabelFrame(app,text="File Management",height=100,width=400)


def refresh():
    # Reset clicked and delete all old options
    global column_names
    global df
    try:
        print(df)
    except:
        pass

    clicked.set('')
    drop['menu'].delete(0, 'end')

    # Insert list of new options (tk._setit hooks them up to var)
    new_choices = column_names
    for choice in new_choices:
        drop['menu'].add_command(label=choice, command=tk._setit(clicked, choice))


def do_layout():
    frame1.pack(side="left", fill="both", expand=True)
    preprocessing_frame.pack(side="top", fill="both", expand=True)
    file_frame.pack(side="bottom", fill="both", expand=True)
    return None


do_layout()

#buttons at File Management
browse_button = tk.Button(file_frame,text="Browse The File",command=lambda: File_dialog())
browse_button.place(relx=0.10,rely=0.40)


loadfile_button = tk.Button(file_frame,text="   Load File   ",command=lambda:Load_csv_data())
loadfile_button.place(relx=0.10,rely=0.60)


savefile_button = tk.Button(file_frame,text="   Save File   ",command=lambda:save())
savefile_button.place(relx=0.10,rely=0.70)


lable_file=ttk.Label(file_frame,text="[-]No File Selected")
lable_file.place(relx=0.10,rely=0.10)

#buttons for Pre-Procesing

lable_encoder_button = tk.Button(preprocessing_frame,text="Lable Encoding",command=lambda:open_label_encoding_window())
lable_encoder_button.pack(side="bottom",fill="both")

#level_encoding_button

level_encoder_button = tk.Button(preprocessing_frame,text="Level Encoding",command=lambda:open_level_encoding_window())
level_encoder_button.pack(side="bottom",fill="both")


    #dropdown

drop = OptionMenu( preprocessing_frame , clicked , *column_names) 
drop.pack(side="top",fill="both") 
    
#delete a column


del_column_button = tk.Button(preprocessing_frame,text="Delete The Column",command=lambda:open_delete_column_window())
del_column_button.pack(side="bottom",fill="both")

#Null value preprocessing

    #drop rows with null values

none_del_button = tk.Button(preprocessing_frame,text="Delete None Values",command=lambda:open_delete_none_window())
none_del_button.pack(side="bottom",fill="both")

    #fill nan with null values
none_fillmean_button = tk.Button(preprocessing_frame,text="Fill None with Mean",command=lambda:open_fillmean_none_window())
none_fillmean_button.pack(side="bottom",fill="both")

    #fill 0 with null values

none_fill_0_button = tk.Button(preprocessing_frame,text="Fill None with 0",command=lambda:open_fill0_none_window())
none_fill_0_button.pack(side="bottom",fill="both")




#displaying the dataframe:

tv1 = ttk.Treeview(frame1)
tv1.place(relheight=1,relwidth=1)


treescrolly = tk.Scrollbar(frame1,orient="vertical",command=tv1.yview)
treescrollx = tk.Scrollbar(frame1,orient="horizontal",command=tv1.xview)
tv1.configure(xscrollcommand=treescrollx.set,yscrollcommand=treescrolly.set)
treescrollx.pack(side="bottom",fill="x")
treescrolly.pack(side="right",fill="y")




def open_fill0_none_window():
    global df
    global column_names
    column_name = str(clicked.get())
    try:
        print(column_names)
        print(column_name)
        print(type(column_name))
        index  = column_names.index(column_name)
        try:
            df[column_names[index]]  = df[column_names[index]].fillna(value=0)
        except Exception as e:
            print(f"[-]Error : {e}")
    except Exception as e:
        tk.messagebox.showerror("Information",f"Error {e} occured while droping try UNDO button ")

    
    clear_data()
    tv1['column'] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["column"]:
        tv1.heading(column,text=column)

    df_rows = df.to_numpy().tolist()

    for row in df_rows:
        tv1.insert("","end",values = row)

    column_names = list(df.columns)
    
    refresh()
    

    return None








def open_fillmean_none_window():
    global df
    global column_names
    column_name = str(clicked.get())
    try:
        print(column_names)
        print(column_name)
        print(type(column_name))
        index  = column_names.index(column_name)
        try:
            #df[column_names[index]]  = df[column_names[index]].fillna(value=0)
            #df[column_names[index]] = df[column_names[index]].astype(int)
            mean_value = df[str(column_names[index])].mean()
            df[column_names[index]] = df[str(column_names[index])].fillna(value=mean_value)
        except Exception as e:
            print(f"[-]Error : {e}")
    except Exception as e:
        tk.messagebox.showerror("Information",f"Error {e} occured while droping try UNDO button ")

    
    clear_data()
    tv1['column'] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["column"]:
        tv1.heading(column,text=column)

    df_rows = df.to_numpy().tolist()

    for row in df_rows:
        tv1.insert("","end",values = row)

    column_names = list(df.columns)
    
    refresh()
    

    return None




def open_delete_none_window():
    global df
    global column_names
    column_name = str(clicked.get())
    try:
        print(column_names)
        print(column_name)
        print(type(column_name))
        index  = column_names.index(column_name)
        try:
            df = df.dropna(subset=[str(column_names[index])])
        except:
            pass
    except Exception as e:
        tk.messagebox.showerror("Information",f"Error {e} occured while droping try UNDO button ")

    
    clear_data()
    tv1['column'] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["column"]:
        tv1.heading(column,text=column)

    df_rows = df.to_numpy().tolist()

    for row in df_rows:
        tv1.insert("","end",values = row)

    column_names = list(df.columns)
    
    refresh()
    

    return None





def open_delete_column_window():
    global df
    global column_names
    column_name = str(clicked.get())
    try:
        print(column_names)
        print(column_name)
        print(type(column_name))
        index  = column_names.index(column_name)
        try:
            df = df.drop(df.columns[index], axis=1)
        except:
            pass
    except Exception as e:
        tk.messagebox.showerror("Information",f"Error {e} occured while droping try UNDO button ")

    
    clear_data()
    tv1['column'] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["column"]:
        tv1.heading(column,text=column)

    df_rows = df.to_numpy().tolist()

    for row in df_rows:
        tv1.insert("","end",values = row)

    column_names = list(df.columns)
    
    refresh()
    

    return None




def open_level_encoding_window():
    global df
    global column_names

    column_name = clicked.get()

    df[column_name] = df[column_name].astype('category')
  
    df[f'{column_name}_new'] = df[column_name].cat.codes
    
    level_encoder_data = pd.DataFrame(level_encoder.fit_transform( df[[f"{column_name}_new"]]).toarray()) 
  
    # Merge with main 
    df = df.join(level_encoder_data) 

    clear_data()
    tv1['column'] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["column"]:
        tv1.heading(column,text=column)

    df_rows = df.to_numpy().tolist()

    for row in df_rows:
        tv1.insert("","end",values = row)

    list_string = list(df.columns)
    column_names = [str(x) for x in list_string]
    refresh()

    return None



def open_label_encoding_window():
    global df
    global column_names

    column_name = clicked.get()
    df[column_name]= label_encoder.fit_transform(df[column_name]) 
  
    df[column_name].unique()

    clear_data()
    tv1['column'] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["column"]:
        tv1.heading(column,text=column)

    df_rows = df.to_numpy().tolist()

    for row in df_rows:
        tv1.insert("","end",values = row)

    refresh()


    return None

def File_dialog():
    filename = filedialog.askopenfilename(initialdir="/home/tamil/Documents/",
                                          title="Select A File",
                                          filetypes=(("csv files","*.csv"),("All Files","*.*")))
    lable_file["text"] = f"{filename}"
    return None


def save(): 
    global df
    try:
        file = filedialog.asksaveasfilename(
                filetypes=[("csv file", ".csv")],
                defaultextension=".csv")
        
        if file:
            df = df.drop(df.columns[0], axis=1)
            df.to_csv(file,index=False)
            tk.messagebox.showinfo("Save File",f"The File is Saved at : {file}")
            lable_file["text"] = f"{file}"
    except Exception as e:
        tk.messagebox.showerror("Information",f"{e}")
    return None

    

def Load_csv_data():
    file_path = lable_file["text"]
    global df,column_names
    try:
        csv_filename = r"{}".format(file_path)
        df = pd.read_csv(csv_filename)
        df = df.reset_index()
        df = df.reset_index().rename(columns={"index":"Index"})
        del df["level_0"]
        list_string = list(df.columns)
        column_names = [str(x) for x in list_string]
        #print(df)
    except ValueError:
        tk.messagebox.showerror("Information","The file you have choosen is Invalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information",f"No Such file as {file_path}")
        return None
    clear_data()
    tv1['column'] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["column"]:
        tv1.heading(column,text=column)

    df_rows = df.to_numpy().tolist()

    for row in df_rows:
        tv1.insert("","end",values = row)

    refresh()

    
    return None





def clear_data():
    tv1.delete(*tv1.get_children())







app.mainloop()












