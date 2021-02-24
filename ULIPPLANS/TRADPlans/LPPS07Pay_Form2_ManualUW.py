from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
import time

class mProAutomate:

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://mprouat.maxlifeinsurance.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        self.wait = WebDriverWait(self.driver, 60)
        action = AC(self.driver)

    def loginFunctionality(self):

        username= self.driver.find_element(By.ID, "userId")
        username.send_keys("129954")

        password= self.driver.find_element(By.ID, "password")
        password.send_keys("India@2020")

        btnSign=self.driver.find_element(By.XPATH,"//*[contains(text(),'SIGN')]")
        btnSign.click()


        btnNewApp=self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@aria-current='page']")))
        print("Login Successful.")

    def newApplicationFormOneStepOne(self):
        windowBefore = self.driver.window_handles[0]

        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@href='/']")))
        btnNewApplication= self.driver.find_element(By.XPATH,"//*[@href='/']")
        btnNewApplication.click()


        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@name='panNumber']")))
        radioButtonDependent = self.driver.find_element(By.XPATH, "//*[@for='dependent']")
        radioButtonDependent.click()
        panFill= self.driver.find_element(By.XPATH,"//*[@name='panNumber']")
        panFill.send_keys("APCPB1546B")

        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@name='mobileNumber']")))
        mobNumberFill= self.driver.find_element(By.XPATH,"//*[@name='mobileNumber']")
        mobNumberFill.send_keys("7042970921")

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@name='email']")))
        emailFill = self.driver.find_element(By.XPATH, "//*[@name='email']")
        emailFill.send_keys("kartik.bisaria@kelltontech.com")

        btnProceed = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        btnProceed.click()

    def newApplicationFormOneStepTwo(self):

        windowBefore = self.driver.window_handles[0]
        print("Window Before=",windowBefore)

        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@name='firstName']")))
        firstNameFill = self.driver.find_element(By.XPATH,"//*[@name='firstName']")
        firstNameFill.send_keys("Bharti")

        lastNameFill = self.driver.find_element(By.XPATH,"//*[@name='lastName']")
        lastNameFill.send_keys("Sharma")

        calendarFill= self.driver.find_element(By.XPATH,"//*[@name='dateOfBirth']")
        calendarFill.click()

        yearDropdown = self.driver.find_element(By.XPATH,"//*[@class='react-datepicker__year-select']")
        yearSel = Select(yearDropdown)
        yearSel.select_by_value('1985')

        monthDropdown = self.driver.find_element(By.XPATH,"//*[@class='react-datepicker__month-select']")
        monthSel= Select(monthDropdown)
        monthSel.select_by_value('3')

        dateSel=self.driver.find_element(By.XPATH,"//*[@aria-label='day-10']")
        dateSel.click()

        proofDropdown= self.driver.find_element(By.XPATH, "(//*[@aria-pressed='false'])[1]")
        proofDropdown.click()
        time.sleep(10)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "// *[contains(text(), 'Driving License')]")))
        proofSel=self.driver.find_element(By.XPATH, "// *[contains(text(), 'Driving License')]")
        proofSel.click()

        houseNumberFill= self.driver.find_element(By.XPATH,"//*[@name='permanentHouseNo']")
        houseNumberFill.send_keys('12312edsfss')

        roadNumberFill = self.driver.find_element(By.XPATH, "//*[@name='permanentRoadNo']")
        roadNumberFill.send_keys('12312edsfss')

        countryFill = self.driver.find_element(By.XPATH, "//*[@name='permanentCountry']")
        countryFill.send_keys('India')
        time.sleep(1)
        countryToSel = self.driver.find_element(By.XPATH, "//*[contains(text(),'Ind')]")
        countryToSel.click()
        time.sleep(1)
        print("Country Filled")
        stateFill = self.driver.find_element(By.XPATH, "//*[@name='permanentState']")
        stateFill.send_keys('Har')
        time.sleep(1)
        stateToSel=self.driver.find_element(By.XPATH, "//*[contains(text(),'HAR')]")
        stateToSel.click()
        time.sleep(1)
        print("State Filled")

        cityFill = self.driver.find_element(By.XPATH, "//*[@name='permanentCity']")
        cityFill.click()
        cityFill.send_keys('GURU')
        time.sleep(1)
        cityToSel= self.driver.find_element(By.XPATH, "//*[contains(text(),'GU')]")
        cityToSel.click()
        time.sleep(1)
        print("City Filled")

        pinToFill= self.driver.find_element(By.XPATH, "//*[@name='permanentPinCode']")
        pinToFill.send_keys('122010')
        time.sleep(1)

        alternateNumberToFill = self.driver.find_element(By.XPATH, "//*[@name='alternateMobileNo']")
        alternateNumberToFill.send_keys('9650479781')
        print("Alternate number Filled")

        lifeInsuredNameFill = self.driver.find_element(By.XPATH, "//*[@name='insurerName']")
        lifeInsuredNameFill.send_keys("Name")
        insuredGenderSelected = self.driver.find_element(By.XPATH, "//*[@for='InsurerGenderMale']")
        insuredGenderSelected.click()
        print("Insured Gender Clicked")

        calendarFill = self.driver.find_element(By.XPATH, "//*[@name='insurerDateOfBirth']")
        calendarFill.click()

        yearDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__year-select']")
        yearSel = Select(yearDropdown)
        yearSel.select_by_value('1985')

        monthDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__month-select']")
        monthSel = Select(monthDropdown)
        monthSel.select_by_value('3')

        dateSel = self.driver.find_element(By.XPATH, "//*[@aria-label='day-10']")
        dateSel.click()
        time.sleep(1)

        dropdownRelationship = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[4]")
        dropdownRelationship.click()
        time.sleep(2)
        dropdownRelationshipOptions = self.driver.find_element(By.XPATH, "//*[@id='liId_Others']")
        dropdownRelationshipOptions.click()
        time.sleep(2)

        enterRelatonship = self.driver.find_element(By.XPATH, "//*[@id='relationshipWithProposerWhenOther_idd']")
        enterRelatonship.send_keys("Partner")
        time.sleep(1)
        selectRelationship = self.driver.find_element(By.XPATH, "//*[@role='menuitem']")
        selectRelationship.click()
        time.sleep(1)

        purposeOfInsuranceDropdown= self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[6]")
        purposeOfInsuranceDropdown.click()

        optionInInsuranceDropdown=self.driver.find_element(By.XPATH,"//*[contains(text(),'Retirement')]")
        optionInInsuranceDropdown.click()
        print("Retirement Selected")

        lifeStageDropdown= self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[7]")
        lifeStageDropdown.click()

        optionInLifeStage= self.driver.find_element(By.XPATH, "//*[contains(text(), 'Married with children')]")
        optionInLifeStage.click()
        print("Single Selected")

        grossIncomeFill = self.driver.find_element(By.XPATH, "//*[@name='income']")
        grossIncomeFill.send_keys('800000')
        print("Gross Income Entered")

        existingPolicy=self.driver.find_element(By.XPATH, "(//*[contains(text(),'No')])[3]")
        existingPolicy.click()

        occupationDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[8]")
        occupationDropdown.click()
        optionInOccupation = self.driver.find_element(By.XPATH, "//*[@id='liId_Self Employed']")
        optionInOccupation.click()
        print("Self Employed Selected")
        time.sleep(2)

        recommendProduct= self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[10]")
        recommendProduct.click()
        time.sleep(5)
        recommendProduct.click()
        time.sleep(1)
        optionInRecommendProduct = self.driver.find_element(By.XPATH, "//*[@id='liId_Max Life Life Perfect Partner Super']")
        optionInRecommendProduct.click()
        print("Product Selected")


        premiumPaymentTerm = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[11]")
        premiumPaymentTerm.click()
        time.sleep(1)
        optionInPremiumPaymentTerm = self.driver.find_element(By.XPATH, "//*[@id='liId_7']")
        optionInPremiumPaymentTerm.click()
        print("Premium Payment Selected")
        time.sleep(2)

        policyTerm = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[12]")
        policyTerm.click()
        time.sleep(2)
        optionInPolicyTerm = self.driver.find_element(By.XPATH, "//*[@id='liId_40']")
        optionInPolicyTerm.click()
        print("Policy Term Selected")
        time.sleep(1)


        premiumCommitFill = self.driver.find_element(By.XPATH, "//*[@name='premiumCommitment']")
        premiumCommitFill.send_keys("90000")
        print("Sum Assured Filled")

        dividendDropdownSelected= self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[14]")
        dividendDropdownSelected.click()
        print("Dividend dropdown Clicked")
        time.sleep(2)

        optionIndividendDropdownSelected = self.driver.find_element(By.XPATH, "//*[@id='liId_Cash']")
        optionIndividendDropdownSelected.click()
        print ("Cash selected")

        buttonProceedClick = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        buttonProceedClick.click()

        time.sleep(4)

        self.driver.switch_to_window(windowBefore)
        time.sleep(2)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@name='fatherName']")))
        fatherNameFill= self.driver.find_element(By.XPATH, "//*[@name='fatherName']")
        fatherNameFill.send_keys("Father")

        motherNameFill = self.driver.find_element(By.XPATH, "//*[@name='motherName']")
        motherNameFill.send_keys("Mother")

        maritalStatus = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[2]")
        maritalStatus.click()
        time.sleep(1)
        optionInMaritalStage = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Married')]")
        optionInMaritalStage.click()
        print("Single Selected")

        educationSelect = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[3]")
        educationSelect.click()
        time.sleep(1)
        optionInEducationDropdown= self.driver.find_element(By.XPATH, "//*[contains(text(), 'Graduate')][1]")
        optionInEducationDropdown.click()
        print("Education Selected")

        industrySelect= self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[4]")
        industrySelect.click()
        time.sleep(1)
        optionInIndustrySelect = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Defence')][1]")
        optionInIndustrySelect.click()
        print("Industry Selected")

        organisationSelect = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[5]")
        organisationSelect.click()
        time.sleep(1)
        optionInOrganisationSelect = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Govt')][1]")
        optionInOrganisationSelect.click()
        print("Organisation Selected")

        natureSelect = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[6]")
        natureSelect.click()
        time.sleep(1)
        optionInNatureSelect = self.driver.find_element(By.XPATH, "(//*[contains(text(), 'Combat')])[1]")
        optionInNatureSelect.click()
        print("Nature Selected")

        preferredLanguage= self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[7]")
        preferredLanguage.click()
        time.sleep(1)
        optionInPreferredLanguage = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Hindi')]")
        optionInPreferredLanguage.click()
        print("Hindi Selected")
        time.sleep(2)

        bankFill = self.driver.find_element(By.XPATH, "//*[@name='bankAccountNo']")
        bankFill.send_keys("99999999999999")

        nameOfAccount = self.driver.find_element(By.XPATH, "//*[@name='bankAccountHolderName']")
        nameOfAccount.send_keys("NameName")

        nameOfIFSCcode = self.driver.find_element(By.XPATH, "//*[@name='bankAccountIFSC']")
        nameOfIFSCcode.send_keys("SBIN0000845")

        codeMICR = self.driver.find_element(By.XPATH, "//*[@name='bankAccountMICR']")
        codeMICR.send_keys("515002206")
        time.sleep(3)

        accountType = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[9]")
        accountType.click()
        time.sleep(2)

        accountTypeSelect = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Savings')]")
        accountTypeSelect.click()
        print("Account Type Selected.")
        time.sleep(1)

        lifeinsuredFatherFill = self.driver.find_element(By.XPATH, "//*[@name='insurerFatherName']")
        lifeinsuredFatherFill.send_keys("InsuredFather")
        lifeinsuredDobProofType = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[11]")
        lifeinsuredDobProofType.click()
        lifeinsuredDobProofOptions = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Aadhaar')]")
        lifeinsuredDobProofOptions.click()

        lifeinsuredEducation = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[12]")
        lifeinsuredEducation.click()
        time.sleep(1)
        lifeinsuredEducationOptions = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Post Graduate')][1]")
        lifeinsuredEducationOptions.click()
        time.sleep(1)

        lifeinsuredMaritalStatus = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[13]")
        lifeinsuredMaritalStatus.click()
        time.sleep(1)
        lifeinsuredMaritalStatusOptions = self.driver.find_element(By.XPATH, "//*[@id='liId_Married']")
        lifeinsuredMaritalStatusOptions.click()
        time.sleep(1)

        industrySelect = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[14]")
        industrySelect.click()
        time.sleep(1)

        optionInIndustrySelect = self.driver.find_element(By.XPATH, "(//*[contains(text(), 'Others')])[1]")
        optionInIndustrySelect.click()
        print("Industry Selected")

        organisationSelect = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[15]")
        organisationSelect.click()
        time.sleep(1)
        optionInOrganisationSelect = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Non-Governmental')][1]")
        optionInOrganisationSelect.click()
        print("Organisation Selected")

        insurerAnnualIncomeFill = self.driver.find_element(By.XPATH, "//*[@name='insurerAnnualIncome']")
        insurerAnnualIncomeFill.send_keys('5000000')
        time.sleep(2)

        occupationSelect = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[16]")
        occupationSelect.click()
        time.sleep(1)


        optionInoccupationSelect = self.driver.find_element(By.XPATH, "//*[@id='liId_Self Employed']")
        optionInoccupationSelect.click()
        print("Organisation Selected")
        time.sleep(2)

        hazardousActivitiesSelect = self.driver.find_element(By.XPATH, "(//*[contains(text(), 'No')])[4]")
        hazardousActivitiesSelect.click()

        criminalSelect = self.driver.find_element(By.XPATH, "(//*[contains(text(), 'No')])[5]")
        criminalSelect.click()

        travelSelect = self.driver.find_element(By.XPATH, "(//*[contains(text(), 'No')])[6]")
        travelSelect.click()

        heightInFeet = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[17]")
        heightInFeet.click()
        time.sleep(1)
        selectHeightInFeet = self.driver.find_element(By.XPATH, "//*[@id='liId_5']")
        selectHeightInFeet.click()

        heightInInches = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[18]")
        heightInInches.click()
        time.sleep(1)
        selectHeightInInches = self.driver.find_element(By.XPATH, "//*[@id='liId_5']")
        selectHeightInInches.click()
        time.sleep(1)

        weightFill = self.driver.find_element(By.XPATH, "//*[@name='insurerWeightInKgs']")
        weightFill.click()
        weightFill.send_keys("60")
        time.sleep(3)

        btnProceedOnPage3 = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        btnProceedOnPage3.click()


    def newApplicationFormOneStepFour(self):

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Proceed')]")))

        btnProceedOnPage4 = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        btnProceedOnPage4.click()
        print("Proceed Button Clicked.")

        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text(),'Cancel')]")))

        verificationLinkPopUp = self.driver.find_element(By.XPATH, "//*[@id='popupProceed']")
        verificationLinkPopUp.click()
        print("Verification Link Sent.")
        time.sleep(5)

    def newApplicationFormOneStepFive(self):

        paymentStep5= self.driver.find_element(By.XPATH, "//*[contains(text(),'Payment')]")
        paymentStep5.click()

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@for='Cheque']")))
        radioCheque = self.driver.find_element(By.XPATH, "//*[@for='Cheque']")
        radioCheque.click()
        print("Cheque Selected.")

        chequeFill = self.driver.find_element(By.XPATH, "//*[@name='paymentChequeNumber']")
        chequeFill.send_keys('1234567234')

        calendarSelect = self.driver.find_element(By.XPATH, "//*[@name='paymentChequeDate']")
        calendarSelect.click()
        time.sleep(1)
        chequeDateSelect = self.driver.find_element(By.XPATH, "//*[text()='1']")
        chequeDateSelect.click()


        chequePayableSelect= self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[2]")
        chequePayableSelect.click()
        time.sleep(1)
        optionInChequePayableSelect = self.driver.find_element(By.XPATH, "//*[text() = 'Local']")
        optionInChequePayableSelect.click()
        time.sleep(1)

        chequeBankName = self.driver.find_element(By.XPATH, "//*[@name='paymentChequeBankName']")
        chequeBankName.send_keys('asjdhfjasflh')

        chequeMicrFill = self.driver.find_element(By.XPATH, "//*[@name='paymentChequeMicr']")
        chequeMicrFill.send_keys('123456789')

        radioChequeRenewal = self.driver.find_element(By.XPATH, "//*[@for='renewalCheque']")
        radioChequeRenewal.click()
        print("Cheque Selected.")

        buttonSave = self.driver.find_element(By.XPATH, "//*[text()='Save']")
        buttonSave.click()
        print("Save button clicked.")


        # time.sleep(5)
        # self.driver.quit()


auto=mProAutomate()
auto.loginFunctionality()
auto.newApplicationFormOneStepOne()
auto.newApplicationFormOneStepTwo()
auto.newApplicationFormOneStepFour()
auto.newApplicationFormOneStepFive()