import tkinter
from tkinter import *
from tkinter.ttk import *
from pdf_viewer import ShowPDF
from cert_parser import CertParser
import clipboard


class ParserGUI:

    def __init__(self, iterator_obj, parser_obj):
        self.iterator_obj = iterator_obj
        self.parser_obj = parser_obj
        self.certs_list = []
        self.active_cert = ''
        self.root = WindowRoot()
        self.frames = ParserFrames(self)
        self.viewer = PDFViewer(self)
        self.listbox = ParserListBox(self)
        self.buttons = ParserButtons(self)
        self.checkboxes = ParserCheckboxes(self)
        self.root.w_root.mainloop()


class WindowRoot:

    def __init__(self):
        self.w_root = Tk()
        self.w_root.geometry('1920x1080')
        self.w_root.title('Certificate Helper')
        self.w_root.resizable(height=False, width=False)


class ParserFrames:

    def __init__(self, gui_obj):
        self.gui_obj = gui_obj

        self.upper_right_frame = tkinter.Frame(self.gui_obj.root.w_root, background='#D3D4D6', height=810, width=960)
        self.upper_right_frame.place(anchor='nw', x=960, y=0)

        self.lower_right_frame = tkinter.Frame(self.gui_obj.root.w_root, background='#D3D4D6', height=270, width=960)
        self.lower_right_frame.place(anchor='nw', x=960, y=810)


class PDFViewer:

    def __init__(self, gui_obj):
        self.gui_obj = gui_obj
        self.pdf_viewer = ShowPDF()
        self.pdf_viewer.img_object_li.clear()
        self.viewer_window = self.pdf_viewer.pdf_view(self.gui_obj.root.w_root, height=66, width=120,
                                                      pdf_location=self.gui_obj.active_cert)
        self.viewer_window.place(anchor='nw', x=0, y=0)


class ParserListBox:

    def __init__(self, gui_obj):
        self.gui_obj = gui_obj

        self.list = tkinter.Listbox(self.gui_obj.frames.upper_right_frame, background='#F1F1F1', height=33, width=40)
        self.list.place(anchor='nw', x=380, y=5)

        self.list2 = tkinter.Listbox(self.gui_obj.frames.upper_right_frame, background='#F1F1F1', height=33, width=40)
        self.list2.place(anchor='nw', x=630, y=5)

        self.list3 = tkinter.Listbox(self.gui_obj.frames.upper_right_frame, background='#F1F1F1', height=3, width=40)
        self.list3.place(anchor='nw', x=130, y=5)

    def fill_list(self, cert):
        self.list.delete(0, 'end')
        self.list2.delete(0, 'end')
        self.list3.delete(0, 'end')
        self.gui_obj.parser_obj = CertParser(cert)
        self.gui_obj.parser_obj.process_certs()
        self.list.insert(1, 'ACCORD Format:')
        self.list2.insert(1, self.gui_obj.parser_obj.results['accord_format'])
        self.list3.insert(1, '---VENDOR NAME---')
        self.list.insert(2, '')
        self.list2.insert(2, '')
        if self.gui_obj.parser_obj.results['vendor_name'] != '':
            self.list3.insert(2, self.gui_obj.parser_obj.results['vendor_name'])
            clipboard.copy(self.gui_obj.parser_obj.results['vendor_name'])
            self.list.insert(3, 'Agent Name:')
            self.list2.insert(3, self.gui_obj.parser_obj.results['agent_name'])
            self.list.insert(4, 'Agency Name:')
            self.list2.insert(4, self.gui_obj.parser_obj.results['agency_name'])
            self.list.insert(5, 'Agent Phone:')
            self.list2.insert(5, self.gui_obj.parser_obj.results['agent_phone'])
            self.list.insert(6, 'Agent Email:')
            self.list2.insert(6, self.gui_obj.parser_obj.results['agent_email'])
            self.list.insert(7, '')
            self.list2.insert(7, '')
            self.list.insert(8, 'GL Number:')
            self.list2.insert(8, self.gui_obj.parser_obj.results['gl_pol_number'])
            self.list.insert(9, 'GL Eff. Date:')
            self.list2.insert(9, self.gui_obj.parser_obj.results['gl_eff_date'])
            self.list.insert(10, 'GL Exp. Date:')
            self.list2.insert(10, self.gui_obj.parser_obj.results['gl_exp_date'])
            self.list.insert(11, 'GL E.O. Amount:')
            self.list2.insert(11, self.gui_obj.parser_obj.results['gl_each_occur'])
            self.list.insert(12, 'GL Op Agg:')
            self.list2.insert(12, self.gui_obj.parser_obj.results['gl_op_agg'])
            self.list.insert(13, 'GL Insurer:')
            self.list2.insert(13, self.gui_obj.parser_obj.results['gl_insurer'])
            self.list.insert(14, '')
            self.list2.insert(14, '')
            self.list.insert(15, 'AL Number:')
            self.list2.insert(15, self.gui_obj.parser_obj.results['al_pol_number'])
            self.list.insert(16, 'AL Eff. Date:')
            self.list2.insert(16, self.gui_obj.parser_obj.results['al_eff_date'])
            self.list.insert(17, 'AL Exp. Date:')
            self.list2.insert(17, self.gui_obj.parser_obj.results['al_exp_date'])
            self.list.insert(18, 'AL Combined Limit:')
            self.list2.insert(18, self.gui_obj.parser_obj.results['al_comb_limit'])
            self.list.insert(19, 'AL Insurer:')
            self.list2.insert(19, self.gui_obj.parser_obj.results['al_insurer'])
            self.list.insert(20, '')
            self.list2.insert(20, '')
            self.list.insert(21, 'UMB Policy Number:')
            self.list2.insert(21, self.gui_obj.parser_obj.results['umb_pol_number'])
            self.list.insert(22, 'UMB Eff. Date:')
            self.list2.insert(22, self.gui_obj.parser_obj.results['umb_eff_date'])
            self.list.insert(23, 'UMB Exp. Date:')
            self.list2.insert(23, self.gui_obj.parser_obj.results['umb_exp_date'])
            self.list.insert(24, 'UMB Each Occur:')
            self.list2.insert(24, self.gui_obj.parser_obj.results['umb_each_occur'])
            self.list.insert(25, 'UMB Aggregate:')
            self.list2.insert(25, self.gui_obj.parser_obj.results['umb_aggregate'])
            self.list.insert(26, 'UMB Insurer:')
            self.list2.insert(26, self.gui_obj.parser_obj.results['umb_insurer'])
            self.list.insert(27, '')
            self.list2.insert(27, '')
            self.list.insert(28, 'WC Policy Number:')
            self.list2.insert(28, self.gui_obj.parser_obj.results['wc_pol_number'])
            self.list.insert(29, 'WC Eff. Date:')
            self.list2.insert(29, self.gui_obj.parser_obj.results['wc_eff_date'])
            self.list.insert(30, 'WC Exp. Date:')
            self.list2.insert(30, self.gui_obj.parser_obj.results['wc_exp_date'])
            self.list.insert(31, 'WC Each Acci:')
            self.list2.insert(31, self.gui_obj.parser_obj.results['wc_each_acci'])
            self.list.insert(32, 'WC Each Employee:')
            self.list2.insert(32, self.gui_obj.parser_obj.results['wc_each_emp'])
            self.list.insert(33, 'WC Policy Limit:')
            self.list2.insert(33, self.gui_obj.parser_obj.results['wc_pol_limit'])
        else:
            self.list3.insert(2, 'Unknown - Unable to Extract')


class ParserButtons:

    def __init__(self, gui_obj):
        self.gui_obj = gui_obj

        self.next_button = Button(self.gui_obj.frames.lower_right_frame, text='BEGIN', command=self.press_next)
        self.next_button.place(anchor='nw', x=790, y=0)

    def press_next(self):
        self.gui_obj.certs_list = self.gui_obj.iterator_obj.process_iteration()
        self.gui_obj.active_cert = self.gui_obj.certs_list[0]
        self.gui_obj.viewer = PDFViewer(self.gui_obj)
        self.gui_obj.listbox.fill_list(self.gui_obj.certs_list[0])
        self.gui_obj.checkboxes.reset_checkbox()
        self.gui_obj.certs_list.pop(0)
        self.gui_obj.buttons.next_button.configure(text='NEXT')


class ParserCheckboxes:

    def __init__(self, gui_obj,):
        self.gui_obj = gui_obj
        self.default_state = True

        self.gl_additional_insured = tkinter.Checkbutton(self.gui_obj.frames.upper_right_frame, background='#D3D4D6',
                                                         state=DISABLED, text='GL Additional Insured',
                                                         command=lambda: self.click_checkbox('gl_additional_insured'))
        self.gl_additional_insured.place(anchor='nw', x=130, y=70)

        self.gl_pnc = tkinter.Checkbutton(self.gui_obj.frames.upper_right_frame, background='#D3D4D6',
                                          state=DISABLED, text='GL Primary/Non Contributory',
                                          command=lambda: self.click_checkbox('gl_pnc'))
        self.gl_pnc.place(anchor='nw', x=130, y=100)

        self.gl_contractual_liab = tkinter.Checkbutton(self.gui_obj.frames.upper_right_frame, background='#D3D4D6',
                                                       state=DISABLED, text='GL Contractual Liab.',
                                                       command=lambda: self.click_checkbox('gl_contractual_liab'))
        self.gl_contractual_liab.place(anchor='nw', x=130, y=130)

        self.al_any_auto = tkinter.Checkbutton(self.gui_obj.frames.upper_right_frame, background='#D3D4D6',
                                               state=DISABLED, text='AL Any Auto',
                                               command=lambda: self.click_checkbox('al_any_auto'))
        self.al_any_auto.place(anchor='nw', x=130, y=160)

        self.al_additional_insured = tkinter.Checkbutton(self.gui_obj.frames.upper_right_frame, background='#D3D4D6',
                                                         state=DISABLED, text='AL Additional Insured',
                                                         command=lambda: self.click_checkbox('al_additional_insured'))
        self.al_additional_insured.place(anchor='nw', x=130, y=190)

        self.al_pnc = tkinter.Checkbutton(self.gui_obj.frames.upper_right_frame, background='#D3D4D6',
                                          state=DISABLED, text='AL Primary/Non Contributory',
                                          command=lambda: self.click_checkbox('al_pnc'))
        self.al_pnc.place(anchor='nw', x=130, y=220)

        self.wc_wos = tkinter.Checkbutton(self.gui_obj.frames.upper_right_frame, background='#D3D4D6',
                                          state=DISABLED, text='WC Waiver of Subrogation',
                                          command=lambda: self.click_checkbox('wc_wos'))
        self.wc_wos.place(anchor='nw', x=130, y=250)

    def click_checkbox(self, requirement):
        try:
            if self.gui_obj.parser_obj.results[requirement]:
                self.gui_obj.parser_obj.results[requirement] = False
            else:
                self.gui_obj.parser_obj.results[requirement] = True
        except KeyError:
            pass

    def reset_checkbox(self):
        if self.gui_obj.checkboxes.default_state:
            self.gui_obj.checkboxes.default_state = False
            self.gui_obj.checkboxes.gl_additional_insured.config(state=NORMAL)
            self.gui_obj.checkboxes.gl_pnc.config(state=NORMAL)
            self.gui_obj.checkboxes.gl_contractual_liab.config(state=NORMAL)
            self.gui_obj.checkboxes.al_any_auto.config(state=NORMAL)
            self.gui_obj.checkboxes.al_additional_insured.config(state=NORMAL)
            self.gui_obj.checkboxes.al_pnc.config(state=NORMAL)
            self.gui_obj.checkboxes.wc_wos.config(state=NORMAL)
        else:
            self.gui_obj.checkboxes.gl_additional_insured.deselect()
            self.gui_obj.checkboxes.gl_pnc.deselect()
            self.gui_obj.checkboxes.gl_contractual_liab.deselect()
            self.gui_obj.checkboxes.al_any_auto.deselect()
            self.gui_obj.checkboxes.al_additional_insured.deselect()
            self.gui_obj.checkboxes.al_pnc.deselect()
            self.gui_obj.checkboxes.wc_wos.deselect()



