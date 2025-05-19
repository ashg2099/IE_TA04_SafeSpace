<template>
  <div class="card h-100"> <!-- Added h-100 class for full height so it can ocuppy col-6 -->
    <div class="card-body">
      <!-- Title & subtitle -->
      <h4 class="card-title fw-bold mb-3">{{ name }}</h4>
      <h6 class="card-subtitle text-muted">{{ type }}</h6>
    </div>

    <!-- Details list -->
    <ul class="list-group list-group-flush border-0">
      <li class="list-group-item border-0">
        <i class="bi bi-geo-alt-fill text-warning me-2"></i>
        <span>{{ address }}</span>
      </li>
      <li class="list-group-item border-0">
        <!-- d-flex: make icon and text as one line block element -->
        <i class="bi bi-telephone-fill text-warning me-2"></i>
        <span>{{ contact }}</span>
      </li>
      <li class="list-group-item border-0">
        <i class="bi bi-globe text-warning me-2"></i>
        <a :href="website" target="_blank" rel="noopener" class="text-decoration-none">
          {{ website }}
        </a>
      </li>
    </ul>

  </div>
</template>

<script setup lang="ts">
interface Props {
  /** Academy name */
  name: string;
  /** Martial art or type (e.g., "Muay Thai") */
  type: string;
  /** Street address */
  address: string;
  /** Contact contact */
  contact: string;
  /** Website URL */
  website: string;
}

defineProps<Props>();
</script>
