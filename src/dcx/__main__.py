import base64
import os
import sys
import os.path
import logging
import json
import time
import traceback
import subprocess
import datetime

from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.chrome.options import Options as CHOptions
from selenium.webdriver.edge.options import Options as EDOptions
from selenium import webdriver

from selenium.webdriver.common.keys import Keys as KEYS
from selenium.webdriver.common.by import By as BY

from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support.ui import Select as SEL
from selenium.webdriver.support import expected_conditions as EC

from urllib.parse import urlparse

import selenium
#from selenium.webdriver.firefox.firefox_profile import FirefoxProfile as FFProfile


FORMAT = '%(asctime)s+00:00 %(levelname)10s: %(message)-80s    (%(filename)s,%(funcName)s:%(lineno)s)'
logging.basicConfig(level=logging.INFO, format=FORMAT)
logging.Formatter.converter = time.gmtime


default_wait = 30


opts = FFOptions()
opts.add_argument("-devtools")
opts.set_preference('media.mediasource.enabled', False)

#opts.add_argument("-jsconsole")



#opts = EDOptions()
#opts = CHOptions()

#driver = webdriver.Remote(command_executor="http://127.0.0.1:4444/wd/hub", options=opts)

driver_mode = "firefox-local"
driver = webdriver.Firefox(options=opts)


logbasedir = os.path.join("log", driver_mode, datetime.datetime.today().strftime("%Y-%m-%d-%H%M%S"))
os.makedirs(logbasedir, exist_ok=False)

logdir_reg = os.path.join(logbasedir, "reg")
os.makedirs(logdir_reg, exist_ok=False)

logdir_viewport_img = os.path.join(logbasedir, "viewport-img")
os.makedirs(logdir_viewport_img, exist_ok=False)

logdir_full_img = os.path.join(logbasedir, "full-img")
os.makedirs(logdir_full_img, exist_ok=False)


reg_activity_log = {}

def reg_write(k, v):
    if not k in reg_activity_log.keys():
        reg_activity_log[k] = len(reg_activity_log.keys())
    with open(os.path.join(logdir_reg, k), 'w') as f:
        f.write(v)

def reg_read(k):
    with open(os.path.join(logdir_reg, k), 'r') as f:
        return f.read()

def content_provider_facade(src, provider_name=""):
    if "+" in provider_name:
        provider_chain = provider_name.split("+")
        for ci in provider_chain:
            src = content_provider_facade(src, ci)
        return src
    if provider_name == "":
        return src
    if provider_name == "bash":
        return subprocess.check_output("""/bin/bash -c '%s'""" % src, shell=True, universal_newlines=True)
    if provider_name == "env":
        for k in envdata.keys():
            kstring = "$" + k
            src = src.replace(kstring, envdata[k])
        return src


def get_all_a_href(min_slashes=0, beneath=None):
    all_href={}
    all_a = driver.find_elements(BY.XPATH, "//a")
    if beneath is not None:
        all_a = beneath.find_elements(BY.XPATH, ".//a")
    for a in all_a:
        href = a.get_attribute("href")
        ac = ['_' for x in href if x=="/"]
        if len(ac) >= min_slashes:
            all_href[href] = True
    return sorted(list(all_href.keys()))


def break_handler(data):
    if data == "?":
        print("")
        print("HELP")
        print("")
    if data == "d":
        b = driver.find_element(BY.XPATH, "//body")
        with open("BODY", "w") as bf:
            bf.write(b.get_attribute("innerHTML"))

        # with open("A", "w") as af:
        #     af.write("\n".join(get_all_a_href(5)))


        pass
        #debug dev
        # vids = driver.find_elements(BY.XPATH, "//video/source")
        # for v in vids:
        #     print(v)
        #     print("_%s_" % v.get_attribute("src"))
        #     print("===")
    if data == "h":
        print("href=%s" % driver.execute_script('return location.href;'))
    if data == "r":
        print("Dumping registry: %d entries" % len(reg_activity_log))
        for x in reg_activity_log.keys():
            print("  %s = %s" % (x, reg_read(x)))
    if data == "q":
        print("QUIT")
        driver.quit()
        sys.exit(0)

# src=["b", "n"], l=2, idx=1
def expand_column(src, idx):
    content = src[idx]
    if idx+1 <= len(src)-1:
        content = content_provider_facade(content, src[idx+1])
    return content


envdata = {}

if os.path.isfile("play.js"):

    if os.path.isfile("play.env"):
        envlines = [l.strip() for l in open("play.env", "r").read().strip().split() if l.strip() != ""]
        for l in envlines:
            epos=l.find("=")
            k = l[0:epos]
            v = l[epos+1:]
            envdata[k]=v

    logging.info("env is " + str(envdata))


    play = json.loads(open("play.js", "r").read())
    play_part_i = 0
    for play_part in play:
        ppl = len(play_part) # play part length
        play_part_i+=1

        logdir_part = os.path.join(logbasedir, "parts", "part-%04d" % play_part_i)
        os.makedirs(logdir_part, exist_ok=False)

        #pre tasks
        viewport_png_in = os.path.join(logdir_viewport_img, 'part-%08d-in.png' % play_part_i)
        driver.save_screenshot(viewport_png_in)

        full_png_in = os.path.join(logdir_full_img, 'part-%08d-in.png' % play_part_i)
        driver.save_full_page_screenshot(full_png_in)


        if play_part[0] == None:
            
            if play_part[1] == "get": ###ntcommand
                url_for_get = expand_column(play_part, 2)
                driver.get(url_for_get)

            if play_part[1] == "sam": ###ntcommand
                sentence = play_part[2]
                subprocess.call("""/bin/bash -c "say -v Samantha '%s'; exit 0" """ % sentence, shell=True)

            if play_part[1] == "max": ###ntcommand
                driver.maximize_window()
                time.sleep(1)

            if play_part[1] == "relget": ###ntcommand
                urlpart_for_get = expand_column(play_part, 2)
                url_actual = driver.execute_script('return location.href;').strip().split("\n")[0].strip()
                url_data = urlparse(url_actual)
                url_target = url_data.scheme + "://" + url_data.netloc + urlpart_for_get
                driver.get(url_target)

            if play_part[1] == "sleep":###ntcommand
                time.sleep(float(play_part[2]))

            if play_part[1] == "halt":###ntcommand
                while True:
                    print("*** DEBUG HALT ***")
                    break_input = input("Press RETURN (no input) to continue (leave DEBUG HALT)... $ ")
                    if break_input == "":
                        break
                    else:
                        break_handler(break_input)

            if play_part[1] == "click_any_const":###ntcommand
                any_consts = [x for x in play_part[2:]]
                constructed_xpath = "//*[" + " or ".join(["text()=\"%s\"" % x for x in any_consts]) + "]"
                any_lel = WDW(driver=driver, timeout=default_wait).until(lambda x: x.find_elements(BY.XPATH, constructed_xpath))
                if any_lel is None or len(any_lel) == 0:
                    raise Exception("could not click one of %s" % str(any_consts))
                #driver.execute_script("arguments[0].scrollIntoView(true);", any_lel[0])
                any_lel[0].click()

            if play_part[1] == "click_any_const_startswith":###ntcommand
                any_consts = [x for x in play_part[2:]]
                constructed_xpath = "//*[" + " or ".join(["starts-with(., \"%s\")" % x for x in any_consts]) + "]"
                logging.info(constructed_xpath)
                any_lel = WDW(driver=driver, timeout=default_wait).until(lambda x: x.find_elements(BY.XPATH, constructed_xpath))
                if any_lel is None or len(any_lel) == 0:
                    raise Exception("could not click one of %s" % str(any_consts))
                any_lel[0].click()

            if play_part[1] == "js64str":###ntcommand
                varname = play_part[2]
                code_plain = base64.b64decode(play_part[3]).decode("utf-8")
                res = str(driver.execute_script(code_plain))
                reg_write(varname, res)

            if play_part[1] == "a":###ntcommand
                varname = play_part[2]
                res="\n".join(get_all_a_href())
                reg_write(varname, res)


        else:
            lel = None # list of elements
            
            if play_part[0] == "//":
                pass
            else:

                if play_part[0].startswith("id:"):
                    target_id = play_part[0][3:]
                    lel = WDW(driver=driver, timeout=default_wait).until(lambda x: x.find_elements(BY.ID, target_id))
                    #lel = driver.find_elements(BY.ID, target_id)
                else:
                    lel = WDW(driver=driver, timeout=default_wait).until(lambda x: x.find_elements(BY.XPATH, play_part[0]))
                    #lel = driver.find_elements(BY.XPATH, play_part[0])

                if play_part[1] == "a":###tcommand
                    varname = play_part[2]
                    res="\n".join(get_all_a_href(beneath=lel[0]))
                    reg_write(varname, res)

                if play_part[1] == "reg_dom":###tcommand
                    varname = play_part[2]
                    reg_write(varname, lel[0].get_attribute("innerHTML"))

                if play_part[1] == "reg_dom1":###tcommand
                    varname = play_part[2]
                    reg_write(varname, lel[0].get_attribute("innerHTML").replace("><", ">\n<"))

                if play_part[1] == "reg_attr":###tcommand
                    attrname = play_part[2]
                    varname = play_part[3]
                    res=str(lel[0].get_attribute(attrname))
                    reg_write(varname, res)

                if play_part[1] == "siv":###tcommand
                    driver.execute_script("arguments[0].scrollIntoView(true);", lel[0])
                    time.sleep(1);

                if play_part[1] == "type": ###tcommand
                    content = expand_column(play_part, 2)
                    # content = play_part[2]
                    # if ppl > 3:
                    #     content = content_provider_facade(content, play_part[3])
                    lel[0].send_keys(content)

                if play_part[1] == "click": ###tcommand
                    lel[0].click()

                if play_part[1] == "checked": ###tcommand
                    if lel[0].is_selected() == False:
                        lel[0].click()

                if play_part[1] == "unchecked": ###tcommand
                    if lel[0].is_selected() == True:
                        lel[0].click()

                if play_part[1] == "clickif": ###tcommand
                    e_type = play_part[2]
                    e_contains = play_part[3]
                    constructed_xpath = "//%s[contains(., \"%s\")]" % (e_type, e_contains)
                    sub_lel = lel[0].find_elements(BY.XPATH, constructed_xpath)
                    if sub_lel is None or len(sub_lel) == 0:
                        logging.info("clickif empty")
                    else:
                        sub_lel[0].click()
                    #any_lel = WDW(driver=driver, timeout=default_wait).until(lambda x: x.find_elements(BY.XPATH, constructed_xpath))


                if play_part[1] == "checked01": ###tcommand
                    varname = play_part[2]
                    if lel[0].is_selected():
                        reg_write(varname, '1')
                    else:
                        reg_write(varname, '0')
                    logging.info("REG: %s = %s" % (varname, reg_read(varname)))

                if play_part[1] == "clear": ###tcommand
                    lel[0].clear()

        #post tasks
        viewport_png_out = os.path.join(logdir_viewport_img, 'part-%08d-out.png' % play_part_i)
        driver.save_screenshot(viewport_png_out)

        full_png_out = os.path.join(logdir_full_img, 'part-%08d-out.png' % play_part_i)
        driver.save_full_page_screenshot(full_png_out)


# driver.save_screenshot("test.png")
driver.quit()
logging.info("finished")
