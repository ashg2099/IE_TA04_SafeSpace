<template>
  <div class="container">
    <h2 class="mb-4">Community Safety Map</h2>

    <div class="filter-container mb-3">
      <div class="filter-row">
        <div class="filter-group">
          <label>Select Suburb</label>
          <div class="multi-select-dropdown">
            <div class="select-header" @click="toggleDropdown('suburb', $event)">
              <span v-if="selectedSuburbs.length === 0">(all)</span>
              <span v-else-if="selectedSuburbs.length === 1">{{ selectedSuburbs[0] }}</span>
              <span v-else>Selected {{ selectedSuburbs.length }} item</span>
              <i class="bi bi-chevron-down"></i>
            </div>
            <div class="select-dropdown" v-show="dropdownVisible.suburb">
              <div class="select-all-option">
                <label>
                  <input
                    type="checkbox"
                    @change="toggleAllOptions('suburb')"
                    :checked="tempSuburbs.length === suburbs.length"
                  />
                  <span>(All)</span>
                </label>
              </div>
              <div class="select-option" v-for="suburb in suburbs" :key="suburb">
                <label>
                  <input type="checkbox" :value="suburb" v-model="tempSuburbs" />
                  <span>{{ suburb }}</span>
                </label>
              </div>
              <div class="select-actions">
                <button @click="applySelection('suburb')" class="apply-btn">Apply</button>
                <button @click="cancelSelection('suburb')" class="cancel-btn">Cancel</button>
              </div>
            </div>
          </div>
        </div>

        <div class="filter-group">
          <label>Select Postcode</label>
          <div class="multi-select-dropdown">
            <div class="select-header" @click="toggleDropdown('postcode', $event)">
              <span v-if="selectedPostcodes.length === 0">(all)</span>
              <span v-else-if="selectedPostcodes.length === 1">{{ selectedPostcodes[0] }}</span>
              <span v-else>Selected {{ selectedPostcodes.length }} item</span>
              <i class="bi bi-chevron-down"></i>
            </div>
            <div class="select-dropdown" v-show="dropdownVisible.postcode">
              <div class="select-all-option">
                <label>
                  <input
                    type="checkbox"
                    @change="toggleAllOptions('postcode')"
                    :checked="tempPostcodes.length === postcodes.length"
                  />
                  <span>(All)</span>
                </label>
              </div>
              <div class="select-option" v-for="postcode in postcodes" :key="postcode">
                <label>
                  <input type="checkbox" :value="postcode" v-model="tempPostcodes" />
                  <span>{{ postcode }}</span>
                </label>
              </div>
              <div class="select-actions">
                <button @click="applySelection('postcode')" class="apply-btn">Apply</button>
                <button @click="cancelSelection('postcode')" class="cancel-btn">Cancel</button>
              </div>
            </div>
          </div>
        </div>

        <!-- Street lighting indicator -->
        <div class="filter-group" v-show="selectedDataType === 'light'">
          <label>Street Light Brightness Level</label>
          <div class="metric-display">
            <div class="metric-value">{{ averageStreetLightLevel.min }}</div>
            <div class="metric-progress light-progress"></div>
            <div class="metric-value">{{ averageStreetLightLevel.max }}</div>
          </div>
        </div>

        <!-- Time period filter -->
        <div class="filter-group" v-show="selectedDataType === 'pedestrian'">
          <label>Select Period Of Time</label>
          <div class="multi-select-dropdown">
            <div class="select-header" @click="toggleDropdown('period', $event)">
              <span v-if="selectedPeriods.length === 0">(All)</span>
              <span v-else-if="selectedPeriods.length === 1">{{ selectedPeriods[0] }}</span>
              <span v-else>Selected {{ selectedPeriods.length }} item</span>
              <i class="bi bi-chevron-down"></i>
            </div>
            <div class="select-dropdown" v-show="dropdownVisible.period">
              <div class="select-all-option">
                <label>
                  <input
                    type="checkbox"
                    @change="toggleAllOptions('period')"
                    :checked="tempPeriods.length === periodOptions.length"
                  />
                  <span>(All)</span>
                </label>
              </div>
              <div class="select-option" v-for="period in periodOptions" :key="period">
                <label>
                  <input type="checkbox" :value="period" v-model="tempPeriods" />
                  <span>{{ period }}</span>
                </label>
              </div>
              <div class="select-actions">
                <button @click="applySelection('period')" class="apply-btn">Apply</button>
                <button @click="cancelSelection('period')" class="cancel-btn">Cancel</button>
              </div>
            </div>
          </div>
        </div>
        <!-- Pedestrian count indicator -->
        <div class="filter-group" v-show="selectedDataType === 'pedestrian'">
          <label>Daily Pedestrian Count</label>
          <div class="metric-display">
            <div class="metric-value">0</div>
            <div class="metric-progress pedestrian-progress"></div>
            <div class="metric-value">{{ averagePedestrianCount }}</div>
          </div>
        </div>
      </div>

      <div class="data-type-selector mt-3">
        <div class="selector-title">Data Type:</div>
        <div class="selector-buttons">
          <button
            @click="selectDataType('pedestrian')"
            :class="['data-type-btn', 'pedestrian', { active: selectedDataType === 'pedestrian' }]"
          >
            <i class="bi bi-people"></i> Pedestrian Count
          </button>
          <button
            @click="selectDataType('light')"
            :class="['data-type-btn', 'lighting', { active: selectedDataType === 'light' }]"
          >
            <i class="bi bi-lightbulb"></i> Street Lighting
          </button>
          <button
            @click="selectDataType('police')"
            :class="['data-type-btn', 'police', { active: selectedDataType === 'police' }]"
          >
            <i class="bi bi-shield"></i> Police Stations
          </button>
        </div>
      </div>
    </div>

    <InforCard card-class="shadow-sm rounded border-0 mb-4" body-class="p-0">
      <div class="map-wrapper">
        <div id="map" class="community-map"></div>

        <div class="data-type-info" v-if="selectedDataType">
          <p v-if="selectedDataType === 'pedestrian'">
            A total of <strong>{{ averagePedestrianCount }}</strong> pedestrians passed through the
            designated area.
          </p>
          <p v-else-if="selectedDataType === 'light'">
            Street lighting helps improve safety in urban areas
          </p>
          <p v-else-if="selectedDataType === 'police'">
            Local police stations provide emergency services
          </p>
          <p v-else-if="selectedDataType === 'crime'">
            Historical crime data helps identify risk areas
          </p>
          <p v-else-if="selectedDataType === 'victims'">
            Understanding victim demographics helps improve safety measures
          </p>
          <p v-else-if="selectedDataType === 'defense'">
            Self-defense centers provide training for personal safety
          </p>
        </div>

        <div v-if="isLoading" class="loading-overlay">
          <div class="spinner-border text-primary" role="status">
            <span class="visually-hidden">Loading...</span>
          </div>
        </div>
      </div>
    </InforCard>
  </div>
  <div class="col-10 col-md-8 col-lg-6 mx-auto p-3">
    <InforCard
      card-class="shadow-sm rounded border-0 mb-4"
      body-class="p-4"
      header-class="bg-primary text-white text-center py-3 rounded-top"
    >
      <div class="safety-tips">
        <div class="tip-item d-flex align-items-start mb-3">
          <div class="tip-icon text-primary me-3">
            <i class="bi bi-geo-alt fs-4"></i>
          </div>
          <div class="tip-content">
            <h6 class="mb-1 fw-bold">Select area you plan to visit</h6>
            <p class="mb-0 text-secondary">
              Plan your travel route in advance and study the situation of your destination
            </p>
          </div>
        </div>

        <div class="tip-item d-flex align-items-start mb-3">
          <div class="tip-icon text-primary me-3">
            <i class="bi bi-people fs-4"></i>
          </div>
          <div class="tip-content">
            <h6 class="mb-1 fw-bold">Choose an area with a large flow of people</h6>
            <p class="mb-0 text-secondary">
              Look for areas with more pedestrians. These areas are usually safer, especially at
              night, as more people around can prevent criminal activities
            </p>
          </div>
        </div>

        <div class="tip-item d-flex align-items-start mb-3">
          <div class="tip-icon text-primary me-3">
            <i class="bi bi-lightbulb fs-4"></i>
          </div>
          <div class="tip-content">
            <h6 class="mb-1 fw-bold">Avoid areas with poor lighting.</h6>
            <p class="mb-0 text-secondary">
              If you must pass through these areas, try to do so during daylight hours or when
              accompanied by others.
            </p>
          </div>
        </div>

        <div class="mt-4 pt-2 border-top">
          <p class="text-muted fst-italic text-center mb-0">
            <i class="bi bi-exclamation-triangle me-1"></i>
            <small>Historical data does not indicate future, Please stay alert at any time</small>
          </p>
        </div>
      </div>
    </InforCard>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted, computed, watch, reactive } from 'vue'
import InforCard from '@/components/InforCard.vue'
import axios from 'axios'

const isLoading = ref(true)
const map = ref(null)
const mapboxgl = ref(null)
const markers = ref([])

const selectedSuburbs = ref([])
const selectedPostcodes = ref([])
const selectedPeriods = ref([])
const selectedDataType = ref('pedestrian')

const tempSuburbs = ref([])
const tempPostcodes = ref([])
const tempPeriods = ref([])

const tempSelections = reactive({
  suburb: [],
  postcode: [],
  period: [],
})

// Dropdown visibility status
const dropdownVisible = reactive({
  suburb: false,
  postcode: false,
  period: false,
})

const periodOptions = ref([
  '1. Late Night (12am-6am)',
  '2. Morning (6am-12pm)',
  '3. Afternoon (12pm-6pm)',
  '4. Night (6pm-12am)',
])

const policeStations = ref([])
const crimeData = ref([])
const streetLights = ref([])
const pedestrianCounts = ref([])
const victimsData = ref([])
const selfDefenseCenters = ref([])

// Add Melbourne area and postcode mapping
const suburbPostcodeMapping = [
  { suburb: 'Carlton', postcode: '3053' },
  { suburb: 'Carlton North', postcode: '3054' },
  { suburb: 'Docklands', postcode: '3008' },
  { suburb: 'East Melbourne', postcode: '3002' },
  { suburb: 'Flemington', postcode: '3031' },
  { suburb: 'Kensington', postcode: '3031' },
  { suburb: 'Melbourne', postcode: '3000' },
  { suburb: 'North Melbourne', postcode: '3051' },
  { suburb: 'Parkville', postcode: '3052' },
  { suburb: 'Princes Hill', postcode: '3054' },
  { suburb: 'South Wharf', postcode: '3006' },
  { suburb: 'South Yarra', postcode: '3141' },
  { suburb: 'Southbank', postcode: '3006' },
  { suburb: 'West Melbourne', postcode: '3003' },
]

// Modify the computed properties of suburbs and postcodes
const suburbs = computed(() => {
  return suburbPostcodeMapping.map((item) => item.suburb)
})

const postcodes = computed(() => {
  return [...new Set(suburbPostcodeMapping.map((item) => item.postcode))]
})

const averagePedestrianCount = computed(() => {
  if (pedestrianCounts.value.length === 0) return '0'

  const total = pedestrianCounts.value.reduce((sum, item) => {
    return sum + (item.total_pedestrian_count || 0)
  }, 0)

  return Math.round(total / pedestrianCounts.value.length).toLocaleString()
})

const averageStreetLightLevel = computed(() => {
  if (streetLights.value.length === 0) return { min: 0, max: 0, avg: 0 }

  let total = 0
  let min = Infinity
  let max = -Infinity

  streetLights.value.forEach((light) => {
    const level = Number(light.emitted_lux_level) || 0
    total += level
    min = Math.min(min, level)
    max = Math.max(max, level)
  })

  return {
    min: min === Infinity ? 0 : Number(min.toFixed(2)),
    max: max === -Infinity ? 0 : Number(max.toFixed(2)),
    avg: Number((total / streetLights.value.length).toFixed(2)),
  }
})

// API URL
const API_BASE_URL = '/api'

const fetchData = async () => {
  try {
    isLoading.value = true

    // Get all data in parallel
    const [policeRes, crimeRes, victimsRes, lightsRes, pedestrianRes, defenseRes] =
      await Promise.all([
        axios.get(`${API_BASE_URL}/police_stations`),
        axios.get(`${API_BASE_URL}/crime`),
        axios.get(`${API_BASE_URL}/victims`),
        axios.get(`${API_BASE_URL}/street_lighting`),
        axios.get(`${API_BASE_URL}/pedestrian_count`),
        axios.get(`${API_BASE_URL}/self_defense_centers`),
      ])

    policeStations.value = policeRes.data
    crimeData.value = crimeRes.data
    victimsData.value = victimsRes.data
    streetLights.value = lightsRes.data
    console.log('Street lighting data count:', streetLights.value.length)
    pedestrianCounts.value = pedestrianRes.data
    selfDefenseCenters.value = defenseRes.data
    console.log('Victim data count:', victimsData.value.length)

    return true
  } catch (error) {
    console.error('Failed to fetch data:', error)
    return false
  } finally {
    isLoading.value = false
  }
}

const initMap = () => {
  mapboxgl.value = window.mapboxgl
  if (!mapboxgl.value) {
    console.error('Mapbox GL JS not loaded')
    return
  }

  mapboxgl.value.accessToken =
    'pk.eyJ1IjoiaG9uZ2xpbmdqaW4xOTk0IiwiYSI6ImNrczhvZTNmbDN0ZnEycHM3aTkyanp3NmsifQ.iCdeT5IE9GlGKmExl0U6zA'

  map.value = new mapboxgl.value.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [144.9631, -37.8136],
    zoom: 12,
  })

  const popup = new mapboxgl.value.Popup({
    closeButton: false,
    closeOnClick: false,
  })

  map.value.on('load', () => {
    addDataSources()

    addAllLayers()

    showSelectedDataLayers('pedestrian')

    setupHoverEffects(popup)
  })
}

const addDataSources = () => {
  map.value.addSource('pedestrian-source', {
    type: 'geojson',
    data: {
      type: 'FeatureCollection',
      features: convertToGeoJSON(pedestrianCounts.value, 'pedestrian'),
    },
  })

  map.value.addSource('light-source', {
    type: 'geojson',
    data: {
      type: 'FeatureCollection',
      features: convertToGeoJSON(streetLights.value, 'light'),
    },
  })

  map.value.addSource('police-source', {
    type: 'geojson',
    data: {
      type: 'FeatureCollection',
      features: convertToGeoJSON(policeStations.value, 'police'),
    },
  })

  map.value.addSource('crime-source', {
    type: 'geojson',
    data: {
      type: 'FeatureCollection',
      features: convertToGeoJSON(crimeData.value, 'crime', true),
    },
  })

  map.value.addSource('victims-source', {
    type: 'geojson',
    data: {
      type: 'FeatureCollection',
      features: convertToGeoJSON(victimsData.value, 'victims', false, true),
    },
  })

  map.value.addSource('defense-source', {
    type: 'geojson',
    data: {
      type: 'FeatureCollection',
      features: convertToGeoJSON(selfDefenseCenters.value, 'defense', false, true),
    },
  })
}

const addAllLayers = () => {
  map.value.addLayer({
    id: 'pedestrian-point',
    type: 'circle',
    source: 'pedestrian-source',
    paint: {
      'circle-color': [
        'interpolate',
        ['linear'],
        ['get', 'total_pedestrian_count'],
        0,
        '#b8e994', // Minimum number of people
        500000,
        '#78e08f', // Smaller number of people
        1000000,
        '#38ada9', // medium number of people
        2000000,
        '#0a3d62', // Larger number of people
        3500000,
        '#0c2461', // Maximum number of people
      ],
      'circle-radius': 8,
      'circle-stroke-width': 1,
      'circle-stroke-color': '#fff',
      'circle-opacity': 0.8,
    },
  })

  map.value.addLayer({
    id: 'light-heat',
    type: 'heatmap',
    source: 'light-source',
    paint: {
      'heatmap-weight': ['interpolate', ['linear'], ['get', 'emitted_lux_level'], 0, 0, 20, 1],
      'heatmap-intensity': ['interpolate', ['linear'], ['zoom'], 10, 1, 15, 3],
      'heatmap-color': [
        'interpolate',
        ['linear'],
        ['heatmap-density'],
        0,
        'rgba(241, 196, 15, 0)',
        0.2,
        'rgba(241, 196, 15, 0.3)',
        0.4,
        'rgba(241, 196, 15, 0.5)',
        0.6,
        'rgba(241, 196, 15, 0.7)',
        0.8,
        'rgba(241, 196, 15, 0.9)',
        1,
        'rgba(241, 196, 15, 1)',
      ],
      'heatmap-radius': ['interpolate', ['linear'], ['zoom'], 10, 15, 15, 25],
      'heatmap-opacity': 0.8,
    },
  })

  map.value.addLayer({
    id: 'light-point',
    type: 'circle',
    source: 'light-source',
    paint: {
      'circle-color': [
        'interpolate',
        ['linear'],
        ['get', 'emitted_lux_level'],
        0,
        '#ffffd9', // darkest
        5,
        '#fee08b', // darker
        10,
        '#fdae61', // medium
        15,
        '#f46d43', // lighter
        20,
        '#d53e4f', // lightest
      ],
      'circle-radius': [
        'interpolate',
        ['linear'],
        ['get', 'emitted_lux_level'],
        0,
        3, // The radius is 3 at minimum brightness.
        20,
        8, // The radius is 8 at maximum brightness.
      ],
      'circle-opacity': ['interpolate', ['linear'], ['get', 'emitted_lux_level'], 0, 0.6, 20, 0.9],
      'circle-stroke-width': 1,
      'circle-stroke-color': '#fff',
    },
  })

  map.value.addLayer({
    id: 'police-point',
    type: 'circle',
    source: 'police-source',
    paint: {
      'circle-color': '#3498db',
      'circle-radius': 10,
      'circle-stroke-width': 2,
      'circle-stroke-color': '#fff',
    },
  })

  map.value.addLayer({
    id: 'police-symbol',
    type: 'symbol',
    source: 'police-source',
    layout: {
      'text-field': '🛡️',
      'text-size': 12,
      'text-offset': [0, -0.1],
      'text-allow-overlap': true,
    },
  })

  map.value.addLayer({
    id: 'crime-heat',
    type: 'heatmap',
    source: 'crime-source',
    paint: {
      'heatmap-weight': ['interpolate', ['linear'], ['get', 'incidents_recorded'], 0, 0, 100, 1],
      'heatmap-intensity': ['interpolate', ['linear'], ['zoom'], 10, 1, 15, 3],
      'heatmap-color': [
        'interpolate',
        ['linear'],
        ['heatmap-density'],
        0,
        'rgba(231, 76, 60, 0)',
        0.2,
        'rgba(231, 76, 60, 0.3)',
        0.4,
        'rgba(231, 76, 60, 0.5)',
        0.6,
        'rgba(231, 76, 60, 0.7)',
        0.8,
        'rgba(231, 76, 60, 0.9)',
        1,
        'rgba(231, 76, 60, 1)',
      ],
      'heatmap-radius': ['interpolate', ['linear'], ['zoom'], 10, 15, 15, 25],
      'heatmap-opacity': 0.8,
    },
  })

  map.value.addLayer({
    id: 'crime-point',
    type: 'circle',
    source: 'crime-source',
    minzoom: 12,
    paint: {
      'circle-color': '#e74c3c',
      'circle-radius': 6,
      'circle-stroke-width': 1,
      'circle-stroke-color': '#fff',
    },
  })

  map.value.addLayer({
    id: 'victims-point',
    type: 'circle',
    source: 'victims-source',
    paint: {
      'circle-color': '#e67e22',
      'circle-radius': 8,
      'circle-stroke-width': 1,
      'circle-stroke-color': '#fff',
    },
  })

  map.value.addLayer({
    id: 'defense-point',
    type: 'circle',
    source: 'defense-source',
    paint: {
      'circle-color': '#9b59b6',
      'circle-radius': 10,
      'circle-stroke-width': 1,
      'circle-stroke-color': '#fff',
    },
  })

  map.value.addLayer({
    id: 'defense-symbol',
    type: 'symbol',
    source: 'defense-source',
    layout: {
      'text-field': '❤️',
      'text-size': 12,
      'text-offset': [0, -0.1],
      'text-allow-overlap': true,
    },
  })

  hideAllLayers()
}

const hideAllLayers = () => {
  const allLayers = [
    'pedestrian-point',
    'light-heat',
    'light-point',
    'police-point',
    'police-symbol',
    'crime-heat',
    'crime-point',
    'victims-point',
    'defense-point',
    'defense-symbol',
  ]

  allLayers.forEach((layer) => {
    map.value.setLayoutProperty(layer, 'visibility', 'none')
  })
}

const showSelectedDataLayers = (type) => {
  // Hide all layers first
  hideAllLayers()

  // Display the corresponding layer according to the selection type
  switch (type) {
    case 'pedestrian':
      if (map.value.getLayer('pedestrian-point')) {
        map.value.setLayoutProperty('pedestrian-point', 'visibility', 'visible')
      }
      break
    case 'light':
      if (map.value.getLayer('light-heat')) {
        map.value.setLayoutProperty('light-heat', 'visibility', 'visible')
      }
      if (map.value.getLayer('light-point')) {
        map.value.setLayoutProperty('light-point', 'visibility', 'visible')
      }
      break
    case 'police':
      if (map.value.getLayer('police-point')) {
        map.value.setLayoutProperty('police-point', 'visibility', 'visible')
      }
      if (map.value.getLayer('police-symbol')) {
        map.value.setLayoutProperty('police-symbol', 'visibility', 'visible')
      }
      break
    case 'crime':
      if (map.value.getLayer('crime-heat')) {
        map.value.setLayoutProperty('crime-heat', 'visibility', 'visible')
      }
      if (map.value.getLayer('crime-point')) {
        map.value.setLayoutProperty('crime-point', 'visibility', 'visible')
      }
      break
    case 'victims':
      if (map.value.getLayer('victims-point')) {
        map.value.setLayoutProperty('victims-point', 'visibility', 'visible')
      }
      break
    case 'defense':
      if (map.value.getLayer('defense-point')) {
        map.value.setLayoutProperty('defense-point', 'visibility', 'visible')
      }
      if (map.value.getLayer('defense-symbol')) {
        map.value.setLayoutProperty('defense-symbol', 'visibility', 'visible')
      }
      break
  }

  applyFilters()
}

const setupHoverEffects = (popup) => {
  const pointLayers = [
    { id: 'pedestrian-point', type: 'pedestrian' },
    { id: 'light-point', type: 'light' },
    { id: 'police-point', type: 'police' },
    { id: 'crime-point', type: 'crime' },
    { id: 'victims-point', type: 'victims' },
    { id: 'defense-point', type: 'defense' },
  ]

  pointLayers.forEach((layer) => {
    map.value.on('mouseenter', layer.id, (e) => {
      map.value.getCanvas().style.cursor = 'pointer'

      const properties = e.features[0].properties

      let popupHTML = generatePopupHTML(layer.type, properties)

      popup.setLngLat(e.lngLat).setHTML(popupHTML).addTo(map.value)
    })

    map.value.on('mouseleave', layer.id, () => {
      map.value.getCanvas().style.cursor = ''
      popup.remove()
    })
  })
}

const generatePopupHTML = (type, props) => {
  const properties = typeof props === 'string' ? JSON.parse(props) : props

  switch (type) {
    case 'pedestrian':
      return `
        <div class="popup-content">
          <h5>Pedestrian Sensor</h5>
          <p>Location: ${properties.sensor_description || 'Unknown'}</p>
          <p>Suburb: ${properties.suburb || 'Unknown'}</p>
          <p>Postcode: ${properties.postcode || 'Unknown'}</p>
          <p>Daily Count: ${properties.total_pedestrian_count || '0'}</p>
        </div>
      `
    case 'light':
      return `
        <div class="popup-content">
          <h5>Street Light</h5>
          <p>ID: ${properties.id || 'Unknown'}</p>
          <p>Postcode: ${properties.postcode || 'Unknown'}</p>
          <p>Brightness: ${properties.emitted_lux_level || 'Unknown'} lux</p>
        </div>
      `
    case 'police':
      return `
        <div class="popup-content">
          <h5>${properties.facility_name || 'Police Station'}</h5>
          <p>Address: ${properties.formatted_address || 'Unknown'}</p>
          <p>Suburb: ${properties.suburb || 'Unknown'}</p>
          <p>Postcode: ${properties.postcode || 'Unknown'}</p>
        </div>
      `
    case 'crime':
      return `
        <div class="popup-content">
          <h5>Crime Incident</h5>
          <p>Type: ${properties.offence_division || 'Unknown'}</p>
          <p>Subtype: ${properties.offence_subdivision || 'Unknown'}</p>
          <p>Incidents: ${properties.incidents_recorded || '0'}</p>
          <p>Suburb: ${properties.suburb_town_name || 'Unknown'}</p>
          <p>Postcode: ${properties.postcode || 'Unknown'}</p>
          <p>Year: ${properties.year || 'Unknown'}</p>
        </div>
      `
    case 'victims':
      return `
        <div class="popup-content">
          <h5>Victim Statistics</h5>
          <p>Crime Type: ${properties.offence_division || 'Unknown'}</p>
          <p>Subtype: ${properties.offence_subdivision || 'Unknown'}</p>
          <p>Victims: ${properties.victims || '0'}</p>
          <p>Total Victims: ${properties.total_victims || '0'}</p>
          <p>Gender: ${properties.sex || 'Unknown'}</p>
          <p>Year: ${properties.year || 'Unknown'}</p>
        </div>
      `
    case 'defense':
      return `
        <div class="popup-content">
          <h5>${properties.academy_name || 'Self Defense Center'}</h5>
          <p>Type: ${properties.type || 'Unknown'}</p>
          <p>Address: ${properties.address || 'Unknown'}</p>
          <p>Contact: ${properties.contact || 'Unknown'}</p>
          ${
            properties.website
              ? `<p><a href="${properties.website}" target="_blank">Website</a></p>`
              : ''
          }
        </div>
      `
    default:
      return '<div class="popup-content"><p>No information available</p></div>'
  }
}

const convertToGeoJSON = (data, type, isCrime = false, simulateLocation = false) => {
  return data.map((item, index) => {
    // Determine coordinates
    let coordinates

    if (item.longitude && item.latitude) {
      coordinates = [item.longitude, item.latitude]
    } else if (item.lon && item.lat) {
      coordinates = [item.lon, item.lat]
    } else if (simulateLocation) {
      coordinates = [144.9631 + (index % 10) * 0.002, -37.8136 - Math.floor(index / 10) * 0.002]
    } else {
      coordinates = [144.9631, -37.8136]
    }

    // If it is street lighting data and there is only postcode but no suburb, then add suburb according to postcode
    let properties = { ...item, dataType: type }

    if (type === 'light' && item.postcode && !item.suburb) {
      // Find the corresponding suburbs according to postcode
      const matchingSuburbs = suburbPostcodeMapping
        .filter((mapping) => mapping.postcode === item.postcode)
        .map((mapping) => mapping.suburb)

      // Use the first matching suburb or the default value
      properties.suburb = matchingSuburbs.length > 0 ? matchingSuburbs[0] : 'Unknown'
    }

    return {
      type: 'Feature',
      properties: properties,
      geometry: {
        type: 'Point',
        coordinates: coordinates,
      },
    }
  })
}

const toggleDropdown = (type, event) => {
  if (event) {
    event.stopPropagation()
  }

  Object.keys(dropdownVisible).forEach((key) => {
    if (key !== type) dropdownVisible[key] = false
  })

  dropdownVisible[type] = !dropdownVisible[type]

  if (dropdownVisible[type]) {
    if (type === 'suburb') tempSelections.suburb = [...tempSuburbs.value]
    else if (type === 'postcode') tempSelections.postcode = [...tempPostcodes.value]
    else if (type === 'period') tempSelections.period = [...tempPeriods.value]
  }
}

const toggleAllOptions = (type) => {
  if (type === 'suburb') {
    if (tempSuburbs.value.length === suburbs.value.length) {
      tempSuburbs.value = []
    } else {
      tempSuburbs.value = [...suburbs.value]
    }
  } else if (type === 'postcode') {
    if (tempPostcodes.value.length === postcodes.value.length) {
      tempPostcodes.value = []
    } else {
      tempPostcodes.value = [...postcodes.value]
    }
  } else if (type === 'period') {
    if (tempPeriods.value.length === periodOptions.value.length) {
      tempPeriods.value = []
    } else {
      tempPeriods.value = [...periodOptions.value]
    }
  }
}

const applySelection = (type) => {
  if (type === 'suburb') {
    selectedSuburbs.value = [...tempSuburbs.value]

    // When selecting suburb, the corresponding postcode is automatically selected
    const relatedPostcodes = new Set()
    selectedSuburbs.value.forEach((suburb) => {
      const found = suburbPostcodeMapping.find((item) => item.suburb === suburb)
      if (found) relatedPostcodes.add(found.postcode)
    })
    selectedPostcodes.value = [...relatedPostcodes]
    tempPostcodes.value = [...relatedPostcodes]
  } else if (type === 'postcode') {
    selectedPostcodes.value = [...tempPostcodes.value]

    const relatedSuburbs = new Set()
    selectedPostcodes.value.forEach((postcode) => {
      suburbPostcodeMapping
        .filter((item) => item.postcode === postcode)
        .forEach((item) => relatedSuburbs.add(item.suburb))
    })
    selectedSuburbs.value = [...relatedSuburbs]
    tempSuburbs.value = [...relatedSuburbs]
  } else if (type === 'period') {
    selectedPeriods.value = [...tempPeriods.value]
  }

  dropdownVisible[type] = false

  if (map.value) {
    applyFilters()
  }
}

const cancelSelection = (type) => {
  if (type === 'suburb') {
    tempSuburbs.value = [...tempSelections.suburb]
  } else if (type === 'postcode') {
    tempPostcodes.value = [...tempSelections.postcode]
  } else if (type === 'period') {
    tempPeriods.value = [...tempSelections.period]
  }

  dropdownVisible[type] = false
}

const initializeDefaultSelections = () => {
  selectedSuburbs.value = [...suburbs.value]
  selectedPostcodes.value = [...postcodes.value]
  selectedPeriods.value = [...periodOptions.value]

  tempSuburbs.value = [...suburbs.value]
  tempPostcodes.value = [...postcodes.value]
  tempPeriods.value = [...periodOptions.value]

  if (map.value) {
    applyFilters()
  }
}

onMounted(async () => {
  try {
    const success = await fetchData()
    if (success) {
      initMap()

      if (map.value) {
        map.value.once('load', () => {
          initializeDefaultSelections()
          showSelectedDataLayers(selectedDataType.value)
        })
      }
    } else {
    }
  } catch (error) {
    console.error('Map initialization error:', error)
  }

  document.addEventListener('click', (event) => {
    const isClickOnHeader = Array.from(document.querySelectorAll('.select-header')).some((header) =>
      header.contains(event.target as Node)
    )

    if (!isClickOnHeader) {
      let clickedOutside = true
      const openDropdowns = document.querySelectorAll('.select-dropdown')

      for (const dropdown of openDropdowns) {
        if (dropdown.contains(event.target as Node)) {
          clickedOutside = false
          break
        }
      }

      if (clickedOutside) {
        Object.keys(dropdownVisible).forEach((key) => {
          dropdownVisible[key] = false
        })
      }
    }
  })
})

onUnmounted(() => {
  if (map.value) {
    map.value.remove()
  }

  document.removeEventListener('click', () => {})
})

const getLayersBySource = (source) => {
  switch (source) {
    case 'pedestrian':
      return ['pedestrian-point']
    case 'light':
      return ['light-heat', 'light-point']
    case 'police':
      return ['police-point', 'police-symbol']
    case 'crime':
      return ['crime-heat', 'crime-point']
    case 'victims':
      return ['victims-point']
    case 'defense':
      return ['defense-point', 'defense-symbol']
    default:
      return []
  }
}

const selectDataType = (type) => {
  selectedDataType.value = type
  console.log('Switched to data type:', type)

  if (type === 'light' || type === 'victims') {
    // Reset to Select All
    selectedSuburbs.value = [...suburbs.value]
    selectedPostcodes.value = [...postcodes.value]

    tempSuburbs.value = [...suburbs.value]
    tempPostcodes.value = [...postcodes.value]

    console.log('Reset filters to show complete data')
  }

  if (map.value && map.value.loaded()) {
    showSelectedDataLayers(type)
  } else if (map.value) {
    map.value.once('load', () => {
      showSelectedDataLayers(type)
    })
  }
}

watch([suburbs, postcodes, periodOptions], () => {
  if (suburbs.value.length > 0 && tempSuburbs.value.length === 0) {
    tempSuburbs.value = [...suburbs.value]
  }

  if (postcodes.value.length > 0 && tempPostcodes.value.length === 0) {
    tempPostcodes.value = [...postcodes.value]
  }

  if (periodOptions.value.length > 0 && tempPeriods.value.length === 0) {
    tempPeriods.value = [...periodOptions.value]
  }
})

const applyFilters = () => {
  if (!map.value) return

  const sources = ['pedestrian', 'light', 'police', 'crime', 'victims', 'defense']

  sources.forEach((source) => {
    let filterExpression = ['all']
    const isLightOrVictims = source === 'light' || source === 'victims'

    // If both suburb and postcode are empty arrays, add a condition that never matches
    if (selectedSuburbs.value.length === 0 && selectedPostcodes.value.length === 0) {
      // Add a condition that cannot be met, so no data will be displayed
      filterExpression.push(['==', ['get', 'id'], 'non_existent_ID'] as any)
    } else {
      // Otherwise use normal filtering logic
      if (
        selectedPostcodes.value.length > 0 &&
        !(isLightOrVictims && selectedPostcodes.value.length === postcodes.value.length)
      ) {
        filterExpression.push([
          'in',
          ['get', 'postcode'],
          ['literal', selectedPostcodes.value],
        ] as any)
      }

      // For light data, only postcode filtering is used, not suburb filtering.
      // Other data are filtered using suburb
      if (
        selectedSuburbs.value.length > 0 &&
        !(isLightOrVictims && selectedSuburbs.value.length === suburbs.value.length)
      ) {
        if (source === 'crime') {
          filterExpression.push([
            'in',
            ['get', 'suburb_town_name'],
            ['literal', selectedSuburbs.value],
          ] as any)
        } else if (source !== 'light') {
          // Do not apply suburb filtering to the light
          filterExpression.push([
            'in',
            ['get', 'suburb'],
            ['literal', selectedSuburbs.value],
          ] as any)
        }
      }
    }

    // Modify the period filtering logic: when source is pedestrian and selectedPeriods is empty, hide all points
    if (source === 'pedestrian') {
      if (selectedPeriods.value.length === 0) {
        // Add an impossible condition to hide all pedestrian data points
        filterExpression.push(['==', ['get', 'period_of_time'], 'non_existent_time_period'] as any)
      } else {
        filterExpression.push([
          'in',
          ['get', 'period_of_time'],
          ['literal', selectedPeriods.value],
        ] as any)
      }
    }

    const layers = getLayersBySource(source)
    layers.forEach((layer) => {
      if (map.value.getLayer(layer)) {
        if (isLightOrVictims && filterExpression.length <= 1) {
          map.value.setFilter(layer, null)
        } else {
          map.value.setFilter(layer, filterExpression)
        }
      }
    })
  })
}

watch([selectedSuburbs, selectedPostcodes, selectedPeriods], () => {
  if (map.value) {
    applyFilters()
  }
})
</script>

<style scoped>
.container {
  padding: 20px;
}

.map-wrapper {
  position: relative;
  width: 100%;
  height: 600px;
}

.community-map {
  width: 100%;
  height: 100%;
  border-radius: 8px;
}

.loading-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgba(255, 255, 255, 0.7);
  z-index: 1000;
}

.safety-tips {
  position: relative;
}

.tip-item:hover {
  background-color: rgba(0, 123, 255, 0.03);
  border-radius: 6px;
  transition: background-color 0.3s ease;
}

.tip-icon {
  min-width: 40px;
  display: flex;
  justify-content: center;
}

:global(.marker) {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  cursor: pointer;
}

:global(.police-marker) {
  background-color: #3498db;
}

:global(.light-marker) {
  background-color: #f1c40f;
  color: black;
}

:global(.pedestrian-marker) {
  background-color: #2ecc71;
}

:global(.crime-marker) {
  background-color: #e74c3c;
}

:global(.victims-marker) {
  background-color: #e67e22;
}

:global(.defense-marker) {
  background-color: #9b59b6;
}

.filter-container {
  background-color: white;
  padding: 15px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.filter-row {
  display: flex;
  gap: 15px;
  flex-wrap: wrap;
  align-items: flex-end;
}

.filter-group {
  flex: 1;
  min-width: 200px;
}

.filter-group label {
  display: block;
  font-size: 14px;
  margin-bottom: 5px;
  font-weight: 500;
}

.data-type-selector {
  display: flex;
  flex-direction: column;
}

.selector-title {
  margin-bottom: 10px;
  font-weight: bold;
}

.selector-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.data-type-btn {
  padding: 8px 15px;
  border: none;
  border-radius: 4px;
  font-weight: 500;
  cursor: pointer;
  opacity: 0.7;
  transition: all 0.2s;
  color: white;
  display: flex;
  align-items: center;
  gap: 5px;
}

.data-type-btn:hover {
  opacity: 0.9;
}

.data-type-btn.active {
  opacity: 1;
  transform: scale(1.05);
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

.data-type-btn.pedestrian {
  background-color: #2ecc71;
}

.data-type-btn.lighting {
  background-color: #f1c40f;
  color: #333;
}

.data-type-btn.police {
  background-color: #3498db;
}

.data-type-btn.crime {
  background-color: #e74c3c;
}

.data-type-btn.victims {
  background-color: #e67e22;
}

.data-type-btn.defense {
  background-color: #9b59b6;
}

.data-type-info {
  position: absolute;
  top: 20px;
  left: 20px;
  background-color: rgba(255, 255, 255, 0.9);
  padding: 10px 15px;
  border-radius: 4px;
  font-size: 16px;
  z-index: 5;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  max-width: 300px;
}

:global(.mapboxgl-popup) {
  max-width: 300px;
}

:global(.mapboxgl-popup-content) {
  padding: 15px;
  border-radius: 8px;
}

.popup-content h5 {
  margin-top: 0;
  margin-bottom: 10px;
  font-weight: bold;
  font-size: 16px;
}

.popup-content p {
  margin: 5px 0;
  font-size: 14px;
}

.multi-select-dropdown {
  position: relative;
  width: 100%;
  user-select: none;
}

.select-header {
  padding: 8px 12px;
  border: 1px solid #ced4da;
  border-radius: 4px;
  background-color: #fff;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 14px;
}

.select-header:hover {
  border-color: #adb5bd;
}

.select-dropdown {
  position: absolute;
  top: 100%;
  left: 0;
  width: 100%;
  overflow-y: visible;
  background-color: #fff;
  border: 1px solid #ced4da;
  border-radius: 4px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  z-index: 1000;
  margin-top: 5px;
}

.select-all-option,
.select-option {
  padding: 6px 12px;
}

.select-all-option {
  border-bottom: 1px solid #eee;
  font-weight: 500;
}

.select-option:hover,
.select-all-option:hover {
  background-color: #f8f9fa;
}

.select-option label,
.select-all-option label {
  display: flex;
  align-items: center;
  margin: 0;
  cursor: pointer;
  width: 100%;
}

.select-option input[type='checkbox'],
.select-all-option input[type='checkbox'] {
  margin-right: 8px;
}

.select-actions {
  display: flex;
  justify-content: flex-end;
  padding: 8px 12px;
  border-top: 1px solid #eee;
  gap: 8px;
}

.apply-btn,
.cancel-btn {
  padding: 4px 12px;
  border: none;
  border-radius: 4px;
  font-size: 12px;
  cursor: pointer;
}

.apply-btn {
  background-color: #007bff;
  color: white;
}

.cancel-btn {
  background-color: #f8f9fa;
  border: 1px solid #ced4da;
}

.metric-display {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 0;
  height: 38px; /* Match the height with select-header */
}

.metric-value {
  font-size: 12px;
  min-width: 30px;
}

.metric-progress {
  flex: 1;
  height: 34px;
  border: 1px solid #bfa5a5;
}

.pedestrian-progress {
  background: linear-gradient(to right, #b8e994, #78e08f, #38ada9, #0a3d62, #0c2461);
}

.light-progress {
  background: linear-gradient(to right, #ffffd9, #fee08b, #fdae61, #f46d43, #d53e4f);
}
</style>