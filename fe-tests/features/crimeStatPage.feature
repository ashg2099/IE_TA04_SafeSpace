Feature: CrimeStatPage

@offenceMap
Scenario: Verify Melbourne Offence Count map is visible
Given I open the home page
When I click the "Explore Crime statistics" button
Then I should see the statistics page
Then I should see the Melbourne Offence Count by suburb map

@mapLayoutAvailable
Scenario: Map should render color-coded neighbourhood overlays
Given I open the home page
When I click the "Explore Crime statistics" button
Then I should see the statistics page
Then I should see the Melbourne Offence Count by suburb map
Then I should see colored overlays for each suburb

@recommendations
Scenario: Safety recommendations are visible to users
Given I open the home page
When I click the "Explore Crime statistics" button
Then I should see the statistics page
Then I should see "Safety Recommendations"
And I should see the tip "Plan your routes with safety in mind"
And I should see the tip "Stay extra cautious in high-risk areas"

@ctaButton
Scenario: 'See more' button is visible and clickable
Given I open the home page
When I click the "Explore Crime statistics" button
Then I should see the statistics page
Then I should see a button labeled "See more"
And the button should be clickable

@OffenceCategories
Scenario: Offence categories list is shown on sidebar
Given I open the home page
When I click the "Explore Crime statistics" button
Then I should see the statistics page
Then I should see "Offence Categories" section
And it should list "A20 Assault and related offences"
And it should list "A50 Robbery"
