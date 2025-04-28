<template>
  <div class="alert" :class="`alert-${type} ${alertClass}`" role="alert">
    <p class="mb-0">
      <i :class="`bi bi-${icon} me-2`" v-if="icon"></i>
      <slot></slot>
    </p>
  </div>
</template>

<script setup lang="ts">
defineProps({
  type: {
    type: String,
    default: 'primary',
    validator: (value: string) => ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark'].includes(value)
  },
  icon: {
    type: String,
    default: ''
  },
  alertClass: {
    type: String,
    default: 'mt-3 p-3'
  }
});
</script>
