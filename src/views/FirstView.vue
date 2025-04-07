<script setup lang="ts">
import HeaderNav from '../components/HeaderNav.vue'
</script>

<template>
  <HeaderNav></HeaderNav>
  <main>
    <div class="p-4 p-md-5 mb-4 rounded text-body-emphasis bg-black border border-white">
      <div class="row align-items-center">
        <div class="col-lg-6 text-white">
          <h1 class="display-5 fw-bold">Feeling unsafe in cities...</h1>
          <p class="lead my-3 fs-3">
            Have you ever felt scared or worried about experiencing street harassment, sexual harassment, or stalking in
            Melbourne?
          </p>
        </div>
        <!-- change-to-real-picture -->
        <div class="col-lg-6">
          <svg aria-label="Welcome image" width="100%" height="800" preserveAspectRatio="xMidYMid slice"
            focusable="false">
            <image href="@/assets/worried.jpg" class="img-fluid rounded" width="100%" height="100%" />
          </svg>
        </div>
      </div>
    </div>

    <div class="p-4 p-md-5 mb-4 rounded text-body-emphasis bg-white text-end border border-dark">
      <div class="row align-items-center">
        <!-- change-to-real-picture -->
        <div class="col-lg-6">
          <svg aria-label="Welcome image" width="100%" height="800" preserveAspectRatio="xMidYMid slice"
            focusable="false">
            <image href="@/assets/women-crowded.jpg" class="img-fluid rounded" width="100%" height="100%" />
          </svg>
        </div>
        <div class="col-lg-6">
          <h1 class="display-5 fw-bold">Welcome to Safe-Place</h1>
          <p class="lead my-3 fs-3">
            Safe-Space is dedicated to boost the mobility and confidence of women in public areas.
            We equip women with the information they need to make safer choices in
            their daily lives.
            Let us help slience your fears in the Melbourne street by our insights and supports.
          </p>
        </div>
      </div>
    </div>

    <div class="p-3 mb-4">
      <h1 class="mb-4 display-5 fw-bold">About Safe Space</h1>

      <!-- add separate 3 div to illustrate feature -->

      <div class="row">
        <div class="col-md-8 d-flex flex-column position-static">
          <h2>Many women in Melbourne still face hidden risks when walking through public spaces — from poorly lit
            streets to areas with high rates of harassment or assault. Yet this information often remains scattered or
            invisible. </h2>
          <p class="lead my-2 fs-4">Our Safety Awareness Tool leverages open data - including including crime
            statistics, street lighting conditions to create interactive maps and visual infographics that make these
            safety gaps visible. </p>
        </div>
      </div>
      <a href="#" class="btn btn-outline-primary mt-2 btn-lg">Safety Visualisation Tool </a>

      <div class="row mt-5 bg-success text-white align-items-center" style="height: 300px;">
        <div class="col-md-4">
        </div>
        <div class="col-md-6 p-4 d-flex flex-column position-static">
          <h2>Life-Saving Tips</h2>
          <p class="lead my-2 fs-4">Immersive yourself into scenarios and challenges, making it
            easy and enjoyable to safety advice.</p>
          <a href="#" class="btn btn-warning mt-2 btn-lg">Start
            Gaming !</a>
        </div>
        <div class="col-md-2"></div>
      </div>
    </div>


  </main>

</template>
