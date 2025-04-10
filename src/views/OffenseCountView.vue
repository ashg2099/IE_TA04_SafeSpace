<template>
  <div class="row my-4">
    <h2>Melbourne Offences Count by Suburb - Year {{ selectedYear }}</h2>
    <!-- <div class="form-group p-2">
      <select id="yearSelect" v-model="selectedYear" class="form-select">
        <option v-for="year in availableYears" :key="year" :value="year">{{ year }}</option>
      </select>
    </div> -->
    <div>The Offences Count represents the number of recorded offences under offence division “A
      Crimes against the person”</div>
  </div>



  <div class="row g-4">
    <div class="col-lg-8">
      <!-- Main map with shadow and rounded corners -->
      <div class="card shadow border-0 overflow-hidden">
        <div class="card-body p-0">
          <MaporTextFrame :url="`${API_BASE_URL}/api/aggregated_map?year=${selectedYear}`" height="1150px" />
        </div>
      </div>
    </div>

    <div class="col-lg-4 d-flex flex-column gap-4">
      <!-- Year selector in its own card -->
      <div class="card shadow-sm">
        <div class="card-body">
          <div class="d-flex align-items-center justify-content-between">
            <label for="yearSelect" class="form-label mb-0 fw-bold">Filter by Year:</label>
            <select id="yearSelect" v-model="selectedYear" class="form-select ms-3" style="max-width: 120px;">
              <option v-for="year in availableYears" :key="year" :value="year">{{ year }}</option>
            </select>
          </div>
        </div>
      </div>

      <div class="card shadow-sm">
        <div class="card-header bg-light py-3">
          <h5 class="mb-0">You Need To Be Aware</h5>
        </div>
        <div class="card-body p-0">
          <MaporTextFrame :url="`${API_BASE_URL}/api/insights?year=${selectedYear}`" height="300px" />
        </div>
      </div>

      <div class="card shadow-sm">
        <div class="card-header bg-light py-3">
          <h5 class="mb-0">Offence Categories</h5>
        </div>
        <div class="card-body">
          <p class="card-text">Offence Division <strong>"A Crimes against the person"</strong> includes:</p>
          <ul class="list-group list-group-flush">
            <li class="list-group-item ps-0 border-0 py-2">• A20 Assault and related offences</li>
            <li class="list-group-item ps-0 border-0 py-2">• A50 Robbery</li>
            <li class="list-group-item ps-0 border-0 py-2">• A70 Stalking, harassment and threatening behaviour</li>
            <li class="list-group-item ps-0 border-0 py-2">• A80 Dangerous and negligent acts endangering people</li>
            <li class="list-group-item ps-0 border-0 py-2">• Other crimes against the person</li>
          </ul>
        </div>
      </div>

      <div class="card shadow-sm bg-light">
        <div class="card-body">
          <h5 class="mb-3">Safety Recommendations</h5>
          <div class="d-flex align-items-center mb-2">
            <span class="bg-success p-1 rounded-circle me-2">
              <i class="bi bi-check text-white"></i>
            </span>
            <span>Plan your routes with safety in mind</span>
          </div>
          <div class="d-flex align-items-center">
            <span class="bg-success p-1 rounded-circle me-2">
              <i class="bi bi-check text-white"></i>
            </span>
            <span>Stay extra cautious in high-risk areas</span>
          </div>
        </div>
      </div>

      <div class="card border-0 bg-warning shadow">
        <div class="card-body">
          <div class="d-flex align-items-center">
            <div class="rounded-circle bg-white p-2 me-3">
              <i class="bi bi-telephone-fill text-danger fs-3"></i>
            </div>
            <div>
              <h5 class="mb-1">Need help?</h5>
              <strong class="fs-5">Call 1800 737 732</strong>
              <div>for emergency assistance</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>


</template>

<script setup lang="ts">
import { ref } from 'vue';
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || '';
import MaporTextFrame from '../components/F1Frames.vue'

const selectedYear = ref(2015);
const availableYears = ref([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]);
</script>

<style scoped></style>
