// Importing necessary modules and required page object models
import { Given, When, Then } from '@wdio/cucumber-framework';
import HomePage from '../page-objects/HomePage';
import CrimePage from '../page-objects/CrimePage';
import UrbanSafetyPage from '../page-objects/UrbanSafetyPage';

// Step definition to open the homepage
Given('I open the home page', async () => {
  await HomePage.open();
});

// Step definition to verify SafeSpace logo in the homepage
Then('I should see the SafeSpace logo', async () => {
  await HomePage.isLogoVisible();
});

// Step definition to click Discover more statistics button in homepage
When('I click the "Discover more statistics" button', async () => {
    await HomePage.clickDiscoverButton();
});

// Step definition to verify explore crime statistics section in homepage
Then('I should see the "Explore Crime statistics" section', async () => {
    await HomePage.isCrimeStatVisible();
});

// Step definition to verify welcome heading in homepage
Then('I should see the "Welcome to the SafeSpace" heading', async () => {
    await HomePage.verifyHeadingVisible();
});
  
// Step definition to verify welcome section text in homepage
Then('I should see the welcome section description', async () => {
    await HomePage.verifyWelcomeTextVisible();
});

// Step definition to click on crime statistics button
When('I click the "Explore Crime statistics" button', async () => {
    await HomePage.clickStatisticsButton();
});

// Step definition to verify crime statistics page
Then('I should see the statistics page', async () => {
    await HomePage.isCrimeStatsPageVisible();
});

// Step definition to verify crime stats yearly map
Then('I should see the Melbourne Offence Count by suburb map', async () => {
    await CrimePage.isOffenseMapVisible();
});

// Step definition to ensure map overlays show suburb level data
Then('I should see colored overlays for each suburb', async () => {
    await CrimePage.isColoroverlayMapVisible();
});

// Step definition to verify the presence of section
Then('I should see {string}', async (sectionTitle: string) => {
    await CrimePage.expectSectionVisible(sectionTitle);
});

// Step definition to verify the presence of safety tips visibility
Then('I should see the tip {string}', async (tip: string) => {
    await CrimePage.expectSafetyTipVisible(tip);
});

// Step definition to verify the button is clickable
Then('I should see a button labeled {string}', async (label: string) => {
    await CrimePage.expectButtonVisible(label);
});

// Step definition to verify the see more button is clickable
Then('the button should be clickable', async () => {
    await CrimePage.expectSeeMoreButtonClickable();
});

// Step definition to verify the offence category section is visible
Then('I should see {string} section', async (section: string) => {
    await CrimePage.expectOffenceCategorySectionVisible(section);
});

// Step definition to verify the list of offence category section is visible
Then('it should list {string}', async (item: string) => {
    await CrimePage.expectOffenceCategoryItemVisible(item);
});

// Step definition to verify the check nearby community button is clickable
Then('I click the "Check Nearby Community" button', async () => {
    await UrbanSafetyPage.clickNearbyCommunityStatsButton();
});

// Step definition to verify the check nearby community button is clickable in what can we do for you cards
Then('I click the "Check Nearby Community" button on the cards section', async () => {
    await UrbanSafetyPage.clickNearbyCommunityStatsCardButton();
});

// Step definition to verify the pedestrian and lighting data page is visible
Then('I should see the pedestrian & lighting page', async () => {
    await UrbanSafetyPage.checkPedestrianandLightingPage();
});

// Step definition to verify the safety advice card is visible
Then('I should see the safety advice card', async () => {
    await UrbanSafetyPage.checkSafetyAdviceCard();
});

// Step definition to verify the first safety advice tip is visible
Then('I should see the first tip {string}', async (tip: string) => {
    await UrbanSafetyPage.expectFirstTipVisible(tip);
});

// Step definition to verify the second safety advice tip is visible
Then('I should see the second tip {string}', async (tip: string) => {
    await UrbanSafetyPage.expectSecondTipVisible(tip);
});

// Step definition to verify the third safety advice tip is visible
Then('I should see the third tip {string}', async (tip: string) => {
    await UrbanSafetyPage.expectThirdTipVisible(tip);
});

// Step definition to verify the historical disclaimer message is visible
Then('I should see historical disclaimer {string}', async (message: string) => {
    await UrbanSafetyPage.expectAlertMessage(message);
});
