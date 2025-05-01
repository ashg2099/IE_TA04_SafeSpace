import { Given, When, Then } from '@wdio/cucumber-framework';
import HomePage from '../page-objects/HomePage';
import CrimePage from '../page-objects/CrimePage';
import UrbanSafetyPage from '../page-objects/UrbanSafetyPage';

Given('I open the home page', async () => {
  await HomePage.open();
});

Then('I should see the SafeSpace logo', async () => {
  await HomePage.isLogoVisible();
});

When('I click the "Discover more statistics" button', async () => {
    await HomePage.clickDiscoverButton();
});

Then('I should see the "Explore Crime statistics" section', async () => {
    await HomePage.isCrimeStatVisible();
});

Then('I should see the "Welcome to the SafeSpace" heading', async () => {
    await HomePage.verifyHeadingVisible();
});
  
Then('I should see the welcome section description', async () => {
    await HomePage.verifyWelcomeTextVisible();
});

When('I click the "Explore Crime statistics" button', async () => {
    await HomePage.clickStatisticsButton();
});

Then('I should see the statistics page', async () => {
    await HomePage.isCrimeStatsPageVisible();
});

Then('I should see the Melbourne Offence Count by suburb map', async () => {
    await CrimePage.isOffenseMapVisible();
});

Then('I should see colored overlays for each suburb', async () => {
    await CrimePage.isColoroverlayMapVisible();
});

Then('I should see {string}', async (sectionTitle: string) => {
    await CrimePage.expectSectionVisible(sectionTitle);
});

Then('I should see the tip {string}', async (tip: string) => {
    await CrimePage.expectSafetyTipVisible(tip);
});

Then('I should see a button labeled {string}', async (label: string) => {
    await CrimePage.expectButtonVisible(label);
});

Then('the button should be clickable', async () => {
    await CrimePage.expectSeeMoreButtonClickable();
});

Then('I should see {string} section', async (section: string) => {
    await CrimePage.expectOffenceCategorySectionVisible(section);
});

Then('it should list {string}', async (item: string) => {
    await CrimePage.expectOffenceCategoryItemVisible(item);
});

Then('I click the "Check Nearby Community" button', async () => {
    await UrbanSafetyPage.clickNearbyCommunityStatsButton();
});

Then('I click the "Check Nearby Community" button on the cards section', async () => {
    await UrbanSafetyPage.clickNearbyCommunityStatsCardButton();
});

Then('I should see the pedestrian & lighting page', async () => {
    await UrbanSafetyPage.checkPedestrianandLightingPage();
});

Then('I should see the safety advice card', async () => {
    await UrbanSafetyPage.checkSafetyAdviceCard();
});

Then('I should see the first tip {string}', async (tip: string) => {
    await UrbanSafetyPage.expectFirstTipVisible(tip);
});

Then('I should see the second tip {string}', async (tip: string) => {
    await UrbanSafetyPage.expectSecondTipVisible(tip);
});

Then('I should see the third tip {string}', async (tip: string) => {
    await UrbanSafetyPage.expectThirdTipVisible(tip);
});

Then('I should see historical disclaimer {string}', async (message: string) => {
    await UrbanSafetyPage.expectAlertMessage(message);
});
