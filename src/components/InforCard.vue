<template>
  <div class="card" :class="cardClass">
    <div class="card-header bg-light" v-if="title" :class="headerClass">
      <h5 class="mb-0">{{ title }}</h5>
    </div>
    <div class="card-body" :class="bodyClass">
      <slot></slot>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps({
  title: {
    type: String,
    default: ''
  },
  cardClass: {
    type: String,
    default: 'shadow-sm'
  },
  bodyClass: {
    type: String,
    default: ''
  },
  headerClass: {
    type: String,
    default: 'py-3'
  }
});
</script>
