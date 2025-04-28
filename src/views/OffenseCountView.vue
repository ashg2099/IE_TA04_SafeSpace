<template>
  <CrimeDashboard title="Melbourne Offences Counts" :dashboardUrl="offenceCountUrl">
    <template #title-actions>
      <ScrollDown targetId="end" text="See more" buttonClass="btn-dark" iconClass="bi bi-arrow-bar-down" />
    </template>

    <template #sidebar-content>
      <InforCard title="You Need To Be Aware">
        <!-- Content here -->
      </InforCard>

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

      <InforCard>
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
      </InforCard>

      <div class="card border-0 bg-warning shadow">
        <div class="card-body">
          <div class="d-flex align-items-center">
            <div class="rounded-circle bg-white p-2 me-3">
              <i class="bi bi-telephone-fill text-danger fs-3"></i>
            </div>
            <div>
              <h5 class="mb-1">Need help?</h5>
              <strong class="fs-5">Call 1800 737 732</strong>
              <div id="end">for emergency assistance</div>
            </div>
          </div>
        </div>
      </div>
    </template>
  </CrimeDashboard>
</template>

<script setup lang="ts">
import CrimeDashboard from '../components/CrimeDashboard.vue';
import ScrollDown from '../components/ScrollDown.vue';
import InforCard from '../components/InforCard.vue'

const offenceCountUrl = import.meta.env.VITE_TABLEAU_DASHBOARD_OFFENCES_COUNT;

</script>

<style scoped></style>
