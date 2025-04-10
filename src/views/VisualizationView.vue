<template>
  <header class="mb-4">
    <h1 class="text-center">SafeSpace Analytics Dashboard</h1>
    <p class="text-center lead">
      Visualizing crime data to help keep communities informed and safe
    </p>
    <hr />
  </header>

  <div class="row mb-4">
    <div class="col-md-12">
      <div class="card">
        <div class="card-header bg-primary text-white d-flex justify-content-between align-items-center">
          <h2 class="h4 mb-0">Melbourne Offences Count by Suburb</h2>
          <div class="form-group mb-0">
            <select v-model="selectedYear" class="form-select" @change="loadMapData">
              <option v-for="year in yearOptions" :key="year" :value="year">{{ year }}</option>
            </select>
          </div>
        </div>
        <div class="card-body">
          <div class="row">
            <div class="col-md-8">
              <div ref="mapContainer" class="map-container">
                <div v-if="isMapLoading" class="text-center py-5">
                  <div class="spinner-border text-primary" role="status">
                    <span class="visually-hidden">Loading...</span>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-4">
              <div v-if="isInsightsLoading" class="text-center py-5">
                <div class="spinner-border text-primary" role="status">
                  <span class="visually-hidden">Loading...</span>
                </div>
              </div>
              <div v-else ref="insightsContainer" class="insights-container"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="row mb-4">
    <div class="col-md-12">
      <div class="card">
        <div class="card-header bg-success text-white d-flex justify-content-between align-items-center">
          <h2 class="h4 mb-0">Australia Victim Counts by Gender</h2>
          <div class="d-flex gap-2">
            <div class="form-group mb-0">
              <select v-model="startYear" class="form-select" @change="loadTrendData">
                <option v-for="year in yearOptions" :key="year" :value="year">{{ year }}</option>
              </select>
            </div>
            <div class="form-group mb-0">
              <select v-model="endYear" class="form-select" @change="loadTrendData">
                <option v-for="year in yearOptions" :key="year" :value="year">{{ year }}</option>
              </select>
            </div>
          </div>
        </div>
        <div class="card-body">
          <div class="row">
            <div class="col-md-8">
              <div ref="trendChartContainer" class="chart-container">
                <div v-if="isTrendChartLoading" class="text-center py-5">
                  <div class="spinner-border text-primary" role="status">
                    <span class="visually-hidden">Loading...</span>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-md-4">
              <div v-if="isTrendInsightsLoading" class="text-center py-5">
                <div class="spinner-border text-primary" role="status">
                  <span class="visually-hidden">Loading...</span>
                </div>
              </div>
              <div v-else ref="trendInsightsContainer" class="insights-container"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="row">
    <div class="col-md-12">
      <div class="card">
        <div class="card-header bg-info text-white">
          <h2 class="h4 mb-0">Detailed Data Report</h2>
        </div>
        <div class="card-body">
          <div ref="trendTableContainer" class="table-container">
            <div v-if="isTableLoading" class="text-center py-5">
              <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <footer class="mt-4 text-center">
    <p>&copy; 2025 SafeSpace - Keeping Communities Informed</p>
    <p class="small">For immediate support, call <strong>1800 737 732</strong> or text <strong>0435 737 732</strong>
    </p>
  </footer>

</template>

<script setup lang="ts">
import { ref, onMounted, watch } from 'vue';

// Configure the base URL for API calls
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || '';

// References to DOM elements
const mapContainer = ref<HTMLElement | null>(null);
const insightsContainer = ref<HTMLElement | null>(null);
const trendChartContainer = ref<HTMLElement | null>(null);
const trendInsightsContainer = ref<HTMLElement | null>(null);
const trendTableContainer = ref<HTMLElement | null>(null);

// State management
const yearOptions = ref<number[]>([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]);
const selectedYear = ref<number>(2015);
const startYear = ref<number>(2015);
const endYear = ref<number>(2024);

// Loading states
const isMapLoading = ref<boolean>(true);
const isInsightsLoading = ref<boolean>(true);
const isTrendChartLoading = ref<boolean>(true);
const isTrendInsightsLoading = ref<boolean>(true);
const isTableLoading = ref<boolean>(true);

// Function to load the crime map data
const loadMapData = async () => {
  if (!mapContainer.value) return;

  isMapLoading.value = true;

  try {
    const response = await fetch(`${API_BASE_URL}/api/aggregated_map?year=${selectedYear.value}`);
    const html = await response.text();

    // Insert the HTML content into the container
    mapContainer.value.innerHTML = html;
    isMapLoading.value = false;

    // Load the insights for the selected year
    loadInsights();
  } catch (error) {
    console.error('Error loading map data:', error);
    mapContainer.value.innerHTML = '<div class="alert alert-danger">Failed to load map data. Please try again later.</div>';
    isMapLoading.value = false;
  }
};

// Function to load insights
const loadInsights = async () => {
  if (!insightsContainer.value) return;

  isInsightsLoading.value = true;

  try {
    const response = await fetch(`${API_BASE_URL}/api/insights?year=${selectedYear.value}`);
    const html = await response.text();

    // Insert the HTML content into the container
    insightsContainer.value.innerHTML = html;
    isInsightsLoading.value = false;
  } catch (error) {
    console.error('Error loading insights:', error);
    insightsContainer.value.innerHTML = '<div class="alert alert-danger">Failed to load insights. Please try again later.</div>';
    isInsightsLoading.value = false;
  }
};

// Function to load trend chart data
const loadTrendChart = async () => {
  if (!trendChartContainer.value) return;

  isTrendChartLoading.value = true;

  try {
    const response = await fetch(`${API_BASE_URL}/api/trend_chart?start_year=${startYear.value}&end_year=${endYear.value}`);
    const html = await response.text();

    // Insert the HTML content into the container
    trendChartContainer.value.innerHTML = html;
    isTrendChartLoading.value = false;
  } catch (error) {
    console.error('Error loading trend chart:', error);
    trendChartContainer.value.innerHTML = '<div class="alert alert-danger">Failed to load trend chart. Please try again later.</div>';
    isTrendChartLoading.value = false;
  }
};

// Function to load trend insights
const loadTrendInsights = async () => {
  if (!trendInsightsContainer.value) return;

  isTrendInsightsLoading.value = true;

  try {
    const response = await fetch(`${API_BASE_URL}/api/trend_insights?start_year=${startYear.value}&end_year=${endYear.value}`);
    const html = await response.text();

    // Insert the HTML content into the container
    trendInsightsContainer.value.innerHTML = html;
    isTrendInsightsLoading.value = false;
  } catch (error) {
    console.error('Error loading trend insights:', error);
    trendInsightsContainer.value.innerHTML = '<div class="alert alert-danger">Failed to load trend insights. Please try again later.</div>';
    isTrendInsightsLoading.value = false;
  }
};

// Function to load trend table
const loadTrendTable = async () => {
  if (!trendTableContainer.value) return;

  isTableLoading.value = true;

  try {
    const response = await fetch(`${API_BASE_URL}/api/trend_table?start_year=${startYear.value}&end_year=${endYear.value}`);
    const html = await response.text();

    // Insert the HTML content into the container
    trendTableContainer.value.innerHTML = html;
    isTableLoading.value = false;
  } catch (error) {
    console.error('Error loading trend table:', error);
    trendTableContainer.value.innerHTML = '<div class="alert alert-danger">Failed to load trend table. Please try again later.</div>';
    isTableLoading.value = false;
  }
};

// Function to load all trend-related data
const loadTrendData = async () => {
  // Ensure start year is not greater than end year
  if (startYear.value > endYear.value) {
    startYear.value = endYear.value;
  }

  await Promise.all([
    loadTrendChart(),
    loadTrendInsights(),
    loadTrendTable()
  ]);
};

// Watch for changes to year selections
watch(selectedYear, () => {
  loadMapData();
});

// Load all data when the component is mounted
onMounted(() => {
  loadMapData();
  loadTrendData();
});
</script>

<style scoped>
.map-container,
.chart-container,
.insights-container,
.table-container {
  width: 100%;
  min-height: 400px;
  border-radius: 4px;
  overflow: hidden;
}

.insights-container {
  padding: 15px;
  background-color: #f8f9fa;
  border-radius: 4px;
  height: 100%;
}

/* Override some Bootstrap styles to make the embedded content look better */
:deep(.js-plotly-plot) {
  width: 100% !important;
}

:deep(table) {
  width: 100% !important;
  margin-bottom: 0 !important;
}

:deep(.folium-map) {
  height: 400px !important;
  width: 100% !important;
  z-index: 1;
}
</style>
