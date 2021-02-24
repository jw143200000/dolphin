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
    # SPARC- 782058,ABBBY6754 | MNYL@2020, max@1234
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
        panFill.send_keys("AKJPJ8800A")

        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@name='mobileNumber']")))
        mobNumberFill= self.driver.find_element(By.XPATH,"//*[@name='mobileNumber']")
        mobNumberFill.send_keys("7042970921")

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@name='email']")))
        emailFill = self.driver.find_element(By.XPATH, "//*[@name='email']")
        emailFill.send_keys("kartik.bisaria@kelltontech.com")

        btnProceed = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        btnProceed.click()

        time.sleep(3)

    def newApplicationFormOneStepTwo(self):

        windowBefore = self.driver.window_handles[0]
        print("Window Before=",windowBefore)

        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@name='firstName']")))
        firstNameFill = self.driver.find_element(By.XPATH,"//*[@name='firstName']")
        firstNameFill.send_keys("NicholasYuvesh")

        lastNameFill = self.driver.find_element(By.XPATH,"//*[@name='lastName']")
        lastNameFill.send_keys("Jonestan")

        lifegenderSelected = self.driver.find_element(By.XPATH, "(//*[contains(text(),'Female')])[1]")
        lifegenderSelected.click()
        print("Gender Clicked")
        time.sleep(1)

        calendarFill= self.driver.find_element(By.XPATH,"//*[@name='dateOfBirth']")
        calendarFill.click()

        yearDropdown = self.driver.find_element(By.XPATH,"//*[@class='react-datepicker__year-select']")
        yearSel = Select(yearDropdown)
        yearSel.select_by_value('1975')

        monthDropdown = self.driver.find_element(By.XPATH,"//*[@class='react-datepicker__month-select']")
        monthSel= Select(monthDropdown)
        monthSel.select_by_value('1')

        dateSel=self.driver.find_element(By.XPATH,"//*[@aria-label='day-2']")
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
        stateFill.send_keys('HARYANA')
        time.sleep(1)
        stateToSel=self.driver.find_element(By.XPATH, "//*[contains(text(),'HAR')]")
        stateToSel.click()
        time.sleep(1)
        print("State Filled")

        cityFill = self.driver.find_element(By.XPATH, "//*[@name='permanentCity']")
        cityFill.click()
        cityFill.send_keys('GURUGRAM')
        time.sleep(1)
        cityToSel= self.driver.find_element(By.XPATH, "//*[contains(text(),'GUR')]")
        cityToSel.click()
        time.sleep(1)
        print("City Filled")

        pinToFill= self.driver.find_element(By.XPATH, "//*[@name='permanentPinCode']")
        pinToFill.send_keys('515331')
        time.sleep(1)

        alternateNumberToFill = self.driver.find_element(By.XPATH, "//*[@name='alternateMobileNo']")
        alternateNumberToFill.send_keys('7977412402')
        print("Alternate number Filled")
        time.sleep(1)

        proofDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[2]")
        proofDropdown.click()
        time.sleep(2)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='liId_Voter ID']")))
        proofSel = self.driver.find_element(By.XPATH, "//*[@id='liId_Aadhaar']")
        proofSel.click()
        time.sleep(1)
        addProofEnter = self.driver.find_element(By.XPATH,
                                                 "//*[@name= 'aadhaarNo']")
        addProofEnter.send_keys("123456789012")
        time.sleep(1)

        ##############Life Insured Details################333
        lifeToInsured = self.driver.find_element(By.XPATH,
                                                 "//*[@name= 'insurerName']")
        lifeToInsured.send_keys("Jaidev Singh Nirmal")
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
        yearSel.select_by_value('1981')

        lifemonthDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__month-select']")
        monthSel = Select(lifemonthDropdown)
        monthSel.select_by_value('1')

        dateSel = self.driver.find_element(By.XPATH, "//*[@aria-label='day-3']")
        dateSel.click()
        time.sleep(2)

        liferelationshipDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[4]")
        liferelationshipDropdown.click()
        time.sleep(1)

        optionInLifeRelationshipProposer = self.driver.find_element(By.XPATH, "//*[@id ='liId_Daughter']")
        optionInLifeRelationshipProposer.click()
        print("Relationship Daughter  Selected.")
        time.sleep(1)

        #################################################33
        purposeOfInsuranceDropdown= self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[6]")
        purposeOfInsuranceDropdown.click()
        time.sleep(1)

        optionInInsuranceDropdown=self.driver.find_element(By.XPATH,"//*[contains(text(),'Protection')]")
        optionInInsuranceDropdown.click()
        print("Retirement Selected")

        lifeStageDropdown= self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[7]")
        lifeStageDropdown.click()
        time.sleep(1)

        optionInLifeStage= self.driver.find_element(By.XPATH, "//*[contains(text(), 'Married with children')]")
        optionInLifeStage.click()
        print("Married Selected")

        grossIncomeFill = self.driver.find_element(By.XPATH, "//*[@name='income']")
        grossIncomeFill.send_keys('700000')
        print("Gross Income Entered")

        existingPolicy=self.driver.find_element(By.XPATH, "(//*[contains(text(),'Yes')])[2]")
        existingPolicy.click()

        sumAssuredFill = self.driver.find_element(By.XPATH, "//*[@name='existingLICover']")
        sumAssuredFill.send_keys('300000')
        print("Gross Income Entered")

        occupationDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[8]")
        occupationDropdown.click()
        optionInOccupation = self.driver.find_element(By.XPATH, "//*[@id='liId_Self Employed']")
        optionInOccupation.click()
        print("Salaried Selected")
        time.sleep(1)

        recommendProduct = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[10]")
        recommendProduct.click()
        time.sleep(5)
        recommendProduct.click()
        time.sleep(1)
        optionInRecommendProduct = self.driver.find_element(By.XPATH, "//*[@id='liId_Select Another Product']")
        # optionInRecommendProduct = self.driver.find_element(By.XPATH, "//*[@id='liId_Max Life S']")
        optionInRecommendProduct.click()
        print("Product Selected")
        time.sleep(2)

        premiumPaymentTerm = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[11]")
        premiumPaymentTerm.click()
        time.sleep(1)
        optionInPremiumPaymentTerm = self.driver.find_element(By.XPATH, "//*[@id='liId_Max Life Saral Jeevan Bima']")
        optionInPremiumPaymentTerm.click()
        print("Premium Payment Selected")
        time.sleep(2)

        variantType = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[12]")
        variantType.click()
        time.sleep(1)
        optionInvariantType = self.driver.find_element(By.XPATH, "//*[@id='liId_Regular Pay']")
        optionInvariantType.click()
        print("Premium Payment Selected")
        time.sleep(1)


        premiumPaymentTerm = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[13]")
        premiumPaymentTerm.click()
        time.sleep(1)
        optionInPremiumPaymentTerm = self.driver.find_element(By.XPATH, "//*[@id='liId_12']")
        optionInPremiumPaymentTerm.click()
        print("Premium Payment Selected")
        time.sleep(1)

        policyTerm = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[14]")
        policyTerm.click()
        time.sleep(1)
        optionInPolicyTerm = self.driver.find_element(By.XPATH, "//*[@id='liId_12']")
        optionInPolicyTerm.click()
        print("Policy Term Selected")
        time.sleep(1)

        paymentFrequency = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[15]")
        paymentFrequency.click()
        time.sleep(1)
        optionInpaymentFrequency = self.driver.find_element(By.XPATH, "//*[@id='liId_Monthly']")
        optionInpaymentFrequency.click()
        print("Mode Of Payment Selected")
        time.sleep(1)

        clickOnCrosOfMonthly = self.driver.find_element(By.XPATH,
                                                "//*[@d='M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z']")
        clickOnCrosOfMonthly.click()


        time.sleep(1)
        SAFill = self.driver.find_element(By.XPATH, "//*[@name='sumAssured']")
        SAFill.send_keys('550000')
        print("SA Entered")

        SmokingHabit = self.driver.find_element(By.XPATH, "//*[@for='smoke']")
        SmokingHabit.click()
        time.sleep(1)


        # dividendDropdownSelected= self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[14]")
        # dividendDropdownSelected.click()
        # print("Dividend dropdown Clicked")
        # time.sleep(2)

        # optionIndividendDropdownSelected = self.driver.find_element(By.XPATH, "//*[@id='liId_Premium Offset']")
        # optionIndividendDropdownSelected.click()
        # print ("Premium Offset selected")
        # time.sleep(1)

        buttonProceedClick = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        buttonProceedClick.click()
        time.sleep(1)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@id='popupProceed'])[1]")))
        buttonYes = self.driver.find_element(By.XPATH, "(//*[@id='popupProceed'])[1]")
        buttonYes.click()

        ########################### step 3 #############################
        time.sleep(8)

        self.driver.switch_to_window(windowBefore)
        time.sleep(2)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@name='fatherName']")))
        fatherNameFill= self.driver.find_element(By.XPATH, "//*[@name='fatherName']")
        fatherNameFill.send_keys("Kiran Raj Shukla")

        motherNameFill = self.driver.find_element(By.XPATH, "//*[@name='motherName']")
        motherNameFill.send_keys("Mandodari")

        maritalStatus = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[2]")
        maritalStatus.click()
        time.sleep(1)
        optionInMaritalStage = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Married')]")
        optionInMaritalStage.click()
        print("Married Selected")

        educationSelect = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[3]")
        educationSelect.click()
        time.sleep(1)
        optionInEducationDropdown= self.driver.find_element(By.XPATH, "//*[@id='liId_Post Graduate']")
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
        optionInOrganisationSelect = self.driver.find_element(By.XPATH, "//*[@id='liId_Private Voluntary Organization (PVO)']")
        optionInOrganisationSelect.click()
        print("Organisation Selected")
        time.sleep(1)

        natureSelect = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[6]")
        natureSelect.click()
        time.sleep(1)
        optionInnatureSelect = self.driver.find_element(By.XPATH,
                                                              "//*[@id='liId_Combat Role']")
        optionInnatureSelect.click()
        print("Combat Selected")
        time.sleep(1)

        sensitiveBorder = self.driver.find_element(By.XPATH, "(//*[contains(text(),'No')])[1]")
        sensitiveBorder.click()

        preferredLanguage= self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[7]")
        preferredLanguage.click()
        time.sleep(1)
        optionInPreferredLanguage = self.driver.find_element(By.XPATH, "//*[@id='liId_Punjabi']")
        optionInPreferredLanguage.click()
        print("Hindi Selected")
        time.sleep(1)

        bankFill = self.driver.find_element(By.XPATH, "//*[@name='bankAccountNo']")
        bankFill.send_keys("99999999999999")

        nameOfAccount = self.driver.find_element(By.XPATH, "//*[@name='bankAccountHolderName']")
        nameOfAccount.send_keys("Mr. Jatin Singh Swaroop")

        nameOfIFSCcode = self.driver.find_element(By.XPATH, "//*[@name='bankAccountIFSC']")
        nameOfIFSCcode.send_keys("SBIN0000845")

        codeMICR = self.driver.find_element(By.XPATH, "//*[@name='bankAccountMICR']")
        codeMICR.send_keys("515002206")
        time.sleep(3)

        accountType = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[9]")
        accountType.click()
        time.sleep(2)

        accountTypeSelect = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Savings Account')]")
        accountTypeSelect.click()
        print("Account Type Selected.")

        # ##################Life Insured Details
        fatherNameFill = self.driver.find_element(By.XPATH, "//*[@name='insurerFatherName']")
        fatherNameFill.send_keys("Ravana Father")

        dobDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[11]")
        dobDropdown.click()
        optiondobDropdown = self.driver.find_element(By.XPATH, "//*[@id='liId_Voter ID']")
        optiondobDropdown.click()
        time.sleep(1)

        educationdropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[12]")
        educationdropdown.click()

        optioneducationdropdownn = self.driver.find_element(By.XPATH, "//*[@id='liId_Senior School(12th Pass)']")
        optioneducationdropdownn.click()
        time.sleep(1)

        maritalStatus = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[13]")
        maritalStatus.click()
        time.sleep(1)
        optionmaritalStatus = self.driver.find_element(By.XPATH, "//*[@id='liId_Married']")
        optionmaritalStatus.click()
        time.sleep(1)

        pregnant = self.driver.find_element(By.XPATH, "(//*[contains(text(),'No')])[2]")
        pregnant.click()

        indsturyDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[14]")
        indsturyDropdown.click()
        time.sleep(1)
        optionindsturyDropdown= self.driver.find_element(By.XPATH, "//*[@id='liId_Aviation/AirForce']")
        optionindsturyDropdown.click()
        time.sleep(1)

        orgDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[15]")
        orgDropdown.click()
        time.sleep(1)
        optionorgDropdown = self.driver.find_element(By.XPATH, "//*[@id='liId_Private Voluntary Organization (PVO)']")
        optionorgDropdown.click()
        time.sleep(1)

        natureDuties = self.driver.find_element(By.XPATH, "(//*[contains(text(),'No')])[3]")
        natureDuties.click()
        time.sleep(1)

        orgDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[16]")
        orgDropdown.click()
        time.sleep(1)
        optionorgDropdown = self.driver.find_element(By.XPATH, "//*[@id ='liId_Agriculture']")
        optionorgDropdown.click()
        time.sleep(1)

        orgDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[17]")
        orgDropdown.click()
        time.sleep(1)
        optionorgDropdown = self.driver.find_element(By.XPATH, "//*[@id ='liId_Agriculture']")
        optionorgDropdown.click()
        time.sleep(1)

        enterIncome = self.driver.find_element(By.XPATH, "//*[@name='insurerAnnualIncome']")
        enterIncome.send_keys("800000")
        time.sleep(1)

        enterIncome = self.driver.find_element(By.XPATH, "//*[@name='insurerSpouseAnnualIncome']")
        enterIncome.send_keys("1000000")
        time.sleep(1)

        enterIncome = self.driver.find_element(By.XPATH, "//*[@name='insurerSpouseTotalInsuranceCover']")
        enterIncome.send_keys("1000000")
        time.sleep(1)

        # enterorg = self.driver.find_element(By.XPATH, "//*[@name='insurerCompanyName']")
        # enterorg.send_keys("MAX")
        # time.sleep(1)

        hazardous = self.driver.find_element(By.XPATH, "//*[@for='InsurerHazardousActivitiesNo']")
        hazardous.click()

        criminal = self.driver.find_element(By.XPATH, "//*[@for='InsurerCriminalChargesNo']")
        criminal.click()

        holiday = self.driver.find_element(By.XPATH, "//*[@for='insurerTravelOrResideAbroadNo']")
        holiday.click()


        heightInFeet = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[18]")
        heightInFeet.click()
        time.sleep(1)
        selectHeightInFeet = self.driver.find_element(By.XPATH, "//*[@id='liId_5']")
        selectHeightInFeet.click()

        heightInInches = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[19]")
        heightInInches.click()
        time.sleep(1)
        selectHeightInInches = self.driver.find_element(By.XPATH, "//*[@id='liId_5']")
        selectHeightInInches.click()
        time.sleep(1)

        weightFill = self.driver.find_element(By.XPATH, "//*[@name='insurerWeightInKgs']")
        weightFill.click()
        weightFill.send_keys("70")
        time.sleep(2)

        btnProceedOnPage4 = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        btnProceedOnPage4.click()
        print("Proceed Button Clicked.")
        time.sleep(1)

        spouseOccupation = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[4]")
        spouseOccupation.click()
        time.sleep(1)
        optionspouseOccupation = self.driver.find_element(By.XPATH, "//*[@id ='liId_Housewife']")
        optionspouseOccupation.click()
        time.sleep(1)

        enterSalary = self.driver.find_element(By.XPATH, "//*[@name='spouseAnnualIncome']")
        enterSalary.send_keys("1000000")
        time.sleep(1)

        enterTotal = self.driver.find_element(By.XPATH, "//*[@name='spouseTotalInsuranceCover']")
        enterTotal.send_keys("10000000")
        time.sleep(1)

        pregnantYes = self.driver.find_element(By.XPATH, "//*[@for='PregnantYes']")
        pregnantYes.click()

        monthsDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[6]")
        monthsDropdown.click()
        time.sleep(1)
        optionmonthsDropdown= self.driver.find_element(By.XPATH, "//*[@id ='liId_6']")
        optionmonthsDropdown.click()
        time.sleep(1)

        complicationsYes = self.driver.find_element(By.XPATH, "//*[@for='PregnancyComplicationsYes']")
        complicationsYes.click()

        enterDetails = self.driver.find_element(By.XPATH, "//*[@name='pregnancyDetails']")
        enterDetails.send_keys("TESTing")
        time.sleep(1)


        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Proceed')]")))
        btnProceedOnPage4 = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        btnProceedOnPage4.click()
        print("Proceed Button Clicked.")
        time.sleep(1)



        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='popupProceed']")))

        verificationLinkPopUp = self.driver.find_element(By.XPATH, "//*[@id='popupProceed']")
        verificationLinkPopUp.click()
        print("Verification Link Sent.")
        time.sleep(2)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Payment')]")))
        paymentStep5 = self.driver.find_element(By.XPATH, "//*[contains(text(),'Payment')]")
        paymentStep5.click()

    def newApplicationFormOneStepFive(self):

        # self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Payment')]")))
        # paymentStep5= self.driver.find_element(By.XPATH, "//*[contains(text(),'Payment')]")
        # paymentStep5.click()

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
# auto.newApplicationFormOneStepFive()