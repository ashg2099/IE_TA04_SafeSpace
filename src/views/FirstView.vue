<script setup lang="ts">
import HeaderNav from '../components/HeaderNav.vue'
</script>

<template>
  <HeaderNav></HeaderNav>
  <main>
    <div class="p-4 p-md-5 mb-4 rounded text-body-emphasis bg-white">
      <div class="row align-items-center">
        <div class="col-lg-6">
          <h1 class="display-4">Welcome to Safe-Space</h1>
          <p class="lead my-3">
            Have you ever felt scared or worried about experiencing street harassment, sexual harassment, or stalking in
            Melbourne?
            Safe-Space is dedicated to boost the mobility and confidence of women in public areas.
            We equip women with the information they need to make safer choices in
            their daily lives.
            Let us help slience your fears in the Melbourne street by our insights and supports.
          </p>
        </div>
        <!-- change-to-real-picture -->
        <div class="col-lg-6">
          <svg aria-label="Welcome image" class="img-fluid rounded" width="100%" height="800"
            preserveAspectRatio="xMidYMid slice" focusable="false">
            <image href="@/assets/worried.jpg" width="100%" height="100%" />
          </svg>
        </div>
      </div>
    </div>

    <div class="p-4 mb-5">
      <h2 class="mb-4">About Safe Space</h2>

      <!-- add separate 3 div to illustrate feature -->

      <div class="row flex-md-row mb-4 position-relative">
        <div class="col-md-4">
          <svg class="bd-placeholder-img img-fluid" width="100%" height="250" xmlns="http://www.w3.org/2000/svg"
            role="img" aria-label="Feature 1" preserveAspectRatio="xMidYMid slice" focusable="false">
            <title>Feature 1</title>
            <rect width="100%" height="100%" fill="#FF6B6B" />
            <text x="50%" y="50%" fill="#fff" text-anchor="middle" dominant-baseline="middle">Feature 1 Image</text>
          </svg>
        </div>
        <div class="col-md-8 p-4 d-flex flex-column position-static">
          <strong class="d-inline-block mb-2 text-primary-emphasis">Community</strong>
          <h3 class="mb-0">Support Groups</h3>
          <p class="card-text mb-auto mt-2">Connect with women who share similar experiences and challenges. Our support
            groups provide a nurturing environment for sharing, healing, and growing together.</p>
          <a href="#" class="btn btn-outline-primary mt-2">Join a group →</a>
        </div>
      </div>

      <div class="row flex-md-row mb-4 position-relative">
        <div class="col-md-4">
          <svg class="bd-placeholder-img img-fluid" width="100%" height="250" xmlns="http://www.w3.org/2000/svg"
            role="img" aria-label="Feature 2" preserveAspectRatio="xMidYMid slice" focusable="false">
            <title>Feature 2</title>
            <rect width="100%" height="100%" fill="#4ECDC4" />
            <text x="50%" y="50%" fill="#fff" text-anchor="middle" dominant-baseline="middle">Feature 2 Image</text>
          </svg>
        </div>
        <div class="col-md-8 p-4 d-flex flex-column position-static">
          <strong class="d-inline-block mb-2 text-success-emphasis">Resources</strong>
          <h3 class="mb-0">Educational Materials</h3>
          <p class="mb-auto mt-2">Access a wide range of educational resources including articles, workshops, and
            courses designed specifically for women's empowerment and personal development.</p>
          <a href="#" class="btn btn-outline-success mt-2">Explore resources →</a>
        </div>
      </div>

      <div class="row g-0 border rounded overflow-hidden flex-md-row mb-4 shadow-sm position-relative">
        <div class="col-md-4">
          <svg class="bd-placeholder-img img-fluid" width="100%" height="250" xmlns="http://www.w3.org/2000/svg"
            role="img" aria-label="Feature 3" preserveAspectRatio="xMidYMid slice" focusable="false">
            <title>Feature 3</title>
            <rect width="100%" height="100%" fill="#FFD166" />
            <text x="50%" y="50%" fill="#fff" text-anchor="middle" dominant-baseline="middle">Feature 3 Image</text>
          </svg>
        </div>
        <div class="col-md-8 p-4 d-flex flex-column position-static">
          <strong class="d-inline-block mb-2 text-warning-emphasis">Services</strong>
          <h3 class="mb-0">Professional Support</h3>
          <p class="card-text mb-auto mt-2">Get connected with professional therapists, counselors, and mentors who
            specialize in women's issues and are dedicated to supporting your journey.</p>
          <a href="#" class="btn btn-outline-warning mt-2">Find support →</a>
        </div>
      </div>

      <div class="row g-0 border rounded overflow-hidden flex-md-row mb-4 shadow-sm position-relative">
        <div class="col-md-4">
          <svg class="bd-placeholder-img img-fluid" width="100%" height="250" xmlns="http://www.w3.org/2000/svg"
            role="img" aria-label="Feature 4" preserveAspectRatio="xMidYMid slice" focusable="false">
            <title>Feature 4</title>
            <rect width="100%" height="100%" fill="#6B5B95" />
            <text x="50%" y="50%" fill="#fff" text-anchor="middle" dominant-baseline="middle">Feature 4 Image</text>
          </svg>
        </div>
        <div class="col-md-8 p-4 d-flex flex-column position-static">
          <strong class="d-inline-block mb-2 text-info-emphasis">Events</strong>
          <h3 class="mb-0">Workshops & Meetups</h3>
          <p class="mb-auto mt-2">Participate in our regular workshops, webinars, and in-person meetups designed to
            empower women through knowledge sharing and community building.</p>
          <a href="#" class="btn btn-outline-info mt-2">See upcoming events →</a>
        </div>
      </div>
    </div>

    <div class="container mb-5">
      <h4 class="fst-italic mb-3">Recent Articles</h4>
      <ul class="list-unstyled">
        <li>
          <a class="d-flex flex-column flex-lg-row gap-3 align-items-start align-items-lg-center py-3 link-body-emphasis text-decoration-none border-top"
            href="#">
            <svg class="bd-placeholder-img" width="100%" height="96" xmlns="http://www.w3.org/2000/svg"
              aria-hidden="true" preserveAspectRatio="xMidYMid slice" focusable="false">
              <rect width="100%" height="100%" fill="#777" />
            </svg>
            <div class="col-lg-8">
              <h6 class="mb-0">Self-Care Practices for Busy Women</h6>
              <small class="text-body-secondary">April 3, 2025</small>
            </div>
          </a>
        </li>
        <li>
          <a class="d-flex flex-column flex-lg-row gap-3 align-items-start align-items-lg-center py-3 link-body-emphasis text-decoration-none border-top"
            href="#">
            <svg class="bd-placeholder-img" width="100%" height="96" xmlns="http://www.w3.org/2000/svg"
              aria-hidden="true" preserveAspectRatio="xMidYMid slice" focusable="false">
              <rect width="100%" height="100%" fill="#777" />
            </svg>
            <div class="col-lg-8">
              <h6 class="mb-0">Building Resilience: Stories from Our Community</h6>
              <small class="text-body-secondary">March 27, 2025</small>
            </div>
          </a>
        </li>
        <li>
          <a class="d-flex flex-column flex-lg-row gap-3 align-items-start align-items-lg-center py-3 link-body-emphasis text-decoration-none border-top"
            href="#">
            <svg class="bd-placeholder-img" width="100%" height="96" xmlns="http://www.w3.org/2000/svg"
              aria-hidden="true" preserveAspectRatio="xMidYMid slice" focusable="false">
              <rect width="100%" height="100%" fill="#777" />
            </svg>
            <div class="col-lg-8">
              <h6 class="mb-0">Women's Health: Understanding Your Body and Mind</h6>
              <small class="text-body-secondary">March 20, 2025</small>
            </div>
          </a>
        </li>
      </ul>
    </div>
  </main>

</template>
