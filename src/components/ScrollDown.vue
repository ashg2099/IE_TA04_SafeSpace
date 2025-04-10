<template>
  <div class="scroll-indicator" :class="additionalClass" @click="scrollToSection()">
    <span class="align-items-center btn" :class="buttonClass">
      <div class="p-2">{{ text }}</div>
      <i :class="iconClass"></i>
    </span>
  </div>
</template>

<script setup lang="ts">
import { defineProps } from 'vue';

interface ScrollDownProps {
  targetId: string;
  text?: string;
  buttonClass?: string;
  iconClass?: string;
  additionalClass?: string;
}

const props = defineProps<ScrollDownProps>();

const scrollToSection = () => {
  const element = document.getElementById(props.targetId);
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' });
  }
}
</script>

<style>
.scroll-indicator {
  cursor: pointer;
  animation: bounce 2s infinite;
}

@keyframes bounce {

  0%,
  20%,
  50%,
  80%,
  100% {
    transform: translateY(0);
  }

  40% {
    transform: translateY(-10px);
  }

  60% {
    transform: translateY(-5px);
  }
}
</style>
