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
    # SPARC- 782058 | MNYL@2020
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
        username.send_keys("447660")

        password= self.driver.find_element(By.ID, "password")
        password.send_keys("Mnyl@2020")

        btnSign=self.driver.find_element(By.XPATH,"//*[contains(text(),'SIGN')]")
        btnSign.click()


        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@aria-current='page']")))
        print("Login Successful.")

    def newApplicationFormOneStepOne(self):
        windowBefore = self.driver.window_handles[0]

        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@href='/']")))
        btnNewApplication= self.driver.find_element(By.XPATH,"//*[@href='/']")
        btnNewApplication.click()

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@name='panNumber']")))
        radioButtonDependent = self.driver.find_element(By.XPATH, "//*[@for='dependent']")
        radioButtonDependent.click()
        time.sleep(1)

        panFill= self.driver.find_element(By.XPATH,"//*[@name='panNumber']")
        panFill.send_keys("GEVPS5657H")

        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@name='mobileNumber']")))
        mobNumberFill= self.driver.find_element(By.XPATH,"//*[@name='mobileNumber']")
        mobNumberFill.send_keys("8898017689")

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@name='email']")))
        emailFill = self.driver.find_element(By.XPATH, "//*[@name='email']")
        emailFill.send_keys("kartik.bisaria@kelltontech.com")

        btnProceed = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        btnProceed.click()

        time.sleep(8)

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
        yearSel.select_by_value('1981')

        monthDropdown = self.driver.find_element(By.XPATH,"//*[@class='react-datepicker__month-select']")
        monthSel= Select(monthDropdown)
        monthSel.select_by_value('11')

        dateSel=self.driver.find_element(By.XPATH,"//*[@aria-label='day-17']")
        dateSel.click()
        time.sleep(2)
        #
        houseNumberFill= self.driver.find_element(By.XPATH,"//*[@name='permanentHouseNo']")
        houseNumberFill.send_keys('12312')

        roadNumberFill = self.driver.find_element(By.XPATH, "//*[@name='permanentRoadNo']")
        roadNumberFill.send_keys('12312')

        countryFill = self.driver.find_element(By.XPATH, "//*[@name='permanentCountry']")
        countryFill.send_keys('India')
        time.sleep(1)
        countryToSel = self.driver.find_element(By.XPATH, "//*[contains(text(),'Ind')]")
        countryToSel.click()
        time.sleep(1)
        print("Country Filled")
        stateFill = self.driver.find_element(By.XPATH, "//*[@name='permanentState']")
        stateFill.send_keys('MAHA')
        time.sleep(1)
        stateToSel=self.driver.find_element(By.XPATH, "//*[contains(text(),'MAHA')]")
        stateToSel.click()
        time.sleep(1)
        print("State Filled")

        cityFill = self.driver.find_element(By.XPATH, "//*[@name='permanentCity']")
        cityFill.click()
        cityFill.send_keys('MUM')
        time.sleep(1)
        cityToSel= self.driver.find_element(By.XPATH, "//*[contains(text(),'MUM')]")
        cityToSel.click()
        time.sleep(1)
        print("City Filled")

        pinToFill= self.driver.find_element(By.XPATH, "//*[@name='permanentPinCode']")
        pinToFill.send_keys('400081')
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
        addProofEnter.send_keys("123456789012")
        time.sleep(1)

        ##############Life Insured Details################333
        lifeToInsured = self.driver.find_element(By.XPATH,
                                                 "//*[@name= 'insurerName']")
        lifeToInsured.send_keys("Ram")
        time.sleep(1)

        lifegenderSelected = self.driver.find_element(By.XPATH, "(//*[contains(text(),'Female')])[2]")
        lifegenderSelected.click()
        print("Gender Clicked")
        time.sleep(1)

        lifecalendarFill = self.driver.find_element(By.XPATH, "//*[@name='insurerDateOfBirth']")
        lifecalendarFill.click()
        time.sleep(1)

        lifeyearDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__year-select']")
        yearSel = Select(lifeyearDropdown)
        yearSel.select_by_value('1983')

        lifemonthDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__month-select']")
        monthSel = Select(lifemonthDropdown)
        monthSel.select_by_value('11')

        dateSel = self.driver.find_element(By.XPATH, "//*[@aria-label='day-14']")
        dateSel.click()
        time.sleep(2)

        liferelationshipDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[4]")
        liferelationshipDropdown.click()
        time.sleep(1)

        optionInLifeRelationshipProposer = self.driver.find_element(By.XPATH, "//*[@id ='liId_Wife']")
        optionInLifeRelationshipProposer.click()
        print("Relationship Brother Selected.")
        time.sleep(1)


        #################################################33
        purposeOfInsuranceDropdown= self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[6]")
        purposeOfInsuranceDropdown.click()
        time.sleep(1)

        optionInInsuranceDropdown=self.driver.find_element(By.XPATH,"//*[contains(text(),'Retirement')]")
        optionInInsuranceDropdown.click()
        print("Retirement Selected")

        lifeStageDropdown= self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[7]")
        lifeStageDropdown.click()

        optionInLifeStage= self.driver.find_element(By.XPATH, "//*[contains(text(), 'Married with children')]")
        optionInLifeStage.click()
        print("Single Selected")

        grossIncomeFill = self.driver.find_element(By.XPATH, "//*[@name='income']")
        grossIncomeFill.send_keys('1100000')
        print("Gross Income Entered")

        existingPolicy=self.driver.find_element(By.XPATH, "(//*[contains(text(),'No')])[3]")
        existingPolicy.click()

        occupationDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[8]")
        occupationDropdown.click()
        optionInOccupation = self.driver.find_element(By.XPATH, "//*[@id='liId_Salaried']")
        optionInOccupation.click()
        print("Salaried Selected")
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
        time.sleep(1)
        optionInPolicyTerm = self.driver.find_element(By.XPATH, "//*[@id='liId_38']")
        optionInPolicyTerm.click()
        print("Policy Term Selected")
        time.sleep(2)

        premiumCommitFill = self.driver.find_element(By.XPATH, "//*[@name='premiumCommitment']")
        premiumCommitFill.send_keys("200000")
        print("Sum Assured Filled")

        dividendDropdownSelected= self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[14]")
        dividendDropdownSelected.click()
        print("Dividend dropdown Clicked")
        time.sleep(2)

        optionIndividendDropdownSelected = self.driver.find_element(By.XPATH, "//*[@id='liId_Cash']")
        optionIndividendDropdownSelected.click()
        print ("Premium Offset selected")
        time.sleep(1)

        buttonProceedClick = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        buttonProceedClick.click()
        time.sleep(1)

        # self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@id='popupProceed'])[1]")))
        # buttonYes= self.driver.find_element(By.XPATH, "(//*[@id='popupProceed'])[1]")
        # buttonYes.click()

        ########################### step 3 #############################
        time.sleep(4)

        self.driver.switch_to_window(windowBefore)
        time.sleep(2)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@name='fatherName']")))
        fatherNameFill= self.driver.find_element(By.XPATH, "//*[@name='fatherName']")
        fatherNameFill.send_keys("Ram")

        motherNameFill = self.driver.find_element(By.XPATH, "//*[@name='motherName']")
        motherNameFill.send_keys("Kumari")

        maritalStatus = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[2]")
        maritalStatus.click()
        time.sleep(1)
        optionInMaritalStage = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Married')]")
        optionInMaritalStage.click()
        print("Single Selected")

        educationSelect = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[3]")
        educationSelect.click()
        time.sleep(1)
        optionInEducationDropdown= self.driver.find_element(By.XPATH, "//*[contains(text(), 'Post Graduate')][1]")
        optionInEducationDropdown.click()
        print("Education Selected")

        industrySelect= self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[4]")
        industrySelect.click()
        time.sleep(1)
        optionInIndustrySelect = self.driver.find_element(By.XPATH, "//*[@id='liId_Defence']")
        optionInIndustrySelect.click()
        print("Industry Selected")
        time.sleep(1)

        organisationSelect = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[5]")
        organisationSelect.click()
        time.sleep(1)
        optionInOrganisationSelect = self.driver.find_element(By.XPATH, "//*[@id='liId_Pvt Ltd']")
        optionInOrganisationSelect.click()
        print("Organisation Selected")
        time.sleep(1)

        organisationFill = self.driver.find_element(By.XPATH, "//*[@name='companyName']")
        organisationFill.send_keys("ORG")

        preferredLanguage= self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[7]")
        preferredLanguage.click()
        time.sleep(1)
        optionInPreferredLanguage = self.driver.find_element(By.XPATH, "//*[@id='liId_English']")
        optionInPreferredLanguage.click()
        print("Hindi Selected")
        time.sleep(1)

        # organisationFill = self.driver.find_element(By.XPATH, "//*[@name='nomineeName']")
        # organisationFill.send_keys("Nominee")
        #
        # calendarNomineeFill = self.driver.find_element(By.XPATH, "//*[@name='nomineeDateOfBirth']")
        # calendarNomineeFill.click()
        #
        # yearNomineeDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__year-select']")
        # yearNomineeSel = Select(yearNomineeDropdown)
        # yearNomineeSel.select_by_value('1994')
        #
        # monthNomineeDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__month-select']")
        # monthNomineeSel = Select(monthNomineeDropdown)
        # monthNomineeSel.select_by_value('3')
        #
        # dateNomineeSel = self.driver.find_element(By.XPATH, "//*[@aria-label='day-10']")
        # dateNomineeSel.click()
        #
        # genderSelected = self.driver.find_element(By.XPATH, "//*[contains(text(),'Male')]")
        # genderSelected.click()
        # print("Gender Clicked")
        #
        # relationshipProposer = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[8]")
        # relationshipProposer.click()
        # time.sleep(1)
        # optionInRelationshipProposer= self.driver.find_element(By.XPATH, "//*[@id ='liId_Brother']")
        # optionInRelationshipProposer.click()
        # print("Relationship Brother Selected.")

        bankFill = self.driver.find_element(By.XPATH, "//*[@name='bankAccountNo']")
        bankFill.send_keys("99999999999999")

        nameOfAccount = self.driver.find_element(By.XPATH, "//*[@name='bankAccountHolderName']")
        nameOfAccount.send_keys("NameName")

        nameOfIFSCcode = self.driver.find_element(By.XPATH, "//*[@name='bankAccountIFSC']")
        nameOfIFSCcode.send_keys("ICIC0001147")

        codeMICR = self.driver.find_element(By.XPATH, "//*[@name='bankAccountMICR']")
        codeMICR.send_keys("110229197")
        time.sleep(3)

        accountType = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[9]")
        accountType.click()
        time.sleep(2)

        accountTypeSelect = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Savings')]")
        accountTypeSelect.click()
        print("Account Type Selected.")
        time.sleep(2)

        ##################Life Insured Details
        fatherNameFill = self.driver.find_element(By.XPATH, "//*[@name='insurerFatherName']")
        fatherNameFill.send_keys("Chotu")

        dobDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[11]")
        dobDropdown.click()

        optiondobDropdown = self.driver.find_element(By.XPATH, "//*[@id='liId_Voter ID']")
        optiondobDropdown.click()
        time.sleep(1)

        educationdropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[12]")
        educationdropdown.click()

        optioneducationdropdownn = self.driver.find_element(By.XPATH, "//*[@id='liId_Graduate']")
        optioneducationdropdownn.click()
        time.sleep(1)

        maritalStatus = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[13]")
        maritalStatus.click()

        optionmaritalStatus = self.driver.find_element(By.XPATH, "//*[@id='liId_Married']")
        optionmaritalStatus.click()
        time.sleep(1)

        indsturyDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[14]")
        indsturyDropdown.click()
        time.sleep(1)

        optionindsturyDropdown= self.driver.find_element(By.XPATH, "//*[@id='liId_Defence']")
        optionindsturyDropdown.click()
        time.sleep(1)

        orgDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[15]")
        orgDropdown.click()
        time.sleep(1)

        optionorgDropdown = self.driver.find_element(By.XPATH, "//*[@id='liId_Public Ltd']")
        optionorgDropdown.click()
        time.sleep(1)

        occDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[17]")
        occDropdown.click()
        time.sleep(1)

        optionoccDropdown = self.driver.find_element(By.XPATH, "//*[@id='liId_Self Employed']")
        optionoccDropdown.click()
        time.sleep(1)

        enterIncome = self.driver.find_element(By.XPATH, "//*[@name='insurerAnnualIncome']")
        enterIncome.send_keys("1100000")
        time.sleep(1)

        spouseDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[18]")
        spouseDropdown.click()
        time.sleep(1)

        optionoccDropdown = self.driver.find_element(By.XPATH, "//*[@id='liId_Salaried']")
        optionoccDropdown.click()
        time.sleep(1)

        spouseIncome = self.driver.find_element(By.XPATH, "//*[@name='insurerSpouseAnnualIncome']")
        spouseIncome.send_keys("1000000")
        time.sleep(1)

        spouseInsurerCover = self.driver.find_element(By.XPATH, "//*[@name='insurerSpouseTotalInsuranceCover']")
        spouseInsurerCover.send_keys("100000")
        time.sleep(1)

        hazardous = self.driver.find_element(By.XPATH, "//*[@for='InsurerHazardousActivitiesNo']")
        hazardous.click()

        criminal = self.driver.find_element(By.XPATH, "//*[@for='InsurerCriminalChargesNo']")
        criminal.click()

        holiday = self.driver.find_element(By.XPATH, "//*[@for='insurerTravelOrResideAbroadNo']")
        holiday.click()


        heightInFeet = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[19]")
        heightInFeet.click()
        time.sleep(1)
        selectHeightInFeet = self.driver.find_element(By.XPATH, "//*[@id='liId_5']")
        selectHeightInFeet.click()

        heightInInches = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[20]")
        heightInInches.click()
        time.sleep(1)
        selectHeightInInches = self.driver.find_element(By.XPATH, "//*[@id='liId_5']")
        selectHeightInInches.click()
        time.sleep(1)

        weightFill = self.driver.find_element(By.XPATH, "//*[@name='insurerWeightInKgs']")
        weightFill.click()
        weightFill.send_keys("65")
        time.sleep(2)

        btnProceedOnPage4 = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        btnProceedOnPage4.click()
        print("Proceed Button Clicked.")
        time.sleep(1)

        #####################################3
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Proceed')]")))
        btnProceedOnPage3 = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        btnProceedOnPage3.click()

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='popupProceed']")))

        verificationLinkPopUp = self.driver.find_element(By.XPATH, "//*[@id='popupProceed']")
        verificationLinkPopUp.click()
        print("Verification Link Sent.")

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
auto.newApplicationFormOneStepFive()