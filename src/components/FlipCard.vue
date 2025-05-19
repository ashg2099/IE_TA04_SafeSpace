<template>
  <div class="flip-card">
    <!-- mouse leave: show card front; mouse on: show card back -->

    <div class="card card-inner border-0 text-center" :class="{ 'is-flipped': isHovered }"
      @mouseenter="isHovered = true" @mouseleave="isHovered = false">

      <!-- Card Front -->
      <div class="card-front position-relative">

        <img :src="backgroundImage" class="card-img" alt="Card background">

        <div class="card-img-overlay d-flex justify-content-center align-items-center">
          <h5 class="card-body">
            <span v-for="(line, index) in frontTextLines" :key="index" class="d-block m-2 front-text">{{
              line
              }}</span>
          </h5>
        </div>

      </div>

      <!-- Card Back -->
      <div class="card-back bg-light d-flex justify-content-center align-items-center">
        <div class="card-body">
          <p class="card-text back-text">{{ backText }}</p>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue';

// Component props
const props = defineProps({
  backgroundImage: {
    type: String,
    required: true
  },
  frontText: {
    type: String,
    required: true
  },
  backText: {
    type: String,
    required: true
  }
});

// Hover state
const isHovered = ref(false);

// Split front text into lines based on commas
const frontTextLines = computed(() => {
  return props.frontText.split(',').map(line => line.trim());
});
</script>

<style scoped>
.flip-card {
  perspective: 1000px;
  /* interact with user */
  cursor: pointer;
  width: 100%;
  aspect-ratio: 1 / 1;
}

.card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  transition: transform 0.8s;
  transform-style: preserve-3d;
  will-change: transform;
}

.is-flipped {
  transform: rotateY(180deg);
}

.card-front,
.card-back {
  /* position both sides absolutely so they stack on top of each other */
  position: absolute;
  /* Make sure both sides fill the entire card */
  width: 100%;
  /* Ensures full overlap */
  height: 100%;
  /* Hide the back side when it's not facing the viewer */
  backface-visibility: hidden;
  /* Safari support */
  -webkit-backface-visibility: hidden;
  overflow: hidden;
}

.card-back {
  transform: rotateY(180deg);
}

.front-text {
  font-weight: 900;
  font-family: 'Lucida Sans';
}

/* responsive font */
@media (min-width: 1200px) {

  /* big screen (col-3) */
  .front-text {
    font-size: 2rem;
  }

  .back-text {
    font-size: 1.25rem;
  }
}

@media (min-width: 768px) and (max-width: 1199.98px) {

  /* medium screen(col-6) */
  .front-text {
    font-size: 2rem;
  }

  .back-text {
    font-size: 1rem;
  }
}

@media (max-width: 767.98px) {

  /* small screen (col-12) */
  .front-text {
    font-size: 2rem;
  }

  .back-text {
    font-size: 1.5rem;
  }
}
</style>
