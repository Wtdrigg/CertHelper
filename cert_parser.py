import pdfquery
from cert_coordinates import CertCoordinates


class CertParser:

    # Constructor, builds and uses an iterator object to list all PDF files in the certificates' folder. Also builds a
    # coordinates object to reference later, and creates the self.results, self.pdf, and self.format_dict
    # attributes for use later.
    def __init__(self, certificate=''):
        self.coordinates = CertCoordinates()
        self.results = {}
        self.pdf = ''
        self.format_dict = {}
        self.certificate = certificate
        
    def pdf_extract(self, x1, y1, x2, y2):
        coordinates = (x1 * 72, y1 * 72, x2 * 72, y2 * 72)
        # noinspection PyUnresolvedReferences
        extracted_text = self.pdf.pq('LTTextLineHorizontal:overlaps_bbox("%d, %d, %d, %d")' % coordinates).text()
        return extracted_text

    def verify_accord(self, coordinates):
        verify = self.pdf_extract(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        if verify == 'The ACORD name and logo are registered marks of ACORD':
            verify_results = 'Standard'
        elif verify == 'the':
            verify_results = 'Alternate'
        else:
            verify_results = 'Scanned'
        print('\nACCORD Format: ' + verify_results)
        return verify_results

    def process_certs(self):
        self.pdf = pdfquery.PDFQuery(self.certificate)
        self.pdf.load(0)
        self.extract_text()

    def extract_text(self):
        verify_results = self.verify_accord(self.coordinates.verify)
        self.results['accord_format'] = verify_results
        if verify_results == 'Standard':
            self.format_dict = self.coordinates.standard
            self.extraction_methods()
        elif verify_results == 'Alternate':
            self.format_dict = self.coordinates.alternate
            self.extraction_methods()
        else:
            print('Scanned certificate, unable to extract')
            self.results['vendor_name'] = ''

    def extraction_methods(self):
        print()
        insurer_dict = self.get_insurers()
        self.results['vendor_name'] = self.get_vendor_name(self.format_dict['vendor_name'])
        self.results['agent_name'] = self.get_agent_name(self.format_dict['agent_name'])
        self.results['agency_name'] = self.get_agency_name(self.format_dict['agency_name'])
        self.results['agent_phone'] = self.get_agent_phone(self.format_dict['agent_phone'])
        self.results['agent_email'] = self.get_agent_email(self.format_dict['agent_email'])
        print()
        self.results['gl_pol_number'] = self.get_gl_policy_number(self.format_dict['gl_pol_number'])
        self.results['gl_eff_date'] = self.get_gl_eff_date(self.format_dict['gl_eff_date'])
        self.results['gl_exp_date'] = self.get_gl_exp_date(self.format_dict['gl_exp_date'])
        self.results['gl_each_occur'] = self.get_gl_each_occurrence(self.format_dict['gl_each_occur'])
        self.results['gl_op_agg'] = self.get_gl_op_agg(self.format_dict['gl_op_agg'])
        self.results['gl_insurer'] = self.get_gl_insurer(self.format_dict['gl_insurer'], insurer_dict)
        print()
        self.results['al_pol_number'] = self.get_al_policy_number(self.format_dict['al_pol_number'])
        self.results['al_eff_date'] = self.get_al_eff_date(self.format_dict['al_eff_date'])
        self.results['al_exp_date'] = self.get_al_exp_date(self.format_dict['al_exp_date'])
        self.results['al_comb_limit'] = self.get_al_comb_limit(self.format_dict['al_comb_limit'])
        self.results['al_insurer'] = self.get_al_insurer(self.format_dict['al_insurer'], insurer_dict)
        print()
        self.results['umb_pol_number'] = self.get_umb_pol_number(self.format_dict['umb_pol_number'])
        self.results['umb_eff_date'] = self.get_umb_eff_date(self.format_dict['umb_eff_date'])
        self.results['umb_exp_date'] = self.get_umb_exp_date(self.format_dict['umb_exp_date'])
        self.results['umb_each_occur'] = self.get_umb_each_occur(self.format_dict['umb_each_occur'])
        self.results['umb_aggregate'] = self.get_umb_aggregate(self.format_dict['umb_aggregate'])
        self.results['umb_insurer'] = self.get_umb_insurer(self.format_dict['umb_insurer'], insurer_dict)
        print()
        self.results['wc_pol_number'] = self.get_wc_pol_number(self.format_dict['wc_pol_number:'])
        self.results['wc_eff_date'] = self.get_wc_eff_date(self.format_dict['wc_eff_date'])
        self.results['wc_exp_date'] = self.get_wc_exp_date(self.format_dict['wc_exp_date'])
        self.results['wc_each_acci'] = self.get_wc_each_acci(self.format_dict['wc_each_acci'])
        self.results['wc_each_emp'] = self.get_wc_each_emp(self.format_dict['wc_each_emp'])
        self.results['wc_pol_limit'] = self.get_wc_pol_limit(self.format_dict['wc_pol_limit'])
        self.results['wc_insurer'] = self.get_wc_insurer(self.format_dict['wc_insurer'], insurer_dict)
        self.set_requirements_default()

    def get_vendor_name(self, coordinates):
        vendor_name = self.pdf_extract(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        print('Vendor Name: ' + vendor_name)
        if vendor_name == '':
            vendor_name = '-'
        return vendor_name

    def get_insurers(self):
        insurer_a = self.pdf_extract(self.format_dict['insurer_a'][0], self.format_dict['insurer_a'][1],
                                     self.format_dict['insurer_a'][2], self.format_dict['insurer_a'][3])
        print('Insurer A: ' + insurer_a)
        insurer_b = self.pdf_extract(self.format_dict['insurer_b'][0], self.format_dict['insurer_b'][1],
                                     self.format_dict['insurer_b'][2], self.format_dict['insurer_b'][3])
        print('Insurer B: ' + insurer_b)
        insurer_c = self.pdf_extract(self.format_dict['insurer_c'][0], self.format_dict['insurer_c'][1],
                                     self.format_dict['insurer_c'][2], self.format_dict['insurer_c'][3])
        print('Insurer C: ' + insurer_c)
        insurer_d = self.pdf_extract(self.format_dict['insurer_d'][0], self.format_dict['insurer_d'][1],
                                     self.format_dict['insurer_d'][2], self.format_dict['insurer_d'][3])
        print('Insurer D: ' + insurer_d)
        insurer_e = self.pdf_extract(self.format_dict['insurer_e'][0], self.format_dict['insurer_e'][1],
                                     self.format_dict['insurer_e'][2], self.format_dict['insurer_e'][3])
        print('Insurer E: ' + insurer_e)
        insurer_f = self.pdf_extract(self.format_dict['insurer_f'][0], self.format_dict['insurer_f'][1],
                                     self.format_dict['insurer_f'][2], self.format_dict['insurer_f'][3])
        print('Insurer F: ' + insurer_f)
        print()
        insurer_dict = {'A': insurer_a, 'B': insurer_b, 'C': insurer_c, 'D': insurer_d, 'E': insurer_e, 'F': insurer_f}
        return insurer_dict

    # Finds and returns the agent name from the certificate. Result is returned as a string.
    def get_agent_name(self, coordinates):
        agent_name = self.pdf_extract(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        if agent_name == '':
            agent_name = '---'
        print('Agent Name: ' + agent_name)
        return agent_name

    # Finds and returns the agency/broker name from the certificate. Result is returned as a string.
    def get_agency_name(self, coordinates):
        agency_name_temp = self.pdf_extract(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        agency_name = ''
        for letter in agency_name_temp:
            if letter not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',']:
                agency_name += letter
            else:
                break
        if agency_name == '':
            agency_name = '---'
        print('Agency Name: ' + agency_name)
        return agency_name

    # Finds and returns the agents phone number from the certificate. Result is returned as a string.
    def get_agent_phone(self, coordinates):
        agent_phone = self.pdf_extract(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        if agent_phone == '':
            agent_phone = '---'
        print('Agent Phone: ' + agent_phone)
        return agent_phone

    # Finds and returns the agents email address from the certificate. Result is returned as a string.
    def get_agent_email(self, coordinates):
        agent_email = self.pdf_extract(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        if agent_email == '':
            agent_email = '---'
        print('Agent Email: ' + agent_email)
        return agent_email

    # Finds and returns the GL policy number from the certificate. Result is returned as a string.
    def get_gl_policy_number(self, coordinates):
        gl_number = self.pdf_extract(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        if gl_number[0:4] in ['X X ', 'x x ']:
            gl_number = gl_number[4:]
        if gl_number == '':
            gl_number = '---'
        print('GL Number: ' + gl_number)
        return gl_number

    # Finds and returns the GL effective date from the certificate. Result is returned as a string.
    def get_gl_eff_date(self, coordinates):
        gl_eff_date = self.pdf_extract(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        temp_date = gl_eff_date.split()
        gl_eff_date = self.read_dates(temp_date, 'eff')
        if gl_eff_date == '':
            gl_eff_date = '---'
        print('GL Eff Date: ' + gl_eff_date)
        return gl_eff_date

    # Finds and returns the GL expiration date from the certificate. Result is returned as a string.
    def get_gl_exp_date(self, coordinates):
        gl_exp_date = self.pdf_extract(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        temp_date = gl_exp_date.split()
        gl_exp_date = self.read_dates(temp_date, 'exp')
        if gl_exp_date == '':
            gl_exp_date = '---'
        print('GL Exp Date: ' + gl_exp_date)
        return gl_exp_date

    # Finds and returns the gl occurrence amount from the certificate. Result is returned as a string.
    def get_gl_each_occurrence(self, coordinates):
        gl_each_occurrence = self.pdf_extract(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        if gl_each_occurrence == '':
            gl_each_occurrence = '---'
        print('GL EO Amount: ' + gl_each_occurrence)
        return gl_each_occurrence

    # Finds and returns the gl op agg amount from the certificate. Result is returned as a string.
    def get_gl_op_agg(self, coordinates):
        gl_op_agg = self.pdf_extract(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        if gl_op_agg == '':
            gl_op_agg = '---'
        print('GL Op Agg: ' + gl_op_agg)
        return gl_op_agg

    # Finds and returns the gl insurer amount from the certificate. Result is returned as a string.
    def get_gl_insurer(self, coordinates, insurer_dict):
        gl_insurer = self.pdf_extract(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        if gl_insurer in ['A', 'B', 'C', 'D', 'E', 'F']:
            print('GL Insurer: ' + insurer_dict[gl_insurer])
            return insurer_dict[gl_insurer]
        else:
            return '---'

    # Finds and returns the al policy number from the certificate. Result is returned as a string.
    def get_al_policy_number(self, coordinates):
        al_pol_number = self.pdf_extract(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        if al_pol_number[0:4] in ['X X ', 'x x ']:
            al_pol_number = al_pol_number[4:]
        if al_pol_number == '':
            al_pol_number = '---'
        print('AL Number: ' + al_pol_number)
        return al_pol_number

    # Finds and returns the al effective date from the certificate. Result is returned as a string.
    def get_al_eff_date(self, coordinates):
        al_eff_date = self.pdf_extract(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        temp_date = al_eff_date.split()
        al_eff_date = self.read_dates(temp_date, 'eff')
        if al_eff_date == '':
            al_eff_date = '---'
        print('AL Eff Date: ' + al_eff_date)
        return al_eff_date

    # Finds and returns the expiration date from the certificate. Result is returned as a string.
    def get_al_exp_date(self, coordinates):
        al_exp_date = self.pdf_extract(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        temp_date = al_exp_date.split()
        al_exp_date = self.read_dates(temp_date, 'exp')
        if al_exp_date == '':
            al_exp_date = '---'
        print('AL Exp Date: ' + al_exp_date)
        return al_exp_date

    # Finds and returns the al combined limit from the certificate. Result is returned as a string.
    def get_al_comb_limit(self, coordinates):
        al_comb_limit = self.pdf_extract(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        if al_comb_limit == '':
            al_comb_limit = '---'
        print('AL Limit Amount: ' + al_comb_limit)
        return al_comb_limit

    # Finds and returns the al insurer from the certificate. Result is returned as a string.
    def get_al_insurer(self, coordinates, insurer_dict):
        al_insurer = self.pdf_extract(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        if al_insurer in ['A', 'B', 'C', 'D', 'E', 'F']:
            print('AL Insurer: ' + insurer_dict[al_insurer])
            return insurer_dict[al_insurer]
        else:
            return '---'

    # Finds and returns the umb policy number from the certificate. Result is returned as a string.
    def get_umb_pol_number(self, coordinates):
        umb_pol_number = self.pdf_extract(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        if umb_pol_number == '':
            umb_pol_number = '---'
        print('UMB Policy Number: ' + umb_pol_number)
        return umb_pol_number

    # Finds and returns umb effective date from the certificate. Result is returned as a string.
    def get_umb_eff_date(self, coordinates):
        umb_eff_date = self.pdf_extract(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        temp_date = umb_eff_date.split()
        umb_eff_date = self.read_dates(temp_date, 'eff')
        if umb_eff_date == '':
            umb_eff_date = '---'
        print('UMB Eff Date: ' + umb_eff_date)
        return umb_eff_date

    # Finds and returns the umb expiration date from the certificate. Result is returned as a string.
    def get_umb_exp_date(self, coordinates):
        umb_exp_date = self.pdf_extract(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        temp_date = umb_exp_date.split()
        umb_exp_date = self.read_dates(temp_date, 'exp')
        if umb_exp_date == '':
            umb_exp_date = '---'
        print('UMB Exp Date: ' + umb_exp_date)
        return umb_exp_date

    # Finds and returns the umb occurrence amount from the certificate. Result is returned as a string.
    def get_umb_each_occur(self, coordinates):
        umb_each_occur = self.pdf_extract(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        if umb_each_occur == '':
            umb_each_occur = '---'
        print('UMB Each Occur: ' + umb_each_occur)
        return umb_each_occur

    # Finds and returns the umb aggregate amount from the certificate. Result is returned as a string.
    def get_umb_aggregate(self, coordinates):
        umb_aggregate = self.pdf_extract(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        if umb_aggregate == '':
            umb_aggregate = '---'
        print('UMB Aggregate: ' + umb_aggregate)
        return umb_aggregate

    # Finds and returns the umb insurer from the certificate. Result is returned as a string.
    def get_umb_insurer(self, coordinates, insurer_dict):
        umb_insurer = self.pdf_extract(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        if umb_insurer in ['A', 'B', 'C', 'D', 'E', 'F']:
            print('UMB Insurer: ' + insurer_dict[umb_insurer])
            return insurer_dict[umb_insurer]
        else:
            return '---'

    # Finds and returns the wc policy number from the certificate. Result is returned as a string.
    def get_wc_pol_number(self, coordinates):
        wc_pol_number = self.pdf_extract(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        if wc_pol_number != '' and wc_pol_number[0] == 'X':
            wc_pol_number = wc_pol_number[2:]
            if wc_pol_number == '':
                wc_pol_number = '-'
        print('WC Policy Number: ' + wc_pol_number)
        return wc_pol_number

    # Finds and returns the wc effective date from the certificate. Result is returned as a string.
    def get_wc_eff_date(self, coordinates):
        wc_eff_date = self.pdf_extract(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        temp_date = wc_eff_date.split()
        wc_eff_date = self.read_dates(temp_date, 'eff')
        if wc_eff_date == '':
            wc_eff_date = '---'
        print('WC Eff Date: ' + wc_eff_date)
        return wc_eff_date

    # Finds and returns the wc expiration date from the certificate. Result is returned as a string.
    def get_wc_exp_date(self, coordinates):
        wc_exp_date = self.pdf_extract(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        temp_date = wc_exp_date.split()
        wc_exp_date = self.read_dates(temp_date, 'exp')
        if wc_exp_date == '':
            wc_exp_date = '---'
        print('WC Exp Date: ' + wc_exp_date)
        return wc_exp_date

    # Finds and returns the wc each accident amount from the certificate. Result is returned as a string.
    def get_wc_each_acci(self, coordinates):
        wc_each_acci = self.pdf_extract(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        if wc_each_acci == '':
            wc_each_acci = '---'
        print('WC Each Acci: ' + wc_each_acci)
        return wc_each_acci

    # Finds and returns the wc each employee amount from the certificate. Result is returned as a string.
    def get_wc_each_emp(self, coordinates):
        wc_each_emp = self.pdf_extract(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        if wc_each_emp == '':
            wc_each_emp = '---'
        print('WC Each Employee: ' + wc_each_emp)
        return wc_each_emp

    # Finds and returns the wc policy limit from the certificate. Result is returned as a string.
    def get_wc_pol_limit(self, coordinates):
        wc_pol_limit = self.pdf_extract(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        if wc_pol_limit == '':
            wc_pol_limit = '---'
        print('WC Policy Limit: ' + wc_pol_limit)
        return wc_pol_limit

    # Finds and returns the wc insurer from the certificate. Result is returned as a string.
    def get_wc_insurer(self, coordinates, insurer_dict):
        wc_insurer = self.pdf_extract(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        if wc_insurer in ['A', 'B', 'C', 'D', 'E', 'F']:
            print('WC Insurer: ' + insurer_dict[wc_insurer])
            return insurer_dict[wc_insurer]
        else:
            return '---'

    def set_requirements_default(self):
        self.results['gl_additional_insured'] = False
        self.results['gl_pnc'] = False
        self.results['gl_contractual_liab'] = False
        self.results['al_any_auto'] = False
        self.results['al_additional_insured'] = False
        self.results['al_pnc'] = False
        self.results['wc_wos'] = False

    # Detects how the agent entered the dates on the certificate. If the format entered is not mm/dd/yyyy then this
    # method will correct it while keeping the date the same.
    def read_dates(self, temp_date, operation):
        list_item = 0
        contained_dates = []
        while True:
            try:
                temp = temp_date[list_item]
                if len(temp) == 8 or len(temp) == 9:
                    temp = self.format_dates(temp)
                if temp[0:2].isdigit():
                    if temp[2] in ['/', '-']:
                        if temp[3:5].isdigit():
                            if temp[5] in ['/', '-']:
                                if temp[6:].isdigit():
                                    contained_dates.append(temp)
                                    if (list_item + 1) == len(temp_date):
                                        break
                                    else:
                                        if (list_item + 1) == len(temp_date):
                                            break
                                        else:
                                            list_item += 1
                                else:
                                    if (list_item + 1) == len(temp_date):
                                        break
                                    else:
                                        list_item += 1
                            else:
                                if (list_item + 1) == len(temp_date):
                                    break
                                else:
                                    list_item += 1
                        else:
                            if (list_item + 1) == len(temp_date):
                                break
                            else:
                                list_item += 1
                    else:
                        if (list_item + 1) == len(temp_date):
                            break
                        else:
                            list_item += 1
                else:
                    if (list_item + 1) == len(temp_date):
                        break
                    else:
                        list_item += 1
            except IndexError:
                break
        if contained_dates:
            if len(contained_dates) > 1:
                if operation == 'eff':
                    result_date = contained_dates[0]
                else:
                    result_date = contained_dates[1]
            else:
                result_date = contained_dates[0]
        else:
            result_date = ''
        return result_date

    # Assists the read dates method by changing the date format from mm-dd-yyyy to mm/dd/yyyy
    @staticmethod
    def format_dates(date):
        counter = 0
        change_1 = False
        change_2 = False
        temp_formatted_1 = ''
        temp_formatted_2 = ''
        for i in date:
            counter += 1
            if counter == 3 and i not in ['/', '-']:
                temp_formatted_1 = '0' + date
                change_1 = True
                break
        if not change_1:
            temp_formatted_1 = date
        counter = 0
        for i in temp_formatted_1:
            counter += 1
            if counter == 6 and i not in ['/', '-']:
                temp_formatted_2 = temp_formatted_1[0:3] + '0' + temp_formatted_1[3:]
                change_2 = True
                break
        if not change_2:
            temp_formatted_2 = temp_formatted_1
        return temp_formatted_2
