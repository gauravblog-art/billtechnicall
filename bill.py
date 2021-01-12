from tkinter import*
import math,random
from tkinter import messagebox
import os


class Bill_app:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#074463"
        title = Label(self.root, text="Billing Software", relief=GROOVE, bd=12, bg=bg_color,
                      fg="white", font=("times new roman", 30, "bold"), pady=2).pack(fill=X)
        # =====================variable===============

        self.sope = IntVar()
        self.creeam = IntVar()
        self.wash = IntVar()
        self.sprey = IntVar()
        self.loshan = IntVar()
        self.oil = IntVar()

        # ===================

        self.maza = IntVar()
        self.cock = IntVar()
        self.frooti = IntVar()
        self.thumbs = IntVar()
        self.limica = IntVar()
        self.sprite = IntVar()

        # ============for grocery========
        self.rice = IntVar()
        self.food = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()

        # ============ for totall product pricess an text variable======
        self.costmotic_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_price = StringVar()

        self.costmotic_tex = StringVar()
        self.grocery_tex = StringVar()
        self.cold_yex = StringVar()

        # ============ for costber==========
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.c_bill = StringVar()
        x = random.randint(1234, 9999)
        self.c_bill.set(str(x))

        self.c_search = StringVar()

        f1 = LabelFrame(self.root, text="costemer deatails", font=(
            "times new roman", 15, "bold"), fg="gold", bg=bg_color)
        f1.place(x=0, y=80, relwidth=1)
        cname_lb = Label(f1, text="customer name", fg="white", bg=bg_color, font=(
            "times new roman", 18, "bold")).grid(row=0, column=0, padx=10, pady=3)
        cname_taxt = Entry(f1, width=15, textvariable=self.c_name, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=1, pady=5, padx=10)

        cphon_lb = Label(f1, text="customer number", fg="white", bg=bg_color, font=(
            "times new roman", 18, "bold")).grid(row=0, column=2, padx=10, pady=3)
        cphon_taxt = Entry(f1, width=15, textvariable=self.c_phone, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=3, pady=5, padx=10)

        cbill_lb = Label(f1, text="customer Bill", fg="white", bg=bg_color, font=(
            "times new roman", 18, "bold")).grid(row=0, column=4, padx=10, pady=3)
        cbill_taxt = Entry(f1, width=15,textvariable=self.c_search, font="arial 15", bd=7, relief=SUNKEN).grid(
            row=0, column=5, pady=5, padx=10)
        bill_btn = Button(f1, text="Search",command=self.find_bill, bg="blue", bd=7,
                          width=10, font="arial 12 bold").grid(row=0, column=6)

        # =============for shiope ================

        f2 = LabelFrame(self.root, text="costmatics", font=(
            "times new roman", 15, "bold"), bd=12, fg="gold", bg=bg_color)
        f2.place(x=3, y=160, width=282, height=350)

        cbha_lb = Label(f2, text="Bah sope", fg="white", bg=bg_color, font=(
            "times new roman", 15, "bold")).grid(row=0, column=0, padx=10, pady=10)
        cbha_taxt = Entry(f2, width=15, textvariable=self.sope, font="arial 10", bd=7, relief=SUNKEN).grid(
            row=0, column=1, pady=10, padx=10)
        cface_lb = Label(f2, text="Face cream", fg="white", bg=bg_color, font=(
            "times new roman", 15, "bold")).grid(row=1, column=0, padx=10, pady=10)
        cface_taxt = Entry(f2, width=15, textvariable=self.creeam, font="arial 10", bd=7, relief=SUNKEN).grid(
            row=1, column=1, pady=10, padx=10)
        cwash_lb = Label(f2, text="Face wash", fg="white", bg=bg_color, font=(
            "times new roman", 15, "bold")).grid(row=2, column=0, padx=10, pady=10)
        cwash_taxt = Entry(f2, width=15, textvariable=self.wash, font="arial 10", bd=7, relief=SUNKEN).grid(
            row=2, column=1, pady=10, padx=10)
        chair_lb = Label(f2, text="Hair Spray", fg="white", bg=bg_color, font=(
            "times new roman", 15, "bold")).grid(row=3, column=0, padx=10, pady=10)
        chair_taxt = Entry(f2, width=15, textvariable=self.sprey, font="arial 10", bd=7, relief=SUNKEN).grid(
            row=3, column=1, pady=10, padx=10)
        cbody_lb = Label(f2, text="Body Loshan", fg="white", bg=bg_color, font=(
            "times new roman", 15, "bold")).grid(row=4, column=0, padx=10, pady=10)
        cbody_taxt = Entry(f2, width=15, textvariable=self.loshan, font="arial 10", bd=7, relief=SUNKEN).grid(
            row=4, column=1, pady=10, padx=10)
        closhan_lb = Label(f2, text="Body oil", fg="white", bg=bg_color, font=(
            "times new roman", 15, "bold")).grid(row=5, column=0, padx=10, pady=10)
        closhan_taxt = Entry(f2, width=15, textvariable=self.oil, font="arial 10", bd=7, relief=SUNKEN).grid(
            row=5, column=1, pady=10, padx=10)

        # ===================grocery for food===============

        f3 = LabelFrame(self.root, text="Grocery", font=(
            "times new roman", 15, "bold"), bd=12, fg="gold", bg=bg_color)
        f3.place(x=580, y=160, width=282, height=350)

        g1_lb = Label(f3, text="Rice", fg="white", bg=bg_color, font=(
            "times new roman", 15, "bold")).grid(row=0, column=0, padx=10, pady=10)
        g1_taxt = Entry(f3, width=15, textvariable=self.rice, font="arial 10", bd=7, relief=SUNKEN).grid(
            row=0, column=1, pady=10, padx=10)
        g2_lb = Label(f3, text="Food oil", fg="white", bg=bg_color, font=(
            "times new roman", 15, "bold")).grid(row=1, column=0, padx=10, pady=10)
        g2_taxt = Entry(f3, width=15, textvariable=self.food, font="arial 10", bd=7, relief=SUNKEN).grid(
            row=1, column=1, pady=10, padx=10)
        g3_lb = Label(f3, text="Daal", fg="white", bg=bg_color, font=(
            "times new roman", 15, "bold")).grid(row=2, column=0, padx=10, pady=10)
        g3_taxt = Entry(f3, width=15, textvariable=self.daal, font="arial 10", bd=7, relief=SUNKEN).grid(
            row=2, column=1, pady=10, padx=10)
        g4_lb = Label(f3, text="Wheat", fg="white", bg=bg_color, font=(
            "times new roman", 15, "bold")).grid(row=3, column=0, padx=10, pady=10)
        g4_taxt = Entry(f3, width=15, textvariable=self.wheat, font="arial 10", bd=7, relief=SUNKEN).grid(
            row=3, column=1, pady=10, padx=10)
        g5_lb = Label(f3, text="Sugar", fg="white", bg=bg_color, font=(
            "times new roman", 15, "bold")).grid(row=4, column=0, padx=10, pady=10)
        g5_taxt = Entry(f3, width=15, textvariable=self.sugar, font="arial 10", bd=7, relief=SUNKEN).grid(
            row=4, column=1, pady=10, padx=10)
        g6_lb = Label(f3, text="Tea", fg="white", bg=bg_color, font=(
            "times new roman", 15, "bold")).grid(row=5, column=0, padx=10, pady=10)
        g6_taxt = Entry(f3, width=15, textvariable=self.tea, font="arial 10", bd=7, relief=SUNKEN).grid(
            row=5, column=1, pady=10, padx=10)
        # =========== drinking======================================

        f4 = LabelFrame(self.root, text="Cold Drink", font=(
            "times new roman", 15, "bold"), bd=12, fg="gold", bg=bg_color)
        f4.place(x=289, y=160, width=282, height=350)

        f1_lb = Label(f4, text="Maza", fg="white", bg=bg_color, font=(
            "times new roman", 15, "bold")).grid(row=0, column=0, padx=10, pady=10)
        f1_taxt = Entry(f4, width=15, textvariable=self.maza, font="arial 10", bd=7, relief=SUNKEN).grid(
            row=0, column=1, pady=10, padx=10)
        f2_lb = Label(f4, text="Cock", fg="white", bg=bg_color, font=(
            "times new roman", 15, "bold")).grid(row=1, column=0, padx=10, pady=10)
        f2_taxt = Entry(f4, width=15, textvariable=self.cock, font="arial 10", bd=7, relief=SUNKEN).grid(
            row=1, column=1, pady=10, padx=10)
        f3_lb = Label(f4, text="Frooti", fg="white", bg=bg_color, font=(
            "times new roman", 15, "bold")).grid(row=2, column=0, padx=10, pady=10)
        f3_taxt = Entry(f4, width=15, textvariable=self.frooti, font="arial 10", bd=7, relief=SUNKEN).grid(
            row=2, column=1, pady=10, padx=10)
        f4_lb = Label(f4, text="Thumbs Up", fg="white", bg=bg_color, font=(
            "times new roman", 15, "bold")).grid(row=3, column=0, padx=10, pady=10)
        f4_taxt = Entry(f4, width=15, textvariable=self.thumbs, font="arial 10", bd=7, relief=SUNKEN).grid(
            row=3, column=1, pady=10, padx=10)
        f5_lb = Label(f4, text="Limca", fg="white", bg=bg_color, font=(
            "times new roman", 15, "bold")).grid(row=4, column=0, padx=10, pady=10)
        f5_taxt = Entry(f4, width=15, textvariable=self.limica, font="arial 10", bd=7, relief=SUNKEN).grid(
            row=4, column=1, pady=10, padx=10)
        f6_lb = Label(f4, text="Sprite", fg="white", bg=bg_color, font=(
            "times new roman", 15, "bold")).grid(row=5, column=0, padx=10, pady=10)
        f6_taxt = Entry(f4, width=15, textvariable=self.sprite, font="arial 10", bd=7, relief=SUNKEN).grid(
            row=5, column=1, pady=10, padx=10)

        # ======== Bill area ============

        f5 = LabelFrame(self.root, text="Bill area", bd=12)
        f5.place(x=900, y=160, width=360, height=350)
        bill_title = Label(f5, text="Billing Area", relief=GROOVE, bd=8, bg=bg_color,
                           fg="white", font=("times new roman", 10, "bold"), pady=2).pack(fill=X)
        scrol_y = Scrollbar(f5, orient=VERTICAL)
        self.textarea = Text(f5, yscrollcommand=scrol_y.set,
                              font=("times new roman", 12, "bold"))
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)
     # ========== Billing manu=================
        f6 = LabelFrame(self.root, text="Grocery", font=(
            "times new roman", 15, "bold"), bd=10, fg="gold", bg=bg_color)
        f6.place(x=0, y=520,  relwidth=1, height=165)

        b1 = Label(f6, text="Total costmotics", bg=bg_color, fg="lightgreen", font=(
            "times new roman", 15, "bold")).grid(row=0, column=0, padx=10, pady=1)
        b1_en = Entry(f6, width=18, textvariable=self.costmotic_price, font="arial 10", bd=7, relief=SUNKEN).grid(
            row=0, column=1, pady=2, padx=10)
        b2 = Label(f6, text="Total Grocery prices", bg=bg_color, fg="lightgreen", font=(
            "times new roman", 15, "bold")).grid(row=1, column=0, padx=10, pady=1)
        b2_en = Entry(f6, width=18, textvariable=self.grocery_price, font="arial 10", bd=7, relief=SUNKEN).grid(
            row=1, column=1, pady=2, padx=10)
        b3 = Label(f6, text="Total Drink prices", bg=bg_color, fg="lightgreen", font=(
            "times new roman", 15, "bold")).grid(row=2, column=0, padx=10, pady=1)
        b3_en = Entry(f6, width=18, textvariable=self.cold_price, font="arial 10", bd=7, relief=SUNKEN).grid(
            row=2, column=1, pady=2, padx=10)

        b4 = Label(f6, text="Total costmatics tax", bg=bg_color, fg="lightgreen", font=(
            "times new roman", 15, "bold")).grid(row=0, column=2, padx=10, pady=1)
        b4_en = Entry(f6, width=18, textvariable=self.costmotic_tex, font="arial 10", bd=7, relief=SUNKEN).grid(
            row=0, column=3, pady=2, padx=10)
        b5 = Label(f6, text="Total Grocery tax", bg=bg_color, fg="lightgreen", font=(
            "times new roman", 15, "bold")).grid(row=1, column=2, padx=10, pady=1)
        b5_en = Entry(f6, width=18, textvariable=self.grocery_tex, font="arial 10", bd=7, relief=SUNKEN).grid(
            row=1, column=3, pady=2, padx=10)
        b6 = Label(f6, text="Total Drink tex", bg=bg_color, fg="lightgreen", font=(
            "times new roman", 15, "bold")).grid(row=2, column=2, padx=10, pady=1)
        b6_en = Entry(f6, width=18, textvariable=self.cold_yex, font="arial 10", bd=7, relief=SUNKEN).grid(
            row=2, column=3, pady=2, padx=10)

        btn_a = Frame(f6, bd=7, relief=GROOVE)
        btn_a.place(x=750, width=500, height=90)


        bill_btn1 = Button(btn_a, command=self.total, text="Total", bg="cadetblue",fg="white", bd=5, pady=15,width=13, font="arial 10 bold").grid(row=0, column=0)
        bill_btn2 = Button(btn_a, command=self.bull_area, text="Genrate Bill",bg="cadetblue", fg="white", bd=5, pady=15,width=13,font="arial 10 bold").grid(row=0, column=1)

        bill_btn3 = Button(btn_a,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",bd=5,pady=15,width=13, font="arial 10 bold").grid(row=0, column=2)
        bill_btn4 = Button(btn_a, text="Exite", command=self.exite_bill_app, bg="cadetblue", fg="white", bd=5, pady=15, width=13, font="arial 10 bold").grid(row=0, column=3)


        self.welcome_bill()


    def total(self):
        self.c = self.sope.get() * 40


        self.c1 = self.creeam.get() * 60
        self.c2 = self.wash.get() * 70
        self.c3 = self.sprey.get() * 80
        self.c4 = self.oil.get() * 120
        self.c5 = self.loshan.get() * 120

        self.g = self.rice.get() * 40
        self.g1=self.food.get() * 60
        self.g2=self.daal.get() * 70
        self.g3=self.wheat.get() * 80
        self.g4=self.sugar.get() * 120
        self.g5=self.tea.get() * 120

        self.d=self.maza.get() * 40
        self.d1=self.cock.get() * 60
        self.d2=self.frooti.get() * 70
        self.d3=self.thumbs.get() * 80
        self.d4=self.limica.get() * 120
        self.d5=self.sprite.get() * 120



        self.total_costmatic_prices=(
                    (self.c) +
                    (self.c1) +
                    (self.c2) +
                    (self.c3) +
                    (self.c4) +
                    (self.c5)
                            )
        self.costmotic_price.set("Rs." + str(self.total_costmatic_prices))
        self.c_tex=round((self.total_costmatic_prices * 0.05), 2)
        self.costmotic_tex.set("Rs." +
                         str(round((self.total_costmatic_prices * 0.05), 2)))
        self.total_grocery_prices=(
                        (self.g) +
                        (self.g1) +
                        (self.g2) +
                        (self.g3) +
                        (self.g4) +
                        (self.g5)
        )
        self.grocery_price.set("Rs." + str(self.total_grocery_prices))
        self.g_tex=round((self.total_grocery_prices * 0.05), 2)
        self.grocery_tex.set("Rs." + str(self.g_tex))
        self.total_drink_prices=(
                        (self.d) +
                        (self.d1) +
                        (self.d2) +
                        (self.d3) +
                        (self.d4) +
                        (self.d5))
        self.cold_price.set("Rs." + str(self.total_drink_prices))

        self.d_tex=round((self.total_drink_prices * 0.05), 2)

        self.cold_yex.set("Rs." + str(self.d_tex))

        self.total_bill=float(self.total_costmatic_prices + self.total_drink_prices + self.total_grocery_prices + self.g_tex + self.c_tex + self.d_tex)




    def welcome_bill(self):
        self.textarea.delete('1.0', END)


        self.textarea.insert(END, "\twelocme to Bill Area\n")
        self.textarea.insert(END, f"\nbill number:    {self.c_bill.get()}")
        self.textarea.insert(END, f"\ncustumer Name : {self.c_name.get()}")
        self.textarea.insert(END, f"\nphone number :   {self.c_phone.get()}")
        self.textarea.insert(END, f"\n===================================")

        self.textarea.insert(END, "\nproducts\t\tqty\t\ttpricess")
        self.textarea.insert(END, f"\n===================================")




    def bull_area(self):
        self.welcome_bill()
        if self.c_name.get() == "" or self.c_phone.get() == "":
            messagebox.showerror("ERROR",
                               "you must fill the username and number")


        elif self.costmotic_price.get() == "Rs.0" and self.grocery_price.get() == "Rs.0" and self.cold_price.get() == "Rs.0":
            messagebox.showerror("ERROR", 'no product sellected pleae check it')
        else:

            if self.sope.get() != 0:
                self.textarea.insert(END,
                           f"\nbash shop\t\t{self.sope.get()}\t\t{self.c}")


            if self.creeam.get() != 0:
                self.textarea.insert(END,f"\nface cream\t\t{self.creeam.get()}\t\t{self.c1}")

            if self.wash.get() != 0:
                self.textarea.insert(END,
                           f"\nface wash\t\t{self.wash.get()}\t\t{self.c2}")


            if self.sprey.get() != 0:
                self.textarea.insert(END,
                           f"\nhair spray\t\t{self.sprey.get()}\t\t{self.c3}")

            if self.loshan.get() != 0:
                self.textarea.insert(END,
                           f"\nbody loshan\t\t{self.loshan.get()}\t\t{self.c4}")

            if self.oil.get() != 0:
                self.textarea.insert(END, f"\nbody oil\t\t{self.oil.get()}\t\t{self.c5}")
            if self.rice.get() != 0:
                self.textarea.insert(END, f"\nrice\t\t{self.rice.get()}\t\t{self.g}")
            if self.food.get() != 0:
                self.textarea.insert(END, f"\nfood\t\t{self.food.get()}\t\t{self.g1}")
            if self.daal.get() != 0:
                self.textarea.insert(END, f"\ndaal\t\t{self.daal.get()}\t\t{self.g2}")
            if self.wheat.get() != 0:
                self.textarea.insert(END, f"\nwheat\t\t{self.wheat.get()}\t\t{self.g3}")
            if self.sugar.get() != 0:
                self.textarea.insert(END, f"\nsugar\t\t{self.sugar.get()}\t\t{self.g4}")


            if self.tea.get() != 0:
                self.textarea.insert(END, f"\ntea\t\t{self.tea.get()}\t\t{self.g5}")


            if self.maza.get() != 0:
                self.textarea.insert(END, f"\nmaza\t\t{self.maza.get()}\t\t{self.d}")


            if self.cock.get() != 0:
                self.textarea.insert(END, f"\ncock\t\t{self.cock.get()}\t\t{self.d1}")


            if self.frooti.get() != 0:
                self.textarea.insert(END,
                           f"\nfrooti\t\t{self.frooti.get()}\t\t{self.d2}")


            if self.thumbs.get() != 0:
                self.textarea.insert(END,
                           f"\nthumbs\t\t{self.thumbs.get()}\t\t{self.d3}")

            if self.limica.get() != 0:
                self.textarea.insert(END,
                           f"\nlimica\t\t{self.limica.get()}\t\t{self.d4}")


            if self.sprite.get() != 0:
                self.textarea.insert(END,
                           f"\nsprite\t\t{self.sprite.get()}\t\t{self.d5}")


            if self.costmotic_tex.get() != "Rs. 0.0":
                self.textarea.insert(
                    END, f"\n-----------------------------------------------------------------")


                self.textarea.insert(
                    END, f"\ncostmotic Tex\t\t\t\t{self.costmotic_tex.get()}")


            if self.cold_yex.get() != "Rs. 0.0":
                self.textarea.insert(END,
                           f"\ncold drink Tex\t\t\t\t{self.cold_yex.get()}")


            if self.grocery_tex.get() != "Rs. 0.0":
                self.textarea.insert(END,
                                f"\ngrocery Tex\t\t\t\t{self.grocery_tex.get()}")
                self.textarea.insert(END,
                       f"\n-----------------------------------------------------------------")
                self.textarea.insert(END, f"\nTotal Bill\t\t\t\t{self.total_bill}")
                self.bill_saved()







    def bill_saved(self):
        op=messagebox.askyesno("yes", "do you want to save this bill")



        if op > 0:
            self.bill_data=self.textarea.get('1.0', END)
            f1=open("bills/" + str(self.c_bill.get()) + ".txt", "w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("saved", f"{self.c_bill.get()} saved successfully")
        else:

            return

    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.c_search.get():
                f1=open(f"bills/{i}","r")
                self.textarea.delete("1.0",END)
                for d in f1:

                   self.textarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("ERROR","bill invalidc no.")
    def clear_data(self):
        op=messagebox.askyesno("CLEAR","do you want to clear.")
        if op>0:
            self.sope.set(0)
            self.creeam = IntVar(0)
            self.wash = IntVar(0)
            self.sprey = IntVar(0)
            self.loshan = IntVar(0)
            self.oil = IntVar(0)

            # ===================

            self.maza = IntVar(0)
            self.cock = IntVar(0)
            self.frooti = IntVar(0)
            self.thumbs = IntVar(0)
            self.limica = IntVar(0)
            self.sprite = IntVar(0)

            # ============for grocery========
            self.rice.set(0)
            self.food.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)

            # ============ for totall product pricess an text variable======
            self.costmotic_price.set("")
            self.grocery_price.set("")
            self.cold_price.set("")

            self.costmotic_tex.set("")
            self.grocery_tex.set("")
            self.cold_yex.set("")

            # ============ for costber==========
            self.c_name.set("")
            self.c_phone.set("")
            self.c_bill.set("")
            x = random.randint(1234, 9999)
            self.c_bill.set(str(x))

            self.c_search.set("")

            self.welcome_bill()
        else:
            return
    def exite_bill_app(self):
        op = messagebox.askyesno("EXITE", "do you want to really exite.")
        if op>0:
            self.root.destroy()





r=Tk()
b=Bill_app(r)
r.mainloop()
