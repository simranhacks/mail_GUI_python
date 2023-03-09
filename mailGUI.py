import tkinter as tk
import smtplib

class MailClient:
    def __init__(self, master):
        self.master = master
        self.master.title("Mail Client")

        # Create entry widgets for email fields
        tk.Label(self.master, text="From:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.from_entry = tk.Entry(self.master, width=50)
        self.from_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

        tk.Label(self.master, text="To:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.to_entry = tk.Entry(self.master, width=50)
        self.to_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

        tk.Label(self.master, text="Subject:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.subject_entry = tk.Entry(self.master, width=50)
        self.subject_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

        # Create text widget for email body
        tk.Label(self.master, text="Message:").grid(row=3, column=0, padx=5, pady=5, sticky="ne")
        self.message_text = tk.Text(self.master, width=50, height=10)
        self.message_text.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

        # Create button to send email
        tk.Button(self.master, text="Send", width=10, command=self.send_email).grid(row=5, column=1, padx=5, pady=5)

    def send_email(self):
        # Get email fields from entry widgets and text widget
        from_addr = self.from_entry.get()
        to_addr = self.to_entry.get()
        subject = self.subject_entry.get()
        message = self.message_text.get("1.0", tk.END)

        # Create email message
        email_message = "From: {}\nTo: {}\nSubject: {}\n\n{}".format(from_addr, to_addr, subject, message)

        # Send email using SMTP server
        try:
            smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
            smtp_server.ehlo()
            smtp_server.starttls()
            smtp_server.login(from_addr, 'yourpassword')
            smtp_server.sendmail(from_addr, to_addr, email_message)
            smtp_server.close()
            tk.messagebox.showinfo("Success", "Email sent successfully!")
        except:
            tk.messagebox.showerror("Error", "Unable to send email.")

if __name__== "__main__":
    root = tk.Tk()
    mail_client = MailClient(root)
    root.mainloop()
