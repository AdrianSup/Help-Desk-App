# to clear tkinter window so the widgets arent stacked when .pack()
def clear_window(windows):
    for i in windows.winfo_children()[1:]:
        i.destroy()

# to refresh ticket treeview for any changes
def refresh_ticket(list, tree):
    tree.delete(*tree.get_children())
    global count
    count = 0
    for value in list:
        count += 1
        if count % 2 == 0:
            tree.insert('', index='end', iid=count, values=(value), tags=('evenrow',))
        else:
            tree.insert('', index='end', iid=count, values=(value), tags=('oddrow',))

    tree.tag_configure("oddrow", background="white")
    tree.tag_configure("evenrow", background="lightblue")