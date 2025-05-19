import { $, $$, expect } from '@wdio/globals';
import type { Browser } from 'webdriverio';
declare const browser: Browser;

// Page object model for crime statistics page 
class CrimePage {

    // CSS & XPath locators to test in the page
    private readonly offenseMapTitleSelector = '#app > main > div:nth-child(1) > div > div > div.d-flex.justify-content-between.align-items-start.mb-2 > h2';
    private readonly mapSelector = '#app > main > div:nth-child(1) > div > div > div.row.g-4 > div.col-lg-8';
    private readonly safetyTipTitleSelector = '#app > main > div:nth-child(1) > div > div > div.row.g-4 > div.col-lg-4.d-flex.flex-column.gap-4.gap-1 > div:nth-child(3) > div > h5';
    private readonly safetyTipsSelector1 = '#app > main > div:nth-child(1) > div > div > div.row.g-4 > div.col-lg-4.d-flex.flex-column.gap-4.gap-1 > div:nth-child(3) > div > div.d-flex.align-items-center.mb-2 > span:nth-child(2)';
    private readonly safetyTipsSelector2 = '#app > main > div:nth-child(1) > div > div > div.row.g-4 > div.col-lg-4.d-flex.flex-column.gap-4.gap-1 > div:nth-child(3) > div > div:nth-child(3) > span:nth-child(2)';
    private readonly seeMoreButtonSelector = '#app > main > div:nth-child(1) > div > div > div.d-flex.justify-content-between.align-items-start.mb-2 > div > span';
    private readonly trendChartTitleSelector = '#app > main > div:nth-child(2) > div > div > div.d-flex.justify-content-between.align-items-start.mb-2 > h2';
    private readonly offenceCategoryHeadingSelector = '#app > main > div:nth-child(1) > div > div > div.row.g-4 > div.col-lg-4.d-flex.flex-column.gap-4.gap-1 > div:nth-child(2) > div.card-header.bg-light.py-3 > h5';
    private readonly offenceCategoryItemsSelector1 = '#app > main > div:nth-child(1) > div > div > div.row.g-4 > div.col-lg-4.d-flex.flex-column.gap-4.gap-1 > div:nth-child(2) > div.card-body > ul > li:nth-child(1)';
    private readonly offenceCategoryItemsSelector2 = '#app > main > div:nth-child(1) > div > div > div.row.g-4 > div.col-lg-4.d-flex.flex-column.gap-4.gap-1 > div:nth-child(2) > div.card-body > ul > li:nth-child(2)';

    private get offenseMap() {
        return $(this.offenseMapTitleSelector);
    }

    private get mapView() {
        return $(this.mapSelector);
    }

    private get safetyRecommendationTip() {
        return $(this.safetyTipTitleSelector);
    }

    private get fristSafetyTip() {
        return $(this.safetyTipsSelector1);
    }

    private get secondSafetyTip() {
        return $(this.safetyTipsSelector2);
    }

    private get seeMoreButton() {
        return $(this.seeMoreButtonSelector);
    }

    private get trendChartTitle() {
        return $(this.trendChartTitleSelector);
    }

    private get offenceCategoryHeading() {
        return $(this.offenceCategoryHeadingSelector);
    }
    
    private get offenceCategoryItem1() {
        return $$(this.offenceCategoryItemsSelector1);
    }

    private get offenceCategoryItem2() {
        return $$(this.offenceCategoryItemsSelector2);
    }
    
    // Function to verify if offense map is visible
    async isOffenseMapVisible(): Promise<void> {
        await this.offenseMap.waitForDisplayed({ timeout: 5000 });
        await expect(this.offenseMap).toBeDisplayed();
    }

    // Function to verify if color overlay in map is visible
    async isColoroverlayMapVisible(): Promise<void> {
        await this.mapView.waitForDisplayed({ timeout: 5000 });
        await expect(this.mapView).toBeDisplayed();
    }

    // Function to verify if safety recommendation section are displayed 
    async expectSectionVisible(title: string) {
        const tipElement = this.safetyRecommendationTip;
        await tipElement.waitForDisplayed({ timeout: 5000 });
        const text = await tipElement.getText();
        await expect(text).toContain(title);
    }

    // Function to verify if safety recommendation tips are displayed 
    async expectSafetyTipVisible(expectedText: string) {
        let tipElement;
    
        if (expectedText === 'Plan your routes with safety in mind') {
            tipElement = this.fristSafetyTip;
        } else if (expectedText === 'Stay extra cautious in high-risk areas') {
            tipElement = this.secondSafetyTip;
        } else {
            throw new Error(`No selector mapped for the tip: "${expectedText}"`);
        }
    
        await tipElement.waitForDisplayed({ timeout: 5000 });
        const actualText = await tipElement.getText();
        await expect(actualText).toContain(expectedText);
    }

    // Function to verify if see more button is present 
    async expectButtonVisible(label: string) {
        await this.seeMoreButton.waitForDisplayed({ timeout: 5000 });
        const text = await this.seeMoreButton.getText();
        await expect(text).toContain(label);
    }

    // Function to verify if see more button is clickable 
    async expectSeeMoreButtonClickable() {
        await this.seeMoreButton.waitForClickable({ timeout: 5000 });
        const isEnabled = await this.seeMoreButton.isEnabled();
        await expect(isEnabled).toBe(true);
        await this.seeMoreButton.click();
        const text = await this.trendChartTitle.getText();
        await expect(text).toContain("Australia Victim Counts");
    }

    // Function to verify if offense category section is present
    async expectOffenceCategorySectionVisible(expectedText: string) {
        await this.offenceCategoryHeading.waitForDisplayed({ timeout: 5000 });
        const text = await this.offenceCategoryHeading.getText();
        await expect(text).toContain(expectedText);
    }
    
    // Function to verify the list of offense category items is visible
    async expectOffenceCategoryItemVisible(expectedItem: string) {
        const item1Text = await (await this.offenceCategoryItem1[0]).getText();
        const item2Text = await (await this.offenceCategoryItem2[0]).getText();
    
        const matches = [item1Text, item2Text].some(text => text.includes(expectedItem));
        await expect(matches).toBe(true);
    }

}

export default new CrimePage();