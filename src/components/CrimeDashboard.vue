<template>
  <div>
    <div class="d-flex justify-content-between align-items-start mb-2">
      <h2>{{ title }}</h2>
      <slot name="title-actions"></slot>
    </div>

    <div class="row g-4">
      <div class="col-lg-8">
        <!-- Main map with shadow and rounded corners -->
        <div class="card shadow border-0 overflow-hidden h-100">
          <div class="card-body p-0 d-flex flex-column">
            <EmbededFrame :url="dashboardUrl" class="flex-grow-1" />
          </div>
        </div>
      </div>

      <!-- right sidebar with cards -->
      <div class="col-lg-4 d-flex flex-column gap-4" :class="sidebarClass">
        <slot name="sidebar-content"></slot>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import EmbededFrame from './EmbededFrame.vue';

defineProps({
  title: {
    type: String,
    required: true
  },
  dashboardUrl: {
    type: String,
    required: true
  },
  sidebarClass: {
    type: String,
    default: 'gap-1'
  }
})

</script>
