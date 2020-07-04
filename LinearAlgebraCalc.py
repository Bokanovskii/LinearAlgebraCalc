import tkinter as tk
from tkinter import *
from tkinter import messagebox
import Matrices
from Matrices import Matrix

# https://www.tutorialspoint.com/python/python_gui_programming.htm
top = tk.Tk()
top.title("Linear Algebra Operations")
top.geometry("500x500")

# topLevel windows
def prod_window():
    
    # intialize window
    prod_win = tk.Toplevel()
    prod_win.title("Products")
    prod_win.minsize(520, 500)

# FOR MATRIX A:    
    # labels for matrix entry
    enter_here_A = Label(prod_win, text = "Enter matrix A below:", 
                        font = ("Courier", 40))
    enter_here_A.pack()

    entry_labels_A = Label(prod_win, text = 
        "# of rows: \n\n # of columns: \n\n Coefficients:\n(space seperated)", font = ("Courier", 20))
    entry_labels_A.place(bordermode = OUTSIDE, relx = 0, rely = .15)    
    # entries for rows and columns
    row_entry_A = Entry(prod_win, font = ("Courier", 20), width = 5)
    row_entry_A.place(bordermode = OUTSIDE, relx = .32, rely = .15)
    col_entry_A = Entry(prod_win, font = ("Courier", 20), width = 5)
    col_entry_A.place(bordermode = OUTSIDE, relx = .352, rely = .23)
    nums_entry_A = Entry(prod_win, font = ("Courier", 20), width = 23)
    nums_entry_A.place(bordermode = OUTSIDE, relx = .375, rely = .31)
    # can set a command to auto update a label or something with values
# FOR MATRIX B: 
    enter_here_B = Label(prod_win, text = "Enter matrix B below:", 
                        font = ("Courier", 40))
    enter_here_B.place(anchor = 'n', relx = .5, rely = .5)

    entry_labels_B = Label(prod_win, text = 
        "# of rows: \n\n # of columns: \n\n Coefficients:\n(space seperated)", font = ("Courier", 20))
    entry_labels_B.place(bordermode = OUTSIDE, relx = 0, rely = .63)    
    # entries for rows and columns
    row_entry_B = Entry(prod_win, font = ("Courier", 20), width = 5)
    row_entry_B.place(bordermode = OUTSIDE, relx = .32, rely = .63)
    col_entry_B = Entry(prod_win, font = ("Courier", 20), width = 5)
    col_entry_B.place(bordermode = OUTSIDE, relx = .352, rely = .71)
    nums_entry_B = Entry(prod_win, font = ("Courier", 20), width = 23)
    nums_entry_B.place(bordermode = OUTSIDE, relx = .375, rely = .79)
    # can set a command to auto update a label or something with values
    
    compute_Butt = Button(prod_win, text = "Compute AB", height = 2,
        width = 30, font = ("Courier", 15), 
        command = lambda: compute_product(row_entry_A.get(),
            col_entry_A.get(), nums_entry_A.get(), 
            row_entry_B.get(), col_entry_B.get(), 
            nums_entry_B.get()))
    compute_Butt.place(anchor = 'center', relx = .5, rely = .95)


def vector_proj_window():
    
    # intialize window
    vect_proj_win = tk.Toplevel()
    vect_proj_win.title("2D Vector Projection")
    vect_proj_win.minsize(520, 400)
     
    enter_vector_here = Label(vect_proj_win, text = 
        "Enter 2D vectors below:", 
                        font = ("Courier", 40))
    enter_vector_here.pack()

    vect_entry_label_w = Label(vect_proj_win, text = 
        "Vector w Coefficients:\n(space seperated)", font = ("Courier", 20),
        underline = 8)
    vect_entry_label_w.place(bordermode = OUTSIDE, relx = 0, rely = .15)    
    w_entry = Entry(vect_proj_win, font = ("Courier", 20), width = 10)
    w_entry.place(bordermode = OUTSIDE, relx = .52, rely = .15)
    vect_entry_label_x = Label(vect_proj_win, text =
        "Vector x Coefficients:\n(space seperated)", font = ("Courier", 20),
        underline = 7)
    vect_entry_label_x.place(bordermode = OUTSIDE, relx = 0, rely = .3)
    x_entry = Entry(vect_proj_win, font = ("Courier", 20), width = 10)
    x_entry.place(bordermode = OUTSIDE, relx = .52, rely = .3)
    note_label = Label(vect_proj_win, text =
        "Note: vector x is projected onto line L such \nthat L passes " +
        "through vector w.", font = ("Courier", 20))
    note_label.place(bordermode = OUTSIDE, relx = 0, rely = .5)

    compute_vect_Butt = Button(vect_proj_win, text = 
        "Compute projected vector y", 
        height = 2, width = 30, font = ("Courier", 15), 
        command = lambda: compute_vect_projection(w_entry.get(), 
        x_entry.get()))
    compute_vect_Butt.place(anchor = 'center', relx = .5, rely = .9)

def vector_refl_window():
    
    # intialize window
    vect_refl_win = tk.Toplevel()
    vect_refl_win.title("2D Vector Reflection")
    vect_refl_win.minsize(520, 400)
     
    enter_vectors_here = Label(vect_refl_win, text = 
        "Enter 2D vectors below:", 
                        font = ("Courier", 40))
    enter_vectors_here.pack()

    vect_entry_label_w2 = Label(vect_refl_win, text = 
        "Vector w Coefficients:\n(space seperated)", font = ("Courier", 20),
        underline = 7)
    vect_entry_label_w2.place(bordermode = OUTSIDE, relx = 0, 
        rely = .15)    
    w_entry2 = Entry(vect_refl_win, font = ("Courier", 20), width = 10)
    w_entry2.place(bordermode = OUTSIDE, relx = .52, rely = .15)
    vect_entry_label_x2 = Label(vect_refl_win, text =
        "Vector x Coefficients:\n(space seperated)", font = ("Courier", 20),
        underline = 7)
    vect_entry_label_x2.place(bordermode = OUTSIDE, relx = 0, rely = .3)
    x_entry2 = Entry(vect_refl_win, font = ("Courier", 20), width = 10)
    x_entry2.place(bordermode = OUTSIDE, relx = .52, rely = .3)
    note_label2 = Label(vect_refl_win, text =
        "Note: vector x is reflected across line L such \nthat L passes " +
        "through vector w.", font = ("Courier", 20))
    note_label2.place(bordermode = OUTSIDE, relx = 0, rely = .5)

    compute_vect_Butt2 = Button(vect_refl_win, text = 
        "Compute reflected vector y", 
        height = 2, width = 30, font = ("Courier", 15), 
        command = lambda: compute_vect_reflection(w_entry2.get(), 
        x_entry2.get()))
    compute_vect_Butt2.place(anchor = 'center', relx = .5, rely = .9)


# Helper functions
def compute_product(Srows_A, Scols_A, Snums_A, Srows_B, Scols_B, Snums_B):
    # make sure that entered values are numerical
    try:
        rows_A = int(Srows_A)
        cols_A = int(Scols_A)
        rows_B = int(Srows_B)
        cols_B = int(Scols_B)
        nums_A = list(map(float, Snums_A.split()))
        nums_B = list(map(float, Snums_B.split()))
    except ValueError:
        messagebox.showerror("ValueError", "Input Numerical Values Please")
    # catch all incorrect input types
    if cols_A != rows_B: 
        messagebox.showerror("Rows != Columns", 
         "Matrix A columns do not equal Matrix B rows. Unable to multiply.")
    if len(nums_A) != (rows_A * cols_A):
        messagebox.showerror("Incorrect # of Coefficients",
         "The number of entered values for Matrix A doesn't match the " + 
         "number of rows and columns.")
    if len(nums_B) != (rows_B * cols_B):
        messagebox.showerror("Incorrect # of Coefficients",
         "The number of entered values for Matrix B doesn't match the " + 
         "number of rows and columns.")
    else:
        Mat_A = Matrix(rows_A, cols_A, nums_A)
        Mat_B = Matrix(rows_B, cols_B, nums_B)
        AB_product = Matrices.product(Mat_A, Mat_B)
        messagebox.showinfo("A * B", "{}".format(AB_product))

def compute_vect_projection(w_vect, x_vect):
    # make sure values are numerical
    try:
        w = list(map(float, w_vect.split()))
        x = list(map(float, x_vect.split()))
    except ValueError:
        messagebox.showerror("ValueError", "Input Numerical Values Please")
    if len(w) != 2: 
        messagebox.showerror("Invalid w", "Vector w is not 2-Dimensional")
    if len(x) !=2:
        messagebox.showerror("Invalid x", "Vector x is not 2-Dimensional")
    else:
        Mat_w = Matrix(2, 1, w)
        Mat_x = Matrix(2, 1, x)
        projected_vector = Matrices.vector_projection(Mat_w, Mat_x)
        messagebox.showinfo("Projection(x) onto L", 
            "{}".format(projected_vector))

def compute_vect_reflection(w_vect, x_vect):
    # make sure values are numerical
    try:
        w2 = list(map(float, w_vect.split()))
        x2 = list(map(float, x_vect.split()))
    except ValueError:
        messagebox.showerror("ValueError", "Input Numerical Values Please")
    if len(w2) != 2: 
        messagebox.showerror("Invalid w", "Vector w is not 2-Dimensional")
    if len(x2) !=2:
        messagebox.showerror("Invalid x", "Vector x is not 2-Dimensional")
    else:
        Mat_w2 = Matrix(2, 1, w2)
        Mat_x2 = Matrix(2, 1, x2)
        reflected_vector = Matrices.vector_reflection(Mat_w2, Mat_x2)
        messagebox.showinfo("Reflection(x) onto L", 
            "{}".format(reflected_vector))
# Main Menu Buttons
Matrix_mult_Butt = tk.Button(top, text = "Matrix Products", height = 4, 
            font = ("Courier", 30), width = 25, command = prod_window)
Matrix_mult_Butt.place(anchor = 'center', relx = .5, rely = .15)
Vector_proj_Butt = tk.Button(top, text = "2D Vector Projection", height = 4,
            font = ("Courier", 30), width = 25, 
            command = vector_proj_window)
Vector_proj_Butt.place(anchor = 'center', relx = .5, rely = .42)
Vector_refl_Butt = tk.Button(top, text = "2D Vector Reflection", height = 4,
            font = ("Courier", 30), width = 25, 
            command = vector_refl_window)
Vector_refl_Butt.place(anchor = 'center', relx = .5, rely = .69)
Help_label = Label(top, text = 
    "Click to open an operation \nspecific calculator", font = 
    ("Courier", 20))
Help_label.place(anchor = 'center', relx = .5, rely = .9) 
# keep seperated
top.mainloop()
