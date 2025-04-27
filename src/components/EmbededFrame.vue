<template>
  <div ref="mapContainer" class="map-container"></div>
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
    default: '800px' // Default height if not specified
  }
});

const mapContainer = ref<HTMLElement | null>(null);
let iframeElement: HTMLIFrameElement | null = null;

function getEmbedUrl(url: string): string {
  try {
    const urlParts = url.split('/');
    const vizIndex = urlParts.indexOf('viz');

    if (vizIndex === -1 || vizIndex + 2 >= urlParts.length) {
      throw new Error('Invalid Tableau URL format');
    }

    const workbook = urlParts[vizIndex + 1];
    let dashboard = urlParts[vizIndex + 2];

    if (dashboard.includes('?')) {
      dashboard = dashboard.split('?')[0];
    }

    return `https://public.tableau.com/views/${workbook}/${dashboard}?:embed=y&:showVizHome=no`;
  } catch (e) {
    console.error('Error processing Tableau URL:', e);
    return url;
  }
}

onMounted(() => {
  if (mapContainer.value) {
    iframeElement = document.createElement('iframe');
    iframeElement.style.width = '100%';
    iframeElement.style.height = props.height;
    iframeElement.style.border = 'none';
    iframeElement.src = getEmbedUrl(props.url);
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
    iframeElement.src = getEmbedUrl(newUrl);
  }
});
</script>

<style scoped>
.map-container {
  width: 100%;
  height: 100%;
  position: relative;
}
</style>
