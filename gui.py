import customtkinter as ctk
from trigger import update_checkin
from auth import register_user, login_user
from tkinter import messagebox
from trigger import get_status
current_user = None
from messages import (
    add_message,
    get_messages,
    delete_message
)
from trigger import (
    update_checkin,
    get_status,
    release_messages
)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.geometry("1200x700")
app.title("Dead Man's Digital Switch")


# -----------------------------
# Functions
# -----------------------------
################################################################################  
def register_action():

    name = register_name.get()
    email = register_email.get()
    password = register_password.get()

    interval = register_interval.get()

    if not interval:
        interval = 7

    success = register_user(
        name,
        email,
        password,
        int(interval)
    )

    if success:
        messagebox.showinfo(
            "Success",
            "Registration Successful"
        )

        show_login()

    else:
        messagebox.showerror(
            "Error",
            "Email already exists"
        )


def login_action():

    email = login_email.get()
    password = login_password.get()

    user = login_user(
        email,
        password
    )

    if user:

        global current_user

        current_user = user

        show_dashboard()

    else:

        messagebox.showerror(
            "Error",
            "Invalid Credentials"
        )


################################################################################        
def open_add_message():

    window = ctk.CTkToplevel()

    window.title("Add Secret Message")
    window.geometry("500x500")

    ctk.CTkLabel(
        window,
        text="Recipient Name"
    ).pack(pady=5)

    recipient_name = ctk.CTkEntry(
        window,
        width=300
    )
    recipient_name.pack()

    ctk.CTkLabel(
        window,
        text="Recipient Email"
    ).pack(pady=5)

    recipient_email = ctk.CTkEntry(
        window,
        width=300
    )
    recipient_email.pack()

    ctk.CTkLabel(
        window,
        text="Subject"
    ).pack(pady=5)

    subject = ctk.CTkEntry(
        window,
        width=300
    )
    subject.pack()

    ctk.CTkLabel(
        window,
        text="Message"
    ).pack(pady=5)

    message_box = ctk.CTkTextbox(
        window,
        width=350,
        height=120
    )

    message_box.pack(pady=10)

    def save():

        add_message(
            current_user[0],
            recipient_name.get(),
            recipient_email.get(),
            subject.get(),
            message_box.get("1.0", "end")
        )

        messagebox.showinfo(
            "Success",
            "Message Saved"
        )

        window.destroy()

    ctk.CTkButton(
        window,
        text="Save Message",
        command=save
    ).pack(pady=20)




def view_messages():

    window = ctk.CTkToplevel()

    window.title("My Messages")
    window.geometry("800x500")

    messages = get_messages(current_user[0])

    if not messages:

        ctk.CTkLabel(
            window,
            text="No Messages Found"
        ).pack(pady=20)

        return

    for msg in messages:

        frame = ctk.CTkFrame(window)
        frame.pack(fill="x", padx=10, pady=5)

        info = f"""
To: {msg[2]}
Email: {msg[3]}
Subject: {msg[4]}
"""

        ctk.CTkLabel(
            frame,
            text=info,
            justify="left"
        ).pack(side="left", padx=10)

        def remove(mid=msg[0]):
            delete_message(mid)
            window.destroy()
            view_messages()

        ctk.CTkButton(
            frame,
            text="Delete",
            command=remove
        ).pack(side="right", padx=10)


from tkinter import messagebox

def checkin():

    print("CHECKIN CLICKED")

    update_checkin(current_user[0])

    messagebox.showinfo(
        "Success",
        "Check-In Successful"
    )


def show_status():

    status = get_status(current_user)

    messagebox.showinfo(
        "Account Status",
        status
    )

from tkinter import messagebox

def release_now():

    count = release_messages(
        current_user[0]
    )

    messagebox.showinfo(
        "Released",
        f"{count} messages sent successfully"
    )




def show_login():

    register_frame.pack_forget()

    login_frame.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )


def show_register():

    login_frame.pack_forget()

    register_frame.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )



def logout():

    global current_user

    current_user = None

    dashboard_frame.pack_forget()

    show_login()




# -----------------------------
# Login Frame
# -----------------------------

login_frame = ctk.CTkFrame(app)

login_title = ctk.CTkLabel(
    login_frame,
    text="Login",
    font=("Arial", 28, "bold")
)

login_title.pack(pady=20)

login_email = ctk.CTkEntry(
    login_frame,
    width=300,
    placeholder_text="Email"
)

login_email.pack(pady=10)

login_password = ctk.CTkEntry(
    login_frame,
    width=300,
    placeholder_text="Password",
    show="*"
)

login_password.pack(pady=10)

login_button = ctk.CTkButton(
    login_frame,
    text="Login",
    command=login_action
)

login_button.pack(pady=15)

goto_register = ctk.CTkButton(
    login_frame,
    text="Register",
    command=show_register
)

goto_register.pack(pady=10)


# -----------------------------
# Register Frame
# -----------------------------

register_frame = ctk.CTkFrame(app)

register_title = ctk.CTkLabel(
    register_frame,
    text="Register",
    font=("Arial", 28, "bold")
)

register_title.pack(pady=20)

register_name = ctk.CTkEntry(
    register_frame,
    width=300,
    placeholder_text="Name"
)

register_name.pack(pady=10)

register_email = ctk.CTkEntry(
    register_frame,
    width=300,
    placeholder_text="Email"
)

register_email.pack(pady=10)

register_password = ctk.CTkEntry(
    register_frame,
    width=300,
    placeholder_text="Password",
    show="*"
)

register_password.pack(pady=10)

register_interval = ctk.CTkEntry(
    register_frame,
    width=300,
    placeholder_text="Interval Days"
)

register_interval.pack(pady=10)

register_button = ctk.CTkButton(
    register_frame,
    text="Register",
    command=register_action
)

register_button.pack(pady=15)

goto_login = ctk.CTkButton(
    register_frame,
    text="Back To Login",
    command=show_login
)

goto_login.pack(pady=10)

#------------------------------DASHBOARD FRAME------------------------------------------------------
# -----------------------------
# Dashboard Frame
# -----------------------------

# =====================================================
# MODERN DASHBOARD
# =====================================================

dashboard_frame = ctk.CTkFrame(app)

# Left Sidebar
sidebar = ctk.CTkFrame(
    dashboard_frame,
    width=250,
    corner_radius=0
)

sidebar.pack(
    side="left",
    fill="y"
)

logo_label = ctk.CTkLabel(
    sidebar,
    text="🛡️DMS",
    font=("Segoe UI", 28, "bold")
)

logo_label.pack(pady=(30,20))

ctk.CTkLabel(
    sidebar,
    text="Automated Emergency System",
    font=("Segoe UI", 12)
).pack()

# Sidebar Buttons

add_message_btn = ctk.CTkButton(
    sidebar,
    text="➕ Add Secret Message",
    command=open_add_message,
    width=220,
    height=40
)

add_message_btn.pack(pady=10)

view_messages_btn = ctk.CTkButton(
    sidebar,
    text="📨 View Messages",
    command=view_messages,
    width=220,
    height=40
)

view_messages_btn.pack(pady=10)

checkin_btn = ctk.CTkButton(
    sidebar,
    text="✅ Check In",
    command=checkin,
    width=220,
    height=40
)

checkin_btn.pack(pady=10)

status_btn = ctk.CTkButton(
    sidebar,
    text="📊 Status",
    command=show_status,
    width=220,
    height=40
)

status_btn.pack(pady=10)

release_btn = ctk.CTkButton(
    sidebar,
    text="🚀 Release Messages",
    command=release_now,
    width=220,
    height=40
)

release_btn.pack(pady=10)

logout_btn = ctk.CTkButton(
    sidebar,
    text="🚪 Logout",
    command=logout,
    width=220,
    height=40
)

logout_btn.pack(
    side="bottom",
    pady=30
)

# =====================================================
# Main Area
# =====================================================

main_area = ctk.CTkFrame(
    dashboard_frame,
    fg_color="transparent"
)

main_area.pack(
    side="right",
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

dashboard_title = ctk.CTkLabel(
    main_area,
    text="Dead Man's Digital Switch",
    font=("Segoe UI", 32, "bold")
)

dashboard_title.pack(
    anchor="w",
    pady=(10,20)
)

welcome_card = ctk.CTkFrame(
    main_area,
    corner_radius=15
)

welcome_card.pack(
    fill="x",
    pady=10
)

welcome_label = ctk.CTkLabel(
    welcome_card,
    text="Welcome",
    font=("Segoe UI", 22, "bold")
)

welcome_label.pack(
    anchor="w",
    padx=20,
    pady=20
)

# Status Card

status_card = ctk.CTkFrame(
    main_area,
    corner_radius=15
)

status_card.pack(
    fill="x",
    pady=10
)

ctk.CTkLabel(
    status_card,
    text="🟢 Account Status",
    font=("Segoe UI", 20, "bold")
).pack(
    anchor="w",
    padx=20,
    pady=(20,5)
)

status_text = ctk.CTkLabel(
    status_card,
    text="🟢 Protected & Active",
    font=("Segoe UI", 18)
)

status_text.pack(
    anchor="w",
    padx=20,
    pady=(0,20)
)

# Statistics Card

stats_card = ctk.CTkFrame(
    main_area,
    corner_radius=15
)

stats_card.pack(
    fill="x",
    pady=10
)

ctk.CTkLabel(
    stats_card,
    text="📈 System Overview",
    font=("Segoe UI", 20, "bold")
).pack(
    anchor="w",
    padx=20,
    pady=(20,10)
)

stats_label = ctk.CTkLabel(
    stats_card,
    text="""
Store multiple secret messages
Track user inactivity
Automatically release messages
Email delivery enabled
""",
    justify="left",
    font=("Segoe UI", 15)
)

stats_label.pack(
    anchor="w",
    padx=20,
    pady=(0,20)
)

footer = ctk.CTkLabel(
    main_area,
    text="Built by Tharun",
    font=("Segoe UI", 12)
)

footer.pack(
    side="bottom",
    pady=10
)

###_________________________________________________________________

def show_dashboard():

    login_frame.pack_forget()
    register_frame.pack_forget()

    welcome_label.configure(
        text=f"Welcome {current_user[1]}"
    )

    dashboard_frame.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )


show_login()

app.mainloop()