import itertools
import win32api
import win32con
import tkinter as tk
import clipboard

def generate_cartesian_products():
    # Define the set of elements
    elements = []
    for i in range(32, 127):
        elements.append(chr(i))

    # Detect when the user right-clicks on an entry-textbox
    while True:
        if win32api.GetAsyncKeyState(win32con.VK_RBUTTON):
            # Check if the cursor is focused on an entry-textbox
            hwnd = win32api.GetForegroundWindow()
            class_name = win32api.GetClassName(hwnd)
            if class_name == 'Edit':
                # Display a dialog box asking the user to specify the length limit
                root = tk.Tk()
                root.withdraw()
                length_limit = tk.simpledialog.askinteger('Length Limit', 'Enter the length limit for the Cartesian products:', minvalue=1, maxvalue=10)
                
                # Generate and submit Cartesian products of the specified length
                for length in range(1, length_limit + 1):
                    for product in itertools.product(elements, repeat=length):
                        # Copy the product to the clipboard
                        product_string = ''.join(product)
                        clipboard.copy(product_string)
                        
                        # Simulate the user pasting the product into the entry-textbox and submitting it
                        win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
                        win32api.keybd_event(win32con.VK_V, 0, 0, 0)
                        win32api.keybd_event(win32con.VK_V, 0, win32con.KEYEVENTF_KEYUP, 0)
                        win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)
                        win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)
                        win32api.keybd_event(win32con.VK_RETURN, 0, win32con.KEYEVENTF_KEYUP, 0)
                
                # Display a message indicating that the operation is complete
                tk.messagebox.showinfo('Done', 'All Cartesian products have been submitted.')
                
            # Wait for the next event
            win32api.Sleep(100)

if __name__ == '__main__':
    generate_cartesian_products()