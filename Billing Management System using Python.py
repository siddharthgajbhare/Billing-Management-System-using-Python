//aall done
from tkinter import *
from tkinter import messagebox, filedialog
from datetime import datetime
import random
import os
import sys
import subprocess


class Bill_App:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x750+0+0")
        self.root.configure(bg="#5B2C6F")
        self.root.title("Super Market Billing Software")
        self.root.resizable(False, False)

        # ============================== VARIABLES ==============================

        self.nutella = IntVar()
        self.noodles = IntVar()
        self.lays = IntVar()
        self.oreo = IntVar()
        self.muffin = IntVar()
        self.silk = IntVar()
        self.namkeen = IntVar()

        self.atta = IntVar()
        self.pasta = IntVar()
        self.rice = IntVar()
        self.oil = IntVar()
        self.sugar = IntVar()
        self.dal = IntVar()
        self.tea = IntVar()

        self.soap = IntVar()
        self.shampoo = IntVar()
        self.lotion = IntVar()
        self.cream = IntVar()
        self.foam = IntVar()
        self.mask = IntVar()
        self.sanitizer = IntVar()

        self.total_sna = StringVar(value="0 Rs")
        self.total_gro = StringVar(value="0 Rs")
        self.total_hyg = StringVar(value="0 Rs")

        self.a = StringVar(value="0 Rs")
        self.b = StringVar(value="0 Rs")
        self.c = StringVar(value="0 Rs")

        self.subtotal = StringVar(value="0 Rs")
        self.discount = StringVar(value="0")
        self.grand_total = StringVar(value="0 Rs")

        self.amount_paid = StringVar(value="0")
        self.change_amount = StringVar(value="0 Rs")

        self.c_name = StringVar()
        self.phone = StringVar()
        self.bill_no = StringVar()
        self.payment_method = StringVar(value="Cash")

        self.generate_bill_number()

        # ============================== TITLE ==============================

        title = Label(
            self.root,
            text="SUPER MARKET BILLING SYSTEM",
            bd=12,
            relief=RIDGE,
            font=("Arial Black", 20),
            bg="#A569BD",
            fg="white"
        )
        title.pack(fill=X)

        # ============================== CUSTOMER DETAILS ==============================

        details = LabelFrame(
            self.root,
            text="Customer Details",
            font=("Arial Black", 12),
            bg="#A569BD",
            fg="white",
            relief=GROOVE,
            bd=10
        )

        details.place(x=0, y=80, relwidth=1)

        Label(
            details,
            text="Customer Name",
            font=("Arial Black", 13),
            bg="#A569BD",
            fg="white"
        ).grid(row=0, column=0, padx=10, pady=5)

        Entry(
            details,
            borderwidth=3,
            width=25,
            textvariable=self.c_name
        ).grid(row=0, column=1, padx=8)

        Label(
            details,
            text="Contact No.",
            font=("Arial Black", 13),
            bg="#A569BD",
            fg="white"
        ).grid(row=0, column=2, padx=10)

        Entry(
            details,
            borderwidth=3,
            width=25,
            textvariable=self.phone
        ).grid(row=0, column=3, padx=8)

        Label(
            details,
            text="Bill No.",
            font=("Arial Black", 13),
            bg="#A569BD",
            fg="white"
        ).grid(row=0, column=4, padx=10)

        Entry(
            details,
            borderwidth=3,
            width=18,
            textvariable=self.bill_no,
            state="readonly"
        ).grid(row=0, column=5, padx=8)

        Label(
            details,
            text="Date",
            font=("Arial Black", 13),
            bg="#A569BD",
            fg="white"
        ).grid(row=0, column=6, padx=10)

        self.date_label = Label(
            details,
            text=datetime.now().strftime("%d-%m-%Y %I:%M %p"),
            font=("Arial Black", 11),
            bg="#A569BD",
            fg="white"
        )
        self.date_label.grid(row=0, column=7, padx=8)

        # ============================== PRODUCTS ==============================

        self.create_product_section(
            "Snacks",
            [
                ("Nutella Choco Spread", self.nutella),
                ("Noodles (1 Pack)", self.noodles),
                ("Lays (10Rs)", self.lays),
                ("Oreo (20Rs)", self.oreo),
                ("Chocolate Muffin", self.muffin),
                ("Dairy Milk Silk (60Rs)", self.silk),
                ("Namkeen (15Rs)", self.namkeen)
            ],
            5,
            180
        )

        self.create_product_section(
            "Grocery",
            [
                ("Aashirvaad Atta (1kg)", self.atta),
                ("Pasta (1kg)", self.pasta),
                ("Basmathi Rice (1kg)", self.rice),
                ("Sunflower Oil (1ltr)", self.oil),
                ("Refined Sugar (1kg)", self.sugar),
                ("Daal (1kg)", self.dal),
                ("Tea Powder (1kg)", self.tea)
            ],
            340,
            180
        )

        self.create_product_section(
            "Beauty & Hygiene",
            [
                ("Bathing Soap", self.soap),
                ("Shampoo (1ltr)", self.shampoo),
                ("Body Lotion (1ltr)", self.lotion),
                ("Face Cream", self.cream),
                ("Shaving Foam", self.foam),
                ("Face Mask (1piece)", self.mask),
                ("Hand Sanitizer (50ml)", self.sanitizer)
            ],
            675,
            180
        )

        # ============================== BILL AREA ==============================

        billarea = Frame(
            self.root,
            bd=10,
            relief=GROOVE,
            bg="#E5B4F3"
        )

        billarea.place(
            x=1010,
            y=180,
            width=330,
            height=380
        )

        Label(
            billarea,
            text="BILL AREA",
            font=("Arial Black", 17),
            bd=7,
            relief=GROOVE,
            bg="#E5B4F3",
            fg="#6C3483"
        ).pack(fill=X)

        scroll_y = Scrollbar(
            billarea,
            orient=VERTICAL
        )

        scroll_y.pack(
            side=RIGHT,
            fill=Y
        )

        self.txtarea = Text(
            billarea,
            yscrollcommand=scroll_y.set,
            font=("Consolas", 9)
        )

        self.txtarea.pack(
            fill=BOTH,
            expand=1
        )

        scroll_y.config(
            command=self.txtarea.yview
        )

        # ============================== SUMMARY ==============================

        summary = LabelFrame(
            self.root,
            text="Billing Summary",
            font=("Arial Black", 11),
            relief=GROOVE,
            bd=8,
            bg="#A569BD",
            fg="white"
        )

        summary.place(
            x=0,
            y=570,
            relwidth=1,
            height=175
        )

        Label(
            summary,
            text="Subtotal",
            font=("Arial Black", 10),
            bg="#A569BD",
            fg="white"
        ).grid(row=0, column=0, padx=8, pady=3)

        Entry(
            summary,
            width=18,
            textvariable=self.subtotal,
            state="readonly"
        ).grid(row=0, column=1)

        Label(
            summary,
            text="Discount %",
            font=("Arial Black", 10),
            bg="#A569BD",
            fg="white"
        ).grid(row=1, column=0, padx=8)

        Entry(
            summary,
            width=18,
            textvariable=self.discount
        ).grid(row=1, column=1)

        Label(
            summary,
            text="Grand Total",
            font=("Arial Black", 10),
            bg="#A569BD",
            fg="white"
        ).grid(row=2, column=0, padx=8)

        Entry(
            summary,
            width=18,
            textvariable=self.grand_total,
            state="readonly"
        ).grid(row=2, column=1)

        Label(
            summary,
            text="Payment",
            font=("Arial Black", 10),
            bg="#A569BD",
            fg="white"
        ).grid(row=0, column=2, padx=8)

        payment_menu = OptionMenu(
            summary,
            self.payment_method,
            "Cash",
            "UPI",
            "Card"
        )

        payment_menu.config(width=14)
        payment_menu.grid(row=0, column=3)

        Label(
            summary,
            text="Amount Paid",
            font=("Arial Black", 10),
            bg="#A569BD",
            fg="white"
        ).grid(row=1, column=2)

        Entry(
            summary,
            width=18,
            textvariable=self.amount_paid
        ).grid(row=1, column=3)

        Label(
            summary,
            text="Change",
            font=("Arial Black", 10),
            bg="#A569BD",
            fg="white"
        ).grid(row=2, column=2)

        Entry(
            summary,
            width=18,
            textvariable=self.change_amount,
            state="readonly"
        ).grid(row=2, column=3)

        # ============================== BUTTONS ==============================

        button_frame = Frame(
            summary,
            bd=5,
            relief=GROOVE,
            bg="#6C3483"
        )

        button_frame.place(
            x=750,
            y=10,
            width=565,
            height=145
        )

        Button(
            button_frame,
            text="TOTAL",
            font=("Arial Black", 11),
            bg="#E5B4F3",
            fg="#6C3483",
            width=10,
            command=self.total
        ).grid(row=0, column=0, padx=5, pady=8)

        Button(
            button_frame,
            text="SAVE BILL",
            font=("Arial Black", 11),
            bg="#E5B4F3",
            fg="#6C3483",
            width=10,
            command=self.save_bill
        ).grid(row=0, column=1, padx=5)

        Button(
            button_frame,
            text="PRINT",
            font=("Arial Black", 11),
            bg="#E5B4F3",
            fg="#6C3483",
            width=10,
            command=self.print_bill
        ).grid(row=0, column=2, padx=5)

        Button(
            button_frame,
            text="SEARCH",
            font=("Arial Black", 11),
            bg="#E5B4F3",
            fg="#6C3483",
            width=10,
            command=self.search_bill
        ).grid(row=1, column=0, padx=5)

        Button(
            button_frame,
            text="CLEAR",
            font=("Arial Black", 11),
            bg="#E5B4F3",
            fg="#6C3483",
            width=10,
            command=self.clear
        ).grid(row=1, column=1, padx=5)

        Button(
            button_frame,
            text="EXIT",
            font=("Arial Black", 11),
            bg="#E5B4F3",
            fg="#6C3483",
            width=10,
            command=self.exit1
        ).grid(row=1, column=2, padx=5)

        self.intro()

        # Keyboard shortcuts
        self.root.bind("<Control-s>", lambda event: self.save_bill())
        self.root.bind("<Control-p>", lambda event: self.print_bill())
        self.root.bind("<Control-r>", lambda event: self.clear())
        self.root.protocol("WM_DELETE_WINDOW", self.exit1)

    # ============================== PRODUCT SECTION ==============================

    def create_product_section(self, title, products, x, y):

        frame = LabelFrame(
            self.root,
            text=title,
            font=("Arial Black", 12),
            bg="#E5B4F3",
            fg="#6C3483",
            relief=GROOVE,
            bd=10
        )

        frame.place(
            x=x,
            y=y,
            height=380,
            width=325
        )

        for row, (name, variable) in enumerate(products):

            Label(
                frame,
                text=name,
                font=("Arial Black", 10),
                bg="#E5B4F3",
                fg="#6C3483"
            ).grid(
                row=row,
                column=0,
                pady=11,
                padx=3
            )

            Entry(
                frame,
                borderwidth=2,
                width=10,
                textvariable=variable
            ).grid(
                row=row,
                column=1,
                padx=8
            )

    # ============================== BILL NUMBER ==============================

    def generate_bill_number(self):

        number = random.randint(1000, 9999)

        self.bill_no.set(
            str(number)
        )

    # ============================== VALIDATION ==============================

    def validate_customer(self):

        if not self.c_name.get().strip():

            messagebox.showerror(
                "Error",
                "Please enter customer name."
            )

            return False

        if not self.phone.get().strip():

            messagebox.showerror(
                "Error",
                "Please enter contact number."
            )

            return False

        if not self.phone.get().isdigit():

            messagebox.showerror(
                "Error",
                "Contact number must contain only digits."
            )

            return False

        return True

    # ============================== TOTAL ==============================

    def total(self):

        if not self.validate_customer():
            return

        try:

            # Snacks
            self.nu = self.nutella.get() * 120
            self.no = self.noodles.get() * 40
            self.la = self.lays.get() * 10
            self.ore = self.oreo.get() * 20
            self.mu = self.muffin.get() * 30
            self.si = self.silk.get() * 60
            self.na = self.namkeen.get() * 15

            total_snacks_price = (
                self.nu +
                self.no +
                self.la +
                self.ore +
                self.mu +
                self.si +
                self.na
            )

            snacks_tax = round(
                total_snacks_price * 0.05,
                2
            )

            # Grocery
            self.at = self.atta.get() * 42
            self.pa = self.pasta.get() * 120
            self.oi = self.oil.get() * 113
            self.ri = self.rice.get() * 160
            self.su = self.sugar.get() * 55
            self.da = self.dal.get() * 76
            self.te = self.tea.get() * 480

            total_grocery_price = (
                self.at +
                self.pa +
                self.oi +
                self.ri +
                self.su +
                self.da +
                self.te
            )

            grocery_tax = round(
                total_grocery_price * 0.01,
                2
            )

            # Hygiene
            self.so = self.soap.get() * 30
            self.sh = self.shampoo.get() * 180
            self.lo = self.lotion.get() * 500
            self.cr = self.cream.get() * 130
            self.fo = self.foam.get() * 85
            self.ma = self.mask.get() * 100
            self.sa = self.sanitizer.get() * 20

            total_hygiene_price = (
                self.so +
                self.sh +
                self.lo +
                self.cr +
                self.fo +
                self.ma +
                self.sa
            )

            hygiene_tax = round(
                total_hygiene_price * 0.10,
                2
            )

            # Category totals
            self.total_sna.set(
                f"{total_snacks_price:.2f} Rs"
            )

            self.total_gro.set(
                f"{total_grocery_price:.2f} Rs"
            )

            self.total_hyg.set(
                f"{total_hygiene_price:.2f} Rs"
            )

            self.a.set(
                f"{snacks_tax:.2f} Rs"
            )

            self.b.set(
                f"{grocery_tax:.2f} Rs"
            )

            self.c.set(
                f"{hygiene_tax:.2f} Rs"
            )

            subtotal = (
                total_snacks_price +
                total_grocery_price +
                total_hygiene_price
            )

            tax = (
                snacks_tax +
                grocery_tax +
                hygiene_tax
            )

            subtotal_with_tax = subtotal + tax

            # Discount
            discount_percent = float(
                self.discount.get() or 0
            )

            if discount_percent < 0 or discount_percent > 100:

                messagebox.showerror(
                    "Error",
                    "Discount must be between 0 and 100."
                )

                return

            discount_amount = round(
                subtotal_with_tax *
                discount_percent /
                100,
                2
            )

            grand_total = round(
                subtotal_with_tax -
                discount_amount,
                2
            )

            self.subtotal.set(
                f"{subtotal_with_tax:.2f} Rs"
            )

            self.grand_total.set(
                f"{grand_total:.2f} Rs"
            )

            # Payment
            paid = float(
                self.amount_paid.get() or 0
            )

            if paid < 0:

                messagebox.showerror(
                    "Error",
                    "Amount paid cannot be negative."
                )

                return

            change = paid - grand_total

            if paid >= grand_total:

                self.change_amount.set(
                    f"{change:.2f} Rs"
                )

            else:

                self.change_amount.set(
                    f"Due: {abs(change):.2f} Rs"
                )

            self.total_all_bill = grand_total

            self.billarea()

        except ValueError:

            messagebox.showerror(
                "Invalid Input",
                "Please enter valid numeric values."
            )

    # ============================== BILL HEADER ==============================

    def intro(self):

        self.txtarea.delete(
            1.0,
            END
        )

        self.txtarea.insert(
            END,
            "\tSUPER MARKET\n"
        )

        self.txtarea.insert(
            END,
            "\tPhone: 739275410\n"
        )

        self.txtarea.insert(
            END,
            "\nBill No. : "
            + self.bill_no.get()
        )

        self.txtarea.insert(
            END,
            "\nCustomer : "
            + self.c_name.get()
        )

        self.txtarea.insert(
            END,
            "\nPhone    : "
            + self.phone.get()
        )

        self.txtarea.insert(
            END,
            "\nDate     : "
            + datetime.now().strftime(
                "%d-%m-%Y %I:%M %p"
            )
        )

        self.txtarea.insert(
            END,
            "\n----------------------------------------\n"
        )

        self.txtarea.insert(
            END,
            "Product\t\tQty\tPrice\n"
        )

        self.txtarea.insert(
            END,
            "----------------------------------------\n"
        )

    # ============================== BILL AREA ==============================

    def billarea(self):

        self.intro()

        products = [

            ("Nutella", self.nutella.get(), self.nu),
            ("Noodles", self.noodles.get(), self.no),
            ("Lays", self.lays.get(), self.la),
            ("Oreo", self.oreo.get(), self.ore),
            ("Muffins", self.muffin.get(), self.mu),
            ("Silk", self.silk.get(), self.si),
            ("Namkeen", self.namkeen.get(), self.na),

            ("Atta", self.atta.get(), self.at),
            ("Pasta", self.pasta.get(), self.pa),
            ("Rice", self.rice.get(), self.ri),
            ("Oil", self.oil.get(), self.oi),
            ("Sugar", self.sugar.get(), self.su),
            ("Daal", self.dal.get(), self.da),
            ("Tea", self.tea.get(), self.te),

            ("Soap", self.soap.get(), self.so),
            ("Shampoo", self.shampoo.get(), self.sh),
            ("Lotion", self.lotion.get(), self.lo),
            ("Cream", self.cream.get(), self.cr),
            ("Foam", self.foam.get(), self.fo),
            ("Mask", self.mask.get(), self.ma),
            ("Sanitizer", self.sanitizer.get(), self.sa)
        ]

        for name, quantity, price in products:

            if quantity != 0:

                self.txtarea.insert(
                    END,
                    f"{name:<15} {quantity:<5} {price:.2f}\n"
                )

        self.txtarea.insert(
            END,
            "----------------------------------------\n"
        )

        self.txtarea.insert(
            END,
            f"Snacks Tax     : {self.a.get()}\n"
        )

        self.txtarea.insert(
            END,
            f"Grocery Tax    : {self.b.get()}\n"
        )

        self.txtarea.insert(
            END,
            f"Hygiene Tax    : {self.c.get()}\n"
        )

        self.txtarea.insert(
            END,
            f"Subtotal       : {self.subtotal.get()}\n"
        )

        self.txtarea.insert(
            END,
            f"Discount       : {self.discount.get()}%\n"
        )

        self.txtarea.insert(
            END,
            f"GRAND TOTAL    : {self.grand_total.get()}\n"
        )

        self.txtarea.insert(
            END,
            f"Payment        : {self.payment_method.get()}\n"
        )

        self.txtarea.insert(
            END,
            f"Amount Paid    : {self.amount_paid.get()} Rs\n"
        )

        self.txtarea.insert(
            END,
            f"Change         : {self.change_amount.get()}\n"
        )

        self.txtarea.insert(
            END,
            "----------------------------------------\n"
        )

        self.txtarea.insert(
            END,
            "\tThank You! Visit Again.\n"
        )

    # ============================== SAVE BILL ==============================

    def save_bill(self):

        if not self.c_name.get().strip():

            messagebox.showerror(
                "Error",
                "Generate the bill first."
            )

            return

        os.makedirs(
            "bills",
            exist_ok=True
        )

        filename = (
            "bills/Bill_"
            + self.bill_no.get()
            + ".txt"
        )

        try:

            with open(
                filename,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(
                    self.txtarea.get(
                        1.0,
                        END
                    )
                )

            messagebox.showinfo(
                "Saved",
                f"Bill saved successfully:\n{filename}"
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                f"Unable to save bill.\n{e}"
            )

    # ============================== PRINT BILL ==============================

    def print_bill(self):

        if not self.txtarea.get(
            1.0,
            END
        ).strip():

            messagebox.showerror(
                "Error",
                "Generate a bill first."
            )

            return

        filename = (
            "print_bill_"
            + self.bill_no.get()
            + ".txt"
        )

        try:

            with open(
                filename,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(
                    self.txtarea.get(
                        1.0,
                        END
                    )
                )

            if sys.platform == "win32":

                os.startfile(
                    os.path.abspath(filename),
                    "print"
                )

            else:

                subprocess.run(
                    ["lp", filename]
                )

        except Exception as e:

            messagebox.showerror(
                "Print Error",
                f"Unable to print bill.\n{e}"
            )

    # ============================== SEARCH BILL ==============================

    def search_bill(self):

        bill_number = filedialog.askstring(
            "Search Bill",
            "Enter Bill Number:"
        )

        if not bill_number:
            return

        filename = (
            "bills/Bill_"
            + bill_number
            + ".txt"
        )

        if os.path.exists(filename):

            with open(
                filename,
                "r",
                encoding="utf-8"
            ) as file:

                bill = file.read()

            self.txtarea.delete(
                1.0,
                END
            )

            self.txtarea.insert(
                END,
                bill
            )

        else:

            messagebox.showerror(
                "Not Found",
                "Bill not found."
            )

    # ============================== CLEAR ==============================

    def clear(self):

        if messagebox.askyesno(
            "Clear",
            "Clear current bill?"
        ):

            variables = [

                self.nutella,
                self.noodles,
                self.lays,
                self.oreo,
                self.muffin,
                self.silk,
                self.namkeen,

                self.atta,
                self.pasta,
                self.rice,
                self.oil,
                self.sugar,
                self.dal,
                self.tea,

                self.soap,
                self.shampoo,
                self.lotion,
                self.cream,
                self.foam,
                self.mask,
                self.sanitizer
            ]

            for variable in variables:
                variable.set(0)

            self.total_sna.set("0 Rs")
            self.total_gro.set("0 Rs")
            self.total_hyg.set("0 Rs")

            self.a.set("0 Rs")
            self.b.set("0 Rs")
            self.c.set("0 Rs")

            self.subtotal.set("0 Rs")
            self.discount.set("0")
            self.grand_total.set("0 Rs")

            self.amount_paid.set("0")
            self.change_amount.set("0 Rs")

            self.c_name.set("")
            self.phone.set("")

            self.generate_bill_number()

            self.intro()

    # ============================== EXIT ==============================

    def exit1(self):

        answer = messagebox.askyesno(
            "Exit",
            "Are you sure you want to exit?"
        )

        if answer:
            self.root.destroy()


# ============================== MAIN ==============================

if __name__ == "__main__":

    root = Tk()

    obj = Bill_App(root)

    root.mainloop()
