<template>
  <div ref="mapContainer"></div>
</template>

<script setup lang="ts">
import { ref, onMounted, watch, onUnmounted } from 'vue';

const props = defineProps({
  url: {
    type: String,
    required: true
  },
  height: {
    type: String,
    default: '500px' // Default height if not specified
  }
});

const mapContainer = ref<HTMLElement | null>(null);
let iframeElement: HTMLIFrameElement | null = null;

onMounted(() => {
  if (mapContainer.value) {
    iframeElement = document.createElement('iframe');
    iframeElement.style.width = '100%';
    iframeElement.style.height = props.height;
    iframeElement.style.border = 'none';
    iframeElement.src = props.url;
    mapContainer.value.appendChild(iframeElement);
  }
});

onUnmounted(() => {
  if (iframeElement && mapContainer.value) {
    mapContainer.value.removeChild(iframeElement);
  }
});

watch(() => props.url, (newUrl) => {
  if (iframeElement) {
    iframeElement.src = newUrl;
  }
});
</script>

<style scoped></style>
