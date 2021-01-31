from selenium.webdriver import Chrome
from selenium.webdriver import ActionChains
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import os
import time
import inspect
import getpass
import logging
from logging_module import logger
import pathlib


user_name = getpass.getuser()
RESULT = os.path.join("C:\\","Users",user_name, "PycharmProjects","logitech_automation", "results")

#log = logging.basicConfig(filename=debug_file, level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - '
#                                                                           '%(message)s')


class Scenario_1:
    def __init__(self, chrome_path, home_page):
        self.chrome_path = chrome_path
        self.home_page = home_page
        #self.log = logging.getLogger(__name__)
        self.logger = logger.get_logger()

    def t1_verify_form_authentication(self):
        '''
        function to verify the 'Form Authentication'
        :return: Returns boolean value
        '''
        try:
            browser = Chrome(self.chrome_path)
            ins_obj = inspect.currentframe()
            func_name = inspect.getframeinfo(ins_obj).function
            ss_file = RESULT + "\\" + func_name + "_" + str(time.time()).split('.')[0] + ".png"
            browser.get(self.home_page)
            browser.find_element_by_link_text("Form Authentication").click()
            html = browser.page_source
            cred = re.search(r'Enter\s<em>(.*?)<.*and.*<em>(.*?)<.*password', html)
            user_name = cred.group(1)
            pass_word = cred.group(2)
            browser.find_element_by_id("username").send_keys(user_name)
            browser.find_element_by_id("password").send_keys(pass_word)
            browser.find_element_by_class_name("radius").click()
            expected_text = "You logged into a secure area!"
            if expected_text in browser.page_source:
                self.logger.info("Login Successful to Form Authentication")
                browser.save_screenshot(ss_file)
                browser.close()
                return True
            else:
                self.logger.error("Login to Form Authentication Failed")
                raise Exception

        except Exception as err:
            self.logger.error(err)
            return False

    def t2_verify_dynamic_loading(self):
        '''
        function to verify the 'Dynamic Loading'
        :return: Returns boolean value
        '''
        try:
            browser = Chrome(self.chrome_path)
            ss_file = RESULT + "\\" + self.t2_verify_dynamic_loading.__name__ + "_" + str(time.time()).split('.')[0] + \
                      ".png"
            browser.get(self.home_page)
            browser.find_element_by_link_text("Dynamic Loading").click()
            browser.find_element_by_link_text("Example 2: Element rendered after the fact").click()
            browser.find_element_by_xpath('//*[@id ="start"]/button').click()
            expected_msg = 'Hello World!'
            element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "finish")))
            if expected_msg in browser.page_source:
                self.logger.info("Dynamic Loading Verified")
                browser.save_screenshot(ss_file)
                browser.close()
                return True
            else:
                self.logger.error("Dynamic Loading is not Verified")
                raise Exception
        except Exception as err:
            self.logger.error(err)
            return False

    def t3_verify_multiple_windows(self):
        '''
                function to verify the 'Multiple Windows'
                :return: Returns boolean value
                '''
        try:
            browser = Chrome(self.chrome_path)
            browser.get(self.home_page)
            browser.find_element_by_link_text("Multiple Windows").click()
            browser.find_element_by_link_text("Click Here").click()
            for handle in browser.window_handles:
                if handle != self.home_page:
                    new_page = handle
            browser.switch_to.window(new_page)
            self.logger.info("The URL of new window opened : {}".format(browser.current_url))
            browser.close()
            browser.switch_to.window(browser.window_handles[0])
            self.logger.info("The title of current window : {}".format(browser.title))
            browser.close()
            return True
        except Exception as err:
            self.logger.error(err)
            return False

    def t4_verify_drag_drop(self):
        '''
                function to verify the 'Drag and Drop'
                :return: Returns boolean value
                '''
        try:
            browser = Chrome(self.chrome_path)
            ins_obj = inspect.currentframe()
            func_name = inspect.getframeinfo(ins_obj).function
            print(func_name)
            ss_file = RESULT + "\\" + func_name + "_" + str(time.time()).split('.')[0] + ".png"
            browser.get(self.home_page)
            browser.find_element_by_link_text("Drag and Drop").click()
            source1 = browser.find_element_by_xpath('//*[@id ="column-a"]')
            target1 = browser.find_element_by_xpath('//*[@id ="column-b"]')
            action = ActionChains(browser)
            action.drag_and_drop(source1, target1).perform()
            self.drag_and_drop(browser, source1, target1)
            browser.save_screenshot(ss_file)
            self.logger.info("Drag and Drop verified successfully")
            browser.close()
            return True
        except Exception as err:
            self.logger.error(err)
            return False

    def t5_verify_frames(self):
        '''
                function to verify the 'Drag and Drop'
                :return: Returns boolean value
                '''
        try:
            browser = Chrome(self.chrome_path)
            ins_obj = inspect.currentframe()
            func_name = inspect.getframeinfo(ins_obj).function
            print(func_name)
            ss_file = RESULT + "\\" + func_name + "_" + str(time.time()).split('.')[0] + ".png"
            browser.get(self.home_page)
            browser.find_element_by_link_text("Frames").click()
            browser.find_element_by_link_text("iFrame").click()
            time.sleep(1)
            inputElement = browser.find_element_by_id("mce_0_ifr")
            inputElement.click()
            inputElement.send_keys(Keys.CONTROL, 'a')
            inputElement.send_keys(Keys.DELETE)
            inputElement.send_keys('Test is Successful')
            inputElement.send_keys(Keys.CONTROL, 'a')
            browser.find_element_by_xpath('//*[@id="content"]/div/div/div[1]/div[1]/div[2]/div/div[3]/button['
                                          '1]').click()
            inputElement.click()
            self.logger.info("Frames Verified")
            browser.save_screenshot(ss_file)
            browser.close()
            return True
        except Exception as err:
            self.logger.error(err)
            return False

    def t6_verify_javascript_alerts(self, text):
        '''
                function to verify the 'JavaScript Alerts'
                :return: Returns boolean value
                '''
        try:
            browser = Chrome(self.chrome_path)
            ins_obj = inspect.currentframe()
            func_name = inspect.getframeinfo(ins_obj).function
            print(func_name)
            ss_file = RESULT + "\\" + func_name + "_" + str(time.time()).split('.')[0] + ".png"
            browser.get(self.home_page)
            browser.find_element_by_link_text("JavaScript Alerts").click()
            browser.find_element_by_xpath('//*[@id="content"]/div/ul/li[2]/button').click()
            WebDriverWait(browser, 10).until(EC.alert_is_present())
            browser.switch_to.alert.dismiss()
            if text in browser.page_source:
                self.logger.info("Alert Verified Successfully")
                browser.close()
                return True
            else:
                self.logger.error("Alert verification Failed")
                browser.close()
                raise Exception

        except Exception as err:
            self.logger.error(err)
            return False

    def drag_and_drop(self, driver, source, target=None, offsetX=0, offsetY=0, delay=25, key=None):
        JS_DRAG_AND_DROP = "var t=arguments,e=t[0],n=t[1],i=t[2]||0,o=t[3]||0,r=t[4]||1,a=t[5]||'',s='alt'===a||'\ue00a'===a,l='ctrl'===a||'\ue009'===a,c='shift'===a||'\ue008'===a,u=e.ownerDocument,f=e.getBoundingClientRect(),g=n?n.getBoundingClientRect():f,p=f.left+f.width/2,d=f.top+f.height/2,h=g.left+(i||g.width/2),m=g.top+(o||g.height/2),v=u.elementFromPoint(p,d),y=u.elementFromPoint(h,m);if(!v||!y){var E=new Error('source or target element is not interactable');throw E.code=15,E}var _={constructor:DataTransfer,effectAllowed:null,dropEffect:null,types:[],files:Object.setPrototypeOf([],null),_items:Object.setPrototypeOf([],{add:function(t,e){this[this.length]={_data:''+t,kind:'string',type:e,getAsFile:function(){},getAsString:function(t){t(this._data)}},_.types.push(e)},remove:function(t){Array.prototype.splice.call(this,65535&t,1),_.types.splice(65535&t,1)},clear:function(t,e){this.length=0,_.types.length=0}}),setData:function(t,e){this.clearData(t),this._items.add(e,t)},getData:function(t){for(var e=this._items.length;e--&&this._items[e].type!==t;);return e>=0?this._items[e]._data:null},clearData:function(t){for(var e=this._items.length;e--&&this._items[e].type!==t;);this._items.remove(e)},setDragImage:function(t){}};function w(t,e,n,i){for(var o=0;o<e.length;++o){var r=u.createEvent('MouseEvent');r.initMouseEvent(e[o],!0,!0,u.defaultView,0,0,0,p,d,l,s,c,!1,0,null),t.dispatchEvent(r)}i&&setTimeout(i,n)}function D(t,e,n,i){var o=u.createEvent('DragEvent');o.initMouseEvent(e,!0,!0,u.defaultView,0,0,0,p,d,l,s,c,!1,0,null),Object.setPrototypeOf(o,null),o.dataTransfer=_,Object.setPrototypeOf(o,DragEvent.prototype),t.dispatchEvent(o),i&&setTimeout(i,n)}'items'in DataTransfer.prototype&&(_.items=_._items),w(v,['pointerdown','mousedown'],1,function(){for(var t=v;t&&!t.draggable;)t=t.parentElement;if(t&&t.contains(v)){var e=y.getBoundingClientRect();D(v,'dragstart',r,function(){var t=y.getBoundingClientRect();p=t.left+h-e.left,d=t.top+m-e.top,D(y,'dragenter',1,function(){D(y,'dragover',r,function(){D(u.elementFromPoint(p,d),'drop',1,function(){D(v,'dragend',1,function(){w(u.elementFromPoint(p,d),['mouseup','pointerup'])})})})})})}})"
        driver.execute_script(JS_DRAG_AND_DROP, source, target, offsetX, offsetY, delay, key)
        time.sleep(delay * 2 / 1000)


class Scenario_2(Scenario_1):
    def __init__(self, chrome_path, home_page):
        self.home_page = home_page
        super().__init__(chrome_path, self.home_page)

    def launch_naukri_app(self):
        '''
        :return:
        '''
        try:
            comp_names = []
            browser = Chrome(self.chrome_path)
            browser.get(self.home_page)
            for x in range(1, len(browser.window_handles)):
                browser.switch_to.window(browser.window_handles[x])
                comp_names.append(re.search(r'.*popups\/(.*?)\/', browser.page_source).group(1))
            self.logger.info('company name to be verified : {}'.format(comp_names[0]))
            for x in range(1, len(browser.window_handles)):
                browser.switch_to.window(browser.window_handles[x])
                if comp_names[0].upper() == browser.title:
                    self.logger.info('Passed: company name {} and  pop-up window title matched'.format(comp_names[0]))
                    browser.close()
                    browser.quit()
                    return True
        except Exception as err:
            self.logger.error(err)
            return False
