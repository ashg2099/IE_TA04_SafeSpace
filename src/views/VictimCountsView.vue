<template>
  <div class="row mb-3">
    <div class="col-12">
      <h2>Australia Victim Counts by Gender - Year {{ startYear }} - {{ endYear }}</h2>
    </div>
  </div>
  <div class="card-body">
    <div class="d-flex justify-content-between mb-4">
      <div class="form-group d-flex align-items-center">
        <label for="startYear" class="me-2">Year Range:</label>
        <select id="startYear" v-model="startYear" class="form-select me-2">
          <option v-for="year in availableYears" :key="year" :value="year">{{ year }}</option>
        </select>
        <span class="me-2">to</span>
        <select id="endYear" v-model="endYear" class="form-select">
          <option v-for="year in availableYears" :key="year" :value="year">{{ year }}</option>
        </select>
      </div>

      <div class="btn-group" role="group">
        <button type="button" class="btn"
          :class="{ 'btn-primary': viewMode === 'graph', 'btn-outline-primary': viewMode !== 'graph' }"
          @click="viewMode = 'graph'">
          Graph
        </button>
        <button type="button" class="btn"
          :class="{ 'btn-primary': viewMode === 'table', 'btn-outline-primary': viewMode !== 'table' }"
          @click="viewMode = 'table'">
          Table
        </button>
      </div>
    </div>

    <div class="row">
      <div class="col-lg-8">
        <div class="card shadow border-0 overflow-hidden">
          <div v-if="viewMode === 'graph'">
            <div class="card-body p-0">
              <MaporTextFrame :url="`${API_BASE_URL}/api/trend_chart?start_year=${startYear}&end_year=${endYear}`"
                height="600px" />
            </div>
          </div>
          <div v-else-if="viewMode === 'table'">
            <div class="card-body p-0">
              <MaporTextFrame :url="`${API_BASE_URL}/api/trend_table?start_year=${startYear}&end_year=${endYear}`"
                height="600px" />
            </div>
          </div>
        </div>
      </div>
      <div class="col-lg-4 d-flex flex-column gap-1">

        <div class="card">
          <div class="card-header bg-light">
            <h4>You need to know</h4>
          </div>
          <div class="card-body">
            <MaporTextFrame :url="`${API_BASE_URL}/api/trend_insights?start_year=${startYear}&end_year=${endYear}`"
              height="300px" />
          </div>
        </div>

        <div class="alert alert-warning mt-3 p-3" role="alert">
          <p class="mb-0">
            <i class="bi bi-info-circle-fill me-2"></i>
            Female Victims are consistently higher than male victim counts across Australia
          </p>
        </div>

        <div class="alert alert-dark mt-3 d-flex align-items-center" role="alert">
          <p class="mb-0">
            <i class="bi bi-share-fill me-2"></i>
            Share safety information with your girls to <span class="fw-bold text-danger">promote street safety
              awareness</span>!
          </p>
        </div>
      </div>
    </div>
  </div>

</template>

<script setup lang="ts">
import { ref } from 'vue';
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || '';
import MaporTextFrame from '../components/F1Frames.vue'

const startYear = ref(2015);
const endYear = ref(2024);
const availableYears = ref([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]);
const viewMode = ref('graph');
</script>

<style scoped></style>
