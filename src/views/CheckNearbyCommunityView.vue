<template>
  <InforCard card-class="shadow-sm rounded border-0 mb-4">
    <EmbededFrame :url="PEDE_LIGHT_Url" class="flex-grow-1" />
  </InforCard>
  <div class="col-10 col-md-8 col-lg-6 mx-auto p-3">
    <InforCard card-class="shadow-sm rounded border-0 mb-4" body-class="p-4"
      header-class="bg-primary text-white text-center py-3 rounded-top">
      <div class="safety-tips">
        <div class="tip-item d-flex align-items-start mb-3">
          <div class="tip-icon text-primary me-3">
            <i class="bi bi-geo-alt fs-4"></i>
          </div>
          <div class="tip-content">
            <h6 class="mb-1 fw-bold">Select area you plan to visit</h6>
            <p class="mb-0 text-secondary">Plan your travel route in advance and study the situation of your destination
            </p>
          </div>
        </div>

        <div class="tip-item d-flex align-items-start mb-3">
          <div class="tip-icon text-primary me-3">
            <i class="bi bi-people fs-4"></i>
          </div>
          <div class="tip-content">
            <h6 class="mb-1 fw-bold">Choose an area with a large flow of people</h6>
            <p class="mb-0 text-secondary">Look for areas with more pedestrians. These areas are usually safer,
              especially at night, as more people around can prevent criminal activities</p>
          </div>
        </div>

        <div class="tip-item d-flex align-items-start mb-3">
          <div class="tip-icon text-primary me-3">
            <i class="bi bi-lightbulb fs-4"></i>
          </div>
          <div class="tip-content">
            <h6 class="mb-1 fw-bold">Avoid areas with poor lighting.</h6>
            <p class="mb-0 text-secondary">If you must pass through these areas, try to do so during daylight hours or
              when accompanied by others.</p>
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
import InforCard from '@/components/InforCard.vue';
import EmbededFrame from '../components/EmbededFrame.vue';

const PEDE_LIGHT_Url = import.meta.env.VITE_TABLEAU_DASHBOARD_PEDE_LIGHT

</script>


<style scoped>
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
</style>
