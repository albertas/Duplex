# -*- coding: utf-8 -*-

from homophony import BrowserTestCase, Browser

class RecipesTestCase(BrowserTestCase):
    """recipes modulio testavimo klasė"""
    def siteTestCase(self):
        """Patikrink pagrindinį tinklapio funkcionalumą"""
        TEST_PORT = 8000
        browser = Browser()
        browser.base = 'http://localhost:%s/' % TEST_PORT
        browser.open('/')
        self.assertEquals(browser.url, 'http://localhost:%s/' % TEST_PORT)
        ctr = browser.getControl(name="prisijungti").click()
        if not 'Bandykite dar kartą' in browser.contents:
            raise Exception('Bad contents, when not logged in')
        browser.getLink(id='sarasas').click()
        self.assertEquals(browser.url, 'http://localhost:%s/sarasas/' % TEST_PORT)
        browser.getLink(id='paieska').click()
        self.assertEquals(browser.url, 'http://localhost:%s/paieska/' % TEST_PORT)
        browser.getLink(id='kontaktai').click()
        self.assertEquals(browser.url, 'http://localhost:%s/kontaktai/' % TEST_PORT)
        browser.getLink(id='pagrindinis').click()
        self.assertEquals(browser.url, 'http://localhost:%s/' % TEST_PORT)
        browser.getLink('Biskvitiniai sklindžiai').click()
        self.assertEquals(browser.url, 'http://localhost:%s/receptas/1/' % TEST_PORT)
        browser.getLink(id='pagrindinis').click()
        self.assertEquals(browser.url, 'http://localhost:%s/' % TEST_PORT)
        browser.getLink('Komentarai').click()
        if not "Norėdami komentuoti, turite prisijungti." in browser.contents:
            raise Exception('Bad contents, when looking comments')
        browser.getLink(id='pagrindinis').click()
        self.assertEquals(browser.url, 'http://localhost:%s/' % TEST_PORT)
        browser.getLink(id='kurimas').click()
        if not "Turite prisijungti" in browser.contents:
            raise Exception('Bad contents, when creating recipe without \
            logging in') 
        browser.getLink('Registruotis').click()
        browser.getForm().submit()
        browser.getControl(name='name').value = 'Tom'
        browser.getControl(name='email').value = 'Tom'
        browser.getControl(name='psw').value = 'Tom'
        browser.getControl(name='psw2').value = 'Tom'
        browser.getForm().submit()
        if not "Enter a valid e-mail address" in browser.contents:
            raise Exception('Bad contents, when not valid field')
        browser.getControl(name='name').value = 'Tom'
        browser.getControl(name='email').value = 'Tom@Tom.com'
        browser.getControl(name='psw').value = 'tom'
        browser.getControl(name='psw2').value = 'tom'
        browser.getForm().submit()
        if not ("Prisijungta" in browser.contents):
            browser.getLink(id='pagrindinis').click()
            browser.getControl(name='name').value = 'UserName'
            browser.getControl(name='psw').value = 'UserName'
            browser.getControl(name="prisijungti").click()
        browser.getLink('Pasikeisti slaptažodį').click()
        browser.getControl(name='psw').value = 'tom'
        browser.getControl(name='newpsw1').value = 'tom'
        browser.getControl(name='newpsw2').value = 'tom'
        browser.getForm().submit()    
        if not "Slaptažodis pakeistas" in browser.contents:
            raise Exception('Bad contents, when changing psw') 
        browser.getLink(id='sarasas').click()
        browser.getLink('Biskvitiniai sklindžiai').click()
        self.assertEquals(browser.url, 'http://localhost:%s/receptas/1/' % TEST_PORT)
        browser.getLink(id='kurimas').click()
        self.assertEquals(browser.url, 'http://localhost:%s/kurimas/' % TEST_PORT)
        browser.getControl(name='name').value = 'Pyragas'
        browser.getControl(name='process').value = 'Kepti orkaitėje.'
        browser.getControl(name='duration').value = '40 min.'
        browser.getControl(name='description').value = 'Skanaus :}'
        browser.getControl('Pyragas')
        browser.getControl('Lietuvių')
        browser.getControl('Kepimas orkaitėje')
        browser.getControl('Lengvas')
        browser.getControl(name='ingredients').value = "."
        browser.getForm(name='kurimo_forma').submit() 
        form = browser.getForm(name='komentaru_forma')
        form.getControl(name='comment').value = "Testinis komentaras"
        form.submit()
        if not "Testinis komentaras" in browser.contents:
            raise Exception('Bad contents, when changing psw')
