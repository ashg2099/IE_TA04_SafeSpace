<template>
  <div class="row mb-3">
    <div class="col-12">
      <h2>Australia Victim Counts</h2>
    </div>
  </div>
  <div class="card-body">
    <div class="row">
      <div class="col-lg-8">
        <div class="card shadow border-0 overflow-hidden">
          <div class="card-body p-0 d-flex flex-column">
            <EmbededFrame :url="victimCount" class="flex-grow-1" />
          </div>
        </div>
      </div>
      <div class="col-lg-4 d-flex flex-column gap-1">
        <div class="card">
          <div class="card-header bg-light">
            <h4>You Need To Be Aware</h4>
          </div>
          <div class="card-body">
            <p>...</p>
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
import EmbededFrame from '../components/EmbededFrame.vue';

const victimCount = import.meta.env.VITE_TABLEAU_DASHBOARD_VICTIM_BY_GENDER;
</script>

<style scoped></style>
