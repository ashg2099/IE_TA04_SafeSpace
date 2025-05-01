import { $, expect } from '@wdio/globals';
import type { Browser } from 'webdriverio';
declare const browser: Browser;

class HomePage {
    // === Locators ===
    private readonly logoSelector = '#app > nav > div > a > img';
    private readonly discoverBtnSelector = '#app > main > main > div.p-4.p-md-5.mb-4.rounded.text-body-emphasis.bg-light > div > div:nth-child(1) > div > span';
    private readonly crimeStatBtnSelector = '#additional-content > div:nth-child(1) > div > div > div.mt-4 > button';
    private readonly welcomeHeadingSelector = '#app > main > main > div.p-4.p-md-5.mb-4.rounded.text-body-emphasis.bg-warning.text-end > div > div:nth-child(2) > h1';
    private readonly welcomeParagraphSelector = '#app > main > main > div.p-4.p-md-5.mb-4.rounded.text-body-emphasis.bg-warning.text-end > div > div:nth-child(2) > p';
    private readonly crimeStatsPageSelector = '#app > main > div:nth-child(1) > div > div > div.d-flex.justify-content-between.align-items-start.mb-2 > h2'
   
    // === Elements ===
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

    // === Actions ===
    async open(): Promise<void> {
        await browser.url('/');
    }

    async isLogoVisible(): Promise<void> {
        await expect(this.logo).toBeDisplayed();
    }

    async clickDiscoverButton(): Promise<void> {
        await this.discoverBtn.scrollIntoView();
        await this.discoverBtn.click();
    }

    async isCrimeStatVisible(): Promise<void> {
        await this.crimeStatBtn.waitForDisplayed({ timeout: 5000 });
        await expect(this.crimeStatBtn).toBeDisplayed();
    }

    async verifyHeadingVisible(): Promise<void> {
        const headingElement = await $(this.welcomeHeadingSelector);
        await expect(headingElement).toBeDisplayed();
    }

    async verifyWelcomeTextVisible(): Promise<void> {
        const paragraphElement = await $(this.welcomeParagraphSelector);
        await expect(paragraphElement).toBeDisplayed();
    }

    async clickStatisticsButton(): Promise<void> {
        await this.realCrimeStatLink.waitForClickable();
        await this.realCrimeStatLink.click();
    }

    async isCrimeStatsPageVisible(): Promise<void> {
        await this.crimeStatPageText.waitForDisplayed({ timeout: 5000 });
        await expect(this.crimeStatPageText).toBeDisplayed();
    }

}

export default new HomePage();