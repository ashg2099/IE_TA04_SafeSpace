import { Given, When, Then } from '@wdio/cucumber-framework';
import HomePage from '../page-objects/HomePage';

Given('I open the home page', async () => {
  await HomePage.open();
});

Then('I should see the SafeSpace logo', async () => {
  await HomePage.isLogoVisible();
});

When('I click the "Discover more statistics" button', async () => {
    await HomePage.clickDiscoverButton();
});

Then('I should see the "See real crime stat" section', async () => {
    await HomePage.isCrimeStatVisible();
});

Then('I should see the "Welcome to the SafeSpace" heading', async () => {
    await HomePage.verifyHeadingVisible();
});
  
Then('I should see the welcome section description', async () => {
    await HomePage.verifyWelcomeTextVisible();
});

When('I click the "Real crime stats" button', async () => {
    await HomePage.clickStatisticsButton();
});

Then('I should see the statistics page', async () => {
    await HomePage.isCrimeStatsPageVisible();
});