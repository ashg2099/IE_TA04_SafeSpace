<template>
  <InforCard card-class="shadow-sm rounded border-0 text-bg-light">
    <!-- Filters -->
    <div class="row g-2 my-4 align-items-end">
      <div class="col-sm-12 col-md-6">
        <label class="form-label fw-semibold">Class Type</label>
        <select v-model="selectedType" class="form-select" style="width: 70%;"> //w-auto
          <option value="">All</option>
          <option v-for="type in types" :key="type" :value="type">{{ type }}</option>
        </select>
      </div>

      <div class="col-12 col-md-4">
        <label class="form-label fw-semibold">Location</label>
        <input v-model="locationQuery" type="text" class="form-control" placeholder="Search by suburb" />
      </div>
    </div>

    <!-- Loading Spinner -->
    <div v-if="loading" class="text-center my-5">
      <div class="spinner-border" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>

    <!-- Error Message -->
    <div v-else-if="error" class="alert alert-danger" role="alert">
      {{ error }}
    </div>

    <!-- Academies Grid -->
    <div v-else>
      <div v-if="paginatedAcademies.length" class="row g-3">
        <div v-for="academy in paginatedAcademies" :key="academy.id" class="col-sm-12 col-md-6">
          <AcademyCard :name="academy.academy_name.trim()" :type="academy.type" :address="academy.address"
            :contact="academy.contact" :website="academy.website" />
        </div>
      </div>

      <!-- No results -->
      <div v-else class="text-center py-5">
        <p class="text-muted">No academies found.</p>
      </div>

      <!-- Pagination - only shown if there's more than one page -->
      <nav v-if="totalPages > 1" class="mt-4">
        <ul class="pagination pagination-lg justify-content-center mb-0">
          <!-- v-bind -->
          <li class="page-item" :class="{ disabled: currentPage === 1 }">
            <button class="page-link" @click="prevPage" aria-label="Previous">
              &laquo;
            </button>
          </li>
          <!-- Page number buttons -->
          <!-- If currentPage is 2 because of goTopage(page), then only the button for page 2 will have the active class. -->
          <li v-for="page in totalPages" :key="page" class="page-item" :class="{ active: currentPage === page }">
            <button class="page-link" @click="goToPage(page)">{{ page }}</button>
          </li>
          <li class="page-item" :class="{ disabled: currentPage === totalPages }">
            <button class="page-link" @click="nextPage" aria-label="Next">
              &raquo;
            </button>
          </li>
        </ul>
      </nav>
    </div>
  </InforCard>
</template>

<script setup lang="ts">
import InforCard from '@/components/InforCard.vue';
import axios from 'axios'
import { onMounted, ref, computed, watch } from 'vue';
import AcademyCard from '@/components/AcademyCard.vue';

interface Academy {
  id: number;
  academy_name: string;
  address: string;
  contact: string;
  type: string;
  website: string;
}

const academies = ref<Academy[]>([]);
const loading = ref<boolean>(true);
const error = ref<string | null>(null);

// Filters
const selectedType = ref<string>('');
const locationQuery = ref<string>('');

// the number of academies shown per page - 4
const pageSize = 4;
const currentPage = ref<number>(1);

// Distinct class types for the select dropdown
// sort -> order by first letter
// Get unique class types for the dropdown filter
// computed properties automatically update when dependencies change
const types = computed(() => [...new Set(academies.value.map(a => a.type))].sort());

// Compute a filtered list of academies based on selected filters
// if no selected filters, return all Academies
// a is callback function, [Academy]
const filteredAcademies = computed(() => {
  return academies.value.filter(a => {
    // Match by class type (if a type is selected, if no selected type -> return true -> apply all data)
    const typeMatch = !selectedType.value || a.type === selectedType.value;
    // Match by location text (case insensitive search)
    const locationMatch = !locationQuery.value || a.address.toLowerCase().includes(locationQuery.value.toLowerCase());
    // Only include academies that match both type and location filters (typeMatch&&locationMatch=True),
    // because filter will return a new [Academy] list
    return typeMatch && locationMatch;
  });
});

// Compute the total number of pages based on the number of filtered academies
// This is a fallback. If the result of Math.ceil(...) is 0 (which can happen if there are no filtered academies), then it will return 1 instead.
// Math.ceil()Rounds up to the nearest whole number.
const totalPages = computed(() => Math.ceil(filteredAcademies.value.length / pageSize) || 1);

// Get current page of academies based on pagination
// = to show only a portion of the full list based on the current page number.
// if is 1, then .slice(0,4)
const paginatedAcademies = computed(() => {
  const start = (currentPage.value - 1) * pageSize;
  return filteredAcademies.value.slice(start, start + pageSize);
});

function prevPage() {
  if (currentPage.value > 1) currentPage.value -= 1;
}

function nextPage() {
  if (currentPage.value < totalPages.value) currentPage.value += 1;
}

function goToPage(page: number) {
  currentPage.value = page;
}

// Watch for filter changes and reset to first page
// This ensures user doesn't end up on an empty page after filtering
// If filters change, reset to first page
watch([selectedType, locationQuery], () => {
  currentPage.value = 1;
});

const API_BASE_URL = '/api'

// Fetch academies data when component is mounted
onMounted(async () => {
  try {
    // Make API request to get academy data
    const { data } = await axios.get<Academy[]>(`${API_BASE_URL}/self_defense_centers`);
    academies.value = data;
  } catch (err: unknown) {
    // Handle different types of errors
    if (axios.isAxiosError(err)) {
      // Extract error message from Axios error response
      error.value = err.response?.data?.message || err.message;
    } else {
      // Generic error message for non-Axios errors
      error.value = 'Failed to load academies.';
    }
  } finally {
    // Always set loading to false when done, regardless of success/failure
    loading.value = false;
  }
});

</script>
