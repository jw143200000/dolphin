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

        username= self.driver.find_element(By.ID, "userId")
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
        enterCustomerId.send_keys("29471")
        # kartik.bisaria@kelltontech.com

        fetchDetailsBtn = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Fetch')]")
        fetchDetailsBtn.click()

        clickOnCross = self.driver.find_element(By.XPATH, "(//*[@d='M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z'])[3]")
        clickOnCross.click()
        # kartik.bisaria@kelltontech.com

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@for='self']")))
        clickOnSelf= self.driver.find_element(By.XPATH, "//*[@for='self']")
        time.sleep(8)
        clickOnSelf.click()


        # time.sleep(30)
        #
        # btnProceed = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        # btnProceed.click()

    def newApplicationFormOneStepTwo(self):
        windowBefore = self.driver.window_handles[0]

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@name='alternateMobileNo']")))

        alternateMobileNumber= self.driver.find_element(By.XPATH, "//*[@name='alternateMobileNo']")
        alternateMobileNumber.send_keys("9650479781")

        stdCode = self.driver.find_element(By.XPATH, "//*[@name='stdCode']")
        stdCode.send_keys("011")

        purposeOfInsuranceDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[3]")
        purposeOfInsuranceDropdown.click()

        optionInInsuranceDropdown = self.driver.find_element(By.XPATH, "//*[@id='liId_Wealth accumulation/Investment']")
        optionInInsuranceDropdown.click()
        print("Retirement Selected")

        lifeStageDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[4]")
        lifeStageDropdown.click()

        optionInLifeStage = self.driver.find_element(By.XPATH, "//*[@id='liId_Married with children']")
        optionInLifeStage.click()
        print("Single Selected")

        grossIncomeFill = self.driver.find_element(By.XPATH, "//*[@name='income']")
        grossIncomeFill.send_keys('1100000')
        print("Gross Income Entered")

        existingPolicy = self.driver.find_element(By.XPATH, "(//*[contains(text(),'No')])[4]")
        existingPolicy.click()

        occupationDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[5]")
        occupationDropdown.click()
        optionInOccupation = self.driver.find_element(By.XPATH, "//*[@id='liId_Salaried']")
        optionInOccupation.click()
        print("Salaried Selected")
        time.sleep(2)

        recommendProduct = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[7]")
        recommendProduct.click()
        time.sleep(10)
        recommendProduct.click()
        time.sleep(1)
        optionInRecommendProduct = self.driver.find_element(By.XPATH, "//*[@id='liId_Select Another Product']")
        optionInRecommendProduct.click()
        print("Product Selected")
        time.sleep(1)

        recommendProductName = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[8]")
        recommendProductName.click()
        time.sleep(1)

        optionInRecommendProductName = self.driver.find_element(By.XPATH, "//*[@id='liId_Max Life Shiksha Plus Super']")
        optionInRecommendProductName.click()
        print("Product Selected")







        premiumTypeDropdown = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[9]")
        premiumTypeDropdown.click()
        time.sleep(1)
        premiumTypeOption = self.driver.find_element(By.XPATH, "//*[@id='liId_15']")
        premiumTypeOption.click()
        print("Premium Type Selected")

        policyTerm = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[10]")
        policyTerm.click()
        time.sleep(1)
        policyTermValue = self.driver.find_element(By.XPATH, "//*[@id='liId_15']")
        policyTermValue.click()
        print("15 Selected")

        modeOfPayment = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[11]")
        modeOfPayment.click()
        time.sleep(1)
        modeOfPaymentValue = self.driver.find_element(By.XPATH, "//*[@id='liId_Annual']")
        modeOfPaymentValue.click()
        print("Annual Selected")

        optionInPaymentMode = self.driver.find_element(By.XPATH, "//*[@id='liId_Annual']")
        optionInPaymentMode.click()

        childCalendarFill = self.driver.find_element(By.XPATH, "//*[@name='childDob']")
        childCalendarFill.click()

        childMonthDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__month-select']")
        childMonthSel = Select(childMonthDropdown)
        childMonthSel.select_by_value('9')

        childDateSel = self.driver.find_element(By.XPATH, "//*[@aria-label='day-31']")
        childDateSel.click()

        premiumCommitFill = self.driver.find_element(By.XPATH, "//*[@name='premiumCommitment']")
        premiumCommitFill.send_keys("200000")
        print("Sum Assured Filled")

        chooseFund = self.driver.find_element(By.XPATH, "//*[@for='chooseFundNo']")
        chooseFund.click()

        chooseFund = self.driver.find_element(By.XPATH, "//*[@for='dynamicFundNo']")
        chooseFund.click()

        systematicFund = self.driver.find_element(By.XPATH, "//*[@for='systematicYes']")
        systematicFund.click()

        investorDropdownSelected = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[13]")
        investorDropdownSelected.click()
        print("Investor dropdown Clicked")
        time.sleep(2)
        optionInvestorDropdownSelected = self.driver.find_element(By.XPATH,
                                                                  "//*[@id='liId_I am comfortable taking on a higher level of risk, knowing it may mean higher returns.']")
        optionInvestorDropdownSelected.click()
        print("Investor dropdown Selected")
        time.sleep(2)

        investmentDropdownSelected = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[14]")
        investmentDropdownSelected.click()
        print("Investment dropdown Clicked")

        optionInvestmentDropdownSelected = self.driver.find_element(By.XPATH,
                                                                    "//*[@id='liId_Portfolio 1 : Equity - 100%- Debt- 0%']")
        optionInvestmentDropdownSelected.click()
        print("Investment Selected")

        investmentDropdownUp = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[15]")
        investmentDropdownUp.click()
        print("Investment dropdown Clicked")

        optionInvestmentDropdownUp = self.driver.find_element(By.XPATH, "//*[@id='liId_30%']")

        optionInvestmentDropdownUp.click()
        print("Investment Up Selected")

        habitDescription = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[16]")
        habitDescription.click()
        print("Habit dropdown Clicked")
        time.sleep(1)

        optionHabitDescription = self.driver.find_element(By.XPATH,
                                                          "//*[@id='liId_I am able to save substantial amount regularly, after covering living expenses.']")

        optionHabitDescription.click()
        print("Habit Selected")
        time.sleep(1)

        buttonProceedClick = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        buttonProceedClick.click()
        time.sleep(1)
        popUp = self.driver.find_element(By.XPATH, "(//*[contains(text(),'Yes')])[6]")
        popUp.click()

        time.sleep(8)

        self.driver.switch_to_window(windowBefore)

    def newApplicationFormOneStepThree(self):

        time.sleep(5)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@name='fatherName']")))
        fatherNameFill = self.driver.find_element(By.XPATH, "//*[@name='fatherName']")
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
        optionInEducationDropdown = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Graduate')][1]")
        optionInEducationDropdown.click()
        print("Education Selected")

        industrySelect = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[4]")
        industrySelect.click()
        time.sleep(1)
        optionInIndustrySelect = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Merchant')][1]")
        optionInIndustrySelect.click()
        print("Industry Selected")

        organisationSelect = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[5]")
        organisationSelect.click()
        time.sleep(1)
        optionInOrganisationSelect = self.driver.find_element(By.XPATH, "//*[@id='liId_Govt']")
        optionInOrganisationSelect.click()
        print("Organisation Selected")

        natureSelect = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[6]")
        natureSelect.click()
        time.sleep(1)
        optionInNatureSelect = self.driver.find_element(By.XPATH, "//*[@id='liId_Cargo Vessel']")
        optionInNatureSelect.click()
        print("Nature Selected")

        organisationFill = self.driver.find_element(By.XPATH, "//*[@name='companyName']")
        organisationFill.send_keys("ORG")
        time.sleep(1)

        preferredLanguage = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[7]")
        preferredLanguage.click()
        time.sleep(1)
        optionInPreferredLanguage = self.driver.find_element(By.XPATH, "//*[@id='liId_Hindi']")
        optionInPreferredLanguage.click()
        print("Hindi Selected")
        time.sleep(2)

        organisationFill = self.driver.find_element(By.XPATH, "//*[@name='nomineeName']")
        organisationFill.send_keys("Nominee")

        calendarNomineeFill = self.driver.find_element(By.XPATH, "//*[@name='nomineeDateOfBirth']")
        calendarNomineeFill.click()

        yearNomineeDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__year-select']")
        yearNomineeSel = Select(yearNomineeDropdown)
        yearNomineeSel.select_by_value('1985')

        monthNomineeDropdown = self.driver.find_element(By.XPATH, "//*[@class='react-datepicker__month-select']")
        monthNomineeSel = Select(monthNomineeDropdown)
        monthNomineeSel.select_by_value('3')

        dateNomineeSel = self.driver.find_element(By.XPATH, "//*[@aria-label='day-10']")
        dateNomineeSel.click()

        genderSelected = self.driver.find_element(By.XPATH, "//*[contains(text(),'Male')]")
        genderSelected.click()
        print("Gender Clicked")

        relationshipProposer = self.driver.find_element(By.XPATH, "(//*[@ tabindex='0'])[9]")
        relationshipProposer.click()
        time.sleep(1)
        optionInRelationshipProposer = self.driver.find_element(By.XPATH, "//*[@id ='liId_Brother']")
        optionInRelationshipProposer.click()
        print("Relationship Brother Selected.")

        enterChildName = self.driver.find_element(By.XPATH, "//*[@name='nomineeChildName']")
        enterChildName.send_keys("Hello")
        print("Child name entered.")

        bankFill = self.driver.find_element(By.XPATH, "//*[@name='bankAccountNo']")
        bankFill.send_keys("99999999999999")

        nameOfAccount = self.driver.find_element(By.XPATH, "//*[@name='bankAccountHolderName']")
        nameOfAccount.send_keys("NameName")

        nameOfIFSCcode = self.driver.find_element(By.XPATH, "//*[@name='bankAccountIFSC']")
        nameOfIFSCcode.send_keys("SBIN0000845")

        codeMICR = self.driver.find_element(By.XPATH, "//*[@name='bankAccountMICR']")
        codeMICR.send_keys("515002206")
        time.sleep(3)

        accountType = self.driver.find_element(By.XPATH, "(//*[@tabindex='0'])[11]")
        accountType.click()
        time.sleep(2)

        accountTypeSelect = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Savings')]")
        accountTypeSelect.click()
        print("Account Type Selected.")
        time.sleep(2)

        calBankAcOpening = self.driver.find_element(By.XPATH, "//*[@name='bankAccOpeningDate']")
        calBankAcOpening.click()

        calDateSelect = self.driver.find_element(By.XPATH, "//*[@aria-label='day-3']")
        calDateSelect.click()


        btnProceedOnPage3 = self.driver.find_element(By.XPATH, "//*[contains(text(),'Proceed')]")
        btnProceedOnPage3.click()
        time.sleep(5)

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

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Cancel')]")))

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
