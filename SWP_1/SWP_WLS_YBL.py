from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains as AC
import time

class mProAutomate:

    # Axis - 655393 | india@2020
    # YBL  - 718842 | mnyl@4321 | Customer ID-  29471, 47942, 616658 (222222)
    # DST  - 934384 | MNYL@2020
    # SPARC- 782058 | MNYL@2020
    # Agency- 447660| Mnyl@2020
    #Ingenium- http://ing247test.maxlifeinsurance.com/ingenium/servlet/pageserver?ProcessClassID=SignOn&PageReturn=index&LocaleID=E

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://mprouat.maxlifeinsurance.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        self.wait = WebDriverWait(self.driver, 60)
        action = AC(self.driver)

    def loginFunctionality(self):

        username = self.driver.find_element(By.ID, "userId")
        username.send_keys("718842")

        password= self.driver.find_element(By.ID, "password")
        password.send_keys("mnyl@4321")

        btnSign=self.driver.find_element(By.XPATH,"//*[contains(text(),'SIGN')]")
        btnSign.click()


        btnNewApp=self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@aria-current='page']")))
        print("Login Successful.")

    def newApplicationFormOneStepOne(self):


        self.wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@href='/']")))
        btnNewApplication= self.driver.find_element(By.XPATH,"//*[@href='/']")
        btnNewApplication.click()

        enterCustomerId = self.driver.find_element(By.XPATH, "//*[@name='CustomerID']")
        # enterCustomerId.send_keys("11111111")
        enterCustomerId.send_keys("5995375")
        # enterCustomerId.send_keys("29471")
        # enterCustomerId.send_keys("2461")

        fetchDetailsBtn = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Fetch')]")
        fetchDetailsBtn.click()

        clickOnCross = self.driver.find_element(By.XPATH, "(//*[@d='M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z'])[3]")
        clickOnCross.click()
        # kartik.bisaria@kelltontech.com

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@for='self']")))
        clickOnSelf= self.driver.find_element(By.XPATH, "//*[@for='dependent']")
        time.sleep(8)
        clickOnSelf.click()

        # self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@name='panNumber']")))
        # panFill = self.driver.find_element(By.XPATH, "//*[@name='panNumber']")
        # panFill.send_keys("DVKPK6111E")


        # time.sleep(30)
        #
        # btnProceed = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        # btnProceed.click()

    def newApplicationFormOneStepTwo(self):
        windowBefore = self.driver.window_handles[0]

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@name='alternateMobileNo']")))

        alternateMobileNumber= self.driver.find_element(By.XPATH, "//*[@name='alternateMobileNo']")
        alternateMobileNumber.send_keys("9650479781")

        # stdCode = self.driver.find_element(By.XPATH, "//*[@name='stdCode']")
        # stdCode.send_keys("011")

        ##############Life Insured Details################
        lifeToInsured = self.driver.find_element(By.XPATH,
                                                 "//*[@name= 'insurerName']")
        lifeToInsured.send_keys("Ram")
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
        yearSel.select_by_value('1975')
        # yearSel.select_by_value('1990')

        lifemonthDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__month-select']")
        monthSel = Select(lifemonthDropdown)
        # monthSel.select_by_value('11')
        monthSel.select_by_value('1')

        # dateSel = self.driver.find_element(By.XPATH, "//*[@aria-label='day-22']")
        dateSel = self.driver.find_element(By.XPATH, "//*[@aria-label='day-12']")
        dateSel.click()
        time.sleep(2)

        liferelationshipDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[3]")
        liferelationshipDropdown.click()
        time.sleep(1)

        optionInLifeRelationshipProposer = self.driver.find_element(By.XPATH, "//*[@id ='liId_Son']")
        optionInLifeRelationshipProposer.click()
        print("Relationship Father Selected.")
        time.sleep(1)
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

        purposeOfInsuranceDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[5]")
        purposeOfInsuranceDropdown.click()

        optionInInsuranceDropdown = self.driver.find_element(By.XPATH, "//*[@id='liId_Retirement']")
        optionInInsuranceDropdown.click()
        print("Retirement Selected")

        lifeStageDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[6]")
        lifeStageDropdown.click()

        optionInLifeStage = self.driver.find_element(By.XPATH, "//*[@id='liId_Married with children']")
        optionInLifeStage.click()
        print("Married Selected")

        grossIncomeFill = self.driver.find_element(By.XPATH, "//*[@name='income']")
        grossIncomeFill.send_keys('1200000')
        print("Gross Income Entered")

        existingPolicy = self.driver.find_element(By.XPATH, "(//*[contains(text(),'No')])[4]")
        existingPolicy.click()

        occupationDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[7]")
        occupationDropdown.click()
        optionInOccupation = self.driver.find_element(By.XPATH, "//*[@id='liId_Salaried']")
        optionInOccupation.click()
        print("Salaried Selected")
        time.sleep(2)

        recommendProduct = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[9]")
        recommendProduct.click()
        time.sleep(8)
        recommendProduct.click()
        time.sleep(1)
        optionInRecommendProduct = self.driver.find_element(By.XPATH, "//*[@id='liId_Max Life Smart Wealth Plan']")
        optionInRecommendProduct.click()
        print("Product Selected")
        time.sleep(1)

        variantDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[10]")
        variantDropdown.click()
        time.sleep(1)
        optionInvariantDropdown = self.driver.find_element(By.XPATH, "//*[@id='liId_Whole Life Income']")
        optionInvariantDropdown.click()
        print("Premium Payment Selected")
        time.sleep(2)

        premiumPaymentTerm = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[11]")
        premiumPaymentTerm.click()
        time.sleep(1)
        optionInPremiumPaymentTerm = self.driver.find_element(By.XPATH, "//*[@id='liId_1']")
        optionInPremiumPaymentTerm.click()
        print("Premium Payment Selected")
        time.sleep(2)

        policyTerm = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[12]")
        policyTerm.click()
        time.sleep(1)
        # optionInPolicyTerm = self.driver.find_element(By.XPATH, "//*[@id='liId_32']")
        optionInPolicyTerm = self.driver.find_element(By.XPATH, "//*[@id='liId_5']")
        optionInPolicyTerm.click()
        print("Policy Term Selected")
        time.sleep(2)

        mode = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[13]")
        mode.click()
        time.sleep(1)
        modeofPayment = self.driver.find_element(By.XPATH, "//*[@id='liId_Single']")
        modeofPayment.click()
        print("Annual Selected")
        time.sleep(2)

        frequency = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[14]")
        frequency.click()
        time.sleep(1)
        optionInfrequency = self.driver.find_element(By.XPATH, "//*[@id='liId_Annual']")
        optionInfrequency.click()
        print("Annual Selected")
        time.sleep(2)

        desiredAnnualIncome = self.driver.find_element(By.XPATH, "//*[@for='desiredAnnualIncomeNo']")
        desiredAnnualIncome.click()
        time.sleep(1)

        annualIncome = self.driver.find_element(By.XPATH, "//*[@name='premiumCommitment']")
        annualIncome.send_keys("250000")
        print("Sum Assured Filled")
        time.sleep(1)

        ################################3

        buttonProceedClick = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        buttonProceedClick.click()
        time.sleep(8)

    def newApplicationFormOneStepThree(self):

        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@name='fatherName']")))
        fatherNameFill = self.driver.find_element(By.XPATH, "//*[@name='fatherName']")
        fatherNameFill.send_keys("Suraj")

        motherNameFill = self.driver.find_element(By.XPATH, "//*[@name='motherName']")
        motherNameFill.send_keys("Kumari")

        maritalStatus = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[2]")
        maritalStatus.click()
        time.sleep(1)
        optionInMaritalStage = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Married')]")
        optionInMaritalStage.click()
        print("Married Selected")

        educationSelect = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[3]")
        educationSelect.click()
        time.sleep(1)
        optionInEducationDropdown = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Graduate')][1]")
        optionInEducationDropdown.click()
        print("Education Selected")

        industrySelect = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[4]")
        industrySelect.click()
        time.sleep(1)
        optionInIndustrySelect = self.driver.find_element(By.XPATH, "//*[@id='liId_Others']")
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

        # natureSelect = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[6]")
        # natureSelect.click()
        # time.sleep(1)
        # optionInNatureSelect = self.driver.find_element(By.XPATH, "//*[@id='liId_Cargo Vessel']")
        # optionInNatureSelect.click()
        # print("Nature Selected")

        organisationFill = self.driver.find_element(By.XPATH, "//*[@name='companyName']")
        organisationFill.send_keys("MAX")
        time.sleep(1)

        preferredLanguage = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[6]")
        preferredLanguage.click()
        time.sleep(1)
        optionInPreferredLanguage = self.driver.find_element(By.XPATH, "//*[@id='liId_English']")
        optionInPreferredLanguage.click()
        print("Hindi Selected")
        time.sleep(1)

        buttonNominee = self.driver.find_element(By.XPATH, "//*[@for='accountNumber01']")
        buttonNominee.click()
        print("Bank Selected.")
        time.sleep(1)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@value='01/01/1800']")))

        calendarNomineeFill = self.driver.find_element(By.XPATH, "//*[@name='nomineeDateOfBirth']")
        calendarNomineeFill.click()

        yearNomineeDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__year-select']")
        yearNomineeSel = Select(yearNomineeDropdown)
        yearNomineeSel.select_by_value('1977')

        monthNomineeDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__month-select']")
        monthNomineeSel = Select(monthNomineeDropdown)
        monthNomineeSel.select_by_value('0')

        dateNomineeSel = self.driver.find_element(By.XPATH, "//*[@aria-label='day-20']")
        dateNomineeSel.click()

        genderSelected = self.driver.find_element(By.XPATH, "//*[contains(text(),'Male')]")
        genderSelected.click()
        print("Gender Clicked")

        relationshipProposer = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[8]")
        relationshipProposer.click()
        time.sleep(1)
        optionInRelationshipProposer = self.driver.find_element(By.XPATH, "//*[@id ='liId_Father']")
        optionInRelationshipProposer.click()
        print("Relationship Brother Selected.")
        time.sleep(1)

        buttonBank = self.driver.find_element(By.XPATH, "//*[@for='accountNumberforBank21']")
        buttonBank.click()
        print("Bank Selected.")
        time.sleep(1)

        ###################Life To Insured #####################

        fatherName = self.driver.find_element(By.XPATH, "//*[@name='insurerFatherName']")
        fatherName.send_keys("Chotu")
        time.sleep(1)

        dobSelect = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[11]")
        dobSelect.click()
        time.sleep(2)
        optiondobSelect = self.driver.find_element(By.XPATH, "//*[@id ='liId_PAN Card']")
        optiondobSelect.click()
        time.sleep(2)

        education = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[12]")
        education.click()
        time.sleep(2)
        optioneducation = self.driver.find_element(By.XPATH, "//*[@id ='liId_Graduate']")
        optioneducation.click()
        time.sleep(2)

        marital = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[13]")
        marital.click()
        time.sleep(2)
        optionmarital = self.driver.find_element(By.XPATH, "//*[@id ='liId_Married']")
        optionmarital.click()
        time.sleep(2)

        clickOnIndian = self.driver.find_element(By.XPATH, "//*[@for='in1']")
        clickOnIndian.click()
        time.sleep(1)

        industry = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[14]")
        industry.click()
        time.sleep(2)
        optionindustry = self.driver.find_element(By.XPATH, "//*[@id ='liId_Defence']")
        optionindustry.click()
        time.sleep(2)

        org = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[15]")
        org.click()
        time.sleep(2)
        optionorg = self.driver.find_element(By.XPATH, "//*[@id ='liId_Non-Governmental Organization (NGO)']")
        optionorg.click()
        time.sleep(1)

        annualIncome= self.driver.find_element(By.XPATH, "//*[@name='insurerAnnualIncome']")
        annualIncome.send_keys("1000000")
        time.sleep(1)

        nature = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[16]")
        nature.click()
        time.sleep(2)
        optionnature = self.driver.find_element(By.XPATH, "//*[@id ='liId_Non-combat role']")
        optionnature.click()
        time.sleep(2)

        occupation = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[17]")
        occupation.click()
        time.sleep(2)
        optionoccupation = self.driver.find_element(By.XPATH, "//*[@id ='liId_Retired']")
        optionoccupation.click()
        time.sleep(2)

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
        weightFill.send_keys("60")
        time.sleep(2)

        btnProceedOnPage4 = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        btnProceedOnPage4.click()
        print("Proceed Button Clicked.")
        time.sleep(1)

    ################################


    def newApplicationFormOneStepFour(self):

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[contains(text(), 'No')])[6]")))

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
        weightFill.send_keys("60")
        time.sleep(2)

        btnProceedOnPage4 = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        btnProceedOnPage4.click()
        print("Proceed Button Clicked.")

        time.sleep(1)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='popupProceed']")))

        # btnProceedOnPage4 = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        # btnProceedOnPage4.click()
        # print("Proceed Button Clicked Again.")
        #
        #
        # self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Cancel')]")))

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

        radioChequeRenewal = self.driver.find_element(By.XPATH, "//*[@for='ECS']")
        radioChequeRenewal.click()
        print("Cheque Selected.")


        raID= self.driver.find_element(By.XPATH, "(// *[@ tabindex='0'])[6]")
        raID.click()
        time.sleep(1)

        raIDValue = self.driver.find_element(By.XPATH, "//*[@id='liId_764878']")
        raIDValue.click()

        sourcingBranchCode = self.driver.find_element(By.XPATH, "//*[@id='sourcingBranchCode_idd']")
        sourcingBranchCode.send_keys("251")

        sourcingBranchCodeValue= self.driver.find_element(By.XPATH, "(// *[contains(text(), '251')])[2]")
        sourcingBranchCodeValue.click()

        buttonSave = self.driver.find_element(By.XPATH, "//*[text()='Save']")
        buttonSave.click()
        print("Save button clicked.")




auto=mProAutomate()
auto.loginFunctionality()
auto.newApplicationFormOneStepOne()
auto.newApplicationFormOneStepTwo()
auto.newApplicationFormOneStepThree()
auto.newApplicationFormOneStepFour()
auto.newApplicationFormOneStepFive()
