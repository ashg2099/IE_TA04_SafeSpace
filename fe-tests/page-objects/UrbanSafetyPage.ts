import { $, $$, expect } from '@wdio/globals';
import type { Browser } from 'webdriverio';
declare const browser: Browser;

// Page object model for urban safety page 
class UrbanSafetyPage {

    // CSS & XPath locators to test in the page
    private readonly explorecommunitySelector = '#offcanvas > div.offcanvas-body > ul > li:nth-child(2) > a';
    private readonly explorecommunityCardSelector = '#additional-content > div:nth-child(2) > div > div > div.mt-4 > button';
    private readonly urbansafetypageSelector = '#app > main > div.card.shadow-sm.rounded.border-0.mb-4 > div';
    private readonly safetyAdviceCardSelector = '#app > main > div.col-10.col-md-8.col-lg-6.mx-auto.p-3 > div > div';
    private readonly alertMessageSelector = '#app > main > div.col-10.col-md-8.col-lg-6.mx-auto.p-3 > div > div > div > div.mt-4.pt-2.border-top > p > small';

    private get exploreCommBtn() {
        return $(this.explorecommunitySelector);
    }

    private get exploreCommCardBtn() {
        return $(this.explorecommunityCardSelector);
    }

    private get exploreCommPage() {
        return $(this.urbansafetypageSelector);
    }

    private get safetyAdviceCardSection() {
        return $(this.safetyAdviceCardSelector);
    }

    private get firstTip() {
        return $('div.tip-item:nth-child(1)');
    }
    
    private get secondTip() {
        return $('div.tip-item:nth-child(2)');
    }
    
    private get thirdTip() {
        return $('div.tip-item:nth-child(3)');
    }

    private get alertMessage() {
        return $(this.alertMessageSelector);
    }
    

    // Function to Click on "Check Nearby Community" button
    async clickNearbyCommunityStatsButton(): Promise<void> {
        await this.exploreCommBtn.waitForClickable();
        await this.exploreCommBtn.click();
    }

    // Function to Click on card button to view urban safety data
    async clickNearbyCommunityStatsCardButton(): Promise<void> {
        await this.exploreCommCardBtn.waitForClickable();
        await this.exploreCommCardBtn.click();
    }

    // Function to verify pedestrian and lighting page
    async checkPedestrianandLightingPage(): Promise<void> {
        await this.exploreCommPage.waitForDisplayed({ timeout: 5000 });
        await expect(this.exploreCommPage).toBeDisplayed();
    }

    // Function to verify safety advice card
    async checkSafetyAdviceCard(): Promise<void> {
        await this.safetyAdviceCardSection.waitForDisplayed({ timeout: 5000 });
        await expect(this.safetyAdviceCardSection).toBeDisplayed();
    }

    // Function to verify first safety tip to conatin the expected text
    async expectFirstTipVisible(expectedTip: string) {
        await this.firstTip.waitForDisplayed({ timeout: 5000 });
        const text = await this.firstTip.getText();
        await expect(text).toContain(expectedTip);
    }
    
    // Function to verify second safety tip to conatin the expected text
    async expectSecondTipVisible(expectedTip: string) {
        await this.secondTip.waitForDisplayed({ timeout: 5000 });
        const text = await this.secondTip.getText();
        await expect(text).toContain(expectedTip);
    }
    
    // Function to verify third safety tip to conatin the expected text
    async expectThirdTipVisible(expectedTip: string) {
        await this.thirdTip.waitForDisplayed({ timeout: 5000 });
        const text = await this.thirdTip.getText();
        await expect(text).toContain(expectedTip);
    }

    // Function to verify alert message to conatin the expected text
    async expectAlertMessage(expectedText: string): Promise<void> {
        await this.alertMessage.waitForDisplayed({ timeout: 5000 });
        await this.alertMessage.scrollIntoView();
        const actualText = await this.alertMessage.getText();
        await expect(actualText).toContain(expectedText);
    }

}

export default new UrbanSafetyPage();