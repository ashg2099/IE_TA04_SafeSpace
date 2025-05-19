import { $, expect } from '@wdio/globals';
import type { Browser } from 'webdriverio';
declare const browser: Browser;

// Page object model for home page
class HomePage {

    // CSS & XPath locators to test in the page
    private readonly logoSelector = '#app > nav > div > a > img';
    private readonly discoverBtnSelector = '#app > main > main > div.p-4.p-md-5.mb-4.rounded.text-body-emphasis.bg-light > div > div:nth-child(1) > div > span';
    private readonly crimeStatBtnSelector = '#additional-content > div:nth-child(1) > div > div > div.mt-4 > button';
    private readonly welcomeHeadingSelector = '#app > main > main > div.p-4.p-md-5.mb-4.rounded.text-body-emphasis.bg-warning.text-end > div > div:nth-child(2) > h1';
    private readonly welcomeParagraphSelector = '#app > main > main > div.p-4.p-md-5.mb-4.rounded.text-body-emphasis.bg-warning.text-end > div > div:nth-child(2) > p';
    private readonly crimeStatsPageSelector = '#app > main > div:nth-child(1) > div > div > div.d-flex.justify-content-between.align-items-start.mb-2 > h2'

    private get logo() {
        return $(this.logoSelector);
    }

    private get discoverBtn() {
        return $(this.discoverBtnSelector);
    }

    private get crimeStatBtn() {
        return $(this.crimeStatBtnSelector);
    }

    private get realCrimeStatLink() {
        return $('#offcanvas > div.offcanvas-body > ul > li:nth-child(1) > a');
    }

    private get crimeStatPageText() {
        return $(this.crimeStatsPageSelector);
    }

    // Function to navigate to base URL
    async open(): Promise<void> {
        await browser.url('/');
    }

    // Function to verify if the logo is visible in the home page
    async isLogoVisible(): Promise<void> {
        await expect(this.logo).toBeDisplayed();
    }

    // Function to click on Discover button
    async clickDiscoverButton(): Promise<void> {
        await this.discoverBtn.scrollIntoView();
        await this.discoverBtn.click();
    }

    // Function to click on crime statistics button
    async isCrimeStatVisible(): Promise<void> {
        await this.crimeStatBtn.waitForDisplayed({ timeout: 5000 });
        await expect(this.crimeStatBtn).toBeDisplayed();
    }

    // Function to verify the heading section is visible
    async verifyHeadingVisible(): Promise<void> {
        const headingElement = await $(this.welcomeHeadingSelector);
        await expect(headingElement).toBeDisplayed();
    }

    // Function to verify the welcome text is visible
    async verifyWelcomeTextVisible(): Promise<void> {
        const paragraphElement = await $(this.welcomeParagraphSelector);
        await expect(paragraphElement).toBeDisplayed();
    }

    // Function to verify the real crime statistics button is clickable
    async clickStatisticsButton(): Promise<void> {
        await this.realCrimeStatLink.waitForClickable();
        await this.realCrimeStatLink.click();
    }

    // Function to verify the real crime statistics page
    async isCrimeStatsPageVisible(): Promise<void> {
        await this.crimeStatPageText.waitForDisplayed({ timeout: 5000 });
        await expect(this.crimeStatPageText).toBeDisplayed();
    }

}

export default new HomePage();