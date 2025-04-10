<template>
  <div class="card shadow-sm rounded bg-light border-0 mb-4">
    <div class="card-body">
      <OffenseCountView />

    </div>
  </div>
  <div class="card shadow-sm rounded bg-light border-0 mb-4">
    <div class="card-body">
      <VictimCountsView />
    </div>
  </div>
</template>

<script setup lang="ts">
import OffenseCountView from '@/views/OffenseCountView.vue';
import VictimCountsView from '@/views/VictimCountsView.vue';
</script>


<style></style>
