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
        username.send_keys("934384")

        password= self.driver.find_element(By.ID, "password")
        password.send_keys("MNYL@2020")

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
        panFill.send_keys("AHQPC9496B")

        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@name='mobileNumber']")))
        mobNumberFill= self.driver.find_element(By.XPATH,"//*[@name='mobileNumber']")
        mobNumberFill.send_keys("7042970921")

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
        firstNameFill.send_keys("Suman")

        lastNameFill = self.driver.find_element(By.XPATH,"//*[@name='lastName']")
        lastNameFill.send_keys("Singh")

        genderSelected = self.driver.find_element(By.XPATH, "(//*[contains(text(),'Female')])[1]")
        genderSelected.click()
        print("Gender Clicked")
        time.sleep(1)

        calendarFill = self.driver.find_element(By.XPATH, "//*[@name='dateOfBirth']")
        calendarFill.click()

        yearDropdown = self.driver.find_element(By.XPATH,"//*[@class='react-datepicker__year-select']")
        yearSel = Select(yearDropdown)
        yearSel.select_by_value('1987')

        monthDropdown = self.driver.find_element(By.XPATH,"//*[@class='react-datepicker__month-select']")
        monthSel= Select(monthDropdown)
        monthSel.select_by_value('10')

        dateSel=self.driver.find_element(By.XPATH,"//*[@aria-label='day-24']")
        dateSel.click()
        time.sleep(2)
        #
        houseNumberFill= self.driver.find_element(By.XPATH,"//*[@name='permanentHouseNo']")
        houseNumberFill.send_keys('House No. 9')

        roadNumberFill = self.driver.find_element(By.XPATH, "//*[@name='permanentRoadNo']")
        roadNumberFill.send_keys('Phase 5')

        countryFill = self.driver.find_element(By.XPATH, "//*[@name='permanentCountry']")
        countryFill.send_keys('India')
        time.sleep(1)
        countryToSel = self.driver.find_element(By.XPATH, "//*[contains(text(),'Ind')]")
        countryToSel.click()
        time.sleep(1)
        print("Country Filled")
        stateFill = self.driver.find_element(By.XPATH, "//*[@name='permanentState']")
        stateFill.send_keys('TAMIL NADU')
        time.sleep(1)
        stateToSel=self.driver.find_element(By.XPATH, "//*[contains(text(),'TAMIL')]")
        stateToSel.click()
        time.sleep(1)
        print("State Filled")

        cityFill = self.driver.find_element(By.XPATH, "//*[@name='permanentCity']")
        cityFill.click()
        cityFill.send_keys('SIVAGANGA')
        time.sleep(2)
        cityToSel= self.driver.find_element(By.XPATH, "//*[contains(text(),'SIVAGANGA')]")
        cityToSel.click()
        time.sleep(1)
        print("City Filled")

        pinToFill= self.driver.find_element(By.XPATH, "//*[@name='permanentPinCode']")
        pinToFill.send_keys('112312')
        time.sleep(1)

        alternateNumberToFill = self.driver.find_element(By.XPATH, "//*[@name='alternateMobileNo']")
        alternateNumberToFill.send_keys('7977412402')
        print("Alternate number Filled")
        time.sleep(1)

        stdCode = self.driver.find_element(By.XPATH, "//*[@name='stdCode']")
        stdCode.send_keys('65656')
        print("STD number Filled")
        time.sleep(1)

        landlineNumber = self.driver.find_element(By.XPATH, "//*[@name='alternateLandlineNo']")
        landlineNumber.send_keys('78787878')
        print("Landline number Filled")
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
        # addProofEnter.send_keys("VT387646783")
        time.sleep(1)

        #######Communication Send To Address########33
        commAddress = self.driver.find_element(By.XPATH, "//*[@for='No']")
        commAddress.click()

        houseNumberFill = self.driver.find_element(By.XPATH, "//*[@name='communicationHouseNo']")
        houseNumberFill.send_keys('92')

        roadNumberFill = self.driver.find_element(By.XPATH, "//*[@name='communicationRoadNo']")
        roadNumberFill.send_keys('53')

        villageFill = self.driver.find_element(By.XPATH, "//*[@name='communicationVillageTown']")
        villageFill.send_keys('Vilage')

        landmarkFill = self.driver.find_element(By.XPATH, "//*[@name='communicationLandmark']")
        landmarkFill.send_keys('Landmark')
        time.sleep(1)

        countryFill = self.driver.find_element(By.XPATH, "//*[@name='communicationCountry']")
        countryFill.send_keys('GREENLAND')
        time.sleep(1)
        countryToSel = self.driver.find_element(By.XPATH, "//*[contains(text(),'Green')]")
        countryToSel.click()
        time.sleep(1)
        print("Country Filled")
        stateFill = self.driver.find_element(By.XPATH, "//*[@name='communicationState']")
        stateFill.send_keys('Land')
        # time.sleep(1)
        # stateToSel = self.driver.find_element(By.XPATH, "//*[contains(text(),'TAMIL NADU')]")
        # stateToSel.click()
        # time.sleep(1)
        print("State Filled")
        time.sleep(1)

        cityFill = self.driver.find_element(By.XPATH, "//*[@name='communicationCity']")
        cityFill.click()
        cityFill.send_keys('SIV')
        # time.sleep(2)
        # cityToSel = self.driver.find_element(By.XPATH, "//*[contains(text(),'SIVAGANGA')]")
        # cityToSel.click()
        # time.sleep(1)
        print("City Filled")
        time.sleep(1)

        pinToFill = self.driver.find_element(By.XPATH, "//*[@name='communicationPinCode']")
        pinToFill.send_keys('6545645654')
        time.sleep(1)

        alternateNumberToFill = self.driver.find_element(By.XPATH, "//*[@name='communicationAlternateMobileNo']")
        alternateNumberToFill.send_keys('978987999898897')
        print("Alternate number Filled")
        time.sleep(1)

        stdCode = self.driver.find_element(By.XPATH, "//*[@name='communicationStdCode']")
        stdCode.send_keys('21212')
        print("STD number Filled")
        time.sleep(1)

        landlineNumber = self.driver.find_element(By.XPATH, "//*[@name='communicationAlternateLandlineNo']")
        landlineNumber.send_keys('32323232')
        print("Landline number Filled")
        time.sleep(1)

        proofDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[3]")
        proofDropdown.click()
        time.sleep(1)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='liId_Copy of latest overseas bank account not more than 3 months old or existing NRE / NRO account statement carrying overseas address']")))
        proofSel = self.driver.find_element(By.XPATH, "//*[@id='liId_Copy of latest overseas bank account not more than 3 months old or existing NRE / NRO account statement carrying overseas address']")
        proofSel.click()
        time.sleep(1)
        addProofEnter = self.driver.find_element(By.XPATH,
                                                 "//*[@name= 'proofNumber']")
        addProofEnter.send_keys("565674565465465654")
        time.sleep(1)

        ##############Life Insured Details################333
        lifeToInsured = self.driver.find_element(By.XPATH,
                                                 "//*[@name= 'insurerName']")
        lifeToInsured.send_keys("Prithivi Singh")
        time.sleep(1)

        lifegenderSelected = self.driver.find_element(By.XPATH, "(//*[contains(text(),'Male')])[2]")
        lifegenderSelected.click()
        print("Gender Clicked")
        time.sleep(1)

        lifecalendarFill = self.driver.find_element(By.XPATH, "//*[@name='insurerDateOfBirth']")
        lifecalendarFill.click()
        time.sleep(1)

        lifeyearDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__year-select']")
        yearSel = Select(lifeyearDropdown)
        yearSel.select_by_value('1987')

        lifemonthDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__month-select']")
        monthSel = Select(lifemonthDropdown)
        monthSel.select_by_value('11')

        dateSel = self.driver.find_element(By.XPATH, "//*[@aria-label='day-31']")
        dateSel.click()
        time.sleep(2)

        liferelationshipDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[5]")
        liferelationshipDropdown.click()
        time.sleep(1)

        optionInLifeRelationshipProposer = self.driver.find_element(By.XPATH, "//*[@id ='liId_Others']")
        optionInLifeRelationshipProposer.click()
        print("Relationship Wife Selected.")
        time.sleep(1)

        fosterRelationship= self.driver.find_element(By.XPATH, "//*[@name='relationshipWithProposerWhenOther']")
        fosterRelationship.send_keys("Foster")
        time.sleep(1)
        optioninfosterRelationship = self.driver.find_element(By.XPATH, "(//*[contains(text(),'Fos')])[1]")
        optioninfosterRelationship.click()
        time.sleep(1)


        #################################################
        purposeOfInsuranceDropdown= self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[7]")
        purposeOfInsuranceDropdown.click()
        time.sleep(1)

        optionInInsuranceDropdown=self.driver.find_element(By.XPATH,"//*[contains(text(),'Protection')]")
        optionInInsuranceDropdown.click()
        print("Retirement Selected")

        lifeStageDropdown= self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[8]")
        lifeStageDropdown.click()

        optionInLifeStage= self.driver.find_element(By.XPATH, "//*[@id='liId_Married with no children']")
        optionInLifeStage.click()
        print("Married Selected")

        grossIncomeFill = self.driver.find_element(By.XPATH, "//*[@name='income']")
        grossIncomeFill.send_keys('1200000')
        print("Gross Income Entered")
        time.sleep(1)

        existingPolicy=self.driver.find_element(By.XPATH, "(//*[contains(text(),'No')])[4]")
        existingPolicy.click()

        occupationDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[9]")
        occupationDropdown.click()
        time.sleep(1)
        optionInOccupation = self.driver.find_element(By.XPATH, "//*[@id='liId_Professional']")
        optionInOccupation.click()
        print("Professional Selected")
        time.sleep(2)

        recommendProduct = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[11]")
        recommendProduct.click()
        time.sleep(5)
        recommendProduct.click()
        time.sleep(1)
        optionInRecommendProduct = self.driver.find_element(By.XPATH, "//*[@id='liId_Max Life Super Term Plan']")
        optionInRecommendProduct.click()
        print("Product Selected")
        time.sleep(2)

        premiumPaymentTerm = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[12]")
        premiumPaymentTerm.click()
        time.sleep(1)
        optionInPremiumPaymentTerm = self.driver.find_element(By.XPATH, "//*[@id='liId_35']")
        optionInPremiumPaymentTerm.click()
        print("Premium Payment Selected")
        time.sleep(2)

        policyTerm = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[13]")
        policyTerm.click()
        time.sleep(1)
        optionInPolicyTerm = self.driver.find_element(By.XPATH, "//*[@id='liId_35']")
        optionInPolicyTerm.click()
        print("Policy Term Selected")
        time.sleep(2)

        levelSA = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[14]")
        levelSA.click()
        time.sleep(1)
        optionInSA = self.driver.find_element(By.XPATH, "//*[@id='liId_Level Sum Assured']")
        optionInSA.click()
        print("Level Selected")
        time.sleep(2)

        SAFill = self.driver.find_element(By.XPATH, "//*[@name='sumAssured']")
        SAFill.send_keys('7500000')
        print("SA Entered")

        SmokingHabit = self.driver.find_element(By.XPATH, "//*[@for='nosmoke']")
        SmokingHabit.click()
        time.sleep(1)

        dividentAdjustment = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[15]")
        dividentAdjustment.click()
        time.sleep(1)

        optionIndividentAdjustment = self.driver.find_element(By.XPATH, "//*[@id='liId_No Adjustment']")
        optionIndividentAdjustment.click()
        print("Dividend Selected")
        time.sleep(2)

        buttonProceedClick = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        buttonProceedClick.click()
        time.sleep(1)

        # self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[@id='popupProceed'])[1]")))
        # buttonYes= self.driver.find_element(By.XPATH, "(//*[@id='popupProceed'])[1]")
        # buttonYes.click()

        ########################### step 3 #############################
        time.sleep(8)

        self.driver.switch_to_window(windowBefore)
        time.sleep(2)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@name='fatherName']")))
        fatherNameFill = self.driver.find_element(By.XPATH, "//*[@name='fatherName']")
        fatherNameFill.send_keys("Manish")

        motherNameFill = self.driver.find_element(By.XPATH, "//*[@name='motherName']")
        motherNameFill.send_keys("Manisha")

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
        optionInEducationDropdown = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Graduate')][1]")
        optionInEducationDropdown.click()
        print("Education Selected")
        time.sleep(1)

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
        optionInOrganisationSelect = self.driver.find_element(By.XPATH, "//*[@id='liId_Pvt Ltd']")
        optionInOrganisationSelect.click()
        print("Organisation Selected")
        time.sleep(1)

        offshorelocation = self.driver.find_element(By.XPATH, "//*[@for='io1']")
        offshorelocation.click()
        time.sleep(1)

        preferredLanguage= self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[6]")
        preferredLanguage.click()
        time.sleep(1)
        optionInPreferredLanguage = self.driver.find_element(By.XPATH, "//*[@id='liId_Bengali']")
        optionInPreferredLanguage.click()
        print("Hindi Selected")
        time.sleep(1)

        bankFill = self.driver.find_element(By.XPATH, "//*[@name='bankAccountNo']")
        bankFill.send_keys("99999999999999")

        nameOfAccount = self.driver.find_element(By.XPATH, "//*[@name='bankAccountHolderName']")
        nameOfAccount.send_keys("NameName")

        nameOfIFSCcode = self.driver.find_element(By.XPATH, "//*[@name='bankAccountIFSC']")
        nameOfIFSCcode.send_keys("SBIN0002300")

        codeMICR = self.driver.find_element(By.XPATH, "//*[@name='bankAccountMICR']")
        codeMICR.send_keys("110002233")
        time.sleep(3)

        accountType = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[8]")
        accountType.click()
        time.sleep(2)

        accountTypeSelect = self.driver.find_element(By.XPATH, "//*[contains(text(), 'NRE')]")
        accountTypeSelect.click()
        print("Account Type Selected.")
        time.sleep(2)
        ##################NRI Details #######################3
        passport = self.driver.find_element(By.XPATH, "//*[@name='passportNumber']")
        passport.send_keys("546546546")
        time.sleep(1)

        visaType = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[10]")
        visaType.click()
        time.sleep(1)
        optionInvisaType = self.driver.find_element(By.XPATH, "//*[@id='liId_Working']")
        optionInvisaType.click()
        time.sleep(1)

        validcalendarFill = self.driver.find_element(By.XPATH, "//*[@name='visaExpiryDate']")
        validcalendarFill.click()

        validyearDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__year-select']")
        validyearSel = Select(validyearDropdown)
        validyearSel.select_by_value('2022')

        validmonthDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__month-select']")
        validmonthSel = Select(validmonthDropdown)
        validmonthSel.select_by_value('10')

        validdateSel = self.driver.find_element(By.XPATH, "//*[@aria-label='day-10']")
        validdateSel.click()
        time.sleep(1)

        passport = self.driver.find_element(By.XPATH, "//*[@name='passportNumber']")
        passport.send_keys("546546546")
        time.sleep(1)

        passportCountry = self.driver.find_element(By.XPATH, "//*[@name='passportIssuingCountry']")
        passportCountry.send_keys("Finland")
        time.sleep(1)

        expirecalendarFill = self.driver.find_element(By.XPATH, "//*[@name='passportExpiryDate']")
        expirecalendarFill.click()

        expirevalidyearDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__year-select']")
        expirevalidyearSel = Select(expirevalidyearDropdown)
        expirevalidyearSel.select_by_value('2022')

        expirevalidmonthDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__month-select']")
        expirevalidmonthSel = Select(expirevalidmonthDropdown)
        expirevalidmonthSel.select_by_value('10')

        expirevaliddateSel = self.driver.find_element(By.XPATH, "//*[@aria-label='day-30']")
        expirevaliddateSel.click()
        time.sleep(1)
        print("passport details filled")

        countryResiding = self.driver.find_element(By.XPATH, "//*[@name='nriCountry']")
        countryResiding.send_keys("Finland")
        time.sleep(1)

        lastEntrycalendarFill = self.driver.find_element(By.XPATH, "//*[@name='entryDateToIndia']")
        lastEntrycalendarFill.click()

        lastEntryyearDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__year-select']")
        lastEntryyearSel = Select(lastEntryyearDropdown)
        lastEntryyearSel.select_by_value('2020')

        lastEntrymonthDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__month-select']")
        lastEntryvalidmonthSel = Select(lastEntrymonthDropdown)
        lastEntryvalidmonthSel.select_by_value('10')

        lastEntrydateSel = self.driver.find_element(By.XPATH, "//*[@aria-label='day-30']")
        lastEntrydateSel.click()
        time.sleep(1)
        print("last entry details filled")

        countryType = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[11]")
        countryType.click()
        time.sleep(1)
        australiaCountry = self.driver.find_element(By.XPATH, "(//*[@type='checkbox'])[1]")
        australiaCountry.click()
        time.sleep(1)
        canadaCountry = self.driver.find_element(By.XPATH, "(//*[@type='checkbox'])[3]")
        canadaCountry.click()
        time.sleep(1)
        germanyCountry = self.driver.find_element(By.XPATH, "(//*[@type='checkbox'])[8]")
        germanyCountry.click()
        time.sleep(1)
        irelandCountry = self.driver.find_element(By.XPATH, "(//*[@type='checkbox'])[13]")
        irelandCountry.click()
        time.sleep(1)
        kosovaCountry = self.driver.find_element(By.XPATH, "(//*[@type='checkbox'])[16]")
        kosovaCountry.click()
        time.sleep(1)
        malaysiaCountry = self.driver.find_element(By.XPATH, "(//*[@type='checkbox'])[18]")
        malaysiaCountry.click()
        time.sleep(1)
        polandCountry = self.driver.find_element(By.XPATH, "(//*[@type='checkbox'])[22]")
        polandCountry.click()
        time.sleep(1)
        spainCountry = self.driver.find_element(By.XPATH, "(//*[@type='checkbox'])[27]")
        spainCountry.click()
        time.sleep(1)
        thailandCountry = self.driver.find_element(By.XPATH, "(//*[@type='checkbox'])[29]")
        thailandCountry.click()
        time.sleep(1)
        ukCountry = self.driver.find_element(By.XPATH, "(//*[@type='checkbox'])[30]")
        ukCountry.click()
        time.sleep(1)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@value='Japan']")))
        time.sleep(2)

        countryResidingLaw = self.driver.find_element(By.XPATH, "//*[@name='residenceCountryAsPerTaxLaws']")
        countryResidingLaw.send_keys("Kenya")
        time.sleep(1)

        foreignType =self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[12]")
        foreignType.click()
        time.sleep(1)

        optionInforeignType = self.driver.find_element(By.XPATH, "//*[@id='liId_Resident Registration Number']")
        optionInforeignType.click()
        time.sleep(1)
        identificaitonNumber = self.driver.find_element(By.XPATH, "//*[@name='identificationNo']")
        identificaitonNumber.send_keys("5654654654645654")
        time.sleep(1)
        issuingCountry = self.driver.find_element(By.XPATH, "//*[@name='issuingCountry']")
        issuingCountry.send_keys("May")
        time.sleep(1)
        optionissuingCountry = self.driver.find_element(By.XPATH, "//*[contains(text(),'May')]")
        optionissuingCountry.click()
        time.sleep(1)

        ##################Life Insured Details
        fatherNameFill = self.driver.find_element(By.XPATH, "//*[@name='insurerFatherName']")
        fatherNameFill.send_keys("Raj Nayan")

        dobDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[14]")
        dobDropdown.click()

        optiondobDropdown = self.driver.find_element(By.XPATH, "//*[@id='liId_Driving License']")
        optiondobDropdown.click()
        time.sleep(1)

        educationdropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[15]")
        educationdropdown.click()
        time.sleep(1)
        optioneducationdropdownn = self.driver.find_element(By.XPATH, "//*[@id='liId_Post Graduate']")
        optioneducationdropdownn.click()
        time.sleep(1)

        maritalStatus = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[16]")
        maritalStatus.click()
        time.sleep(1)

        optionmaritalStatus = self.driver.find_element(By.XPATH, "//*[@id='liId_Married']")
        optionmaritalStatus.click()
        time.sleep(1)

        indsturyDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[17]")
        indsturyDropdown.click()

        optionindsturyDropdown= self.driver.find_element(By.XPATH, "//*[@id='liId_Aviation/AirForce']")
        optionindsturyDropdown.click()
        time.sleep(1)

        orgDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[18]")
        orgDropdown.click()
        time.sleep(1)

        optionorgDropdown = self.driver.find_element(By.XPATH, "//*[@id='liId_Society']")
        optionorgDropdown.click()
        time.sleep(1)

        occDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[19]")
        occDropdown.click()
        time.sleep(1)

        optionoccDropdown = self.driver.find_element(By.XPATH, "//*[@id='liId_Professional']")
        optionoccDropdown.click()
        time.sleep(1)

        enterIncome = self.driver.find_element(By.XPATH, "//*[@name='insurerAnnualIncome']")
        enterIncome.send_keys("500000")
        time.sleep(1)

        hobby = self.driver.find_element(By.XPATH, "//*[@for='InsurerHazardousActivitiesNo']")
        hobby.click()

        criminal = self.driver.find_element(By.XPATH, "//*[@for='InsurerCriminalChargesNo']")
        criminal.click()

        holiday = self.driver.find_element(By.XPATH, "//*[@for='insurerTravelOrResideAbroadNo']")
        holiday.click()

        heightInFeet = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[20]")
        heightInFeet.click()
        time.sleep(1)
        selectHeightInFeet = self.driver.find_element(By.XPATH, "//*[@id='liId_5']")
        selectHeightInFeet.click()

        heightInInches = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[21]")
        heightInInches.click()
        time.sleep(1)
        selectHeightInInches = self.driver.find_element(By.XPATH, "//*[@id='liId_5']")
        selectHeightInInches.click()
        time.sleep(1)

        weightFill = self.driver.find_element(By.XPATH, "//*[@name='insurerWeightInKgs']")
        weightFill.click()
        weightFill.send_keys("165")
        time.sleep(2)

        btnProceedOnPage3 = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        btnProceedOnPage3.click()
        print("Proceed Button Clicked.")
        time.sleep(4)

        ############# Payor Details ################
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[contains(text(),'Yes')])[1]")))

        payorDifferent = self.driver.find_element(By.XPATH, "(//*[contains(text(),'Yes')])[1]")
        payorDifferent.click()
        time.sleep(1)

        payorName = self.driver.find_element(By.XPATH, "//*[@name='payorName']")
        payorName.send_keys("S")
        time.sleep(1)

        payorDob = self.driver.find_element(By.XPATH, "//*[@name='payorDateOfBirth']")
        payorDob.click()
        time.sleep(1)

        payorDobDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__year-select']")
        payorDobDropdownSel = Select(payorDobDropdown)
        payorDobDropdownSel.select_by_value('1971')

        payorDobDropdownSel = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__month-select']")
        payorDobDropdownSelSel = Select(payorDobDropdownSel)
        payorDobDropdownSelSel.select_by_value('4')

        payordateSel = self.driver.find_element(By.XPATH, "//*[@aria-label='day-31']")
        payordateSel.click()
        time.sleep(1)
        print("payor Date Select")

        payorAdd = self.driver.find_element(By.XPATH, "//*[@name='payorAddress']")
        payorAdd.send_keys("Add")
        time.sleep(1)

        payorState = self.driver.find_element(By.XPATH, "//*[@name='payorState']")
        payorState.send_keys("BIHA")
        time.sleep(1)
        payorstateToSel = self.driver.find_element(By.XPATH, "//*[contains(text(),'BIH')]")
        payorstateToSel.click()
        time.sleep(1)
        print("State Filled")
        time.sleep(1)

        payorannualIncome = self.driver.find_element(By.XPATH, "//*[@name='payorAnnualIncome']")
        payorannualIncome.send_keys("1000000")
        time.sleep(1)

        payorPAN = self.driver.find_element(By.XPATH, "//*[@name='payorPanNumber']")
        payorPAN.send_keys("AKJPJ8800A")
        time.sleep(1)

        payorRelationship = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[2]")
        payorRelationship.click()
        time.sleep(1)
        optionInpayorRelationship = self.driver.find_element(By.XPATH, "//*[@id='liId_Grandparent']")
        optionInpayorRelationship.click()
        time.sleep(1)

        bankEnter = self.driver.find_element(By.XPATH, "//*[@name='payorBankAccountNo']")
        bankEnter.send_keys("3876839763")
        time.sleep(1)

        bankNameEnter = self.driver.find_element(By.XPATH, "//*[@name='payorBankName']")
        bankNameEnter.send_keys("SBI Bank")
        time.sleep(1)

        bankBranchEnter = self.driver.find_element(By.XPATH, "//*[@name='payorBankBranch']")
        bankBranchEnter.send_keys("New Delhi")
        time.sleep(1)
        ######################################### EIA ###########
        eiaRadio = self.driver.find_element(By.XPATH, "//*[@for='politicallypower3']")
        eiaRadio.click()
        time.sleep(1)

        openNewAccount = self.driver.find_element(By.XPATH, "//*[@for='QA2New']")
        openNewAccount.click()
        time.sleep(1)

        eiaDropdown = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[4]")
        eiaDropdown.click()
        time.sleep(1)
        optionIneiaDropdown = self.driver.find_element(By.XPATH, "//*[@id='liId_NSDL Database Management Limited']")
        optionIneiaDropdown.click()
        time.sleep(1)

        btnProceedOnPage4 = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        btnProceedOnPage4.click()
        print("Proceed Button Clicked.")
        time.sleep(1)

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
        chequeBankName.send_keys('SBI Bank')

        chequeMicrFill = self.driver.find_element(By.XPATH, "//*[@name='paymentChequeMicr']")
        chequeMicrFill.send_keys('110002233')

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