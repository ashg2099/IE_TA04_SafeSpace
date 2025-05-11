<template>
  <nav class="navbar navbar-expand-md fixed-top bg-white border-bottom border-dark">
    <div class="container-fluid">
      <RouterLink class="navbar-brand" to="/">
        <img alt="logo" src="@/assets/logo.svg" width="100" height="100" />
      </RouterLink>

      <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvas"
        aria-controls="offcanvas" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvas" aria-labelledby="offcanvasLabel">
        <div class="offcanvas-header">
          <img alt="logo" class="offcanvas-title" id="offcanvasLabel" src="@/assets/logo.svg" width="100"
            height="100" />
          <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
        </div>
        <div class="offcanvas-body">
          <ul class="navbar-nav ms-auto mb-2 mb-md-0">
            <li class="nav-item">
              <RouterLink class="nav-link" to="/explore-crime-stat">Explore Crime Statistics</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/check-nearby-community">Check Nearby Community</RouterLink>
            </li>
            <!-- Add new link for the safety game -->
            <li class="nav-item">
              <RouterLink class="nav-link" to="/safety-game">Safety Challenge</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </nav>
  <!-- Add spacing for the fixed navigation bar to prevent content from being covered -->
  <div style="padding-top: 80px;"></div>
</template>
