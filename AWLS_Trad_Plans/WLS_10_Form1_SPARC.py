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

    # Axis - 655393 | india@2020
    # YBL  - 718842 | mnyl@4321 | Customer ID-  29471, 47942, 616658, 626018, 866238 (222222), 2454, 2455, 2456, 2457
    # DST  - 934384 | MNYL@2020
    # SPARC- 782058, ABBBY6754 | MNYL@2020, max@1234
    # Agency- 447660, 127065| Mnyl@2020
    #Ingenium- http://ing247test.maxlifeinsurance.com/ingenium/servlet/pageserver?ProcessClassID=SignOn&PageReturn=index&LocaleID=E



    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://mprouat.maxlifeinsurance.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        self.wait = WebDriverWait(self.driver, 60)
        action = AC(self.driver)

    def loginFunctionality(self):

        username= self.driver.find_element(By.ID, "userId")
        username.send_keys("ABBBY6754")

        password= self.driver.find_element(By.ID, "password")
        password.send_keys("max@1234")

        btnSign=self.driver.find_element(By.XPATH,"//*[contains(text(),'SIGN')]")
        btnSign.click()


        btnNewApp=self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@aria-current='page']")))
        print("Login Successful.")

    def newApplicationFormOneStepOne(self):

        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@href='/']")))
        btnNewApplication= self.driver.find_element(By.XPATH,"//*[@href='/']")
        btnNewApplication.click()


        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@name='panNumber']")))
        panFill= self.driver.find_element(By.XPATH,"//*[@name='panNumber']")
        panFill.send_keys("AOUHT0432T")

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
        firstNameFill.send_keys("Dharam ")

        lastNameFill = self.driver.find_element(By.XPATH,"//*[@name='lastName']")
        lastNameFill.send_keys("Tiwari")

        calendarFill= self.driver.find_element(By.XPATH,"//*[@name='dateOfBirth']")
        calendarFill.click()

        yearDropdown = self.driver.find_element(By.XPATH,"//*[@class='react-datepicker__year-select']")
        yearSel = Select(yearDropdown)
        yearSel.select_by_value('1990')
        time.sleep(1)

        monthDropdown = self.driver.find_element(By.XPATH,"//*[@class='react-datepicker__month-select']")
        monthSel= Select(monthDropdown)
        monthSel.select_by_value('11')

        dateSel=self.driver.find_element(By.XPATH,"(//*[@aria-label='day-13'])[1]")
        dateSel.click()
        time.sleep(2)

        houseNumberFill= self.driver.find_element(By.XPATH,"//*[@name='permanentHouseNo']")
        houseNumberFill.send_keys('House no. 23')

        roadNumberFill = self.driver.find_element(By.XPATH, "//*[@name='permanentRoadNo']")
        roadNumberFill.send_keys('Sector 28')

        countryFill = self.driver.find_element(By.XPATH, "//*[@name='permanentCountry']")
        countryFill.send_keys('India')
        time.sleep(1)
        countryToSel = self.driver.find_element(By.XPATH, "//*[contains(text(),'Ind')]")
        countryToSel.click()
        time.sleep(1)
        print("Country Filled")
        stateFill = self.driver.find_element(By.XPATH, "//*[@name='permanentState']")
        stateFill.send_keys('ANDHRA')
        time.sleep(1)
        stateToSel=self.driver.find_element(By.XPATH, "//*[contains(text(),'ANDHRA')]")
        stateToSel.click()
        time.sleep(1)
        print("State Filled")

        cityFill = self.driver.find_element(By.XPATH, "//*[@name='permanentCity']")
        cityFill.click()
        cityFill.send_keys('HYDE')
        time.sleep(1)
        cityToSel= self.driver.find_element(By.XPATH, "//*[contains(text(),'HYDE')]")
        cityToSel.click()
        time.sleep(1)
        print("City Filled")

        pinToFill= self.driver.find_element(By.XPATH, "//*[@name='permanentPinCode']")
        pinToFill.send_keys('110047')
        time.sleep(1)

        alternateNumberToFill = self.driver.find_element(By.XPATH, "//*[@name='alternateMobileNo']")
        alternateNumberToFill.send_keys('7977412402')
        print("Alternate number Filled")
        time.sleep(1)

        proofDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[2]")
        proofDropdown.click()
        time.sleep(2)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='liId_Voter ID']")))
        proofSel = self.driver.find_element(By.XPATH, "//*[@id='liId_Voter ID']")
        proofSel.click()
        time.sleep(1)

        addProofEnter = self.driver.find_element(By.XPATH,
                                                 "//*[@name= 'proofNumber']")
        addProofEnter.send_keys("3252345235235235235235235")
        time.sleep(1)

        purposeOfInsuranceDropdown= self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[4]")
        purposeOfInsuranceDropdown.click()
        time.sleep(1)

        optionInInsuranceDropdown=self.driver.find_element(By.XPATH,"//*[contains(text(),'Retirement')]")
        optionInInsuranceDropdown.click()
        print("Protection Selected")

        lifeStageDropdown= self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[5]")
        lifeStageDropdown.click()
        time.sleep(1)

        optionInLifeStage= self.driver.find_element(By.XPATH, "//*[contains(text(), 'Married')]")
        optionInLifeStage.click()
        print("Single Selected")

        grossIncomeFill = self.driver.find_element(By.XPATH, "//*[@name='income']")
        grossIncomeFill.send_keys('5000000')
        print("Gross Income Entered")

        existingPolicy=self.driver.find_element(By.XPATH, "(//*[contains(text(),'No')])[3]")
        existingPolicy.click()

        occupationDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[6]")
        occupationDropdown.click()
        optionInOccupation = self.driver.find_element(By.XPATH, "//*[@id='liId_Professional']")
        optionInOccupation.click()
        print("Professional Selected")
        time.sleep(2)

        recommendProduct= self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[8]")
        recommendProduct.click()
        time.sleep(5)
        recommendProduct.click()
        time.sleep(1)
        optionInRecommendProduct = self.driver.find_element(By.XPATH, "//*[@id='liId_Select Another Product']")
        optionInRecommendProduct.click()
        print("Product Selected")
        time.sleep(1)

        optionsInrecommendProduct = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[9]")
        optionsInrecommendProduct.click()
        time.sleep(1)
        optionssInRecommendProduct = self.driver.find_element(By.XPATH, "//*[@id='liId_Max Life Whole Life Super']")
        optionssInRecommendProduct.click()
        print("Product Selected")
        time.sleep(1)


        premiumPaymentTerm = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[10]")
        premiumPaymentTerm.click()
        time.sleep(1)
        optionInPremiumPaymentTerm = self.driver.find_element(By.XPATH, "//*[@id='liId_10']")
        optionInPremiumPaymentTerm.click()
        print("Premium Payment Selected")
        time.sleep(2)

        policyTerm = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[11]")
        policyTerm.click()
        time.sleep(1)
        optionInPolicyTerm = self.driver.find_element(By.XPATH, "//*[@id='liId_70']")
        optionInPolicyTerm.click()
        print("Policy Term Selected")
        time.sleep(2)

        dividentAdjustment = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[12]")
        dividentAdjustment.click()
        time.sleep(1)
        optiondividentAdjustment = self.driver.find_element(By.XPATH, "//*[@id='liId_No Adjustment']")
        optiondividentAdjustment.click()
        print("Policy Term Selected")
        time.sleep(2)

        modeOfPayment = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[13]")
        modeOfPayment.click()
        time.sleep(1)
        optinoInmodeOfPayment = self.driver.find_element(By.XPATH, "//*[@id='liId_Quarterly']")
        optinoInmodeOfPayment.click()
        print("Dividend option")
        time.sleep(2)

        premiumCommitFill = self.driver.find_element(By.XPATH, "//*[@name='premiumCommitment']")
        premiumCommitFill.send_keys("90000")
        print("Sum Assured Filled")

        dividendDropdownSelected= self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[14]")
        dividendDropdownSelected.click()
        time.sleep(1)
        optinoInDividend  = self.driver.find_element(By.XPATH, "//*[@id='liId_PUA']")
        optinoInDividend.click()
        print("Dividend option")
        time.sleep(2)

        riderWOP = self.driver.find_element(By.XPATH, "//*[@name='isWOPPlusRider']")
        riderWOP.click()
        time.sleep(2)

        buttonProceedClick = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        buttonProceedClick.click()

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@id='popupProceed'])[1]")))
        buttonYes= self.driver.find_element(By.XPATH, "(//*[@id='popupProceed'])[1]")
        buttonYes.click()

        # ########################### step 3 #############################
        time.sleep(10)

        self.driver.switch_to_window(windowBefore)
        time.sleep(2)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@name='fatherName']")))
        fatherNameFill= self.driver.find_element(By.XPATH, "//*[@name='fatherName']")
        fatherNameFill.send_keys("Ram")

        motherNameFill = self.driver.find_element(By.XPATH, "//*[@name='motherName']")
        motherNameFill.send_keys("Singh")

        maritalStatus = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[2]")
        maritalStatus.click()
        time.sleep(1)
        optionInMaritalStage = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Married')]")
        optionInMaritalStage.click()
        print("Single Selected")
        time.sleep(1)

        educationSelect = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[3]")
        educationSelect.click()
        time.sleep(1)
        optionInEducationDropdown= self.driver.find_element(By.XPATH, "//*[contains(text(), 'Primary')][1]")
        optionInEducationDropdown.click()
        print("Education Selected")

        industrySelect= self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[4]")
        industrySelect.click()
        time.sleep(1)
        optionInIndustrySelect = self.driver.find_element(By.XPATH, "//*[@id='liId_Oil & Natural Gas']")
        optionInIndustrySelect.click()
        print("Industry Selected")
        time.sleep(1)

        organisationSelect = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[5]")
        organisationSelect.click()
        time.sleep(1)
        optionInOrganisationSelect = self.driver.find_element(By.XPATH, "//*[@id='liId_Public Ltd']")
        optionInOrganisationSelect.click()
        print("Organisation Selected")
        time.sleep(1)

        preferredLanguage= self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[6]")
        preferredLanguage.click()
        time.sleep(1)
        optionInPreferredLanguage = self.driver.find_element(By.XPATH, "//*[@id='liId_Bengali']")
        optionInPreferredLanguage.click()
        print("Hindi Selected")
        time.sleep(1)

        nomineeFill = self.driver.find_element(By.XPATH, "//*[@name='nomineeName']")
        nomineeFill.send_keys("Kiran Kumari")

        calendarNomineeFill = self.driver.find_element(By.XPATH, "//*[@name='nomineeDateOfBirth']")
        calendarNomineeFill.click()

        yearNomineeDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__year-select']")
        yearNomineeSel = Select(yearNomineeDropdown)
        yearNomineeSel.select_by_value('1992')

        monthNomineeDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__month-select']")
        monthNomineeSel = Select(monthNomineeDropdown)
        monthNomineeSel.select_by_value('11')

        dateNomineeSel = self.driver.find_element(By.XPATH, "//*[@aria-label='day-30']")
        dateNomineeSel.click()

        genderSelected = self.driver.find_element(By.XPATH, "//*[contains(text(),'Female')]")
        genderSelected.click()
        print("Gender Clicked")

        relationshipProposer = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[8]")
        relationshipProposer.click()
        time.sleep(1)
        optionInRelationshipProposer= self.driver.find_element(By.XPATH, "//*[@id ='liId_Wife']")
        optionInRelationshipProposer.click()
        print("Relationship Brother Selected.")
        time.sleep(1)

        bankFill = self.driver.find_element(By.XPATH, "//*[@name='bankAccountNo']")
        bankFill.send_keys("99999999999999")

        nameOfAccount = self.driver.find_element(By.XPATH, "//*[@name='bankAccountHolderName']")
        nameOfAccount.send_keys("Kiran Kumari")

        nameOfIFSCcode = self.driver.find_element(By.XPATH, "//*[@name='bankAccountIFSC']")
        nameOfIFSCcode.send_keys("KKBK0000199")

        codeMICR = self.driver.find_element(By.XPATH, "//*[@name='bankAccountMICR']")
        codeMICR.send_keys("110485028")
        time.sleep(3)

        accountType = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[10]")
        accountType.click()
        time.sleep(2)

        accountTypeSelect = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Savings')]")
        accountTypeSelect.click()
        print("Account Type Selected.")
        time.sleep(2)

        btnProceedOnPage3 = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        btnProceedOnPage3.click()
        time.sleep(5)

    def newApplicationFormOneStepFour(self):

        hazardousActivitiesSelect = self.driver.find_element(By.XPATH, "(//*[contains(text(), 'No')])[6]")
        hazardousActivitiesSelect.click()

        criminalSelect = self.driver.find_element(By.XPATH, "(//*[contains(text(), 'No')])[7]")
        criminalSelect.click()

        travelSelect = self.driver.find_element(By.XPATH, "(//*[contains(text(), 'No')])[8]")
        travelSelect.click()

        heightInFeet = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[4]")
        heightInFeet.click()
        time.sleep(1)
        selectHeightInFeet = self.driver.find_element(By.XPATH, "//*[@id='liId_5']")
        selectHeightInFeet.click()

        heightInInches = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[5]")
        heightInInches.click()
        time.sleep(1)
        selectHeightInInches = self.driver.find_element(By.XPATH, "//*[@id='liId_5']")
        selectHeightInInches.click()
        time.sleep(1)

        weightFill = self.driver.find_element(By.XPATH, "//*[@name='weight']")
        weightFill.click()
        weightFill.send_keys("80")
        time.sleep(2)

        btnProceedOnPage4 = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        btnProceedOnPage4.click()
        print("Proceed Button Clicked.")

        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text(),'Cancel')]")))

        clickCancel = self.driver.find_element(By.XPATH, "//*[contains(text(),'Cancel')]")
        clickCancel.click()

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='popupProceed']")))

        verificationLinkPopUp = self.driver.find_element(By.XPATH, "//*[@id='popupProceed']")
        verificationLinkPopUp.click()
        print("Verification Link Sent.")
        # time.sleep(2)

    def newApplicationFormOneStepFive(self):

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Payment')]")))
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
        chequeDateSelect = self.driver.find_element(By.XPATH, "//*[text()='2']")
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