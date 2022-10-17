from re import X
from time import sleep
from xpath_map import XpathMap
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from subprocess import CREATE_NO_WINDOW

class ChromeDriver:

    def __init__(self):
        self.driver = self.chromedriver_setup()
        self.actions = self.actionchains_setup()
        self.map = XpathMap()
        self.operation_map = {}
        self.open_riskonnect()

    def chromedriver_setup(self):
        my_options = webdriver.ChromeOptions()
        my_options.add_argument('user-data-dir=C:/Users/driggerst/Python/CertHelper/User Data')
        chrome_service = ChromeService('C:/Users/driggerst/Python/CertHelper/chromedriver.exe')
        chrome_service.creationflags = CREATE_NO_WINDOW
        driver_Setup = webdriver.Chrome(options=my_options, 
                                        executable_path='C:/Users/driggerst/Python/CertHelper'
                                                        '/chromedriver.exe',
                                        service=chrome_service)
        return driver_Setup

    def actionchains_setup(self):
        actions = ActionChains(self.driver)
        return actions

    def switch_tab_to_1(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def switch_tab_to_2(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def switch_tab_to_3(self):
        self.driver.switch_to.window(self.driver.window_handles[2])

    def close_current_tab(self):
        self.driver.close()

    def open_riskonnect(self):
        self.driver.get('https://riskonnectvmc.lightning.force.com/lightning/page/home')
        login_button_element = self.driver.find_element(By.XPATH, self.map.basics['login_button'])
        login_button_element.click()

    def load_vendor(self, parser_results):
        search_button_element = self.driver.find_element(By.XPATH, self.map.basics['search_button'])
        search_button_element.click()
        sleep(0.5)
        search_bar_element = self.driver.find_element(By.XPATH, self.map.basics['search_bar'])
        search_bar_element.send_keys(parser_results['vendor_name'])
        search_bar_element.send_keys(Keys.ENTER)
        WebDriverWait(self.driver, 20).until(ec.presence_of_element_located((By.XPATH, self.map.basics['search_result_first'])))
        first_result_element = self.driver.find_element(By.XPATH, self.map.basics['search_result_first'])
        self.actions.key_down(Keys.CONTROL).perform()
        self.actions.click(first_result_element).perform()
        self.actions.key_up(Keys.CONTROL).perform()
        self.home_button_element = self.driver.find_element(By.XPATH, self.map.basics['home_button'])
        self.home_button_element.click()
        self.switch_tab_to_2()
        WebDriverWait(self.driver, 20).until(ec.presence_of_element_located((By.XPATH, self.map.basics['coi_page_button'])))
        self.coi_button = self.driver.find_element(By.XPATH, self.map.basics['coi_page_button'])
        self.coi_button.click()

    def determine_operation_type(self):
        tier_1_check = self.driver.find_elements(By.XPATH, self.map.basics['tier_1_check'])
        tier_2_check = self.driver.find_elements(By.XPATH, self.map.basics['tier_2_check'])
        if tier_1_check:
            print('Operation Detected: Tier 1\n')
            self.operation_map = self.map.map_tier1_renew
        elif tier_2_check:
            print('Operation Detected: Tier 2\n')
            self.operation_map = self.map.map_tier2_renew
        else:
            raise Exception('Unable to detect operation, please try again\n')

    def submit_agent(self, parser_results):
        if parser_results['agent_name'] != '---':
            click_button_element = self.driver.find_element(By.XPATH, self.operation_map['click_box'])
            click_button_element.click()
            sleep(0.5)
            agent_name_element = self.driver.find_element(By.XPATH, self.operation_map['agent_name'])
            agent_name_element.clear()
            agent_name_element.send_keys(parser_results['agent_name'])

    def submit_agency(self, parser_results):
        if parser_results['agency_name'] != '---':
            agency_name_element = self.driver.find_element(By.XPATH, self.operation_map['agency_name'])
            agency_name_element.clear()
            agency_name_element.send_keys(parser_results['agency_name'])

    def submit_agent_phone(self, parser_results):
        if parser_results['agent_phone'] != '---':
            agent_phone_element = self.driver.find_element(By.XPATH, self.operation_map['agent_phone'])
            agent_phone_element.clear()
            agent_phone_element.send_keys(parser_results['agent_phone'])

    def submit_agent_email(self, parser_results):
        if parser_results['agent_email'] != '---':
            agent_email_element = self.driver.find_element(By.XPATH, self.operation_map['agent_email'])
            agent_email_element.clear()
            agent_email_element.send_keys(parser_results['agent_email'])

    def submit_gl_number(self, parser_results):
        locator = self.driver.find_element(By.XPATH, self.operation_map['gl_locator'])
        self.actions.move_to_element(locator).perform()
        if parser_results['gl_pol_number'] != '---':
            gl_pol_number_element = self.driver.find_element(By.XPATH, self.operation_map['gl_pol_number'])
            gl_pol_number_element.clear()
            gl_pol_number_element.send_keys(parser_results['gl_pol_number'])

    def submit_gl_eff_date(self, parser_results):
        if parser_results['gl_eff_date'] != '---':
            gl_eff_date_element = self.driver.find_element(By.XPATH, self.operation_map['gl_eff_date'])
            gl_eff_date_element.clear()
            gl_eff_date_element.send_keys(parser_results['gl_eff_date'])

    def submit_gl_exp_date(self, parser_results):
        if parser_results['gl_exp_date'] != '---':
            gl_exp_date_element = self.driver.find_element(By.XPATH, self.operation_map['gl_exp_date'])
            gl_exp_date_element.clear()
            gl_exp_date_element.send_keys(parser_results['gl_exp_date'])

    def submit_gl_each_occur(self, parser_results):
        if parser_results['gl_each_occur'] != '---':
            gl_each_occur_element = self.driver.find_element(By.XPATH, self.operation_map['gl_each_occur'])
            gl_each_occur_element.clear()
            gl_each_occur_element.send_keys(parser_results['gl_each_occur'])

    def submit_gl_op_agg(self, parser_results):
        if parser_results['gl_op_agg'] != '---':
            gl_op_agg_element = self.driver.find_element(By.XPATH, self.operation_map['gl_op_agg'])
            gl_op_agg_element.clear()
            gl_op_agg_element.send_keys(parser_results['gl_op_agg'])

    def submit_gl_additional_insured(self, parser_results):
        gl_additional_element = self.driver.find_element(By.XPATH, self.operation_map['gl_additional_insured'])
        gl_additional_element.click()
        sleep(0.2)
        if parser_results['gl_additional_insured']:
            gl_additional_element.send_keys('y')
            sleep(0.2)
            gl_additional_element.send_keys(Keys.ENTER)
        else:
            gl_additional_element.send_keys('n')
            sleep(0.2)
            gl_additional_element.send_keys(Keys.ENTER)
        sleep(0.2)

    def submit_gl_pnc(self, parser_results):
        gl_pnc_element = self.driver.find_element(By.XPATH, self.operation_map['gl_pnc'])
        gl_pnc_element.click()
        sleep(0.2)
        if parser_results['gl_pnc']:
            gl_pnc_element.send_keys('y')
            sleep(0.2)
            gl_pnc_element.send_keys(Keys.ENTER)
        else:
            gl_pnc_element.send_keys('n')
            sleep(0.2)
            gl_pnc_element.send_keys(Keys.ENTER)
        sleep(0.2)

    def submit_gl_contractual_liab(self, parser_results):
        gl_contractual_liab_element = self.driver.find_element(By.XPATH, self.operation_map['gl_contractual_liab'])
        gl_contractual_liab_element.click()
        sleep(0.2)
        if parser_results['gl_contractual_liab']:
            gl_contractual_liab_element.send_keys('y')
            sleep(0.2)
            gl_contractual_liab_element.send_keys(Keys.ENTER)
        else:
            gl_contractual_liab_element.send_keys('n')
            sleep(0.2)
            gl_contractual_liab_element.send_keys(Keys.ENTER)
        sleep(0.2)

    def submit_gl_insurer(self, parser_results):
        if parser_results['gl_insurer'] != '---':
            gl_insurer_element = self.driver.find_element(By.XPATH, self.operation_map['gl_insurer'])
            gl_insurer_element.clear()
            gl_insurer_element.send_keys(parser_results['gl_insurer'])

    def submit_al_number(self, parser_results):
        locator = self.driver.find_element(By.XPATH, self.operation_map['al_locator'])
        self.actions.move_to_element(locator).perform()
        if parser_results['al_pol_number'] != '---':
            al_pol_number_element = self.driver.find_element(By.XPATH, self.operation_map['al_pol_number'])
            al_pol_number_element.clear()
            al_pol_number_element.send_keys(parser_results['al_pol_number'])

    def submit_al_eff_date(self, parser_results):
        if parser_results['al_eff_date'] != '---':
            al_eff_date_element = self.driver.find_element(By.XPATH, self.operation_map['al_eff_date'])
            al_eff_date_element.clear()
            al_eff_date_element.send_keys(parser_results['al_eff_date'])

    def submit_al_exp_date(self, parser_results):
        if parser_results['al_exp_date'] != '---':
            al_exp_date_element = self.driver.find_element(By.XPATH, self.operation_map['al_exp_date'])
            al_exp_date_element.clear()
            al_exp_date_element.send_keys(parser_results['al_exp_date'])

    def submit_al_comb_limit(self, parser_results):
        if parser_results['al_comb_limit'] != '---':
            al_comb_limit_element = self.driver.find_element(By.XPATH, self.operation_map['al_comb_limit'])
            al_comb_limit_element.clear()
            al_comb_limit_element.send_keys(parser_results['al_comb_limit'])

    def submit_al_any_auto(self, parser_results):
        al_any_auto_element = self.driver.find_element(By.XPATH, self.operation_map['al_any_auto'])
        al_any_auto_element.click()
        sleep(0.2)
        if parser_results['al_any_auto']:
            al_any_auto_element.send_keys('y')
            sleep(0.2)
            al_any_auto_element.send_keys(Keys.ENTER)
        else:
            al_any_auto_element.send_keys('n')
            sleep(0.2)
            al_any_auto_element.send_keys(Keys.ENTER)
        sleep(0.2)

    def submit_al_additional_insured(self, parser_results):
        al_additional_element = self.driver.find_element(By.XPATH, self.operation_map['al_additional_insured'])
        al_additional_element.click()
        sleep(0.2)
        if parser_results['al_additional_insured']:
            al_additional_element.send_keys('y')
            sleep(0.2)
            al_additional_element.send_keys(Keys.ENTER)
        else:
            al_additional_element.send_keys('n')
            sleep(0.2)
            al_additional_element.send_keys(Keys.ENTER)
        sleep(0.2)

    def submit_al_pnc(self, parser_results):
        al_pnc_element = self.driver.find_element(By.XPATH, self.operation_map['al_pnc'])
        al_pnc_element.click()
        sleep(0.2)
        if parser_results['al_pnc']:
            al_pnc_element.send_keys('y')
            sleep(0.2)
            al_pnc_element.send_keys(Keys.ENTER)
        else:
            al_pnc_element.send_keys('n')
            sleep(0.2)
            al_pnc_element.send_keys(Keys.ENTER)
        sleep(0.2)

    def submit_al_insurer(self, parser_results):
        if parser_results['al_insurer'] != '---':
            al_insurer_element = self.driver.find_element(By.XPATH, self.operation_map['al_insurer'])
            al_insurer_element.clear()
            al_insurer_element.send_keys(parser_results['al_insurer'])

    def submit_umb_number(self, parser_results):
        locator = self.driver.find_element(By.XPATH, self.operation_map['umb_locator'])
        self.actions.move_to_element(locator).perform()
        if parser_results['umb_pol_number'] != '---':
            umb_pol_number_element = self.driver.find_element(By.XPATH, self.operation_map['umb_pol_number'])
            umb_pol_number_element.clear()
            umb_pol_number_element.send_keys(parser_results['umb_pol_number'])

    def submit_umb_eff_date(self, parser_results):
        if parser_results['umb_eff_date'] != '---':
            umb_eff_date_element = self.driver.find_element(By.XPATH, self.operation_map['umb_eff_date'])
            umb_eff_date_element.clear()
            umb_eff_date_element.send_keys(parser_results['umb_eff_date'])

    def submit_umb_exp_date(self, parser_results):
        if parser_results['umb_exp_date'] != '---':
            umb_exp_date_element = self.driver.find_element(By.XPATH, self.operation_map['umb_exp_date'])
            umb_exp_date_element.clear()
            umb_exp_date_element.send_keys(parser_results['umb_exp_date'])

    def submit_umb_each_occur(self, parser_results):
        if parser_results['umb_each_occur'] != '---':
            umb_comb_limit_element = self.driver.find_element(By.XPATH, self.operation_map['umb_each_occur'])
            umb_comb_limit_element.clear()
            umb_comb_limit_element.send_keys(parser_results['umb_each_occur'])

    def submit_umb_aggregate(self, parser_results):
        if parser_results['umb_aggregate'] != '---':
            umb_aggregate_element = self.driver.find_element(By.XPATH, self.operation_map['umb_aggregate'])
            umb_aggregate_element.clear()
            umb_aggregate_element.send_keys(parser_results['umb_aggregate'])

    def submit_umb_insurer(self, parser_results):
        if parser_results['umb_insurer'] != '---':
            umb_insurer_element = self.driver.find_element(By.XPATH, self.operation_map['umb_insurer'])
            umb_insurer_element.clear()
            umb_insurer_element.send_keys(parser_results['umb_insurer'])

    def submit_wc_number(self, parser_results):
        locator = self.driver.find_element(By.XPATH, self.operation_map['wc_locator'])
        self.actions.move_to_element(locator).perform()
        if parser_results['wc_pol_number'] != '---':
            wc_pol_number_element = self.driver.find_element(By.XPATH, self.operation_map['umb_pol_number'])
            wc_pol_number_element.clear()
            wc_pol_number_element.send_keys(parser_results['wc_pol_number'])

    def submit_wc_eff_date(self, parser_results):
        if parser_results['wc_eff_date'] != '---':
            umb_wc_date_element = self.driver.find_element(By.XPATH, self.operation_map['wc_eff_date'])
            umb_wc_date_element.clear()
            umb_wc_date_element.send_keys(parser_results['wc_eff_date'])

    def submit_wc_exp_date(self, parser_results):
        if parser_results['wc_exp_date'] != '---':
            submit_wc_exp_date = self.driver.find_element(By.XPATH, self.operation_map['wc_exp_date'])
            submit_wc_exp_date.clear()
            submit_wc_exp_date.send_keys(parser_results['wc_exp_date'])

    def submit_wc_each_acci(self, parser_results):
        if parser_results['wc_each_acci'] != '---':
            wc_each_acci_element = self.driver.find_element(By.XPATH, self.operation_map['wc_each_acci'])
            wc_each_acci_element.clear()
            wc_each_acci_element.send_keys(parser_results['wc_each_acci'])

    def submit_wc_each_emp(self, parser_results):
        if parser_results['wc_each_emp'] != '---':
            wc_each_emp = self.driver.find_element(By.XPATH, self.operation_map['wc_each_emp'])
            wc_each_emp.clear()
            wc_each_emp.send_keys(parser_results['wc_each_emp'])

    def submit_wc_pol_limit(self, parser_results):
        if parser_results['wc_pol_limit'] != '---':
            wc_pol_limit = self.driver.find_element(By.XPATH, self.operation_map['wc_pol_limit'])
            wc_pol_limit.clear()
            wc_pol_limit.send_keys(parser_results['wc_pol_limit'])

    def submit_wc_wos(self, parser_results):
        wc_wos_element = self.driver.find_element(By.XPATH, self.operation_map['wc_wos'])
        wc_wos_element.click()
        sleep(0.2)
        if parser_results['wc_wos']:
            wc_wos_element.send_keys('y')
            sleep(0.2)
            wc_wos_element.send_keys(Keys.ENTER)
        else:
            wc_wos_element.send_keys('n')
            sleep(0.2)
            wc_wos_element.send_keys(Keys.ENTER)
        sleep(0.2)

    def submit_wc_insurer(self, parser_results):
        if parser_results['wc_insurer'] != '---':
            wc_insurer_element = self.driver.find_element(By.XPATH, self.operation_map['wc_insurer'])
            wc_insurer_element.clear()
            wc_insurer_element.send_keys(parser_results['wc_insurer'])

    def save_and_submit(self):
        save_button_element = self.driver.find_element(By.XPATH, self.map.basics['save_button'])
        save_button_element.click()
    # ----------------------------------------------------------------------------------- 

    def submit_to_rk(self, parser_results):
        self.determine_operation_type()
        self.submit_agent(parser_results)
        self.submit_agency(parser_results)
        self.submit_agent_phone(parser_results)
        self.submit_agent_email(parser_results)
        self.submit_gl_number(parser_results)
        self.submit_gl_eff_date(parser_results)
        self.submit_gl_exp_date(parser_results)
        self.submit_gl_each_occur(parser_results)
        self.submit_gl_op_agg(parser_results)
        self.submit_gl_additional_insured(parser_results)
        self.submit_gl_pnc(parser_results)
        self.submit_gl_contractual_liab(parser_results)
        self.submit_gl_insurer(parser_results)
        self.submit_al_number(parser_results)
        self.submit_al_eff_date(parser_results)
        self.submit_al_exp_date(parser_results)
        self.submit_al_comb_limit(parser_results)
        self.submit_al_any_auto(parser_results)
        self.submit_al_additional_insured(parser_results)
        self.submit_al_pnc(parser_results)
        self.submit_al_insurer(parser_results)
        self.submit_umb_number(parser_results)
        self.submit_umb_eff_date(parser_results)
        self.submit_umb_exp_date(parser_results)
        self.submit_umb_each_occur(parser_results)
        self.submit_umb_aggregate(parser_results)
        self.submit_umb_insurer(parser_results)
        self.submit_wc_number(parser_results)
        self.submit_wc_eff_date(parser_results)
        self.submit_wc_exp_date(parser_results)
        self.submit_wc_each_acci(parser_results)
        self.submit_wc_each_emp(parser_results)
        self.submit_wc_pol_limit(parser_results)
        self.submit_wc_wos(parser_results)
        self.submit_wc_insurer(parser_results)
        self.save_and_submit()
